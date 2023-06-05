import logging
import os

# Get the absolute path for the log file
log_file_path = os.path.abspath('mylog.log')

# Configure the logger
logging.basicConfig(filename=log_file_path, level=logging.DEBUG)

# Write some log messages
logging.debug('This is a debug message.')
logging.info('This is an informational message.')
logging.warning('This is a warning message.')
logging.error('This is an error message.')
