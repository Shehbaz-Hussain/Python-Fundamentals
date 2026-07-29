"""
File: example15.py
Topic: Using Lambda Function with reduce()

Description:
This example demonstrates how lambda functions can be used with
the reduce() function to combine multiple values into a single
result.

Concepts Covered:
- Lambda functions with reduce()
- Importing reduce from functools
- Cumulative operations

Python Version:
Python 3.13+
"""

from functools import reduce


# Creating a list of numbers
numbers = [5, 10, 15, 20]


# Using reduce() with a lambda function to calculate the total
total = reduce(
    lambda first, second: first + second,
    numbers
)


# Displaying the final result
print(total)


"""
Expected Output:

50


Explanation:

1. The reduce() function is imported from the functools module.
2. A list of numbers is created.
3. The lambda function receives two values at a time:
   - first
   - second

4. reduce() repeatedly applies the lambda function:

   5 + 10 = 15
   15 + 15 = 30
   30 + 20 = 50

5. The final combined value is stored in 'total'.

Best Practice:

Use reduce() when multiple values need to be combined into a
single result. For simple operations such as addition, built-in
functions like sum() may be clearer.

Real-World Relevance:

reduce() with lambda functions is useful for aggregation tasks,
data processing pipelines, statistical calculations, and
combining information from collections.
"""