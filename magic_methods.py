class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.pages})"

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.pages == other.pages

    def __add__(self, other):
        return self.pages + other.pages

# Example usage
book1 = Book("1984", "George Orwell", 328)
book2 = Book("Animal Farm", "George Orwell", 112)

print(book1)  # Output: '1984' by George Orwell
print(repr(book1))  # Output: Book('1984', 'George Orwell', 328)
print(len(book1))  # Output: 328
print(book1 == book2)  # Output: False
print(book1 + book2)  # Output: 440
