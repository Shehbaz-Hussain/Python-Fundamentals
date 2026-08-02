"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 03
Exercise Title: Find the Larger Number Using a Lambda Function
Difficulty: Beginner

Objective:
    Create a lambda function that accepts two numbers and returns the larger
    value using a conditional expression. Store the lambda function in a
    meaningful variable and test it with different pairs of numbers.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a lambda function that returns the larger of two numbers.
find_larger = lambda first_number, second_number: (
    first_number if first_number >= second_number else second_number
)

# Call the lambda function with different pairs of numbers.
print(find_larger(10, 15))
print(find_larger(42, 18))
print(find_larger(8, 8))


"""
===============================================================================
Expected Output
===============================================================================

15
42
8

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A lambda function is created using the 'lambda' keyword.
2. The function accepts two parameters:
       - first_number
       - second_number
3. A conditional expression compares both values.
4. If 'first_number' is greater than or equal to 'second_number', it is
   returned; otherwise, 'second_number' is returned.
5. The lambda function is stored in the variable 'find_larger'.
6. The function is called three times using different pairs of numbers,
   including equal values.
7. Each returned value is displayed using the print() function.

How the Lambda Expression Works
-------------------------------

Lambda expression:

    lambda first_number, second_number:
        first_number if first_number >= second_number else second_number

- 'lambda' creates an anonymous function.
- The function accepts two parameters.
- The conditional expression compares the two values.
- If the condition is True, the first number is returned.
- Otherwise, the second number is returned.
- The result is returned automatically without using the 'return' keyword.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- Anonymous functions
- Multiple parameters
- Conditional expressions
- Comparison operators
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(1)

Explanation:
Comparing two numbers requires constant time.

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
- Keep lambda expressions concise and readable.
- Use a conditional expression only for simple decision-making.
- Test the function with different input values, including equal numbers.

===============================================================================
Common Mistakes
===============================================================================

- Using the 'def' keyword instead of a lambda function.
- Forgetting the 'else' part of the conditional expression.
- Reversing the comparison logic.
- Forgetting to assign the lambda function to a variable.
- Not testing the function with equal values.

===============================================================================
Alternative Approach
===============================================================================

Another valid implementation is:

    find_larger = lambda a, b: a if a > b else b

This also returns the larger value, but when both numbers are equal, it returns
the second operand instead of the first. Both produce the same numeric result.

===============================================================================
Real-World Relevance
===============================================================================

Conditional lambda functions are commonly used in:

- Data preprocessing
- Business rule evaluation
- Report generation
- Data validation
- Automation workflows

===============================================================================
Key Takeaways
===============================================================================

- Lambda functions can include conditional expressions.
- A conditional expression enables simple decision-making in a single
  expression.
- Lambda functions are useful for short comparison operations.
- Meaningful variable names improve code readability and maintainability.
===============================================================================
"""