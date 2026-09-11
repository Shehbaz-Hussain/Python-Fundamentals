"""
Project 08: Employee Payroll System

Description:
    Demonstrates inheritance, method overriding, super(), and
    polymorphism through a common calculate_pay() interface.
"""


class Employee:
    """Represent a general employee."""

    def __init__(self, name):
        """Initialize an employee."""
        self.name = name

    def calculate_pay(self):
        """Return the employee's calculated pay."""
        return 0

    def display_info(self):
        """Display employee information."""
        print(f"Employee: {self.name}")


class FullTimeEmployee(Employee):
    """Represent a full-time employee."""

    def __init__(self, name, monthly_salary):
        """Initialize a full-time employee."""
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        """Return the monthly salary."""
        return self.monthly_salary

    def display_info(self):
        """Display full-time employee information."""
        super().display_info()
        print("Type: Full-Time")
        print(f"Monthly Salary: ${self.monthly_salary:.2f}")


class PartTimeEmployee(Employee):
    """Represent a part-time employee."""

    def __init__(self, name, hourly_rate, hours_worked):
        """Initialize a part-time employee."""
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        """Calculate pay from hourly rate and hours worked."""
        return self.hourly_rate * self.hours_worked

    def display_info(self):
        """Display part-time employee information."""
        super().display_info()
        print("Type: Part-Time")
        print(f"Hourly Rate: ${self.hourly_rate:.2f}")
        print(f"Hours Worked: {self.hours_worked}")


class ContractEmployee(Employee):
    """Represent a contract employee."""

    def __init__(self, name, contract_amount):
        """Initialize a contract employee."""
        super().__init__(name)
        self.contract_amount = contract_amount

    def calculate_pay(self):
        """Return the contract payment."""
        return self.contract_amount

    def display_info(self):
        """Display contract employee information."""
        super().display_info()
        print("Type: Contract")
        print(
            f"Contract Amount: "
            f"${self.contract_amount:.2f}"
        )


employees = [
    FullTimeEmployee(
        "Ali",
        5000,
    ),
    PartTimeEmployee(
        "Ayesha",
        25,
        80,
    ),
    ContractEmployee(
        "Hamza",
        3500,
    ),
]

print("Employee Payroll System")
print("=" * 40)

total_payroll = 0

for employee in employees:
    employee.display_info()

    pay = employee.calculate_pay()

    print(f"Calculated Pay: ${pay:.2f}")
    print()

    total_payroll += pay

print("=" * 40)
print(f"Total Payroll: ${total_payroll:.2f}")