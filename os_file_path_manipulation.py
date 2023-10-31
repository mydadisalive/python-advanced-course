import os

# Join path components to create a complete path
full_path = os.path.join("directory", "subdirectory", "file.txt")
print("Full Path:", full_path)

# Split a path into directory and filename
directory, filename = os.path.split(full_path)
print("Directory:", directory)
print("Filename:", filename)
