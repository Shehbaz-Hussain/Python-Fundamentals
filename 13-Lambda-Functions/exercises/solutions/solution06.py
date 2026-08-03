"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 06
Exercise Title: Calculate the Area of a Rectangle
Difficulty: Beginner

Objective:
    Create a lambda function that accepts the length and width of a rectangle
    and returns its area. Store the lambda function in a meaningful variable
    and test it using different rectangle dimensions.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a lambda function that calculates the area of a rectangle.
calculate_area = lambda length, width: length * width

# Call the lambda function with different rectangle dimensions.
print(calculate_area(4, 5))
print(calculate_area(6, 6))
print(calculate_area(12, 7))
print(calculate_area(15, 15))


"""
===============================================================================
Expected Output
===============================================================================

20
36
84
225

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A lambda function is created using the 'lambda' keyword.
2. The function accepts two parameters:
       - length
       - width
3. The expression 'length * width' calculates the area of the rectangle.
4. The lambda function is stored in the variable 'calculate_area'.
5. The function is called four times using different rectangle dimensions,
   including both rectangles and a square.
6. Each calculated area is displayed using the print() function.

How the Lambda Expression Works
-------------------------------

Lambda expression:

    lambda length, width: length * width

- 'lambda' creates an anonymous function.
- 'length' and 'width' are the input parameters.
- The multiplication operator (*) calculates the rectangle's area.
- The result of the expression is returned automatically.
- The lambda function can be reused with different dimensions.

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
Calculating the area requires a single multiplication, which takes constant
time.

===============================================================================
Space Complexity
===============================================================================

O(1)

Explanation:
The solution uses a constant amount of additional memory.

===============================================================================
Best Practices
===============================================================================

- Use descriptive variable names such as 'calculate_area'.
- Choose meaningful parameter names that reflect their purpose.
- Keep lambda expressions simple and limited to a single calculation.
- Test the function with different rectangle dimensions to verify correctness.

===============================================================================
Common Mistakes
===============================================================================

- Using the 'def' keyword instead of a lambda function.
- Adding the length and width instead of multiplying them.
- Reversing the formula with an incorrect arithmetic operation.
- Forgetting to assign the lambda function to a variable.
- Not testing both rectangular and square dimensions.

===============================================================================
Alternative Approach
===============================================================================

Another valid implementation is:

    calculate_area = lambda l, w: l * w

Using shorter parameter names produces the same result, although descriptive
names generally improve readability.

===============================================================================
Real-World Relevance
===============================================================================

Area calculations are commonly used in:

- Construction and architecture
- Interior design
- Land measurement
- Inventory and packaging systems
- Engineering and CAD applications

===============================================================================
Key Takeaways
===============================================================================

- Lambda functions can perform mathematical calculations with multiple
  parameters.
- The area of a rectangle is calculated by multiplying its length by its width.
- Lambda functions automatically return the result of their expression.
- Descriptive variable and parameter names make code easier to understand and
  maintain.
===============================================================================
"""