# KPI_calculator
Python Flask app presenting an xlsx-file with project KPIs for PPS VR reporting
    
### File structure
The .py files should both be in the main directory, and the index.html file should be in a subdirectory named 'templates'
```
|______ app.py
|______ kpi_calculator.py
|______ templates
            |_______ index.html
```

### Dependencies (see [requirements.txt](requirements.txt))
| Name | min Version |
|-|-|
| python | 3.11.9 |
| flask | 2.2.5 |
| pandas | 2.2.1 |
| numpy | 1.26.4 |
| python-fmrest | 1.7.3 |
| XlsxWriter | 3.1.1 |

### Running the app
After setting up the files with the correct structure (see above, the app is run using the command
>\> python app.py

The index page is then served on http://127.0.0.1:5000
This page will be used from the PPS Filemaker Project Database using the Filemaker "run from url" command.
Until then it is used from https://kpi-calculator-pps.apps.k8s.gu.se.

### Development
- 20240831: kpi_calculator.py needs refactoring to make use of pandas vetorized functions
- ~~20240530: Since the file generation takes some time, a spinner will be added~~ done 20240607
