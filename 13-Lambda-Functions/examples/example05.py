"""
File: example05.py
Topic: Lambda Function Without Parameters

Description:
This example demonstrates how to create and use a lambda function
that does not require any parameters.

Concepts Covered:
- Parameterless lambda functions
- Calling lambda functions
- Automatic return values

Python Version:
Python 3.13+
"""


# Creating a lambda function without parameters
get_message = lambda: "Learning Python Lambda Functions"


# Calling the lambda function
message = get_message()


# Displaying the returned value
print(message)


"""
Expected Output:

Learning Python Lambda Functions


Explanation:

1. The lambda function does not contain any parameters.
2. The expression returns a string value directly.
3. The lambda function is called using empty parentheses.
4. The returned string is stored in the variable 'message'.
5. The value is displayed using the print() function.

Best Practice:

Parameterless lambda functions are valid in Python but are
less common. Use them only when the operation is very simple
and a regular function would add unnecessary complexity.

Real-World Relevance:

Parameterless lambda functions can be useful for simple
callbacks, event handling, and situations where a small
function needs to return a fixed value.
"""