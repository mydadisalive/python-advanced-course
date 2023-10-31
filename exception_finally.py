try:
    file = open("my_file.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("Error: File not found")
finally:
    file.close()
