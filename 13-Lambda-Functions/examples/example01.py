"""
File: example01.py
Topic: Basic Lambda Function Syntax

Description:
This example demonstrates the basic syntax of a lambda function.
A lambda function is a small anonymous function that contains a single expression.

Concepts Covered:
- Lambda function creation
- Calling a lambda function
- Automatic return value

Python Version:
Python 3.13+
"""


# Creating a lambda function that adds 5 to a number
add_five = lambda number: number + 5


# Calling the lambda function
result = add_five(10)


# Displaying the result
print(result)


"""
Expected Output:

15


Explanation:

1. The lambda function receives the value 10.
2. The parameter 'number' stores the value 10.
3. The expression number + 5 is evaluated.
4. The result 15 is automatically returned.
5. The returned value is stored in the variable 'result'.

Best Practice:

Use lambda functions for small and simple operations.
For complex logic, prefer regular functions created with 'def'.

Real-World Relevance:

Simple lambda functions are commonly used for short calculations,
data processing operations, and as arguments to functions like
map(), filter(), and sorted().
"""