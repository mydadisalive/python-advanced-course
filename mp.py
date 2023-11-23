import multiprocessing
import time

def calculate_square(number):
    if number == 3:
        time.sleep(5)
    result = number * number
    print(f"The square of {number} is {result}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    processes = []

    for num in numbers:
        process = multiprocessing.Process(target=calculate_square, args=(num,))
        processes.append(process)
        process.start()

    # DO STUFF

    for process in processes:
        process.join()

    print("All processes have finished.")
