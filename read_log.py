def process_log_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Process each line of the log file
            # Extract relevant information, perform analysis, etc.
            yield line.strip()

# Using the log file generator
log_generator = process_log_file('mylog.log')
for line in log_generator:
    # Do something with the log line
    print(line)
