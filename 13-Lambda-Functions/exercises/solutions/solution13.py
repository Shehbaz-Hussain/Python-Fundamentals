"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 13
Exercise Title: Aggregating Values with reduce() and Lambda
Difficulty: Intermediate

Objective:
    Practice using the functools.reduce() function together with a lambda
    function to combine all elements of a sequence into a single result.
    Calculate the total sum of a list of numbers and complete the challenge by
    calculating their product.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

from functools import reduce

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a list of numbers.
numbers = [5, 10, 15, 20, 25]

# Calculate the total sum using reduce() and a lambda function.
total_sum = reduce(
    lambda accumulated_value, current_value:
    accumulated_value + current_value,
    numbers,
)

# Challenge: Calculate the product of all numbers.
total_product = reduce(
    lambda accumulated_value, current_value:
    accumulated_value * current_value,
    numbers,
)

# Display the results.
print("Original Numbers:")
print(numbers)

print("\nTotal Sum:")
print(total_sum)

print("\nProduct of All Numbers:")
print(total_product)


"""
===============================================================================
Expected Output
===============================================================================

Original Numbers:
[5, 10, 15, 20, 25]

Total Sum:
75

Product of All Numbers:
375000

===============================================================================
Step-by-Step Explanation
===============================================================================

1. The reduce() function is imported from the functools module.
2. A list of numbers is created.
3. The first reduce() operation uses a lambda function to add each number to
   an accumulated total.
4. The process continues until all numbers have been combined into a single
   sum.
5. As an additional challenge, a second reduce() operation multiplies each
   number to calculate the overall product.
6. The original list, the total sum, and the product are displayed.

How the Lambda Expressions Work
-------------------------------

First lambda expression:

    lambda accumulated_value, current_value:
        accumulated_value + current_value

- 'accumulated_value' stores the running total.
- 'current_value' is the next number from the list.
- Each step adds the current number to the accumulated total.
- The final result is the sum of all numbers.

Second lambda expression:

    lambda accumulated_value, current_value:
        accumulated_value * current_value

- 'accumulated_value' stores the running product.
- 'current_value' is multiplied with the accumulated result.
- The final result is the product of all numbers.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- reduce()
- functools module
- Lists
- Return values
- Arithmetic operations
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(n)

Explanation:
Each reduce() operation processes every element in the list exactly once.
Since two reduce() operations are performed sequentially, the overall time
complexity remains O(n).

===============================================================================
Space Complexity
===============================================================================

O(1)

Explanation:
Apart from a few variables used to store the results, no additional memory
proportional to the input size is required.

===============================================================================
Best Practices
===============================================================================

- Import only the required function from the functools module.
- Use reduce() only when combining all elements into a single result.
- Keep lambda expressions concise and focused on one operation.
- Use descriptive variable names for accumulated values and results.

===============================================================================
Common Mistakes
===============================================================================

- Forgetting to import reduce() from functools.
- Using sum() instead of reduce() when the exercise requires reduce().
- Reversing the addition or multiplication logic.
- Using a traditional for loop instead of reduce().
- Forgetting that reduce() returns a single value rather than a list.

===============================================================================
Alternative Approach
===============================================================================

Another valid implementation is to provide an initial value to reduce():

    total_sum = reduce(
        lambda accumulated_value, current_value:
        accumulated_value + current_value,
        numbers,
        0,
    )

This explicitly starts the accumulation from zero.

===============================================================================
Real-World Relevance
===============================================================================

The reduce() function is commonly used in:

- Data aggregation
- Financial reporting
- Statistical calculations
- Business analytics
- Data processing pipelines

===============================================================================
Key Takeaways
===============================================================================

- reduce() combines all elements of an iterable into a single result.
- Lambda functions provide concise aggregation logic.
- The functools module provides the reduce() function.
- reduce() is useful for cumulative operations such as summation and
  multiplication.
===============================================================================
"""