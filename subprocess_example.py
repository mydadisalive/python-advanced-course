import subprocess

# Command to run
command = "ls -l"

# Run the command and capture the output
try:
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    print("Command output:")
    print(output)
except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")
