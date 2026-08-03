"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 10
Exercise Title: Calculate the Total Salary Including Bonus
Difficulty: Beginner

Objective:
    Create a lambda function that accepts a basic salary and a bonus
    percentage, then returns the employee's total salary after adding the
    bonus. Store the lambda function in a meaningful variable and test it
    using different salary and bonus values.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a lambda function that calculates the total salary after adding
# the bonus.
calculate_total_salary = (
    lambda basic_salary, bonus_percentage:
    basic_salary + (basic_salary * bonus_percentage / 100)
)

# Call the lambda function with different salary and bonus combinations.
print(calculate_total_salary(50000, 5))
print(calculate_total_salary(60000, 10))
print(calculate_total_salary(70000, 15))
print(calculate_total_salary(100000, 20))


"""
===============================================================================
Expected Output
===============================================================================

52500.0
66000.0
80500.0
120000.0

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A lambda function is created using the 'lambda' keyword.
2. The function accepts two parameters:
       - basic_salary
       - bonus_percentage
3. The bonus amount is calculated using the formula:

       basic_salary * bonus_percentage / 100

4. The calculated bonus is added to the basic salary.
5. The lambda function is stored in the variable
   'calculate_total_salary'.
6. The function is called four times using different salary and bonus
   combinations.
7. Each calculated total salary is displayed using the print() function.

How the Lambda Expression Works
-------------------------------

Lambda expression:

    lambda basic_salary, bonus_percentage:
        basic_salary + (basic_salary * bonus_percentage / 100)

- 'lambda' creates an anonymous function.
- 'basic_salary' represents the employee's base salary.
- 'bonus_percentage' represents the percentage of the bonus.
- The bonus amount is calculated as a percentage of the basic salary.
- The calculated bonus is added to the basic salary.
- The resulting total salary is returned automatically.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- Multiple parameters
- Return values
- Arithmetic operations
- Percentage calculations
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(1)

Explanation:
The calculation requires a fixed number of arithmetic operations, so it runs
in constant time.

===============================================================================
Space Complexity
===============================================================================

O(1)

Explanation:
The solution uses a constant amount of additional memory.

===============================================================================
Best Practices
===============================================================================

- Use descriptive names for variables and parameters.
- Group arithmetic operations with parentheses to improve readability.
- Test the function with different salary and bonus values.
- Keep lambda expressions limited to a single, clear calculation.

===============================================================================
Common Mistakes
===============================================================================

- Subtracting the bonus instead of adding it.
- Forgetting to divide the bonus percentage by 100.
- Misplacing parentheses, leading to incorrect calculations.
- Using the 'def' keyword instead of a lambda function.
- Forgetting to assign the lambda function to a variable before calling it.

===============================================================================
Alternative Approach
===============================================================================

Another valid implementation is:

    calculate_total_salary = (
        lambda salary, bonus: salary * (1 + bonus / 100)
    )

This produces the same result using an equivalent mathematical formula.

===============================================================================
Real-World Relevance
===============================================================================

Salary calculations are commonly used in:

- Payroll management systems
- Human resource (HR) software
- Employee compensation applications
- Financial reporting systems
- Business automation tools

===============================================================================
Key Takeaways
===============================================================================

- Lambda functions can perform practical business calculations.
- Percentage values must be divided by 100 before applying them.
- Parentheses improve readability and reduce the chance of calculation errors.
- Lambda functions are ideal for short mathematical expressions that return a
  single result.
===============================================================================
"""