# Audit Files Downloader Tool

## Overview
This tool provides a distributed solution for downloading and concatenating KoboToolbox audit files using the Kobo API. Leveraging Dask for distributed computing, the tool efficiently handles large-scale data processing tasks. 

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a data engineering convention
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/globals.yml`

## Setup Instructions

To get started, clone the GitHub repository to your local machine.

Before running the code, you have two options for installing python dependencies: using either `pip` or `conda`.

### Dependencies Installation with Pip

To install them, run the following command on `pip_requirements_.txt` file located in the `conf` directory:

```
pip install -r conf/pip_requirements_.txt
```

### Dependencies Installation with Conda

Alternatively, you can use conda to manage dependencies.
Before running the code, please ensure you have Conda (Miniconda) installed. If you don't have it installed, follow the steps below:

1. **Download and Install Miniconda**:
   - Visit the [Miniconda download page](https://docs.conda.io/en/latest/miniconda.html) and download the installer for your operating system.
   - Follow the installation instructions provided on the Miniconda website.

2. **Create the Conda Environment**:
   - Open a terminal or command prompt.
   - Navigate to the root directory of the project.
   - Run the following command to create a new Conda environment from the `conda_environment.yml` file located in the `conf` directory:

     ```sh
     conda env create -f conf/conda_environment.yml
     ```

3. **Activate the Conda Environment**:
   - After the environment is created, activate it by running:

     ```sh
     conda activate audit-files-downloader
     ```

## User Configuration

To customize the project settings according to your requirements, you need to create a `globals.yml` file in the `conf/local` directory. This file will contain user-specific parameters that the project relies on. Below are the variables that should be defined in the `globals.yml` file along with example values:

```yaml
# Raw Data - Variable survey ID
raw_data_survey_id: _uuid

# Kobo API 
asset_uid: XXXXX
kobo_server: eu.kobotoolbox.org
kobo_credentials: Token XXXX

# Don't modify url except if Kobo API url have changed
url: https://${kobo_server}/api/v2/assets/${asset_uid}/data/?format=json
```
Ensure that you replace the placeholder values with your actual survey ID variable name (`raw_data_survey_id`), Kobo project ID (`asset_uid`), Kobo Server (`kobo_server`), and Kobo API credentials (`kobo_credentials`). The `url` variable should typically not be modified unless there are changes to the Kobo API URL.

## How to run the code

You can run the pipeline with the following command:

```
kedro run
```

## Data Access

The project's data is accessible within the `data` directory. It contains two main datasets:

- **Concatenated Audit Files**: The concatenated audit files are stored in `audit_data.csv`. These files have been aggregated to provide a comprehensive overview of the audit data. This consolidated format facilitates easier analysis and exploration of the audit information.

- **Kobo Raw Data**: The raw data from Kobo is stored in `raw_data.json`. To ensure compatibility with nested fields and prevent format errors when loading the data into Python or R, it has been preserved in JSON format. This format ensures that nested structures are maintained accurately during loading and processing.

## Project Information

- **Author:** Quentin Villotta
- **Date:** June 7, 2024
- **Technology:** Python
- **Main Libraries:**  Kedro, Pandas, Dask, Distributed