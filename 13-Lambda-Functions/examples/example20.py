"""
File: example20.py
Topic: Lambda Function for Data Cleaning

Description:
This example demonstrates how lambda functions can be used with
map() to clean and standardize text data.

Concepts Covered:
- Lambda functions with map()
- String transformation
- Data cleaning

Python Version:
Python 3.13+
"""


# Creating a list of user-entered names with extra spaces
names = [
    "  Ali  ",
    " Sara ",
    "  Ahmed",
    "Zain  "
]


# Removing extra spaces from each name
clean_names = list(
    map(
        lambda name: name.strip(),
        names
    )
)


# Displaying cleaned names
print(clean_names)


"""
Expected Output:

['Ali', 'Sara', 'Ahmed', 'Zain']


Explanation:

1. A list containing names with unnecessary spaces is created.
2. The map() function applies the lambda function to every name.
3. The lambda function uses strip() to remove extra spaces.
4. Each cleaned name is added to the new list.
5. The final cleaned data is stored in 'clean_names'.

Best Practice:

Use lambda functions for simple data cleaning operations.
When cleaning rules become more complicated, use regular
functions to improve readability and maintainability.

Real-World Relevance:

Data cleaning is an essential step in data science, machine
learning, analytics, and software systems where user input
must be standardized before processing.
"""