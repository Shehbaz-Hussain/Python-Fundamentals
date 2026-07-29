"""
File: example08.py
Topic: Lambda Function with Boolean Return Values

Description:
This example demonstrates how lambda functions can return Boolean
values by evaluating a condition.

Concepts Covered:
- Lambda functions with conditions
- Boolean return values
- Comparison operators with lambda functions

Python Version:
Python 3.13+
"""


# Creating a lambda function that checks if a number is positive
is_positive = lambda number: number > 0


# Passing values to the lambda function
first_result = is_positive(15)
second_result = is_positive(-5)


# Displaying the returned Boolean values
print(first_result)
print(second_result)


"""
Expected Output:

True
False


Explanation:

1. The lambda function receives one parameter named 'number'.
2. The expression checks whether the value is greater than zero.
3. The comparison operation returns either True or False.
4. Lambda functions automatically return the result of the expression.
5. Different arguments produce different Boolean results.

Best Practice:

Lambda functions are suitable for short condition checks.
For complex validation rules, use a regular function with a
descriptive name.

Real-World Relevance:

Boolean lambda functions are commonly used with functions such
as filter() to select data based on conditions, validate values,
and create simple decision rules in applications.
"""