from collections import defaultdict

# Create a defaultdict with a default value of 0
grades = defaultdict(int)

# Add grades for students
grades['Alice'] = 95
grades['Bob'] = 88

# Access a missing key (returns the default value, 0)
print("Charlie's grade:", grades['Charlie'])
