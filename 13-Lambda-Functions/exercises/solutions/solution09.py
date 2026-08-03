"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 09
Exercise Title: Calculate the Final Price After Discount
Difficulty: Beginner

Objective:
    Create a lambda function that accepts the original product price and the
    discount percentage, then returns the final price after applying the
    discount. Store the lambda function in a meaningful variable and test it
    using different prices and discount percentages.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a lambda function that calculates the final price after a discount.
calculate_final_price = (
    lambda original_price, discount_percentage:
    original_price - (original_price * discount_percentage / 100)
)

# Call the lambda function with different prices and discount percentages.
print(calculate_final_price(100, 10))
print(calculate_final_price(500, 20))
print(calculate_final_price(900, 25))
print(calculate_final_price(100, 50))


"""
===============================================================================
Expected Output
===============================================================================

90.0
400.0
675.0
50.0

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A lambda function is created using the 'lambda' keyword.
2. The function accepts two parameters:
       - original_price
       - discount_percentage
3. The discount amount is calculated using the formula:

       original_price * discount_percentage / 100

4. The discount amount is subtracted from the original price.
5. The lambda function is stored in the variable 'calculate_final_price'.
6. The function is called four times with different prices and discount
   percentages.
7. Each calculated final price is displayed using the print() function.

How the Lambda Expression Works
-------------------------------

Lambda expression:

    lambda original_price, discount_percentage:
        original_price - (original_price * discount_percentage / 100)

- 'lambda' creates an anonymous function.
- 'original_price' represents the item's initial price.
- 'discount_percentage' represents the discount rate.
- The discount amount is calculated as a percentage of the original price.
- The calculated discount is subtracted from the original price.
- The final price is returned automatically.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- Multiple parameters
- Return values
- Arithmetic operations
- Percentage calculations
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(1)

Explanation:
The calculation involves a fixed number of arithmetic operations, so it
executes in constant time.

===============================================================================
Space Complexity
===============================================================================

O(1)

Explanation:
The solution uses a constant amount of additional memory.

===============================================================================
Best Practices
===============================================================================

- Use descriptive names for variables and parameters.
- Group arithmetic operations with parentheses to improve readability.
- Test the function with different discount percentages.
- Keep lambda expressions limited to a single, clear calculation.

===============================================================================
Common Mistakes
===============================================================================

- Adding the discount instead of subtracting it.
- Forgetting to divide the percentage by 100.
- Misplacing parentheses, leading to incorrect calculations.
- Using the 'def' keyword instead of a lambda function.
- Forgetting to assign the lambda function to a variable.

===============================================================================
Alternative Approach
===============================================================================

Another valid implementation is:

    calculate_final_price = (
        lambda price, discount: price * (1 - discount / 100)
    )

This produces the same result using an equivalent mathematical formula.

===============================================================================
Real-World Relevance
===============================================================================

Discount calculations are commonly used in:

- E-commerce applications
- Retail billing systems
- Point-of-sale (POS) software
- Invoice generation
- Business and financial reporting

===============================================================================
Key Takeaways
===============================================================================

- Lambda functions can perform practical business calculations.
- Percentage calculations require dividing the percentage value by 100.
- Parentheses improve readability and help avoid calculation errors.
- Lambda functions are well suited for short mathematical expressions that
  return a single result.
===============================================================================
"""