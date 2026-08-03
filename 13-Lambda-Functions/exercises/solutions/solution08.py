"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 08
Exercise Title: Calculate the Power of a Number
Difficulty: Beginner

Objective:
    Create a lambda function that accepts a base and an exponent, then returns
    the value of the base raised to the given exponent. Store the lambda
    function in a meaningful variable and test it with different values.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a lambda function that calculates the power of a number.
calculate_power = lambda base, exponent: base ** exponent

# Call the lambda function with different base and exponent values.
print(calculate_power(2, 3))
print(calculate_power(5, 2))
print(calculate_power(7, 0))
print(calculate_power(3, 4))


"""
===============================================================================
Expected Output
===============================================================================

8
25
1
81

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A lambda function is created using the 'lambda' keyword.
2. The function accepts two parameters:
       - base
       - exponent
3. The exponentiation operator (**) raises the base to the specified exponent.
4. The lambda function is stored in the variable 'calculate_power'.
5. The function is called four times using different base and exponent values.
6. The calculated result is displayed using the print() function.

How the Lambda Expression Works
-------------------------------

Lambda expression:

    lambda base, exponent: base ** exponent

- 'lambda' creates an anonymous function.
- 'base' is the number to be raised.
- 'exponent' specifies the power.
- The '**' operator performs exponentiation.
- The result of the expression is returned automatically.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- Multiple parameters
- Return values
- Exponentiation operator
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(1)

Explanation:
Exponentiation is treated as a constant-time arithmetic operation for this
exercise.

===============================================================================
Space Complexity
===============================================================================

O(1)

Explanation:
The solution uses a constant amount of additional memory.

===============================================================================
Best Practices
===============================================================================

- Use meaningful variable and parameter names.
- Keep lambda expressions simple and focused on a single calculation.
- Test the function with different exponents, including 0 and 1.
- Use Python's built-in exponentiation operator (**) for clarity and
  readability.

===============================================================================
Common Mistakes
===============================================================================

- Using the multiplication operator (*) instead of the exponentiation operator
  (**).
- Reversing the base and exponent parameters.
- Using the 'def' keyword instead of a lambda function.
- Forgetting to assign the lambda function to a variable.
- Testing with only one input pair.

===============================================================================
Alternative Approach
===============================================================================

Another valid implementation is:

    calculate_power = lambda number, power: number ** power

This uses different parameter names while producing the same result.

===============================================================================
Real-World Relevance
===============================================================================

Exponentiation is commonly used in:

- Scientific computing
- Engineering calculations
- Financial modeling
- Machine learning algorithms
- Mathematical simulations

===============================================================================
Key Takeaways
===============================================================================

- Lambda functions can perform exponentiation using the '**' operator.
- The exponentiation operator raises a base to a specified power.
- Lambda functions automatically return the result of their expression.
- Simple mathematical formulas are well suited for lambda expressions.
===============================================================================
"""