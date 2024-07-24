def debug(func):
    """Decorator to print function call details - arguments and return value."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

@debug
def greet(name):
    return f"Hello, {name}!"

# Example usage
add(5, 3)
greet("Alice")
