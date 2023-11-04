import itertools

# Create an iterator that generates an infinite sequence of numbers starting from 1
counter = itertools.count(start=1)

# Use the counter in a for loop to print the first 5 numbers
for _ in range(5):
    print(next(counter))  # Retrieve the next number from the iterator
