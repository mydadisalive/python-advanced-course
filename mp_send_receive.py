import multiprocessing

# Function to send data through the pipe
def sender(conn, data):
    for item in data:
        print(f"Sender is sending {item} through the pipe")
        conn.send(item)
    conn.close()  # Close the connection after sending data

# Function to receive data from the pipe
def receiver(conn):
    received_data = []
    while True:
        try:
            item = conn.recv()
            if item is None:
                break
            received_data.append(item)
            print(f"Receiver received {item} from the pipe")
        except EOFError:
            break
    conn.close()  # Close the connection when done
    return received_data

if __name__ == "__main__":
    data_to_send = [1, 2, 3, 4, 5]

    # Create a Pipe for communication
    parent_conn, child_conn = multiprocessing.Pipe()

    # Create two processes: one for sending data and one for receiving
    sender_process = multiprocessing.Process(target=sender, args=(child_conn, data_to_send))
    receiver_process = multiprocessing.Process(target=receiver, args=(parent_conn,))

    # Start the processes
    sender_process.start()
    receiver_process.start()

    # Wait for both processes to finish
    sender_process.join()
    parent_conn.send(None)  # Signal the receiver process to stop
    receiver_process.join()

    # Retrieve and print the received data
    received_data = receiver_process.get()
    print("Received data:", received_data)
