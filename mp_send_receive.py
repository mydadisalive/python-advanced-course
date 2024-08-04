import multiprocessing

# Function to send data through the pipe
def sender(conn, data):
    for item in data:
        print(f"Sender is sending {item} through the pipe")
        conn.send(item)
    conn.send(None)  # Send termination signal
    conn.close()  # Close the connection after sending data

# Function to receive data from the pipe
def receiver(conn, queue):
    received_data = []
    while True:
        item = conn.recv()
        if item is None:  # Check for the termination signal
            break
        received_data.append(item)
        print(f"Receiver received {item} from the pipe")
    conn.close()  # Close the connection when done
    queue.put(received_data)  # Send the received data back to the main process

if __name__ == "__main__":
    data_to_send = [1, 2, 3, 4, 5]

    # Create a Pipe for communication
    parent_conn, child_conn = multiprocessing.Pipe()
    queue = multiprocessing.Queue()

    # Create two processes: one for sending data and one for receiving
    sender_process = multiprocessing.Process(target=sender, args=(child_conn, data_to_send))
    receiver_process = multiprocessing.Process(target=receiver, args=(parent_conn, queue))

    # Start the processes
    sender_process.start()
    receiver_process.start()

    # Wait for the sender process to finish
    sender_process.join()

    # Wait for the receiver process to finish
    receiver_process.join()

    # Retrieve and print the received data
    received_data = queue.get()
    print("Received data:", received_data)
