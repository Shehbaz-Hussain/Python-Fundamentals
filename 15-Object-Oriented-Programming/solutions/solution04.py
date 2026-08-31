"""
Solution 04: Instance Methods

Implements exercise04 by defining a Rectangle class with
instance attributes and an instance method for calculating
its area.
"""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, length, width):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width

    def calculate_area(self):
        """Return the area of the rectangle."""
        return self.length * self.width


rectangle = Rectangle(10, 5)

print(f"Area: {rectangle.calculate_area()}")