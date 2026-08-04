"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 22
Exercise Title: Business Logic - Customer Discount Processing
Difficulty: Advanced

Objective:
    Apply lambda functions to implement business rules for customer discounts
    using map(), filter(), sorted(), and reduce().

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

# Create the customer orders dataset.
orders = [
    ("Ali", "Gold", 25000),
    ("Sara", "Silver", 18000),
    ("Ahmed", "Gold", 42000),
    ("Ayesha", "Platinum", 55000),
    ("Usman", "Silver", 16000),
    ("Fatima", "Gold", 39000),
    ("Bilal", "Platinum", 61000),
    ("Hina", "Silver", 21000),
]


# Calculate the discount based on membership type.
calculate_discount = lambda membership, amount: (
    amount * 0.20
    if membership == "Platinum"
    else amount * 0.10
    if membership == "Gold"
    else amount * 0.05
)

# Create a processed order report.
processed_orders = list(
    map(
        lambda order: (
            order[0],
            order[1],
            order[2],
            calculate_discount(order[1], order[2]),
            order[2] - calculate_discount(order[1], order[2]),
        ),
        orders,
    )
)

# Filter customers whose final payable amount is at least 30,000.
customers_above_threshold = list(
    filter(
        lambda order: order[4] >= 30000,
        processed_orders,
    )
)

# Calculate the total of all final payable amounts.
total_final_amount = reduce(
    lambda total, order: total + order[4],
    processed_orders,
    0,
)

# Sort customers by final payable amount in descending order.
sorted_by_final_amount = sorted(
    processed_orders,
    key=lambda order: order[4],
    reverse=True,
)

# -----------------------------------------------------------------------------
# Challenge Solutions
# -----------------------------------------------------------------------------

# Count customers by membership category.
gold_members = len(
    list(filter(lambda order: order[1] == "Gold", orders))
)

silver_members = len(
    list(filter(lambda order: order[1] == "Silver", orders))
)

platinum_members = len(
    list(filter(lambda order: order[1] == "Platinum", orders))
)

# Display only Platinum customers.
platinum_customers = list(
    filter(
        lambda order: order[1] == "Platinum",
        processed_orders,
    )
)

# Sort report alphabetically by customer name.
sorted_by_customer_name = sorted(
    processed_orders,
    key=lambda order: order[0],
)

# Calculate the average final payable amount.
average_final_amount = total_final_amount / len(processed_orders)

# -----------------------------------------------------------------------------
# Display Results
# -----------------------------------------------------------------------------

print("Original Order Records:")
print(orders)

print("\nProcessed Orders:")
print(processed_orders)

print("\nCustomers with Final Amount >= 30,000:")
print(customers_above_threshold)

print("\nTotal Final Payable Amount:")
print(total_final_amount)

print("\nCustomers Sorted by Final Payable Amount:")
print(sorted_by_final_amount)

print("\nMembership Counts:")
print(f"Gold: {gold_members}")
print(f"Silver: {silver_members}")
print(f"Platinum: {platinum_members}")

print("\nPlatinum Customers:")
print(platinum_customers)

print("\nReport Sorted by Customer Name:")
print(sorted_by_customer_name)

print("\nAverage Final Payable Amount:")
print(average_final_amount)


"""
===============================================================================
Expected Output
===============================================================================

Original Order Records:
[('Ali', 'Gold', 25000), ('Sara', 'Silver', 18000),
 ('Ahmed', 'Gold', 42000), ('Ayesha', 'Platinum', 55000),
 ('Usman', 'Silver', 16000), ('Fatima', 'Gold', 39000),
 ('Bilal', 'Platinum', 61000), ('Hina', 'Silver', 21000)]

Processed Orders:
[('Ali', 'Gold', 25000, 2500.0, 22500.0),
 ('Sara', 'Silver', 18000, 900.0, 17100.0),
 ('Ahmed', 'Gold', 42000, 4200.0, 37800.0),
 ('Ayesha', 'Platinum', 55000, 11000.0, 44000.0),
 ('Usman', 'Silver', 16000, 800.0, 15200.0),
 ('Fatima', 'Gold', 39000, 3900.0, 35100.0),
 ('Bilal', 'Platinum', 61000, 12200.0, 48800.0),
 ('Hina', 'Silver', 21000, 1050.0, 19950.0)]

Customers with Final Amount >= 30,000:
[('Ahmed', 'Gold', 42000, 4200.0, 37800.0),
 ('Ayesha', 'Platinum', 55000, 11000.0, 44000.0),
 ('Fatima', 'Gold', 39000, 3900.0, 35100.0),
 ('Bilal', 'Platinum', 61000, 12200.0, 48800.0)]

Total Final Payable Amount:
240450.0

Customers Sorted by Final Payable Amount:
[('Bilal', 'Platinum', 61000, 12200.0, 48800.0),
 ('Ayesha', 'Platinum', 55000, 11000.0, 44000.0),
 ('Ahmed', 'Gold', 42000, 4200.0, 37800.0),
 ('Fatima', 'Gold', 39000, 3900.0, 35100.0),
 ('Ali', 'Gold', 25000, 2500.0, 22500.0),
 ('Hina', 'Silver', 21000, 1050.0, 19950.0),
 ('Sara', 'Silver', 18000, 900.0, 17100.0),
 ('Usman', 'Silver', 16000, 800.0, 15200.0)]

Membership Counts:
Gold: 3
Silver: 3
Platinum: 2

Platinum Customers:
[('Ayesha', 'Platinum', 55000, 11000.0, 44000.0),
 ('Bilal', 'Platinum', 61000, 12200.0, 48800.0)]

Report Sorted by Customer Name:
...

Average Final Payable Amount:
30056.25

===============================================================================
Step-by-Step Explanation
===============================================================================

1. The original customer order records are stored as tuples.
2. A lambda expression calculates the discount according to the membership
   type:
   - Platinum: 20%
   - Gold: 10%
   - Silver: 5%
3. map() creates a new list containing:
   - Customer name
   - Membership type
   - Original amount
   - Discount amount
   - Final payable amount
4. filter() selects only customers whose final payable amount is at least
   30,000.
5. reduce() calculates the total of all final payable amounts.
6. sorted() orders customers from the highest final payable amount to the
   lowest.
7. The challenge tasks count membership categories, display Platinum
   customers, sort the report alphabetically by customer name, and calculate
   the average final payable amount.

How the Lambda Expressions Work
-------------------------------

Lambda 1:

    lambda membership, amount: ...

Determines the discount percentage according to the membership type.

Lambda 2:

    lambda order: (...)

Creates a new processed customer record containing calculated values.

Lambda 3:

    lambda order: order[4] >= 30000

Keeps only customers whose final payable amount meets the required limit.

Lambda 4:

    lambda total, order: total + order[4]

Accumulates all final payable amounts into a single total.

Lambda 5:

    lambda order: order[4]

Returns the final payable amount used for sorting.

Lambda 6:

    lambda order: order[0]

Returns the customer name for alphabetical sorting.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- map()
- filter()
- reduce()
- sorted()
- key parameter
- Conditional expressions
- Lists
- Tuples
- Arithmetic operations
- Business logic

===============================================================================
Time Complexity
===============================================================================

Overall Complexity: O(n log n)

Explanation:
- map(): O(n)
- filter(): O(n)
- reduce(): O(n)
- sorted(): O(n log n)

Sorting dominates the running time.

===============================================================================
Space Complexity
===============================================================================

Overall Complexity: O(n)

Explanation:
Several new lists are created while preserving the original dataset.

===============================================================================
Best Practices
===============================================================================

- Keep business rules separate from data processing logic.
- Use descriptive variable names for calculated results.
- Preserve the original dataset.
- Use functional programming tools for collection processing.

===============================================================================
Common Mistakes
===============================================================================

- Applying an incorrect discount percentage.
- Using the original amount instead of the final amount for filtering or
  sorting.
- Forgetting to import reduce().
- Modifying the original dataset.
- Using incorrect tuple indexes.

===============================================================================
Alternative Approach
===============================================================================

The discount percentage could be stored in a dictionary such as:

    {"Platinum": 0.20, "Gold": 0.10, "Silver": 0.05}

The lambda expression could then retrieve the percentage directly instead of
using nested conditional expressions.

===============================================================================
Real-World Relevance
===============================================================================

This technique is commonly used in:

- E-commerce systems
- Customer loyalty programs
- Billing applications
- Financial reporting
- Retail business analytics

===============================================================================
Key Takeaways
===============================================================================

- Lambda functions simplify business rule implementation.
- map() transforms datasets efficiently.
- filter() extracts records matching business conditions.
- reduce() performs aggregate calculations.
- sorted() enables flexible reporting using custom keys.
===============================================================================
"""