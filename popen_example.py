import subprocess

# Command to run
command = "ls -l"

# Create a Popen object for the command
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

# Capture and print the standard output
stdout, stderr = process.communicate()
print("Standard Output:")
print(stdout)

# Check for errors
if process.returncode != 0:
    print(f"Command failed with return code {process.returncode}")
    print("Standard Error:")
    print(stderr)
