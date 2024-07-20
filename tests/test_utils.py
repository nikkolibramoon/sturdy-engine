import os
import pytest
import pandas as pd
from src.utils import setup_logging, ensure_directory_exists, read_csv, save_csv

@pytest.fixture(scope="module")
def setup_and_teardown():
    log_file = 'project.log'
    raw_csv_path = 'data/raw/test_data.csv'
    processed_csv_path = 'data/processed/test_data_cleaned.csv'
    test_directory = 'data/test_directory'

    # Cleanup old test files
    if os.path.exists(raw_csv_path):
        os.remove(raw_csv_path)
    if os.path.exists(processed_csv_path):
        os.remove(processed_csv_path)
    if os.path.exists(log_file):
        os.remove(log_file)
    if os.path.exists(test_directory):
        os.rmdir(test_directory)

    # Create necessary directories
    os.makedirs(os.path.dirname(raw_csv_path), exist_ok=True)
    os.makedirs(os.path.dirname(processed_csv_path), exist_ok=True)
    
    yield {
        'log_file': log_file,
        'raw_csv_path': raw_csv_path,
        'processed_csv_path': processed_csv_path,
        'test_directory': test_directory
    }

    # Cleanup after tests
    if os.path.exists(raw_csv_path):
        os.remove(raw_csv_path)
    if os.path.exists(processed_csv_path):
        os.remove(processed_csv_path)
    if os.path.exists(log_file):
        os.remove(log_file)
    if os.path.exists(test_directory):
        os.rmdir(test_directory)

def test_setup_logging(setup_and_teardown):
    log_file = 'test_log.log'
    setup_logging(log_file)
    print("Log setup complete.")

    log_file_path = os.path.abspath(log_file)
    print(f"Checking if log file exists at: {log_file_path}")
    assert os.path.exists(log_file_path), f"Log file was not created at: {log_file_path}"
    with open(log_file_path, 'r') as f:
        log_contents = f.read()
    print(log_contents)

def test_ensure_directory_exists(setup_and_teardown):
    test_directory = setup_and_teardown['test_directory']
    ensure_directory_exists(test_directory)
    assert os.path.exists(test_directory), f"Directory was not created at: {test_directory}"

def test_read_csv(setup_and_teardown):
    raw_csv_path = setup_and_teardown['raw_csv_path']
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    df.to_csv(raw_csv_path, index=False)
    read_df = read_csv(raw_csv_path)
    pd.testing.assert_frame_equal(df, read_df)

    with pytest.raises(FileNotFoundError):
        read_csv('non_existent_file.csv')

    empty_csv_path = setup_and_teardown['raw_csv_path'].replace('test_data.csv', 'empty.csv')
    with open(empty_csv_path, 'w') as f:
        pass  # Create an empty file
    with pytest.raises(ValueError):
        read_csv(empty_csv_path)
    os.remove(empty_csv_path)

def test_save_csv(setup_and_teardown):
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    processed_csv_path = setup_and_teardown['processed_csv_path']
    save_csv(df, processed_csv_path)
    saved_df = pd.read_csv(processed_csv_path)
    pd.testing.assert_frame_equal(df, saved_df)

    with pytest.raises(Exception):
        save_csv(df, '/invalid_path/test_data.csv')
