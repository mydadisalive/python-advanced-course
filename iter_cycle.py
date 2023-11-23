import itertools

# Create an iterator that cycles through a list of colors
colors = ["Red", "Green", "Blue"]
color_cycle = itertools.cycle(colors)

# Use the color_cycle in a for loop to print the next 10 colors
for _ in range(20):
    print(next(color_cycle))  # Retrieve the next color from the cycle
