"""
Solution 03: Instance Attributes

Implements exercise03 by defining a Book class with title
and author instance attributes and creating two Book objects.
"""


class Book:
    """Represent a book."""

    def __init__(self, title, author):
        """Initialize a book with a title and author."""
        self.title = title
        self.author = author


book1 = Book("Python Basics", "Ali")
book2 = Book("Object-Oriented Python", "Ayesha")

print(f"Title: {book1.title}")
print(f"Author: {book1.author}")

print()

print(f"Title: {book2.title}")
print(f"Author: {book2.author}")