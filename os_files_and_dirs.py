import os

# Get the current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# List files and directories in a directory
directory_contents = os.listdir(current_directory)
print("Directory Contents:", directory_contents)

# Create a new directory
new_directory = "my_new_directory"
os.mkdir(new_directory)

# Rename a file or directory
os.rename("old_file.txt", "new_file.txt")

# Remove a file
os.remove("file_to_remove.txt")

# Remove an empty directory
os.rmdir(new_directory)

# Remove a directory and its contents recursively
os.removedirs("my_directory_to_remove")

# Check if a file or directory exists
file_exists = os.path.exists("my_file.txt")
print("File Exists:", file_exists)
