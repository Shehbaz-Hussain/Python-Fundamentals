"""
Topic: Inheritance

Description:
Demonstrates how a subclass inherits attributes and methods
from a parent class.
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