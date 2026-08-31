"""
Solution 08: Class Attributes

Implements exercise08 by defining a shared company class
attribute and displaying it for multiple Employee objects.
"""


class Employee:
    """Represent an employee."""

    company = "Tech Solutions"

    def __init__(self, name):
        """Initialize an employee with a name."""
        self.name = name

    def display_info(self):
        """Display the employee's name and company."""
        print(f"Name: {self.name}")
        print(f"Company: {self.company}")


employee1 = Employee("Ali")
employee2 = Employee("Ayesha")

employee1.display_info()

print()

employee2.display_info()