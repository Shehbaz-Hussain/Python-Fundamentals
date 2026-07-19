"""
File: 12-Functions/examples/example07.py
Topic: Positional Arguments

Description:
This example demonstrates how positional arguments work in Python.
When using positional arguments, values are assigned to parameters
based on their order. The first argument is assigned to the first
parameter, the second argument to the second parameter, and so on.
"""


# Define a function with three parameters
def display_book(title, author, year):
    """Display information about a book."""
    print("Book Information")
    print("----------------")
    print("Title :", title)
    print("Author:", author)
    print("Year  :", year)
    print()


# Call the function using positional arguments
display_book("Python Basics", "John Smith", 2025)

display_book("Learning Functions", "Sarah Khan", 2026)