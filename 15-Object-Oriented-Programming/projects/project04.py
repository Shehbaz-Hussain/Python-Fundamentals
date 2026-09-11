"""
Project 04: Library Management System

Description:
    Demonstrates object state, instance methods, encapsulation
    conventions, and object behavior.
"""


class Book:
    """Represent a library book."""

    def __init__(self, title, author):
        """Initialize a book."""
        self.title = title
        self.author = author
        self._is_available = True

    def display_info(self):
        """Display book information."""
        status = "Available" if self._is_available else "Borrowed"

        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")

    def borrow(self):
        """Borrow the book if it is available."""
        if not self._is_available:
            print(f'"{self.title}" is already borrowed.')
            return

        self._is_available = False
        print(f'"{self.title}" has been borrowed successfully.')

    def return_book(self):
        """Return the book if it is currently borrowed."""
        if self._is_available:
            print(f'"{self.title}" is already available.')
            return

        self._is_available = True
        print(f'"{self.title}" has been returned successfully.')


book1 = Book(
    "Python Programming",
    "John Smith",
)

book2 = Book(
    "Object-Oriented Python",
    "Jane Smith",
)

books = [book1, book2]

print("Library Management System")
print("=" * 40)

print("\nAvailable Books")
print("-" * 40)

for book in books:
    book.display_info()
    print()

print("Library Transactions")
print("-" * 40)

book1.borrow()
book1.borrow()
book1.return_book()

print("\nFinal Book Information")
print("-" * 40)

for book in books:
    book.display_info()
    print()