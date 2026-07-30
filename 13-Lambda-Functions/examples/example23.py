"""
File: example23.py
Topic: Lambda Function for Calculating Discounts

Description:
This example demonstrates how lambda functions can be used for
simple business calculations such as applying discounts to prices.

Concepts Covered:
- Lambda functions with mathematical expressions
- Real-world calculations
- Data transformation

Python Version:
Python 3.13+
"""


# Creating a lambda function to calculate discounted price
apply_discount = lambda price, discount: price - (price * discount / 100)


# Applying a 15% discount to a product price
final_price = apply_discount(200, 15)


# Displaying the calculated price
print(final_price)


"""
Expected Output:

170.0


Explanation:

1. The lambda function receives two parameters:
   - price
   - discount percentage

2. The expression calculates the discount amount:

   price * discount / 100

3. The discount amount is subtracted from the original price.

4. The lambda function automatically returns the final value.

5. The calculated price is stored in 'final_price'.

Best Practice:

Lambda functions are useful for short calculations.
For complex business rules involving multiple conditions,
use a regular function for better readability.

Real-World Relevance:

Discount calculations are common in e-commerce platforms,
billing systems, financial applications, and automation
software.
"""