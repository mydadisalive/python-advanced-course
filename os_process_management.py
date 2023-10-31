import os

# Get the current process ID
pid = os.getpid()
print("Current Process ID:", pid)

# Execute a new process (for example, open a file with the default application)
os.system("open my_document.txt")
