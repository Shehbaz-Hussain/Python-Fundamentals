"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Project 03: Customer Filtering System

Difficulty:
Intermediate

Estimated Completion Time:
60 Minutes

Objective:
Build a customer filtering and analysis system using lambda functions,
filter(), map(), and sorted() to process customer information and generate
useful business insights.

This project introduces how companies process customer data for analysis,
segmentation, and decision-making.

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

A company wants to analyze customer information to identify valuable customers.

The business team needs a system that can:

- Calculate customer spending levels.
- Classify customers.
- Find active customers.
- Sort customers based on purchases.
- Generate a customer analysis report.


Functional Requirements:
-----------------------

The program must:

1. Store customer records.
2. Calculate total spending using map().
3. Assign customer categories.
4. Filter active customers.
5. Sort customers by spending amount.
6. Display a customer report.


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

- External libraries
- Classes
- File handling
- Database systems


Implementation Roadmap:
-----------------------

Step 1:
Create customer records.

Step 2:
Calculate total spending using map().

Step 3:
Classify customers based on spending.

Step 4:
Filter active customers.

Step 5:
Sort customers by purchase value.

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
        "amounts": [5000, 3000, 7000]
    },
    {
        "name": "Sara",
        "orders": 5,
        "amounts": [2000, 1500]
    },
    {
        "name": "Ahmed",
        "orders": 18,
        "amounts": [9000, 6000, 8000]
    },
    {
        "name": "Fatima",
        "orders": 2,
        "amounts": [1000]
    },
    {
        "name": "Usman",
        "orders": 10,
        "amounts": [4000, 3500, 2500]
    }
]


# =============================================================================
# Step 1: Calculate Total Spending
# =============================================================================

customer_spending = list(
    map(
        lambda customer: {
            **customer,
            "total_spending": sum(customer["amounts"])
        },
        customers
    )
)


# =============================================================================
# Step 2: Assign Customer Category
# =============================================================================

categorized_customers = list(
    map(
        lambda customer: {
            **customer,
            "category": (
                "VIP"
                if customer["total_spending"] >= 15000
                else "Regular"
                if customer["total_spending"] >= 5000
                else "New"
            )
        },
        customer_spending
    )
)


# =============================================================================
# Step 3: Filter Active Customers
# =============================================================================

active_customers = list(
    filter(
        lambda customer: customer["orders"] >= 5,
        categorized_customers
    )
)


# =============================================================================
# Step 4: Sort Customers By Spending
# =============================================================================

ranked_customers = sorted(
    categorized_customers,
    key=lambda customer: customer["total_spending"],
    reverse=True
)


# =============================================================================
# Customer Analysis Report
# =============================================================================

print("=" * 65)
print("CUSTOMER ANALYTICS REPORT")
print("=" * 65)

for customer in ranked_customers:
    print(
        f"Name: {customer['name']}\n"
        f"Orders: {customer['orders']}\n"
        f"Total Spending: Rs. {customer['total_spending']}\n"
        f"Category: {customer['category']}\n"
    )


print("=" * 65)
print(f"Total Customers: {len(categorized_customers)}")
print(f"Active Customers: {len(active_customers)}")
print("=" * 65)


"""
===============================================================================
Sample Input:
===============================================================================

Customer records:

[
    {
        "name": "Ali",
        "orders": 12,
        "amounts": [5000, 3000, 7000]
    }
]


===============================================================================
Sample Output:
===============================================================================

=================================================================
CUSTOMER ANALYTICS REPORT
=================================================================

Name: Ahmed
Orders: 18
Total Spending: Rs. 23000
Category: VIP

Name: Ali
Orders: 12
Total Spending: Rs. 15000
Category: VIP

Name: Usman
Orders: 10
Total Spending: Rs. 10000
Category: Regular

Name: Sara
Orders: 5
Total Spending: Rs. 3500
Category: New

Name: Fatima
Orders: 2
Total Spending: Rs. 1000
Category: New

=================================================================
Total Customers: 5
Active Customers: 4
=================================================================


===============================================================================
Detailed Explanation:
===============================================================================

This project demonstrates how lambda functions can process business data.

The first map() calculates each customer's total spending.

Example:

lambda customer:
    sum(customer["amounts"])


The second map() adds customer categories based on spending.

The filter() function identifies active customers:

filter(
    lambda customer: customer["orders"] >= 5,
    customers
)


The sorted() function ranks customers by spending:

sorted(
    customers,
    key=lambda customer: customer["total_spending"],
    reverse=True
)


The key parameter allows sorting based on a specific value.


===============================================================================
Code Walkthrough:
===============================================================================

1. Customer Data

Stores customer names, order counts, and purchase amounts.

2. Spending Calculation

map() transforms customer records by adding spending information.

3. Customer Segmentation

lambda functions classify customers.

4. Customer Filtering

filter() selects active customers.

5. Ranking

sorted() generates a spending-based ranking.


===============================================================================
Best Practices:
===============================================================================

- Use lambda functions for simple transformations.
- Keep data processing steps readable.
- Use meaningful names for processed data.
- Avoid deeply nested lambda expressions.
- Use built-in functions when they improve clarity.


===============================================================================
Common Mistakes:
===============================================================================

1. Incorrect spending calculations.

2. Forgetting reverse=True for ranking.

3. Using filter() when transformation is required.

4. Writing complicated lambda expressions.


===============================================================================
Possible Improvements:
===============================================================================

- Add customer lifetime value calculation.
- Add purchase frequency analysis.
- Create customer recommendations.
- Store customer information permanently.
- Add visualization reports.


===============================================================================
Bonus Challenges:
===============================================================================

1. Use reduce() to calculate total company revenue.

2. Find the highest spending customer.

3. Create a loyalty reward system.

4. Add customer ranking numbers.


===============================================================================
Real-World Applications:
===============================================================================

Similar techniques are used in:

- Customer relationship management systems
- Marketing analytics
- Recommendation engines
- Business intelligence platforms
- Machine learning data preparation


===============================================================================
Key Learning Outcomes:
===============================================================================

After completing this project, learners should understand:

✓ Processing customer data using lambda functions
✓ Transforming records with map()
✓ Filtering information with filter()
✓ Ranking data using sorted()
✓ Applying functional programming concepts in business scenarios

===============================================================================
"""