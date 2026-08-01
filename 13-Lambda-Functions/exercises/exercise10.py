"""
===============================================================================
File Name: exercise10.py

Exercise Title:
Calculate the Total Salary Including Bonus

Topic:
Lambda Functions with Parameters and Return Values

Description:
Practice creating a lambda function that accepts multiple parameters and
returns a calculated result based on a real-world salary calculation.

Concepts Covered:
- Lambda functions
- Multiple parameters
- Return values
- Arithmetic operations
- Percentage calculations
- Function invocation

Python Version:
Python 3.13+
===============================================================================

Learning Objective
------------------
Learn how to create and use a lambda function that performs a practical
business calculation by computing an employee's total salary after adding
a bonus percentage.

Problem Statement
-----------------
Create a lambda function that accepts:

- Basic salary
- Bonus percentage

The lambda function should calculate and return the employee's total salary
after adding the bonus.

Formula:

Total Salary = Basic Salary + (Basic Salary × Bonus Percentage ÷ 100)

Store the lambda function in a meaningful variable and test it using
different salary and bonus values.

Requirements
------------
1. Create a lambda function with two parameters:
   - basic_salary
   - bonus_percentage

2. Calculate the bonus amount.

3. Return the total salary after adding the bonus.

4. Store the lambda function in a meaningful variable.

5. Call the lambda function with at least four different salary and bonus
   combinations.

6. Display each calculated total salary using the print() function.

Constraints
-----------
- Use a lambda function.
- Do not use the `def` keyword.
- The lambda expression must consist of only one expression.
- Assume all inputs are valid positive numbers.
- Use meaningful variable names.

Hints
-----
- Calculate the bonus amount first:

    basic_salary * bonus_percentage / 100

- Add the bonus amount to the basic salary.

- Test the function with different bonus percentages such as:

    5%
    10%
    15%
    20%

Expected Output
---------------
Your output should be similar to:

52500.0
66000.0
80500.0
120000.0

(The exact values depend on the salary and bonus percentages you choose.)

Related Concepts
----------------
- Lambda Functions
- Function Parameters
- Return Values
- Arithmetic Operators
- Percentage Calculations
- Business Logic
- Function Calls
"""