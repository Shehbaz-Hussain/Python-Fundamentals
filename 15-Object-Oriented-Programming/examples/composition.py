"""
Topic: Composition

Description:
Demonstrates composition by modeling a Car that contains
an Engine object.
"""


class Engine:
    """Represent an engine."""

    def start(self):
        """Start the engine."""
        print("Engine started.")


class Car:
    """Represent a car composed of an Engine."""

    def __init__(self, brand):
        """Initialize a car with an engine."""
        self.brand = brand
        self.engine = Engine()

    def start(self):
        """Start the car using its engine."""
        print(f"{self.brand} is starting.")
        self.engine.start()


car = Car("Toyota")

car.start()