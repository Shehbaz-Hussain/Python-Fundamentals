"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 01
Exercise Title: Create Your First Lambda Function
Difficulty: Beginner

Objective:
    Create a basic lambda function that accepts one number and returns its
    square. Store the lambda function in a variable and call it using
    different integer values.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a lambda function that returns the square of a number.
square_number = lambda number: number * number

# Call the lambda function with different integer values.
print(square_number(3))
print(square_number(5))
print(square_number(10))


"""
===============================================================================
Expected Output
===============================================================================

9
25
100

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A lambda function is created using the lambda keyword.
2. The function accepts one parameter named 'number'.
3. The expression 'number * number' calculates the square of the value.
4. The lambda function is stored in the variable 'square_number'.
5. The function is called three times with different integer values:
       - 3
       - 5
       - 10
6. Each returned result is displayed using the print() function.

How the Lambda Expression Works
-------------------------------

Lambda expression:

    lambda number: number * number

- 'lambda' creates an anonymous function.
- 'number' is the single parameter.
- 'number * number' is the expression whose result is automatically returned.
- Assigning the lambda to 'square_number' allows it to be reused like a normal
  function.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- Anonymous functions
- Function parameters
- Return values
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(1)

Explanation:
Squaring a single integer requires constant time.

===============================================================================
Space Complexity
===============================================================================

O(1)

Explanation:
The solution uses only a constant amount of additional memory.

===============================================================================
Best Practices
===============================================================================

- Store lambda functions in descriptive variables.
- Keep lambda expressions short and readable.
- Use meaningful parameter names.
- Use lambda functions only for simple operations.

===============================================================================
Common Mistakes
===============================================================================

- Using 'def' instead of 'lambda'.
- Forgetting to store the lambda in a variable.
- Using multiple parameters.
- Forgetting to call the lambda function.
- Using an incorrect expression for squaring.

===============================================================================
Alternative Approach
===============================================================================

Use the exponentiation operator:

    square_number = lambda number: number ** 2

===============================================================================
Real-World Relevance
===============================================================================

Simple lambda functions are frequently used for small calculations during:

- Data preprocessing
- Automation
- Business analytics
- Machine learning feature engineering

===============================================================================
Key Takeaways
===============================================================================

- Lambda functions are anonymous functions.
- They automatically return the result of their expression.
- They are ideal for short, single-expression operations.
===============================================================================
"""