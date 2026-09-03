"""
Solution 18: Composition

Implements exercise18 by modeling a Car that contains an
Engine object and delegates engine startup to that object.
"""


class Engine:
    """Represent an engine."""

    def start(self):
        """Display a message indicating that the engine started."""
        print("Engine started.")


class Car:
    """Represent a car composed of an Engine."""

    def __init__(self, brand):
        """Initialize a car with a brand and an engine."""
        self.brand = brand
        self.engine = Engine()

    def start(self):
        """Start the car using its engine."""
        print(f"{self.brand} is starting.")
        self.engine.start()


car = Car("Toyota")

car.start()