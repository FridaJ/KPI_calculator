#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template
from flask import send_file
from kpi_calculator import get_kpis
import logging
import sys
import zipfile
import os

# For print statement redirects
class RedirectStdoutToFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.original_stdout = sys.stdout

    def __enter__(self):
        self.file = open(self.file_path, 'w')
        sys.stdout = self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.original_stdout
        self.file.close()

app = Flask(__name__)

# Create dir for created files
os.makedirs("files", exist_ok=False)

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html') 

def run_kpi_calc():
    # Capture the print statements for log file
    with RedirectStdoutToFile('files/pps_data.log'):
        try:
            # Run the KPI script function
            get_kpis()
        except Exception as e:
            print("An error occurred while running kpi_calculator.py:", e)

# Route to handle file download
@app.route('/files/<path:filename>', methods=['GET'])
def download_file(filename):    
    # Run the function to generate KPIs and log output
    run_kpi_calc()
    return send_from_directory(directory='files', filename=filename)

'''
@app.route('/download')
def download_zip_file():
    # Run the function to generate KPIs and log output
    run_kpi_calc()
    
    # Create a zip file and add the Excel file and the log file to it
    with zipfile.ZipFile('KPI_files.zip', 'w') as zipf:
        zipf.write('kpis_VR.xlsx')
        zipf.write('pps_data.log')
        
    return send_file('KPI_files.zip', as_attachment=True)
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)








