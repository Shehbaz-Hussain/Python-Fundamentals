"""
Solution 09: Instance vs Class Attributes

Implements exercise09 by demonstrating an instance-specific
attribute and a shared class attribute.
"""


class Employee:
    """Represent an employee."""

    company = "Tech Solutions"

    def __init__(self, name, salary):
        """Initialize an employee with name and salary."""
        self.name = name
        self.salary = salary

    def display_info(self):
        """Display the employee's information."""
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary:.2f}")
        print(f"Company: {self.company}")


employee1 = Employee("Ali", 50000)
employee2 = Employee("Ayesha", 60000)

employee1.display_info()

print()

employee2.display_info()

Employee.company = "AI Solutions"

print("\nAfter changing the class attribute:")

employee1.display_info()

print()

employee2.display_info()