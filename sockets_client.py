import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server's host and port
host = '127.0.0.1'
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Send data to the server
message = "Hello, server!"
client_socket.send(message.encode())

# Close the socket
client_socket.close()
