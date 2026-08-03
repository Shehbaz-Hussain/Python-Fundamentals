"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 04
Exercise Title: Determine Whether a Number Is Even
Difficulty: Beginner

Objective:
    Create a lambda function that accepts an integer and returns True if the
    number is even; otherwise, return False. Store the lambda function in a
    meaningful variable and test it with different integer values.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a lambda function that checks whether a number is even.
is_even = lambda number: number % 2 == 0

# Test the lambda function with different integers.
print(is_even(2))
print(is_even(7))
print(is_even(10))
print(is_even(15))
print(is_even(24))


"""
===============================================================================
Expected Output
===============================================================================

True
False
True
False
True

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A lambda function is created using the 'lambda' keyword.
2. The function accepts one parameter named 'number'.
3. The modulus operator (%) calculates the remainder when the number is divided
   by 2.
4. The expression 'number % 2 == 0' checks whether the remainder is zero.
5. If the remainder is zero, the expression evaluates to True.
6. Otherwise, it evaluates to False.
7. The lambda function is stored in the variable 'is_even'.
8. The function is called with five different integers.
9. Each Boolean result is displayed using the print() function.

How the Lambda Expression Works
-------------------------------

Lambda expression:

    lambda number: number % 2 == 0

- 'lambda' creates an anonymous function.
- 'number' is the input parameter.
- 'number % 2' calculates the remainder after dividing by 2.
- '== 0' checks whether the remainder is zero.
- The comparison returns either True or False automatically.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- Anonymous functions
- Function parameters
- Boolean return values
- Modulus operator
- Comparison operators
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(1)

Explanation:
The modulus operation and comparison both require constant time.

===============================================================================
Space Complexity
===============================================================================

O(1)

Explanation:
The solution uses a constant amount of additional memory.

===============================================================================
Best Practices
===============================================================================

- Use descriptive names such as 'is_even' for Boolean-returning functions.
- Keep lambda expressions concise and focused on a single task.
- Test the function with both even and odd numbers.
- Use direct Boolean expressions instead of unnecessary conditional logic.

===============================================================================
Common Mistakes
===============================================================================

- Forgetting to compare the remainder with zero.
- Using division (/) instead of the modulus (%) operator.
- Returning strings such as "True" and "False" instead of Boolean values.
- Using the 'def' keyword instead of a lambda function.
- Testing with too few input values.

===============================================================================
Alternative Approach
===============================================================================

Another valid implementation is:

    is_even = lambda number: not number % 2

This also returns True for even numbers and False for odd numbers.

===============================================================================
Real-World Relevance
===============================================================================

Even-number checks are commonly used in:

- Data validation
- Scheduling systems
- Numerical computations
- Automation scripts
- Algorithm design and optimization

===============================================================================
Key Takeaways
===============================================================================

- Lambda functions can return Boolean values.
- The modulus operator is commonly used to test divisibility.
- A number is even when the remainder after division by 2 is zero.
- Simple logical checks are ideal use cases for lambda functions.
===============================================================================
"""