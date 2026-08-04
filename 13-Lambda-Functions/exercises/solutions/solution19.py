"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 19
Exercise Title: Customer Information Processing Using Lambda Functions
Difficulty: Intermediate–Advanced

Objective:
    Practice processing customer information using lambda functions together
    with map(), filter(), and sorted(). Extract customer names, filter
    customers based on purchase amount, sort customer records, and complete
    additional data processing tasks while keeping the original data unchanged.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a list of customer records.
customers = [
    ("Ali", "Gilgit", 18500),
    ("Sara", "Islamabad", 72000),
    ("Ahmed", "Lahore", 46000),
    ("Ayesha", "Karachi", 98000),
    ("Usman", "Gilgit", 25000),
    ("Fatima", "Peshawar", 81000),
]

# Create a list containing only customer names.
customer_names = list(
    map(
        lambda customer: customer[0],
        customers,
    )
)

# Filter customers whose purchase amount is at least 50,000.
customers_with_high_purchases = list(
    filter(
        lambda customer: customer[2] >= 50000,
        customers,
    )
)

# Sort customers by purchase amount in descending order.
customers_sorted_by_purchase = sorted(
    customers,
    key=lambda customer: customer[2],
    reverse=True,
)

# Challenge 1: Sort customers by city and then by customer name.
customers_sorted_by_city_and_name = sorted(
    customers,
    key=lambda customer: (customer[1], customer[0]),
)

# Challenge 2: Create a list containing customer names and 10% loyalty bonuses.
customer_loyalty_bonus = list(
    map(
        lambda customer: (
            customer[0],
            customer[2] * 0.10,
        ),
        customers,
    )
)

# Display the results.
print("Original Customers:")
print(customers)

print("\nCustomer Names:")
print(customer_names)

print("\nCustomers with Purchases >= 50,000:")
print(customers_with_high_purchases)

print("\nCustomers Sorted by Purchase Amount:")
print(customers_sorted_by_purchase)

print("\nCustomers Sorted by City and Name:")
print(customers_sorted_by_city_and_name)

print("\nCustomer Loyalty Bonuses:")
print(customer_loyalty_bonus)


"""
===============================================================================
Expected Output
===============================================================================

Original Customers:
[('Ali', 'Gilgit', 18500), ('Sara', 'Islamabad', 72000),
 ('Ahmed', 'Lahore', 46000), ('Ayesha', 'Karachi', 98000),
 ('Usman', 'Gilgit', 25000), ('Fatima', 'Peshawar', 81000)]

Customer Names:
['Ali', 'Sara', 'Ahmed', 'Ayesha', 'Usman', 'Fatima']

Customers with Purchases >= 50,000:
[('Sara', 'Islamabad', 72000), ('Ayesha', 'Karachi', 98000),
 ('Fatima', 'Peshawar', 81000)]

Customers Sorted by Purchase Amount:
[('Ayesha', 'Karachi', 98000), ('Fatima', 'Peshawar', 81000),
 ('Sara', 'Islamabad', 72000), ('Ahmed', 'Lahore', 46000),
 ('Usman', 'Gilgit', 25000), ('Ali', 'Gilgit', 18500)]

Customers Sorted by City and Name:
[('Ali', 'Gilgit', 18500), ('Usman', 'Gilgit', 25000),
 ('Sara', 'Islamabad', 72000), ('Ayesha', 'Karachi', 98000),
 ('Ahmed', 'Lahore', 46000), ('Fatima', 'Peshawar', 81000)]

Customer Loyalty Bonuses:
[('Ali', 1850.0), ('Sara', 7200.0), ('Ahmed', 4600.0),
 ('Ayesha', 9800.0), ('Usman', 2500.0), ('Fatima', 8100.0)]

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A list of customer records is created. Each tuple contains:
   - Customer name
   - City
   - Total purchase amount

2. The map() function with a lambda expression extracts only the customer
   names from each record.

3. The filter() function with a lambda expression selects customers whose
   purchase amount is greater than or equal to 50,000.

4. The sorted() function uses the key parameter with a lambda expression to
   sort customer records by purchase amount in descending order.

5. For the first challenge, another sorted() call orders the records first
   by city and then alphabetically by customer name.

6. For the second challenge, map() with a lambda expression creates a new
   list containing each customer's name and a loyalty bonus equal to 10% of
   the purchase amount.

7. All generated results are displayed with meaningful headings.

How the Lambda Expressions Work
-------------------------------

First lambda expression:

    lambda customer: customer[0]

- Returns the customer's name.
- map() collects all names into a new list.

Second lambda expression:

    lambda customer: customer[2] >= 50000

- Returns True for customers whose purchase amount is at least 50,000.
- filter() keeps only those records.

Third lambda expression:

    lambda customer: customer[2]

- Returns the purchase amount.
- sorted() uses this value to order the records.

Fourth lambda expression:

    lambda customer: (customer[1], customer[0])

- Returns a tuple containing:
    - City
    - Customer name
- sorted() first sorts by city and then by customer name.

Fifth lambda expression:

    lambda customer: (customer[0], customer[2] * 0.10)

- Returns a tuple containing:
    - Customer name
    - Loyalty bonus (10% of purchase amount)

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- map()
- filter()
- sorted()
- key parameter
- Lists
- Tuples
- Arithmetic operations
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(n log n)

Explanation:
- map() processes each record once: O(n)
- filter() processes each record once: O(n)
- sorted() performs sorting in O(n log n)

The sorting operation dominates the overall time complexity.

===============================================================================
Space Complexity
===============================================================================

O(n)

Explanation:
New lists are created for the mapped, filtered, and sorted results while the
original customer list remains unchanged.

===============================================================================
Best Practices
===============================================================================

- Preserve the original data by using sorted() instead of sort().
- Keep each lambda expression focused on a single task.
- Use descriptive variable names that clearly describe each result.
- Use tuple keys when sorting by multiple fields.

===============================================================================
Common Mistakes
===============================================================================

- Forgetting to convert map() or filter() objects into lists.
- Using incorrect tuple indexes when accessing customer information.
- Forgetting reverse=True when sorting in descending order.
- Modifying the original list instead of creating a new sorted list.
- Calculating the loyalty bonus using an incorrect percentage.

===============================================================================
Alternative Approach
===============================================================================

Another valid implementation is to create the loyalty bonus list using:

    lambda customer: (
        customer[0],
        round(customer[2] * 0.10, 2),
    )

This formats the bonus value to two decimal places.

===============================================================================
Real-World Relevance
===============================================================================

These techniques are commonly used in:

- Customer relationship management (CRM) systems
- Sales reporting
- Customer loyalty programs
- Business analytics
- Retail and e-commerce platforms

===============================================================================
Key Takeaways
===============================================================================

- map() transforms data into a new form.
- filter() selects records that satisfy specific conditions.
- sorted() with the key parameter provides flexible sorting.
- Lambda functions simplify data transformation, filtering, and sorting.
- Structured records such as tuples can be processed efficiently using
  functional programming tools.
===============================================================================
"""