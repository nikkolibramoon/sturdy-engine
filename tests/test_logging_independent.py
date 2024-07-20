from src.utils import setup_logging
import os

log_file = 'test_log.log'
setup_logging(log_file)
print("Log setup complete.")

log_file_path = os.path.abspath(log_file)
print(f"Checking if log file exists at: {log_file_path}")
assert os.path.exists(log_file_path), f"Log file was not created at: {log_file_path}"
with open(log_file_path, 'r') as f:
    log_contents = f.read()
print(log_contents)
