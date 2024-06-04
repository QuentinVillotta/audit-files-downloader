# audit_files_downloader

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a data engineering convention
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/globals.yml`

### Setup Instructions

Before running the code, you have two options for installing dependencies: using either *pip* or *conda*.

#### Dependencies Installation with Pip

To install them, run the following command on `pip_requirements_.txt` file located in the `conf` directory:

```
pip install -r conf/pip_requirements_.txt
```

#### Dependencies Installation with Conda

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

## How to run the pipeline

You can run the pipeline with the following command:

```
kedro run
```

## Data Access

The project's data is accessible within the `data` directory. It contains two main datasets:

- **Kobo Raw Data**: The raw data from Kobo is stored in `raw_data.json`. To ensure compatibility with nested fields and prevent format errors when loading the data into Python or R, it has been preserved in JSON format. This format ensures that nested structures are maintained accurately during loading and processing.

- **Concatenated Audit Files**: The concatenated audit files are stored in `audit_data.csv`. These files have been aggregated to provide a comprehensive overview of the audit data. This consolidated format facilitates easier analysis and exploration of the audit information.

Accessing the data in the `data` directory allows users to utilize both the original raw data and the processed audit files effectively for their analysis and research purposes.
