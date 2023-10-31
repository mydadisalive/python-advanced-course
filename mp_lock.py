import multiprocessing

# Function to increment a shared counter using a Lock
def increment_counter(counter, lock):
    for _ in range(1000):
        with lock:
            counter.value += 1

# Function to decrement a shared counter using a Lock
def decrement_counter(counter, lock):
    for _ in range(1000):
        with lock:
            counter.value -= 1

if __name__ == "__main__":
    # Create a shared counter and a Lock to protect it
    counter = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()

    # Create two processes: one for incrementing and one for decrementing
    increment_process = multiprocessing.Process(target=increment_counter, args=(counter, lock))
    decrement_process = multiprocessing.Process(target=decrement_counter, args=(counter, lock))

    # Start the processes
    increment_process.start()
    decrement_process.start()

    # Wait for both processes to finish
    increment_process.join()
    decrement_process.join()

    # Print the final value of the counter
    print("Final counter value:", counter.value)
