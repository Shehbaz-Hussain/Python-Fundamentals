"""
Project 10: Integrated OOP Management System

Description:
    Integrates the major foundational OOP concepts covered in
    Module 15:

    - Classes
    - Objects
    - Instance attributes
    - Class attributes
    - Instance methods
    - Class methods
    - Static methods
    - Encapsulation conventions
    - Inheritance
    - Method overriding
    - super()
    - Polymorphism
    - Composition
"""


class Employee:
    """Represent a general employee."""

    company = "AI Solutions"

    def __init__(self, name, salary, employee_id):
        """Initialize an employee."""
        self.name = name
        self.salary = salary
        self._employee_id = employee_id

    @classmethod
    def change_company(cls, new_company):
        """Change the company name shared by the class."""
        cls.company = new_company

    @staticmethod
    def is_valid_salary(salary):
        """Return whether the salary is greater than zero."""
        return salary > 0

    def display_info(self):
        """Display general employee information."""
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary:.2f}")
        print(f"Employee ID: {self._employee_id}")
        print(f"Company: {self.company}")

    def calculate_bonus(self):
        """Calculate the standard employee bonus."""
        return self.salary * 0.05


class Developer(Employee):
    """Represent a developer."""

    def __init__(
        self,
        name,
        salary,
        employee_id,
        programming_language,
    ):
        """Initialize a developer."""
        super().__init__(
            name,
            salary,
            employee_id,
        )

        self.programming_language = programming_language

    def display_info(self):
        """Display developer information."""
        super().display_info()
        print(
            f"Programming Language: "
            f"{self.programming_language}"
        )

    def calculate_bonus(self):
        """Calculate the developer bonus."""
        return self.salary * 0.10


class Manager(Employee):
    """Represent a manager."""

    def __init__(
        self,
        name,
        salary,
        employee_id,
        team_size,
    ):
        """Initialize a manager."""
        super().__init__(
            name,
            salary,
            employee_id,
        )

        self.team_size = team_size

    def display_info(self):
        """Display manager information."""
        super().display_info()
        print(f"Team Size: {self.team_size}")

    def calculate_bonus(self):
        """Calculate the manager bonus."""
        return self.salary * 0.15


class DataScientist(Employee):
    """Represent a data scientist."""

    def __init__(
        self,
        name,
        salary,
        employee_id,
        specialization,
    ):
        """Initialize a data scientist."""
        super().__init__(
            name,
            salary,
            employee_id,
        )

        self.specialization = specialization

    def display_info(self):
        """Display data scientist information."""
        super().display_info()
        print(
            f"Specialization: "
            f"{self.specialization}"
        )

    def calculate_bonus(self):
        """Calculate the data scientist bonus."""
        return self.salary * 0.12


class Department:
    """Represent a department containing employees."""

    def __init__(self, name):
        """Initialize a department."""
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        """Add an employee to the department."""
        self.employees.append(employee)

    def remove_employee(self, employee):
        """Remove an employee from the department."""
        if employee in self.employees:
            self.employees.remove(employee)
            print(
                f"{employee.name} removed from "
                f"{self.name}."
            )
        else:
            print(
                f"{employee.name} is not a member "
                f"of {self.name}."
            )

    def display_employees(self):
        """Display all employees in the department."""
        print(f"Department: {self.name}")
        print("=" * 45)

        if not self.employees:
            print("No employees in this department.")
            return

        for employee in self.employees:
            employee.display_info()
            print()

    def calculate_total_payroll(self):
        """Calculate the total salary of all employees."""
        total = 0

        for employee in self.employees:
            total += employee.salary

        return total

    def calculate_total_bonuses(self):
        """
        Calculate the total bonuses using polymorphism.

        Each employee object provides its own implementation of
        calculate_bonus().
        """
        total = 0

        for employee in self.employees:
            total += employee.calculate_bonus()

        return total


def display_bonus_report(employees):
    """
    Display bonus information for a collection of employees.

    The function relies on the common calculate_bonus() behavior
    rather than checking the concrete employee type.
    """
    for employee in employees:
        bonus = employee.calculate_bonus()

        print(
            f"{employee.name}: "
            f"${bonus:.2f}"
        )


def main():
    """Run the integrated OOP management system."""
    developer = Developer(
        "Ali",
        70000,
        "EMP-001",
        "Python",
    )

    manager = Manager(
        "Ayesha",
        90000,
        "EMP-002",
        5,
    )

    data_scientist = DataScientist(
        "Hamza",
        80000,
        "EMP-003",
        "Machine Learning",
    )

    employee = Employee(
        "Sara",
        50000,
        "EMP-004",
    )

    employees = [
        developer,
        manager,
        data_scientist,
        employee,
    ]

    department = Department(
        "Artificial Intelligence"
    )

    for current_employee in employees:
        department.add_employee(current_employee)

    Employee.change_company(
        "AI Engineering Solutions"
    )

    print("Integrated OOP Management System")
    print("=" * 45)

    print("\nEmployee Information")
    print("-" * 45)

    department.display_employees()

    print("Payroll Summary")
    print("-" * 45)

    payroll = department.calculate_total_payroll()

    print(f"Total Payroll: ${payroll:.2f}")

    print("\nBonus Report")
    print("-" * 45)

    display_bonus_report(
        department.employees
    )

    total_bonuses = (
        department.calculate_total_bonuses()
    )

    print(
        f"\nTotal Bonuses: "
        f"${total_bonuses:.2f}"
    )

    print("\nSalary Validation")
    print("-" * 45)

    print(
        f"$50,000 valid: "
        f"{Employee.is_valid_salary(50000)}"
    )

    print(
        f"$0 valid: "
        f"{Employee.is_valid_salary(0)}"
    )

    print("\nRemoving an Employee")
    print("-" * 45)

    department.remove_employee(employee)

    print("\nUpdated Department")
    print("-" * 45)

    department.display_employees()


if __name__ == "__main__":
    main()