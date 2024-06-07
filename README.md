# KPI_calculator
Python Flask app presenting an xlsx-file with project KPIs for PPS VR reporting

### Downloading Files

### Direct Download

1. Navigate to the main page of the repository on GitHub.
2. Click the **Code** button near the top right of the repository page.
3. In the dropdown, click **Download ZIP**.
4. Extract the downloaded ZIP file to access the files.

### Cloning the Repository

To clone the repository using Git, follow these steps:

1. Make sure you have Git installed on your machine. If not, download and install it from [git-scm.com](https://git-scm.com/).
2. Open a terminal or command prompt.
3. Use the `git clone` command followed by the repository URL. For example:

    ```sh
    git clone https://github.com/FridaJ/KPI_calculator
    ```
    
### File structure
The .py files should both be in the main directory, and the index.html file should be in a subdirectory named 'templates'
```
|______ app.py
|______ kpi_calculator.py
|______ templates
            |_______ index.html
```

### Dependencies
| Name | min Version |
|-|-|
| python | 3.11.9 |
| flask | 2.2.5 |
| pandas | 2.2.1 |
| numpy | 1.26.4 |
| python-fmrest | 1.7.3 |
| XlsWriter | 3.1.1 |

### Running the app
After setting up the files with the correct structure (see above, the app is run using the command
>\> python app.py

The index page is then served on http://127.0.0.1:5000
This page will be used from the PPS Filemaker Project Database using the Filemaker "run from url" command.

### Development
- ~~20240530: Since the file generation takes some time, a spinner will be added~~ done 20240607
