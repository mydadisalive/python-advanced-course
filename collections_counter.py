from collections import Counter

# Count the occurrences of elements in a list
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
fruit_counter = Counter(fruits)

# Access the count of a specific element
print(f"Count of 'banana': {fruit_counter['banana']}")

# Get a list of unique elements
unique_fruits = list(fruit_counter.keys())
print("Unique fruits:", unique_fruits)


#print(Counter('abdaasbfds').most_common())