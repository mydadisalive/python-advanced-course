# Define a generator function
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# Create a generator object
counter = count_up_to(5)

# Iterate through the generator and print values
for number in counter:
    print(number)
