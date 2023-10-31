def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print("Error:", e)
