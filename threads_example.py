import threading

# Shared counter
counter = 0

# Lock for synchronized output
output_lock = threading.Lock()

# Function to increment the counter
def increment_counter():
    global counter
    for _ in range(1000):
        with output_lock:
            counter += 1

if __name__ == "__main__":
    # Create two threads
    thread1 = threading.Thread(target=increment_counter)
    thread2 = threading.Thread(target=increment_counter)

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    # Print the final value of the counter
    with output_lock:
        print("Final counter value:", counter)
