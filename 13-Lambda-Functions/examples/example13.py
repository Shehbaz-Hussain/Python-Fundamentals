"""
File: example13.py
Topic: Using Lambda Function with sorted()

Description:
This example demonstrates how lambda functions can be used with
the sorted() function to define a custom sorting rule.

Concepts Covered:
- Lambda functions with sorted()
- key parameter
- Custom sorting logic

Python Version:
Python 3.13+
"""


# Creating a list of words
words = ["Python", "AI", "Programming", "Code"]


# Sorting words based on their length
sorted_words = sorted(
    words,
    key=lambda word: len(word)
)


# Displaying the sorted list
print(sorted_words)


"""
Expected Output:

['AI', 'Code', 'Python', 'Programming']


Explanation:

1. A list of words is created.
2. The sorted() function arranges the items according to a rule.
3. The key parameter receives a lambda function.
4. The lambda function calculates the length of each word.
5. Python uses those lengths to determine the sorting order.
6. The sorted result is stored in 'sorted_words'.

Best Practice:

Use lambda functions with sorted() when the sorting rule is
short and easy to understand. For complicated sorting logic,
use a regular function with a descriptive name.

Real-World Relevance:

Custom sorting with lambda functions is widely used for sorting
records, ranking data, organizing files, and preparing datasets
for analysis or machine learning workflows.
"""