import os

# Run a system command and capture the output
output = os.popen("ls -l").read()
print("Command Output:")
print(output)
