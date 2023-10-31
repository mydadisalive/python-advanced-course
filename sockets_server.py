import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server's host and port
host = '127.0.0.1'
port = 12345

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

print(f"Server is listening on {host}:{port}")

# Accept a connection from a client
client_socket, addr = server_socket.accept()
print(f"Accepted connection from {addr}")

# Receive data from the client
data = client_socket.recv(1024)
print(f"Received: {data.decode()}")

# Close the sockets
client_socket.close()
server_socket.close()
