"""
File: example12.py
Topic: Using Lambda Function with filter()

Description:
This example demonstrates how lambda functions can be used with
the filter() function to select elements that satisfy a condition.

Concepts Covered:
- Lambda functions with filter()
- Boolean conditions
- Filtering data

Python Version:
Python 3.13+
"""


# Creating a list of numbers
numbers = [10, 15, 20, 25, 30]


# Using filter() with a lambda function to select even numbers
even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)


# Displaying the filtered values
print(even_numbers)


"""
Expected Output:

[10, 20, 30]


Explanation:

1. A list containing different numbers is created.
2. The filter() function checks each element in the list.
3. The lambda function tests whether each number is divisible
   by 2.
4. If the condition returns True, the number is kept.
5. If the condition returns False, the number is removed.
6. The filtered values are converted into a list.

Best Practice:

Use filter() with lambda functions for simple selection
conditions. If the filtering logic becomes complex, create a
regular function with a descriptive name.

Real-World Relevance:

filter() with lambda functions is commonly used for data
cleaning, validation, searching records, and selecting relevant
data from large datasets.
"""