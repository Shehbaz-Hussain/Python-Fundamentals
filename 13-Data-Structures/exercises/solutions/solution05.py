"""
Module 13 - Data Structures
Solution 05: Creating and Accessing a Dictionary

Purpose:
Provide a complete solution for Exercise 05 by demonstrating how to
create a dictionary and access values using their keys.
"""

# Create a dictionary containing information about a book.
book = {
    "title": "Python Basics",
    "author": "John Smith",
    "pages": 250
}

# Print the complete dictionary.
print(book)

# Print the value associated with the "title" key.
print(book["title"])

# Print the value associated with the "author" key.
print(book["author"])

# Expected Output:
# {'title': 'Python Basics', 'author': 'John Smith', 'pages': 250}
# Python Basics
# John Smith