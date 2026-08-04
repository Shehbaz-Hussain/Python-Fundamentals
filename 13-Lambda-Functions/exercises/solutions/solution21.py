"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 21
Exercise Title: Sales Data Analytics Dashboard
Difficulty: Advanced

Objective:
    Use lambda functions together with map(), filter(), reduce(), and
    sorted() to perform basic data analytics on sales records.

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

# Create the sales dataset.
sales_data = [
    ("Laptop", "Electronics", 15, 95000),
    ("Mouse", "Electronics", 120, 1800),
    ("Desk", "Furniture", 18, 22000),
    ("Chair", "Furniture", 35, 12000),
    ("Monitor", "Electronics", 22, 38000),
    ("Printer", "Electronics", 10, 27000),
]

# Create a list containing each product and its total revenue.
product_revenues = list(
    map(
        lambda product: (
            product[0],
            product[2] * product[3],
        ),
        sales_data,
    )
)

# Filter products whose revenue exceeds 500,000.
high_revenue_products = list(
    filter(
        lambda product: product[1] > 500000,
        product_revenues,
    )
)

# Calculate the total company revenue.
total_company_revenue = reduce(
    lambda total, product: total + product[1],
    product_revenues,
    0,
)

# Sort products by revenue in descending order.
products_sorted_by_revenue = sorted(
    product_revenues,
    key=lambda product: product[1],
    reverse=True,
)

# Challenge 1: Calculate the average revenue per product.
average_revenue = total_company_revenue / len(product_revenues)

# Challenge 2: Display the three highest-revenue products.
top_three_products = products_sorted_by_revenue[:3]

# Challenge 3: Create a list of product names in uppercase.
uppercase_product_names = list(
    map(
        lambda product: product[0].upper(),
        sales_data,
    )
)

# -----------------------------------------------------------------------------
# Display Results
# -----------------------------------------------------------------------------

print("Original Sales Records:")
print(sales_data)

print("\nProduct Revenues:")
print(product_revenues)

print("\nProducts with Revenue Greater Than 500,000:")
print(high_revenue_products)

print("\nTotal Company Revenue:")
print(total_company_revenue)

print("\nProducts Sorted by Revenue (Highest First):")
print(products_sorted_by_revenue)

print("\nAverage Revenue Per Product:")
print(average_revenue)

print("\nTop Three Highest-Revenue Products:")
print(top_three_products)

print("\nProduct Names (Uppercase):")
print(uppercase_product_names)


"""
===============================================================================
Expected Output
===============================================================================

Original Sales Records:
[('Laptop', 'Electronics', 15, 95000),
 ('Mouse', 'Electronics', 120, 1800),
 ('Desk', 'Furniture', 18, 22000),
 ('Chair', 'Furniture', 35, 12000),
 ('Monitor', 'Electronics', 22, 38000),
 ('Printer', 'Electronics', 10, 27000)]

Product Revenues:
[('Laptop', 1425000),
 ('Mouse', 216000),
 ('Desk', 396000),
 ('Chair', 420000),
 ('Monitor', 836000),
 ('Printer', 270000)]

Products with Revenue Greater Than 500,000:
[('Laptop', 1425000),
 ('Monitor', 836000)]

Total Company Revenue:
3563000

Products Sorted by Revenue (Highest First):
[('Laptop', 1425000),
 ('Monitor', 836000),
 ('Chair', 420000),
 ('Desk', 396000),
 ('Printer', 270000),
 ('Mouse', 216000)]

Average Revenue Per Product:
593833.3333333334

Top Three Highest-Revenue Products:
[('Laptop', 1425000),
 ('Monitor', 836000),
 ('Chair', 420000)]

Product Names (Uppercase):
['LAPTOP', 'MOUSE', 'DESK', 'CHAIR', 'MONITOR', 'PRINTER']

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A list of sales records is created.
2. map() with a lambda function calculates the revenue for every product.
3. filter() selects only products whose revenue exceeds 500,000.
4. reduce() adds all product revenues to calculate the company's total
   revenue.
5. sorted() arranges the products from the highest revenue to the lowest.
6. The average revenue is calculated by dividing the total revenue by the
   number of products.
7. The first three records from the sorted list represent the highest-
   revenue products.
8. Another map() operation converts every product name to uppercase.
9. All results are displayed with clear headings.

How the Lambda Expressions Work
-------------------------------

Lambda 1:

    lambda product: (product[0], product[2] * product[3])

Returns the product name and its calculated revenue.

Lambda 2:

    lambda product: product[1] > 500000

Returns True for products whose revenue exceeds 500,000.

Lambda 3:

    lambda total, product: total + product[1]

Accumulates revenue values into a single total.

Lambda 4:

    lambda product: product[1]

Returns the revenue value used by sorted().

Lambda 5:

    lambda product: product[0].upper()

Returns the uppercase version of each product name.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- map()
- filter()
- reduce()
- sorted()
- key parameter
- Lists
- Tuples
- String methods
- Arithmetic operations

===============================================================================
Time Complexity
===============================================================================

Overall Complexity: O(n log n)

Explanation:
- map(): O(n)
- filter(): O(n)
- reduce(): O(n)
- sorted(): O(n log n)

Sorting dominates the total running time.

===============================================================================
Space Complexity
===============================================================================

Overall Complexity: O(n)

Explanation:
Several new lists are created while the original dataset remains unchanged.

===============================================================================
Best Practices
===============================================================================

- Preserve the original dataset.
- Keep each lambda expression focused on one task.
- Use descriptive variable names.
- Perform calculations before filtering when the filter depends on
  computed values.

===============================================================================
Common Mistakes
===============================================================================

- Using incorrect tuple indexes.
- Forgetting to import reduce().
- Forgetting to convert map() and filter() objects into lists.
- Sorting the original dataset instead of the calculated revenue list.
- Using unit price instead of revenue for sorting.

===============================================================================
Alternative Approach
===============================================================================

Instead of mapping revenues first, the revenue calculation could be
performed directly inside filter(), reduce(), and sorted(). However,
creating the intermediate revenue list improves readability and avoids
repeating the same calculation.

===============================================================================
Real-World Relevance
===============================================================================

This type of processing is commonly used in:

- Retail analytics dashboards
- Sales reporting systems
- Revenue analysis
- Business intelligence
- Inventory performance monitoring

===============================================================================
Key Takeaways
===============================================================================

- map() efficiently transforms data.
- filter() extracts records matching business rules.
- reduce() aggregates values into a single result.
- sorted() supports custom ordering using lambda expressions.
- Combining functional programming tools enables concise and readable
  data analysis workflows.
===============================================================================
"""