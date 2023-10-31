import itertools

# Create two iterable lists
colors1 = ["Red", "Green", "Blue"]
colors2 = ["Yellow", "Purple", "Orange"]

# Use chain to combine the two lists into a single iterable
combined_colors = itertools.chain(colors1, colors2)

# Iterate through the combined iterable
for color in combined_colors:
    print(color)
