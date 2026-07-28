"""
File: example02.py
Topic: Lambda Function with Parameters

Description:
This example demonstrates how lambda functions can accept parameters
and use those values inside their expression.

Concepts Covered:
- Lambda parameters
- Passing arguments to lambda functions
- Automatic return values

Python Version:
Python 3.13+
"""


# Creating a lambda function with one parameter
square_number = lambda number: number ** 2


# Passing an argument to the lambda function
result = square_number(7)


# Displaying the returned value
print(result)


"""
Expected Output:

49


Explanation:

1. The lambda function receives one parameter named 'number'.
2. The value 7 is passed as an argument.
3. The expression number ** 2 calculates the square of 7.
4. Lambda functions automatically return the expression result.
5. The returned value is stored in 'result'.

Best Practice:

Use lambda functions when the operation is short, clear, and
requires only a single expression.

Real-World Relevance:

Lambda functions with parameters are commonly used for small
calculations, data transformations, and as callback functions
in Python applications.
"""