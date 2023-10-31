import random

# Generate a random integer between 1 and 100 (inclusive)
random_integer = random.randint(1, 100)
print("Random Integer:", random_integer)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random Float:", random_float)

# Generate a random choice from a list
colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
random_choice = random.choice(colors)
print("Random Choice:", random_choice)

# Shuffle a list randomly
random.shuffle(colors)
print("Shuffled Colors:", colors)
