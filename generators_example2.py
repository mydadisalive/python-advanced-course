def read_log_file(log_file):
    with open(log_file, 'r') as file:
        for line in file:
            yield line

# Usage
log_file = "large_log_file.txt"
for log_entry in read_log_file(log_file):
    process_log_entry(log_entry)
