import datetime
import time

# Define a generator function
def count_up_to(n):
    i = 1
    while i <= n:
        yield datetime.datetime.now()
        i += 1

# Create a generator object
counter = count_up_to(10)

# Iterate through the generator and print values
for number in counter:
    print(number)
    time.sleep(1)
    break






