"""
File: example24.py
Topic: Lambda Function for Processing Customer Data

Description:
This example demonstrates how lambda functions can be used to
extract and transform information from customer records.

Concepts Covered:
- Lambda functions with map()
- Extracting values from structured data
- Data transformation

Python Version:
Python 3.13+
"""


# Creating customer records
customers = [
    ("Ali", "Pakistan"),
    ("Sara", "United Kingdom"),
    ("Ahmed", "Canada"),
    ("Zain", "Australia")
]


# Extracting customer names using map() and lambda
customer_names = list(
    map(
        lambda customer: customer[0],
        customers
    )
)


# Displaying extracted customer names
print(customer_names)


"""
Expected Output:

['Ali', 'Sara', 'Ahmed', 'Zain']


Explanation:

1. A list of customer records is created.
2. Each record contains:
   - Customer name
   - Customer country

3. The map() function applies the lambda function to each record.
4. The lambda function extracts the first value from every tuple.
5. The extracted names are stored in a new list.

Best Practice:

Use lambda functions with map() for simple extraction and
transformation tasks. For complex customer processing logic,
use regular functions with descriptive names.

Real-World Relevance:

Extracting and transforming customer information is common in
customer relationship management systems, databases, analytics
platforms, backend applications, and machine learning data
preparation pipelines.
"""