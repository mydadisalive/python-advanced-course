import threading

# Shared counter
counter = 0

# Lock for synchronized output
output_lock = threading.Lock()

# Function to increment the counter
def increment_counter():
    """
    Increments a shared counter by 1, 1000 times, while ensuring thread safety using a lock.

    Global Variables:
        counter (int): The shared counter to be incremented.

    Returns:
        None
    """
    global counter
    for _ in range(1000):
        with output_lock:
            counter += 1
            print(threading.current_thread().name, counter)

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
