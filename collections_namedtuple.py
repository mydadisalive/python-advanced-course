from collections import namedtuple 

# Define a named tuple type
Person = namedtuple('Person', ['first_name', 'last_name', 'age'])

# Create instances of the named tuple
person1 = Person('John', 'Doe', 30)
person2 = Person('Alice', 'Smith', 25)

# Access fields using dot notation
print("Person 1:", person1.first_name, person1.last_name, person1.age)
print(person1)
