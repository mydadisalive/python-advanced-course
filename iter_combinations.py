import itertools

# Create an iterable
colors = ["Red", "Green", "Blue", "Yellow"]

# Generate all combinations of 2 colors
combinations = itertools.combinations(colors, 2)

# Print the combinations
for combo in combinations:
    print(combo)
