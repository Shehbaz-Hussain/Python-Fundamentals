"""
Project 05: Vehicle Management System

Description:
    Demonstrates inheritance, inherited attributes, instance
    methods, and method overriding.
"""


class Vehicle:
    """Represent a general vehicle."""

    def __init__(self, brand, model):
        """Initialize a vehicle."""
        self.brand = brand
        self.model = model

    def display_info(self):
        """Display vehicle information."""
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

    def start(self):
        """Start the vehicle."""
        print(f"{self.brand} {self.model} is starting.")


class Car(Vehicle):
    """Represent a car."""

    def start(self):
        """Start the car."""
        print(
            f"{self.brand} {self.model} starts "
            "with an ignition system."
        )


class Motorcycle(Vehicle):
    """Represent a motorcycle."""

    def start(self):
        """Start the motorcycle."""
        print(
            f"{self.brand} {self.model} starts "
            "with a starter button."
        )


class Truck(Vehicle):
    """Represent a truck."""

    def start(self):
        """Start the truck."""
        print(
            f"{self.brand} {self.model} starts "
            "with a heavy-duty engine."
        )


vehicles = [
    Car("Toyota", "Corolla"),
    Motorcycle("Honda", "CBR"),
    Truck("Volvo", "FH"),
]

print("Vehicle Management System")
print("=" * 40)

for vehicle in vehicles:
    vehicle.display_info()
    vehicle.start()
    print()