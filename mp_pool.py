import multiprocessing

# Function to calculate the square of a number
def square(x):
    return x * x

if __name__ == "__main__":
    # Create a Pool with 4 worker processes
    with multiprocessing.Pool(processes=4) as pool:
        # Define a list of numbers to calculate squares for
        numbers = [1, 2, 3, 4, 5]

        # Use the map function to apply the square function to each number in parallel
        results = pool.map(square, numbers)

    # Print the results
    print("Original numbers:", numbers)
    print("Squared numbers:", results)
