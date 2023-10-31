from collections import Counter

# Count the occurrences of elements in a list
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
fruit_counter = Counter(fruits)

# Access the count of a specific element
print(f"Count of 'apple': {fruit_counter['apple']}")

# Get a list of unique elements
unique_fruits = list(fruit_counter.keys())
print("Unique fruits:", unique_fruits)
