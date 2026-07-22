"""
Project: Employee Salary Calculator

Description:
This project demonstrates how functions can be used to calculate
an employee's gross salary based on the basic salary and
allowances.
"""


def calculate_house_allowance(basic_salary):
    """Return the house allowance (20% of basic salary)."""
    return basic_salary * 0.20


def calculate_medical_allowance(basic_salary):
    """Return the medical allowance (10% of basic salary)."""
    return basic_salary * 0.10


def calculate_gross_salary(basic_salary):
    """Return the gross salary."""
    house_allowance = calculate_house_allowance(basic_salary)
    medical_allowance = calculate_medical_allowance(basic_salary)

    return basic_salary + house_allowance + medical_allowance


def main():
    """Run the employee salary calculator."""
    print("Employee Salary Calculator")
    print("--------------------------")

    basic_salary = float(input("Enter the basic salary: "))

    house_allowance = calculate_house_allowance(basic_salary)
    medical_allowance = calculate_medical_allowance(basic_salary)
    gross_salary = calculate_gross_salary(basic_salary)

    print("\nSalary Details")
    print("--------------")
    print(f"Basic Salary: {basic_salary:.2f}")
    print(f"House Allowance: {house_allowance:.2f}")
    print(f"Medical Allowance: {medical_allowance:.2f}")
    print(f"Gross Salary: {gross_salary:.2f}")


main()