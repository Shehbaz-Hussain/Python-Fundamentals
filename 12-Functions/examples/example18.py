"""
File: 12-Functions/examples/example18.py
Topic: Employee Salary Calculation Using Functions

Description:
This example demonstrates how multiple functions can work together
to calculate an employee's gross salary. Each function performs
a single task, making the program modular, reusable, and easier
to maintain.
"""


def calculate_house_rent_allowance(basic_salary):
    """Return the house rent allowance (20% of basic salary)."""
    return basic_salary * 0.20


def calculate_medical_allowance(basic_salary):
    """Return the medical allowance (10% of basic salary)."""
    return basic_salary * 0.10


def calculate_gross_salary(basic_salary):
    """Return the gross salary."""
    house_rent = calculate_house_rent_allowance(basic_salary)
    medical = calculate_medical_allowance(basic_salary)

    return basic_salary + house_rent + medical


# Employee salary
basic_salary = 50000

# Perform calculations
house_rent = calculate_house_rent_allowance(basic_salary)
medical = calculate_medical_allowance(basic_salary)
gross_salary = calculate_gross_salary(basic_salary)

# Display salary details
print("Employee Salary Report")
print("----------------------")
print("Basic Salary           :", basic_salary)
print("House Rent Allowance   :", house_rent)
print("Medical Allowance      :", medical)
print("Gross Salary           :", gross_salary)