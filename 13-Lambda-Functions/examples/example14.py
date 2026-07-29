"""
File: example14.py
Topic: Using Lambda Function with Multiple Iterables

Description:
This example demonstrates how lambda functions can work with
multiple iterables using the map() function.

Concepts Covered:
- Lambda functions with multiple parameters
- map() with multiple iterables
- Combining values from different collections

Python Version:
Python 3.13+
"""


# Creating two lists of numbers
first_numbers = [1, 2, 3, 4]
second_numbers = [10, 20, 30, 40]


# Using map() with a lambda function to add values from both lists
combined_numbers = list(
    map(
        lambda first, second: first + second,
        first_numbers,
        second_numbers
    )
)


# Displaying the combined results
print(combined_numbers)


"""
Expected Output:

[11, 22, 33, 44]


Explanation:

1. Two lists containing numbers are created.
2. The map() function processes elements from both lists.
3. The lambda function receives two parameters:
   - first
   - second

4. During each iteration:
   - first receives a value from first_numbers.
   - second receives a value from second_numbers.

5. The lambda expression adds both values together.
6. The resulting values are stored in a new list.

Best Practice:

When using lambda functions with multiple iterables, make sure
the relationship between the values is clear and the operation
remains simple.

Real-World Relevance:

Processing multiple data sources together is common in data
analysis, machine learning preprocessing, financial calculations,
and automation workflows.
"""