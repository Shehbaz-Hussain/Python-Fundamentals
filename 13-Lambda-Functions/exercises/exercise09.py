"""
===============================================================================
File Name: exercise09.py
Exercise Title: Calculate the Final Price After Discount
Topic: Lambda Functions with Parameters and Return Values
Description:
    Practice creating a lambda function that accepts a product price and a
    discount percentage, then returns the final price after applying the
    discount.

Concepts Covered:
    - Lambda functions
    - Multiple parameters
    - Return values
    - Arithmetic operations
    - Percentage calculations
    - Function invocation

Python Version:
    Python 3.13+
===============================================================================

Learning Objective
------------------
Learn how to create a lambda function that performs a practical business
calculation using multiple parameters and returns the computed result.

Problem Statement
-----------------
Create a lambda function that accepts:
- the original product price
- the discount percentage

The function should return the final price after subtracting the discount.

Store the lambda function in a meaningful variable and test it using different
prices and discount percentages.

Requirements
------------
1. Create a lambda function with two parameters:
   - original_price
   - discount_percentage
2. Calculate the discount amount.
3. Return the final price after applying the discount.
4. Store the lambda function in a meaningful variable.
5. Call the function with at least four different sets of values.
6. Display each result using the print() function.

Constraints
-----------
- Use a lambda function.
- Do not define a regular function using the `def` keyword.
- The lambda expression must contain only one expression.
- Assume all prices and discount percentages are valid.
- Use meaningful variable names.

Hints
-----
- The discount amount can be calculated as:

    original_price * discount_percentage / 100

- Subtract the discount amount from the original price.
- Test the function with discounts such as 10%, 20%, and 50%.

Expected Output
---------------
Your output should be similar to the following:

90.0
400.0
675.0
50.0

(The exact values depend on the prices and discount percentages you choose.)

Related Concepts
----------------
- Lambda Functions
- Function Parameters
- Return Values
- Arithmetic Operators
- Percentage Calculations
- Function Calls
- Business Calculations
"""