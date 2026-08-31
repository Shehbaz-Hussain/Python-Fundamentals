"""
Solution 05: Using self

Implements exercise05 by defining an Employee class and
using self to access instance attributes inside an
instance method.
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


employee = Employee("Ali", "Artificial Intelligence")

employee.display_info()