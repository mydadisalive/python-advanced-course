import gc

# Create a simple class
class MyClass:
    def __init__(self):
        print("MyClass instance created")

# Create an instance of MyClass
obj = MyClass()

# Manually remove the reference to the object
obj = None

# Trigger a manual garbage collection
gc.collect()

print("Garbage collection done")
