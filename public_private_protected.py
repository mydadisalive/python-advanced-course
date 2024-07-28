# good example: https://www.linkedin.com/pulse/static-method-vs-class-instance-python-3-ryan-parsa-kvgdc/

class MyClass:
    def __init__(self):
        self.public_var = "I am public"
        self._protected_var = "I am protected"
        self.__private_var = "I am private"

    def public_method(self):
        return "Public method"

    def _protected_method(self):
        return "Protected method"

    def __private_method(self):
        return "Private method"

    # Accessing the private method within the class
    def access_private_method(self):
        return self.__private_method()

obj = MyClass()

# Accessing public variables and methods
print(obj.public_var)  # I am public
print(obj.public_method())  # Public method

# Accessing protected variables and methods
print(obj._protected_var)  # I am protected
print(obj._protected_method())  # Protected method

# Accessing private variables and methods directly will raise an AttributeError
# print(obj.__private_var)  # AttributeError
# print(obj.__private_method())  # AttributeError

# Accessing private variables and methods through name mangling
print(obj._MyClass__private_var)  # I am private
print(obj.access_private_method())  # Private method


