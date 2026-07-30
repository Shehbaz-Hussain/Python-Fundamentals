"""
File: example19.py
Topic: Lambda Function for Extracting Specific Data

Description:
This example demonstrates how lambda functions can be used with
map() to extract specific information from structured data.

Concepts Covered:
- Lambda functions with map()
- Extracting values from data
- Data transformation

Python Version:
Python 3.13+
"""


# Creating a list of product records
products = [
    ("Laptop", 1200),
    ("Mouse", 25),
    ("Keyboard", 75),
    ("Monitor", 300)
]


# Extracting product names using map() and lambda
product_names = list(
    map(
        lambda product: product[0],
        products
    )
)


# Displaying extracted product names
print(product_names)


"""
Expected Output:

['Laptop', 'Mouse', 'Keyboard', 'Monitor']


Explanation:

1. A list of product records is created.
2. Each product record contains:
   - Product name
   - Product price

3. The map() function applies the lambda function to every item.
4. The lambda function returns the first element of each tuple.
5. The product names are collected into a new list.

Best Practice:

Use lambda functions with map() for simple data extraction.
For complex data processing, use a regular function with a
descriptive name.

Real-World Relevance:

Extracting specific fields from data is common in databases,
APIs, data science pipelines, machine learning preprocessing,
and backend applications.
"""