import os
import pandas as pd
import logging

def setup_logging(log_file='project.log'):
    """
    Set up logging for the project.
    """
    try:
        logging.basicConfig(filename=log_file,
                            level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info('Logging is set up.')
        print(f"Log file path: {os.path.abspath(log_file)}")
    except Exception as e:
        print(f"Failed to set up logging: {e}")

def ensure_directory_exists(directory):
    """
    Ensure that a directory exists.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def read_csv(filepath):
    """
    Read a CSV file and return a DataFrame.
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at path {filepath} does not exist.")
    except pd.errors.EmptyDataError:
        raise ValueError(f"The file at path {filepath} is empty.")
    except Exception as e:
        raise Exception(f"An error occurred while reading {filepath}: {e}")

def save_csv(df, filepath):
    """
    Save a DataFrame to a CSV file.
    """
    try:
        df.to_csv(filepath, index=False)
    except Exception as e:
        raise Exception(f"An error occurred while saving to {filepath}: {e}")
