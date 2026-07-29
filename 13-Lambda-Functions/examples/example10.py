"""
File: example10.py
Topic: Lambda Function with Mathematical Expression

Description:
This example demonstrates how lambda functions can perform
mathematical calculations using parameters and expressions.

Concepts Covered:
- Lambda functions with arithmetic operations
- Multiple calculations in one expression
- Automatic return values

Python Version:
Python 3.13+
"""


# Creating a lambda function to calculate the area of a rectangle
calculate_area = lambda length, width: length * width


# Passing values to the lambda function
area = calculate_area(12, 5)


# Displaying the returned value
print(area)


"""
Expected Output:

60


Explanation:

1. The lambda function accepts two parameters:
   - length
   - width

2. The values 12 and 5 are passed as arguments.

3. The expression:

   length * width

   calculates the area of the rectangle.

4. Lambda functions automatically return the result
   of their expression.

5. The calculated area is stored in the variable 'area'.

Best Practice:

Lambda functions are suitable for simple mathematical
calculations. If a calculation requires multiple steps or
complex logic, use a regular function.

Real-World Relevance:

Simple mathematical lambda functions are useful in data
processing, scientific calculations, automation scripts,
and situations where short calculations are required.
"""