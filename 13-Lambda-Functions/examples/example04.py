"""
File: example04.py
Topic: Lambda Function with String Parameters

Description:
This example demonstrates how lambda functions can accept string
parameters and create formatted text output.

Concepts Covered:
- Lambda functions with string parameters
- String formatting
- Passing string arguments

Python Version:
Python 3.13+
"""


# Creating a lambda function that formats a greeting message
create_greeting = lambda name: f"Hello, {name}!"


# Passing a string argument to the lambda function
message = create_greeting("Shehbaz")


# Displaying the returned value
print(message)


"""
Expected Output:

Hello, Shehbaz!


Explanation:

1. The lambda function receives one parameter named 'name'.
2. The string "Shehbaz" is passed as an argument.
3. The f-string combines the text with the provided name.
4. The lambda function automatically returns the generated message.
5. The returned string is stored in the variable 'message'.

Best Practice:

Use lambda functions with strings for simple formatting
operations. If the text processing becomes complex, use a
regular function for better readability.

Real-World Relevance:

String-based lambda functions are commonly used in data
processing, formatting output, generating labels, and preparing
text data for applications.
"""