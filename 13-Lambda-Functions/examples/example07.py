"""
File: example07.py
Topic: Lambda Function with Multiple Arguments

Description:
This example demonstrates how lambda functions can accept multiple
arguments and perform an operation using all provided values.

Concepts Covered:
- Multiple lambda parameters
- Passing multiple arguments
- Arithmetic operations with lambda functions

Python Version:
Python 3.13+
"""


# Creating a lambda function with three parameters
calculate_total = lambda first, second, third: first + second + third


# Passing three arguments to the lambda function
total = calculate_total(10, 20, 30)


# Displaying the returned value
print(total)


"""
Expected Output:

60


Explanation:

1. The lambda function accepts three parameters:
   - first
   - second
   - third

2. The values 10, 20, and 30 are passed as arguments.

3. The expression:
   
   first + second + third

   adds all three values together.

4. Lambda functions automatically return the result
   of their expression.

5. The final result is stored in the variable 'total'.

Best Practice:

Use multiple parameters in lambda functions only when the
calculation remains simple and understandable.

Real-World Relevance:

Lambda functions with multiple arguments are useful for small
calculations, combining values, custom sorting rules, and
simple data processing tasks.
"""