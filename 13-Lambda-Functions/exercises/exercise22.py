"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Exercise 22: Business Logic - Customer Discount Processing

Difficulty:
Advanced

Estimated Time:
35–45 Minutes

Objective:
Apply lambda functions to implement business rules for customer discounts
using map(), filter(), sorted(), and reduce().

Instructions:
An online store stores customer orders in the following format:

(Customer Name, Membership Type, Order Amount)

Create the following list:

orders = [
    ("Ali", "Gold", 25000),
    ("Sara", "Silver", 18000),
    ("Ahmed", "Gold", 42000),
    ("Ayesha", "Platinum", 55000),
    ("Usman", "Silver", 16000),
    ("Fatima", "Gold", 39000),
    ("Bilal", "Platinum", 61000),
    ("Hina", "Silver", 21000)
]

Business Rules:

- Platinum members receive a 20% discount.
- Gold members receive a 10% discount.
- Silver members receive a 5% discount.

Perform the following tasks:

1. Display the original order records.

2. Use map() with a lambda function to create a new list containing:

   (
       Customer Name,
       Membership Type,
       Original Amount,
       Discount Amount,
       Final Amount
   )

3. Use filter() with a lambda function to display only customers whose
   final payable amount is greater than or equal to 30,000.

4. Import reduce from functools and calculate the total value of all
   final payable amounts.

5. Use sorted() with the key parameter and a lambda function to sort
   customers by their final payable amount in descending order.

6. Display every generated result clearly.

Requirements:
- Use lambda functions.
- Use map(), filter(), reduce(), and sorted().
- Do not modify the original dataset.
- Follow PEP 8 style guidelines.

Challenge:

1. Count how many customers belong to each membership category.
2. Display only Platinum customers.
3. Produce a report sorted alphabetically by customer name.
4. Calculate the average final payable amount.
===============================================================================
"""