"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Exercise 19: Customer Information Processing Using Lambda Functions

Difficulty:
Intermediate–Advanced

Estimated Time:
25–35 Minutes

Objective:
Practice processing customer information using lambda functions together
with map(), filter(), sorted(), and the key parameter.

Instructions:
A company stores customer records in the following format:

(Name, City, Total Purchase Amount)

Create the following list:

customers = [
    ("Ali", "Gilgit", 18500),
    ("Sara", "Islamabad", 72000),
    ("Ahmed", "Lahore", 46000),
    ("Ayesha", "Karachi", 98000),
    ("Usman", "Gilgit", 25000),
    ("Fatima", "Peshawar", 81000)
]

Perform the following tasks:

1. Display the original customer records.

2. Use map() with a lambda function to create a list containing only
   customer names.

3. Use filter() with a lambda function to create a list of customers
   whose total purchase amount is greater than or equal to 50,000.

4. Use sorted() with the key parameter and a lambda function to sort
   the customer records by purchase amount in descending order.

5. Display all generated results using clear headings.

Expected Output Format:

Original Customers:
...

Customer Names:
...

Customers with Purchases ≥ 50,000:
...

Customers Sorted by Purchase Amount:
...

Requirements:
- Use lambda functions.
- Use map().
- Use filter().
- Use sorted().
- Keep the original customer list unchanged.
- Follow PEP 8 style guidelines.

Challenge:
1. Create another sorted list ordered alphabetically by city and then
   by customer name.
2. Use map() with a lambda function to create a new list showing each
   customer's name along with a 10% loyalty bonus based on their total
   purchase amount.
===============================================================================
"""