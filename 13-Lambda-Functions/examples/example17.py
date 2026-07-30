"""
File: example17.py
Topic: Lambda Function for Filtering Real-World Data

Description:
This example demonstrates how lambda functions can be used with
filter() to select specific data based on a condition.

Concepts Covered:
- Lambda functions with filter()
- Filtering structured data
- Conditional data selection

Python Version:
Python 3.13+
"""


# Creating a list of employee salaries
salaries = [2500, 4200, 3100, 5800, 1900]


# Filtering salaries greater than or equal to 4000
high_salaries = list(
    filter(
        lambda salary: salary >= 4000,
        salaries
    )
)


# Displaying filtered salaries
print(high_salaries)


"""
Expected Output:

[4200, 5800]


Explanation:

1. A list containing employee salary values is created.
2. The filter() function checks each salary value.
3. The lambda function compares each salary with 4000.
4. Values that satisfy the condition return True.
5. Only matching values are included in the final list.
6. The filtered salaries are stored in 'high_salaries'.

Best Practice:

Use lambda functions with filter() when the filtering condition
is short and clear. For complex business rules, use a regular
function with a meaningful name.

Real-World Relevance:

Filtering data based on conditions is common in software
systems, analytics platforms, financial applications, employee
management systems, and machine learning data preparation.
"""