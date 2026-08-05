"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Project 07: Customer Analytics System

Difficulty:
Intermediate

Estimated Completion Time:
60-75 Minutes

Objective:
Build a customer analytics system using lambda functions, map(), filter(), and
sorted() to analyze customer purchase behavior, classify customers, identify
valuable customers, and generate business insights.

This project demonstrates how functional programming concepts can be applied
to customer data analysis workflows.

Python Version:
3.13+

===============================================================================
"""


# =============================================================================
# Project Description
# =============================================================================

"""
Problem Statement:
------------------

An online business wants to analyze customer purchasing behavior.

The company stores customer information including:

- Customer name
- Number of purchases
- Total purchase amount

The marketing team needs a system that can:

- Calculate customer spending categories.
- Identify valuable customers.
- Rank customers based on spending.
- Generate a customer analytics report.


Functional Requirements:
-----------------------

The program must:

1. Store customer records.
2. Calculate customer categories using map().
3. Filter valuable customers.
4. Sort customers by spending.
5. Display an analytics report.


Prerequisites:
--------------

Learners should understand:

- Lambda functions
- map()
- filter()
- sorted()
- key parameter
- Lists
- Dictionaries


Constraints:
------------

Do not use:

- Import statements
- External libraries
- Classes
- File handling
- Advanced concepts


Implementation Roadmap:
-----------------------

Step 1:
Create customer data.

Step 2:
Calculate customer spending information.

Step 3:
Assign customer segments.

Step 4:
Filter valuable customers.

Step 5:
Sort customers by spending.

Step 6:
Generate the final report.

===============================================================================
"""


# =============================================================================
# Customer Dataset
# =============================================================================

customers = [
    {
        "name": "Ali",
        "orders": 12,
        "total_spent": 45000
    },
    {
        "name": "Sara",
        "orders": 5,
        "total_spent": 12000
    },
    {
        "name": "Ahmed",
        "orders": 20,
        "total_spent": 85000
    },
    {
        "name": "Fatima",
        "orders": 8,
        "total_spent": 30000
    },
    {
        "name": "Usman",
        "orders": 3,
        "total_spent": 7000
    }
]


# =============================================================================
# Step 1: Add Customer Segment Using map()
# =============================================================================

customers_with_segment = list(
    map(
        lambda customer: {
            **customer,
            "segment": (
                "Premium"
                if customer["total_spent"] >= 50000
                else "Regular"
                if customer["total_spent"] >= 15000
                else "Basic"
            )
        },
        customers
    )
)


# =============================================================================
# Step 2: Filter Valuable Customers
# =============================================================================

valuable_customers = list(
    filter(
        lambda customer: customer["total_spent"] >= 30000,
        customers_with_segment
    )
)


# =============================================================================
# Step 3: Sort Customers By Spending
# =============================================================================

ranked_customers = sorted(
    customers_with_segment,
    key=lambda customer: customer["total_spent"],
    reverse=True
)


# =============================================================================
# Customer Analytics Report
# =============================================================================

print("=" * 70)
print("CUSTOMER ANALYTICS REPORT")
print("=" * 70)

rank = 1

for customer in ranked_customers:
    print(
        f"Rank: {rank}\n"
        f"Customer: {customer['name']}\n"
        f"Orders: {customer['orders']}\n"
        f"Total Spending: Rs. {customer['total_spent']}\n"
        f"Customer Segment: {customer['segment']}\n"
    )

    rank += 1


print("=" * 70)
print(f"Total Customers: {len(customers_with_segment)}")
print(f"Valuable Customers: {len(valuable_customers)}")
print("=" * 70)


"""
===============================================================================
Sample Input:
===============================================================================

{
    "name": "Ali",
    "orders": 12,
    "total_spent": 45000
}


===============================================================================
Sample Output:
===============================================================================

======================================================================
CUSTOMER ANALYTICS REPORT
======================================================================

Rank: 1
Customer: Ahmed
Orders: 20
Total Spending: Rs. 85000
Customer Segment: Premium

Rank: 2
Customer: Ali
Orders: 12
Total Spending: Rs. 45000
Customer Segment: Regular

Rank: 3
Customer: Fatima
Orders: 8
Total Spending: Rs. 30000
Customer Segment: Regular

Rank: 4
Customer: Sara
Orders: 5
Total Spending: Rs. 12000
Customer Segment: Basic

Rank: 5
Customer: Usman
Orders: 3
Total Spending: Rs. 7000
Customer Segment: Basic

======================================================================
Total Customers: 5
Valuable Customers: 3
======================================================================


===============================================================================
Detailed Explanation:
===============================================================================

This project shows how lambda functions can process customer information.

The map() function transforms customer records by adding a customer segment.

Example:

lambda customer:
    "Premium" if spending is high


The filter() function selects customers who meet the business condition.

Example:

filter(
    lambda customer: customer["total_spent"] >= 30000,
    customers
)


The sorted() function ranks customers based on spending:

sorted(
    customers,
    key=lambda customer: customer["total_spent"],
    reverse=True
)


===============================================================================
Code Walkthrough:
===============================================================================

1. Customer Dataset

Contains customer purchase information.

2. Customer Segmentation

map() adds customer categories.

3. Customer Filtering

filter() identifies valuable customers.

4. Customer Ranking

sorted() creates a spending-based ranking.


===============================================================================
Best Practices:
===============================================================================

- Use map() when creating transformed data.
- Use filter() when selecting records.
- Use sorted() with key for custom sorting.
- Keep lambda functions simple.
- Use descriptive variable names.


===============================================================================
Common Mistakes:
===============================================================================

1. Using complicated lambda expressions.

2. Forgetting reverse=True for ranking.

3. Filtering before adding required data.

4. Sorting using the wrong dictionary value.


===============================================================================
Possible Improvements:
===============================================================================

- Add customer loyalty points.
- Add purchase frequency analysis.
- Create recommendation rules.
- Connect customer analysis with machine learning models.


===============================================================================
Bonus Challenges:
===============================================================================

1. Find the highest spending customer.

2. Calculate average spending.

3. Create a loyalty program.

4. Add customer ranking levels.


===============================================================================
Real-World Applications:
===============================================================================

These concepts are used in:

- Customer relationship management systems
- Recommendation systems
- E-commerce analytics
- Marketing automation
- Data science workflows


===============================================================================
Key Learning Outcomes:
===============================================================================

After completing this project, learners should understand:

✓ Processing customer data using lambda functions
✓ Transforming records using map()
✓ Filtering business information
✓ Ranking records using sorted()
✓ Applying functional programming in analytics tasks

===============================================================================
"""