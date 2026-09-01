"""
Solution 15: Using super()

Implements exercise15 by using super() to reuse the parent
class initializer and display_info() method.
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
    """Represent a manager."""

    def __init__(self, name, department):
        """Initialize a manager using the parent initializer."""
        super().__init__(name)
        self.department = department

    def display_info(self):
        """Display the manager's information."""
        super().display_info()
        print(f"Department: {self.department}")


manager = Manager("Ayesha", "Artificial Intelligence")

manager.display_info()