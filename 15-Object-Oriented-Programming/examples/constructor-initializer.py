"""
Topic: Constructor and Initializer

Description:
Demonstrates how __init__() initializes an object after
the instance has been created.
"""


class Employee:
    """Represent an employee."""

    def __init__(self, name, department):
        """Initialize an employee with a name and department."""
        self.name = name
        self.department = department

    def display_info(self):
        """Display the employee's information."""
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")


employee = Employee("Ayesha", "Artificial Intelligence")

employee.display_info()