"""
Topic: Method Overriding

Description:
Demonstrates how a subclass can provide its own implementation
of a method inherited from a parent class.
"""


class Vehicle:
    """Represent a general vehicle."""

    def start(self):
        """Display a default starting message."""
        print("The vehicle is starting.")


class Car(Vehicle):
    """Represent a car."""

    def start(self):
        """Override the start method for a car."""
        print("The car starts with a key.")


class ElectricCar(Vehicle):
    """Represent an electric car."""

    def start(self):
        """Override the start method for an electric car."""
        print("The electric car starts silently.")


vehicle = Vehicle()
car = Car()
electric_car = ElectricCar()

vehicle.start()
car.start()
electric_car.start()