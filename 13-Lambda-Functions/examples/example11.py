"""
File: example11.py
Topic: Using Lambda Function with map()

Description:
This example demonstrates how lambda functions can be used with
the map() function to transform every element in an iterable.

Concepts Covered:
- Lambda functions with map()
- Data transformation
- Applying operations to multiple values

Python Version:
Python 3.13+
"""


# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]


# Using map() with a lambda function to double each number
doubled_numbers = list(
    map(lambda number: number * 2, numbers)
)


# Displaying the transformed list
print(doubled_numbers)


"""
Expected Output:

[2, 4, 6, 8, 10]


Explanation:

1. A list containing five numbers is created.
2. The map() function applies the lambda function to every item.
3. The lambda parameter 'number' receives each value one by one.
4. Each number is multiplied by 2.
5. The transformed values are converted into a list.
6. The final list is stored in 'doubled_numbers'.

Best Practice:

Use map() with lambda functions when the same simple
transformation needs to be applied to every element.
For complex transformations, use a regular function.

Real-World Relevance:

map() with lambda functions is commonly used in data
preprocessing, feature transformation, automation scripts,
and machine learning data preparation workflows.
"""