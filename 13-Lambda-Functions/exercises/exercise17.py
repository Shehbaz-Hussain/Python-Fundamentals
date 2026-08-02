"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Exercise 17: Product Data Processing with Lambda Functions

Difficulty:
Intermediate–Advanced

Estimated Time:
25–30 Minutes

Objective:
Practice processing product information using lambda functions together
with map(), filter(), and sorted().

Instructions:
An online store stores product records in the following format:

(Product Name, Category, Price)

Create the following list:

products = [
    ("Laptop", "Electronics", 95000),
    ("Keyboard", "Electronics", 3500),
    ("Chair", "Furniture", 12000),
    ("Mouse", "Electronics", 1800),
    ("Desk", "Furniture", 22000),
    ("Monitor", "Electronics", 38000)
]

Perform the following tasks:

1. Display the original product records.

2. Use map() with a lambda function to create a new list containing
   product names converted to uppercase.

3. Use filter() with a lambda function to create a list of products
   whose price is greater than 20,000.

4. Use sorted() with the key parameter and a lambda function to sort
   the products by price in descending order.

5. Display each result with clear headings.

Expected Output Format:

Original Products:
...

Product Names (Uppercase):
...

Products Above 20,000:
...

Products Sorted by Price (High to Low):
...

Requirements:
- Use lambda functions.
- Use map().
- Use filter().
- Use sorted().
- Keep the original list unchanged.
- Follow PEP 8 style guidelines.

Challenge:
Create another sorted list that orders the products alphabetically by
their category and then by product name using an appropriate lambda
expression.
===============================================================================
"""