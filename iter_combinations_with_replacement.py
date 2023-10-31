import itertools

# Create an iterable
colors = ["Red", "Green", "Blue"]

# Generate all combinations with replacement of 2 colors
combinations = itertools.combinations_with_replacement(colors, 2)

# Print the combinations
for combo in combinations:
    print(combo)
