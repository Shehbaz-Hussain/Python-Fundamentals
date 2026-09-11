"""
Project 03: Employee Management System

Description:
    Demonstrates class attributes, instance attributes, instance
    methods, and the distinction between shared and individual
    object state.
"""


class Employee:
    """Represent an employee."""

    company = "Tech Solutions"

    def __init__(self, name, salary, department):
        """Initialize an employee."""
        self.name = name
        self.salary = salary
        self.department = department

    def display_info(self):
        """Display employee information."""
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary:.2f}")
        print(f"Department: {self.department}")
        print(f"Company: {self.company}")

    def update_department(self, new_department):
        """Update the employee's department."""
        self.department = new_department


employee1 = Employee(
    "Ali",
    70000,
    "Artificial Intelligence",
)

employee2 = Employee(
    "Ayesha",
    65000,
    "Software Engineering",
)

employee3 = Employee(
    "Hamza",
    60000,
    "Data Science",
)

employees = [employee1, employee2, employee3]

print("Employee Management System")
print("=" * 40)

for employee in employees:
    employee.display_info()
    print()

print("Updating Employee Department")
print("=" * 40)

employee1.update_department("Machine Learning")

employee1.display_info()

print("\nChanging Company")
print("=" * 40)

Employee.company = "AI Engineering Solutions"

for employee in employees:
    print(f"{employee.name}: {employee.company}")