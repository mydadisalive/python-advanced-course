def check_value(value):
    if value > 100:
        raise Exception(f"Value too high: {value}. It should be 100 or less.")
    elif value < 1:
        raise Exception(f"Value too low: {value}. It should be 1 or more.")
    else:
        return f"Value {value} is within range."

# Example usage
try:
    print(check_value(150))
except Exception as e:
    print(f"An error occurred: {e}")

try:
    print(check_value(0))
except Exception as e:
    print(f"An error occurred: {e}")
