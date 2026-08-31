"""
Solution 06: Initialize Object State

Implements exercise06 by using __init__() to initialize the
name and price attributes of a Product object.
"""


class Product:
    """Represent a product."""

    def __init__(self, name, price):
        """Initialize a product with a name and price."""
        self.name = name
        self.price = price

    def display_info(self):
        """Display the product information."""
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")


product = Product("Laptop", 1200)

product.display_info()