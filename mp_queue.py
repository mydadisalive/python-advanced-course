import multiprocessing

# Function to add squares of numbers to a queue
def calculate_squares(numbers, queue):
    for num in numbers:
        result = num * num
        queue.put(result)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result_queue = multiprocessing.Queue()

    # Create a process for calculating squares and putting them in the queue
    process1 = multiprocessing.Process(target=calculate_squares, args=(numbers, result_queue))

    # Start the process
    process1.start()

    # Wait for the process to finish
    process1.join()

    # Retrieve and print the squares
    squares = []
    while not result_queue.empty():
        square = result_queue.get()
        squares.append(square)

    print("Calculated squares:", squares)
