"""
Topic: super()

Description:
Demonstrates how super() can be used in a subclass to access
behavior from the parent class.
"""


class Employee:
    """Represent an employee."""

    def __init__(self, name):
        """Initialize an employee with a name."""
        self.name = name

    def display_info(self):
        """Display the employee's name."""
        print(f"Name: {self.name}")


class Manager(Employee):
    """Represent a manager who inherits from Employee."""

    def __init__(self, name, department):
        """Initialize a manager using the parent initializer."""
        super().__init__(name)
        self.department = department

    def display_info(self):
        """Display manager information."""
        super().display_info()
        print(f"Department: {self.department}")


manager = Manager("Ayesha", "Artificial Intelligence")

manager.display_info()