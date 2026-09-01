"""
Solution 13: Inheritance

Implements exercise13 by defining a Vehicle parent class and
a Car subclass that inherits its initializer and start() method.
"""


class Vehicle:
    """Represent a general vehicle."""

    def __init__(self, brand):
        """Initialize a vehicle with a brand."""
        self.brand = brand

    def start(self):
        """Display a message indicating that the vehicle starts."""
        print(f"{self.brand} vehicle is starting.")


class Car(Vehicle):
    """Represent a car that inherits from Vehicle."""


car = Car("Toyota")

print(f"Brand: {car.brand}")
car.start()