class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Example usage
v1 = Vector(2, 3)
v2 = Vector(5, 7)
v3 = v1 + v2
v4 = v2 - v1

print(v3)  # Output: Vector(7, 10)
print(v4)  # Output: Vector(3, 4)
