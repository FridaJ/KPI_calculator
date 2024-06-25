from flask import Flask, render_template, send_file, abort, after_this_request
from kpi_calculator import get_kpis
import sys
import zipfile
import os
import io
import time
import threading

# T capture print statements, with buffering
class BufferedIOHandler(io.TextIOBase):
    def __init__(self, file_path):
        self.buffer = io.StringIO()
        self.file_path = file_path

    def write(self, s):
        self.buffer.write(s)
        if '\n' in s:
            self.flush()

    def flush(self):
        with open(self.file_path, 'a') as f:
            f.write(self.buffer.getvalue())
        self.buffer.seek(0)
        self.buffer.truncate()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_zip.html')

# Function to run KPI calculations and create zip file
def run_kpi_calc():
    with BufferedIOHandler('pps_data.log') as log_buffer:
        sys.stdout = log_buffer
        try:
            get_kpis()
        except Exception as e:
            print(f'An error occurred while running kpi_calculator.py: {e}')
        finally:
            log_buffer.flush()
            sys.stdout = sys.__stdout__  # Reset stdout to default

    with zipfile.ZipFile('KPI_files.zip', 'w') as zipf:
        zipf.write('kpis_VR.xlsx')
        zipf.write('pps_data.log')
        
        
# Route to trigger and handle file download
@app.route('/download')
def trigger_and_download():

    if not os.path.exists('KPI_files.zip'):
        threading.Thread(target=run_kpi_calc).start()

    # Check continuously if file exists, timeout after 1 minute
    timeout = 60  # 1 minute
    start_time = time.time()

    while not os.path.exists('KPI_files.zip'):   
        if time.time() - start_time > timeout:
            return "File not generated", 404
        time.sleep(1)  # Check every second

    @after_this_request
    # After try / except block with send_file
    # remove_files will automatically be called
    def remove_files(response):
        try:
            os.remove('KPI_files.zip')
            os.remove('kpis_VR.xlsx')
            os.remove('pps_data.log')
        except Exception as e:
            print(f'Error removing files: {e}')
        return response

    try:
        return send_file('KPI_files.zip', as_attachment=True)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=5000)

