"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 02
Exercise Title: Add Two Numbers Using a Lambda Function
Difficulty: Beginner

Objective:
    Create a lambda function that accepts two numbers and returns their sum.
    Store the lambda function in a variable and call it using different pairs
    of integer values.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a lambda function that returns the sum of two numbers.
add_numbers = lambda first_number, second_number: first_number + second_number

# Call the lambda function with different pairs of integer values.
print(add_numbers(10, 5))
print(add_numbers(20, 22))
print(add_numbers(100, 3))


"""
===============================================================================
Expected Output
===============================================================================

15
42
103

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A lambda function is created using the 'lambda' keyword.
2. The function accepts two parameters:
       - first_number
       - second_number
3. The expression 'first_number + second_number' calculates the sum.
4. The lambda function is stored in the variable 'add_numbers'.
5. The function is called three times with different values.
6. Each result is displayed using the print() function.

How the Lambda Expression Works
-------------------------------

Lambda expression:

    lambda first_number, second_number: first_number + second_number

- 'lambda' creates an anonymous function.
- The function accepts two parameters.
- The expression adds both numbers.
- The computed value is returned automatically.
- Assigning the lambda to 'add_numbers' allows it to be reused.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- Anonymous functions
- Multiple parameters
- Arithmetic operations
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(1)

Explanation:
Adding two numbers requires constant time.

===============================================================================
Space Complexity
===============================================================================

O(1)

Explanation:
The solution uses only a constant amount of additional memory.

===============================================================================
Best Practices
===============================================================================

- Use descriptive variable names.
- Keep lambda expressions concise.
- Use meaningful parameter names.
- Reserve lambda functions for simple operations.

===============================================================================
Common Mistakes
===============================================================================

- Using the 'def' keyword.
- Forgetting to assign the lambda to a variable.
- Using an incorrect number of parameters.
- Writing multiple expressions inside the lambda.
- Forgetting to call the lambda function.

===============================================================================
Alternative Approach
===============================================================================

Use shorter parameter names:

    add_numbers = lambda a, b: a + b

===============================================================================
Real-World Relevance
===============================================================================

Simple lambda expressions are commonly used in:

- Data preprocessing
- Financial calculations
- Business analytics
- Automation scripts
- Data transformation pipelines

===============================================================================
Key Takeaways
===============================================================================

- Lambda functions can accept multiple parameters.
- They automatically return the value of their expression.
- They are useful for short arithmetic operations and other simple tasks.
===============================================================================
"""