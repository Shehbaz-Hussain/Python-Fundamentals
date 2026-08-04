"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 20
Exercise Title: Sales Data Processing Using Lambda Functions
Difficulty: Advanced

Objective:
    Apply lambda functions to a realistic sales dataset by combining
    map(), filter(), reduce(), and sorted() to perform business-oriented
    data processing tasks.

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

# Create a list of sales records.
sales = [
    ("Ali", "North", 125000),
    ("Sara", "South", 98000),
    ("Ahmed", "East", 143500),
    ("Ayesha", "West", 167000),
    ("Usman", "North", 89500),
    ("Fatima", "South", 152000),
    ("Bilal", "East", 110000),
    ("Hina", "West", 76000),
]

# Create a list containing the salespeople's names in uppercase.
salespeople_uppercase = list(
    map(
        lambda record: record[0].upper(),
        sales,
    )
)

# Filter sales records with sales amounts of at least 120,000.
sales_above_target = list(
    filter(
        lambda record: record[2] >= 120000,
        sales,
    )
)

# Calculate the total sales amount.
total_sales = reduce(
    lambda total, record: total + record[2],
    sales,
    0,
)

# Calculate the average sales amount.
average_sales = total_sales / len(sales)

# Sort sales records by sales amount in descending order.
sales_sorted_by_amount = sorted(
    sales,
    key=lambda record: record[2],
    reverse=True,
)

# Challenge 1: Sort by region and then by salesperson.
sales_sorted_by_region_and_name = sorted(
    sales,
    key=lambda record: (record[1], record[0]),
)

# Challenge 2: Create projected sales after a 5% increase.
projected_sales = list(
    map(
        lambda record: (
            record[0],
            record[2] * 1.05,
        ),
        sales,
    )
)

# Challenge 3: Count records meeting the sales target.
target_count = len(
    list(
        filter(
            lambda record: record[2] >= 120000,
            sales,
        )
    )
)

# Display the results.
print("Original Sales Records:")
print(sales)

print("\nSalespeople (Uppercase):")
print(salespeople_uppercase)

print("\nSales >= 120,000:")
print(sales_above_target)

print("\nTotal Sales:")
print(total_sales)

print("\nAverage Sales:")
print(average_sales)

print("\nSales Sorted by Amount (Highest First):")
print(sales_sorted_by_amount)

print("\nSales Sorted by Region and Salesperson:")
print(sales_sorted_by_region_and_name)

print("\nProjected Sales After 5% Increase:")
print(projected_sales)

print("\nNumber of Sales Records Meeting the 120,000 Target:")
print(target_count)


"""
===============================================================================
Expected Output
===============================================================================

Original Sales Records:
[('Ali', 'North', 125000), ('Sara', 'South', 98000),
 ('Ahmed', 'East', 143500), ('Ayesha', 'West', 167000),
 ('Usman', 'North', 89500), ('Fatima', 'South', 152000),
 ('Bilal', 'East', 110000), ('Hina', 'West', 76000)]

Salespeople (Uppercase):
['ALI', 'SARA', 'AHMED', 'AYESHA', 'USMAN', 'FATIMA', 'BILAL', 'HINA']

Sales >= 120,000:
[('Ali', 'North', 125000), ('Ahmed', 'East', 143500),
 ('Ayesha', 'West', 167000), ('Fatima', 'South', 152000)]

Total Sales:
961000

Average Sales:
120125.0

Sales Sorted by Amount (Highest First):
[('Ayesha', 'West', 167000), ('Fatima', 'South', 152000),
 ('Ahmed', 'East', 143500), ('Ali', 'North', 125000),
 ('Bilal', 'East', 110000), ('Sara', 'South', 98000),
 ('Usman', 'North', 89500), ('Hina', 'West', 76000)]

Sales Sorted by Region and Salesperson:
[('Ahmed', 'East', 143500), ('Bilal', 'East', 110000),
 ('Ali', 'North', 125000), ('Usman', 'North', 89500),
 ('Fatima', 'South', 152000), ('Sara', 'South', 98000),
 ('Ayesha', 'West', 167000), ('Hina', 'West', 76000)]

Projected Sales After 5% Increase:
[('Ali', 131250.0), ('Sara', 102900.0), ('Ahmed', 150675.0),
 ('Ayesha', 175350.0), ('Usman', 93975.0), ('Fatima', 159600.0),
 ('Bilal', 115500.0), ('Hina', 79800.0)]

Number of Sales Records Meeting the 120,000 Target:
4

===============================================================================
Step-by-Step Explanation
===============================================================================

1. The reduce() function is imported from the functools module.
2. A list of sales records is created. Each tuple contains:
   - Salesperson
   - Region
   - Sales amount
3. The map() function with a lambda expression converts each salesperson's
   name to uppercase.
4. The filter() function selects only the sales records with amounts greater
   than or equal to 120,000.
5. The reduce() function calculates the total sales amount by adding the
   sales amount from each record.
6. The average sales amount is calculated by dividing the total sales by the
   number of records.
7. The sorted() function orders the sales records by sales amount in
   descending order.
8. The first challenge sorts the records by region and then by salesperson.
9. The second challenge creates a new list containing each salesperson's
   name and their projected sales after a 5% increase.
10. The third challenge counts the number of records meeting the sales target
    by combining filter() and len() without using a traditional for loop.
11. All results are displayed using meaningful headings.

How the Lambda Expressions Work
-------------------------------

First lambda expression:

    lambda record: record[0].upper()

- Returns the salesperson's name in uppercase.

Second lambda expression:

    lambda record: record[2] >= 120000

- Returns True for records meeting the sales target.

Third lambda expression:

    lambda total, record: total + record[2]

- Adds each sales amount to the running total.

Fourth lambda expression:

    lambda record: record[2]

- Returns the sales amount for sorting.

Fifth lambda expression:

    lambda record: (record[1], record[0])

- Returns a tuple containing:
  - Region
  - Salesperson
- sorted() first orders by region and then by salesperson.

Sixth lambda expression:

    lambda record: (record[0], record[2] * 1.05)

- Returns the salesperson's name and projected sales after a 5% increase.

Seventh lambda expression:

    lambda record: record[2] >= 120000

- Returns True for sales records that meet the target.
- filter() selects matching records, and len() counts them.

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
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(n log n)

Explanation:
- map() processes each record once: O(n)
- filter() processes each record once: O(n)
- reduce() processes each record once: O(n)
- sorted() performs sorting in O(n log n)

The sorting operation dominates the overall time complexity.

===============================================================================
Space Complexity
===============================================================================

O(n)

Explanation:
New lists are created for the mapped, filtered, and sorted results while the
original sales list remains unchanged.

===============================================================================
Best Practices
===============================================================================

- Keep lambda expressions concise and focused on one responsibility.
- Preserve the original dataset by using sorted() instead of sort().
- Use descriptive variable names for transformed and filtered data.
- Use functional programming tools when processing collections of records.

===============================================================================
Common Mistakes
===============================================================================

- Forgetting to import reduce() from functools.
- Using incorrect tuple indexes when accessing record fields.
- Forgetting to convert map() or filter() objects into lists.
- Omitting reverse=True when sorting in descending order.
- Using a traditional for loop when the exercise explicitly requires
  functional programming techniques.

===============================================================================
Alternative Approach
===============================================================================

Another valid implementation is to count sales records meeting the target
using reduce():

    target_count = reduce(
        lambda count, record: count + (record[2] >= 120000),
        sales,
        0,
    )

This also avoids using a traditional for loop.

===============================================================================
Real-World Relevance
===============================================================================

These techniques are commonly used in:

- Sales analytics
- Business intelligence dashboards
- Customer performance reporting
- Revenue forecasting
- Data processing pipelines

===============================================================================
Key Takeaways
===============================================================================

- map() transforms records into new values.
- filter() selects records based on specified conditions.
- reduce() aggregates multiple values into a single result.
- sorted() with the key parameter provides flexible sorting.
- Lambda functions enable concise and readable functional programming.
===============================================================================
"""