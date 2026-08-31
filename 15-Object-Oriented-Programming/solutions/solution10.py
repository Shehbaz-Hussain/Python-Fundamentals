"""
Solution 10: Class Method

Implements exercise10 by using a class method to update the
shared company attribute for all Employee objects.
"""


class Employee:
    """Represent an employee."""

    company = "Tech Solutions"

    def __init__(self, name):
        """Initialize an employee with a name."""
        self.name = name

    @classmethod
    def change_company(cls, new_company):
        """Change the company for the Employee class."""
        cls.company = new_company

    def display_info(self):
        """Display the employee's name and company."""
        print(f"Name: {self.name}")
        print(f"Company: {self.company}")


employee1 = Employee("Ali")
employee2 = Employee("Ayesha")

Employee.change_company("AI Solutions")

employee1.display_info()

print()

employee2.display_info()