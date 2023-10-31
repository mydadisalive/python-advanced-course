import itertools

# Create an iterable
colors = ["Red", "Green", "Blue"]

# Generate all permutations of the colors
permutations = itertools.permutations(colors)

# Print the permutations
for perm in permutations:
    print(perm)
