"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Exercise 21: Sales Data Analytics Dashboard

Difficulty:
Advanced

Estimated Time:
35–45 Minutes

Objective:
Use lambda functions together with map(), filter(), reduce(), and
sorted() to perform basic data analytics on sales records.

Instructions:
A retail company stores sales information in the following format:

(Product, Category, Units Sold, Unit Price)

Create the following list:

sales_data = [
    ("Laptop", "Electronics", 15, 95000),
    ("Mouse", "Electronics", 120, 1800),
    ("Desk", "Furniture", 18, 22000),
    ("Chair", "Furniture", 35, 12000),
    ("Monitor", "Electronics", 22, 38000),
    ("Printer", "Electronics", 10, 27000)
]

Perform the following tasks:

1. Display the original sales records.

2. Use map() with a lambda function to create a new list containing:
   (Product Name, Total Revenue)

   Revenue = Units Sold × Unit Price

3. Use filter() with a lambda function to extract products whose
   revenue exceeds 500,000.

4. Import reduce from functools and calculate the total company
   revenue.

5. Use sorted() with a lambda function to sort products by revenue
   from highest to lowest.

6. Display all results with appropriate headings.

Requirements:
- Use lambda functions.
- Use map(), filter(), reduce(), and sorted().
- Keep the original dataset unchanged.
- Follow PEP 8 style guidelines.

Challenge:
1. Calculate the average revenue per product.
2. Display the three highest-revenue products.
3. Create a list containing only product names in uppercase using
   another lambda expression.

===============================================================================
"""