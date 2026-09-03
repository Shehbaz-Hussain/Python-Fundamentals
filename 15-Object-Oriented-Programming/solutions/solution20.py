"""
Solution 20: Integrated OOP Design

Implements exercise20 by combining inheritance, method
overriding, super(), instance attributes, and polymorphism.
"""


class Employee:
    """Represent a general employee."""

    def __init__(self, name, salary):
        """Initialize an employee with a name and salary."""
        self.name = name
        self.salary = salary

    def display_info(self):
        """Display the employee's name and salary."""
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary:.2f}")


class Developer(Employee):
    """Represent a developer."""

    def __init__(self, name, salary, programming_language):
        """Initialize a developer."""
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        """Display developer information."""
        super().display_info()
        print(f"Programming Language: {self.programming_language}")


class Manager(Employee):
    """Represent a manager."""

    def __init__(self, name, salary, team_size):
        """Initialize a manager."""
        super().__init__(name, salary)
        self.team_size = team_size

    def display_info(self):
        """Display manager information."""
        super().display_info()
        print(f"Team Size: {self.team_size}")


employees = [
    Employee("Ali", 50000),
    Developer("Ayesha", 70000, "Python"),
    Manager("Hamza", 80000, 8),
]

for employee in employees:
    employee.display_info()
    print()