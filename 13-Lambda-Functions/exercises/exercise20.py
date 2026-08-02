"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Exercise 20: Sales Data Processing Using Lambda Functions

Difficulty:
Advanced

Estimated Time:
30–40 Minutes

Objective:
Apply lambda functions to a realistic sales dataset by combining
map(), filter(), reduce(), and sorted() to perform business-oriented
data processing tasks.

Instructions:
A company stores monthly sales records in the following format:

(Salesperson, Region, Sales Amount)

Create the following list:

sales = [
    ("Ali", "North", 125000),
    ("Sara", "South", 98000),
    ("Ahmed", "East", 143500),
    ("Ayesha", "West", 167000),
    ("Usman", "North", 89500),
    ("Fatima", "South", 152000),
    ("Bilal", "East", 110000),
    ("Hina", "West", 76000)
]

Perform the following tasks:

1. Display the original sales records.

2. Use map() with a lambda function to create a new list containing
   the names of all salespeople in uppercase.

3. Use filter() with a lambda function to create a list containing
   sales records where the sales amount is at least 120,000.

4. Import reduce from functools and use reduce() with a lambda
   function to calculate the total sales amount.

5. Calculate the average sales amount using the total obtained from
   reduce().

6. Use sorted() with the key parameter and a lambda function to sort
   the records by sales amount in descending order.

7. Display every result using meaningful headings.

Expected Output Format:

Original Sales Records:
...

Salespeople (Uppercase):
...

Sales ≥ 120,000:
...

Total Sales:
...

Average Sales:
...

Sales Sorted by Amount (Highest First):
...

Requirements:
- Use lambda functions.
- Use map().
- Use filter().
- Use reduce().
- Use sorted().
- Keep the original sales list unchanged.
- Follow PEP 8 style guidelines.

Challenge:
1. Create another sorted list ordered by region and then by salesperson.
2. Use map() with a lambda function to generate a new list containing
   each salesperson's name and a projected sales value after a 5%
   increase.
3. Count how many sales records meet or exceed the 120,000 target
   without using a traditional for loop.
===============================================================================
"""