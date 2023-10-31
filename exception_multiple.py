try:
    file = open("non_existent_file.txt", "r")
    data = file.read()
    file.close()
except (FileNotFoundError, PermissionError):
    print("Error: File not found or permission denied")
