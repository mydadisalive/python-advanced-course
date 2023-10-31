import itertools

# Create an iterable
numbers = [1, 2, 3, 4, 5]

# Use accumulate to get the cumulative sum
cumulative_sum = itertools.accumulate(numbers)

# Print the cumulative sum
for result in cumulative_sum:
    print(result)
