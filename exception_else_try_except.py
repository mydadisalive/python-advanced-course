try:
    value = int(input("Enter a positive number: "))
except ValueError:
    print("Invalid input")
else:
    if value < 0:
        print("Input must be positive")
    else:
        print("Valid input:", value)
