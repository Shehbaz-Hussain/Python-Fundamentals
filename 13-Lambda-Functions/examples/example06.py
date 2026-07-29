"""
File: example06.py
Topic: Lambda Function with Default Parameters

Description:
This example demonstrates how lambda functions can use default
parameter values. Default parameters allow a lambda function to
use a predefined value when an argument is not provided.

Concepts Covered:
- Lambda functions with default parameters
- Optional arguments
- Automatic return values

Python Version:
Python 3.13+
"""


# Creating a lambda function with a default parameter
greet_user = lambda name="Guest": f"Hello, {name}!"


# Calling the lambda function without providing an argument
default_message = greet_user()


# Calling the lambda function with a custom argument
custom_message = greet_user("Ali")


# Displaying the returned values
print(default_message)
print(custom_message)


"""
Expected Output:

Hello, Guest!
Hello, Ali!


Explanation:

1. The lambda function has one parameter named 'name'.
2. The parameter has a default value of "Guest".
3. When no argument is provided, Python uses the default value.
4. When "Ali" is passed, it replaces the default value.
5. The lambda function automatically returns the generated string.

Best Practice:

Use default parameters in lambda functions only for simple
cases. If the function requires complex default logic, use a
regular function created with 'def'.

Real-World Relevance:

Default parameters are useful when creating simple formatting
functions, configuration helpers, and callback functions where
a common default value is needed.
"""