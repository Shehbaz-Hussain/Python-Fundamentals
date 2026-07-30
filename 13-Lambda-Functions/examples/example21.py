"""
File: example21.py
Topic: Combining Lambda Functions with map() and filter()

Description:
This example demonstrates how lambda functions can be combined
with map() and filter() to process data in multiple stages.

Concepts Covered:
- Lambda functions with filter()
- Lambda functions with map()
- Multi-step data processing

Python Version:
Python 3.13+
"""


# Creating a list of product prices
prices = [50, 120, 75, 200, 30, 150]


# Filtering products with prices greater than or equal to 100
expensive_prices = filter(
    lambda price: price >= 100,
    prices
)


# Applying a 10% discount to filtered prices
discounted_prices = list(
    map(
        lambda price: price * 0.9,
        expensive_prices
    )
)


# Displaying final prices
print(discounted_prices)


"""
Expected Output:

[108.0, 180.0, 135.0]


Explanation:

1. A list of product prices is created.
2. The filter() function selects only prices greater than or
   equal to 100.
3. The lambda function checks each price condition.
4. The map() function applies a 10% discount to the filtered
   prices.
5. The second lambda function calculates the discounted values.
6. The final transformed list is stored in 'discounted_prices'.

Best Practice:

Combining lambda functions with map() and filter() is useful for
simple data pipelines. If the processing steps become difficult
to understand, use named functions for better readability.

Real-World Relevance:

Multi-step data processing is common in e-commerce systems,
financial applications, analytics platforms, and machine
learning preprocessing workflows.
"""