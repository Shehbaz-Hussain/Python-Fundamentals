"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 07
Exercise Title: Calculate the Average of Three Numbers
Difficulty: Beginner

Objective:
    Create a lambda function that accepts three numbers and returns their
    average. Store the lambda function in a meaningful variable and test it
    using different sets of values.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a lambda function that calculates the average of three numbers.
calculate_average = (
    lambda first_number, second_number, third_number:
    (first_number + second_number + third_number) / 3
)

# Call the lambda function with different sets of values.
print(calculate_average(10, 15, 20))
print(calculate_average(5, 10, 10))
print(calculate_average(-5, 0, 5))
print(calculate_average(40, 44, 44))


"""
===============================================================================
Expected Output
===============================================================================

15.0
8.333333333333334
0.0
42.666666666666664

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A lambda function is created using the 'lambda' keyword.
2. The function accepts three parameters:
       - first_number
       - second_number
       - third_number
3. The three numbers are added together.
4. The total is divided by 3 to calculate the average.
5. The lambda function is stored in the variable 'calculate_average'.
6. The function is called four times using different sets of values,
   including positive, negative, and zero values.
7. Each calculated average is displayed using the print() function.

How the Lambda Expression Works
-------------------------------

Lambda expression:

    lambda first_number, second_number, third_number:
        (first_number + second_number + third_number) / 3

- 'lambda' creates an anonymous function.
- The function accepts three input parameters.
- The expression adds the three numbers.
- The sum is divided by 3 to calculate the average.
- The result is returned automatically without using the 'return' keyword.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- Multiple parameters
- Return values
- Arithmetic operations
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(1)

Explanation:
The calculation performs a fixed number of arithmetic operations, regardless
of the input values.

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
- Use parentheses to improve the readability of mathematical expressions.
- Keep lambda expressions concise and limited to a single calculation.
- Test the function with different types of numeric values.

===============================================================================
Common Mistakes
===============================================================================

- Forgetting to divide the sum by 3.
- Dividing only the last number by 3 because of missing parentheses.
- Using the 'def' keyword instead of a lambda function.
- Forgetting to assign the lambda function to a variable.
- Testing with only one set of input values.

===============================================================================
Alternative Approach
===============================================================================

Another valid implementation is:

    calculate_average = lambda a, b, c: (a + b + c) / 3

This produces the same result while using shorter parameter names.

===============================================================================
Real-World Relevance
===============================================================================

Average calculations are widely used in:

- Student grade management systems
- Data analysis
- Business reporting
- Scientific calculations
- Performance evaluation dashboards

===============================================================================
Key Takeaways
===============================================================================

- Lambda functions can accept multiple parameters.
- Mathematical formulas can be written as a single lambda expression.
- Parentheses improve readability and help avoid calculation errors.
- Lambda functions are suitable for short calculations that return a single
  value.
===============================================================================
"""