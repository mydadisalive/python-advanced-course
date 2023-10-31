from collections import ChainMap

# Create two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Chain the dictionaries
chain = ChainMap(dict1, dict2)

# Access values
print("Value of 'a':", chain['a'])
print("Value of 'b':", chain['b'])
print("Value of 'c':", chain['c'])
