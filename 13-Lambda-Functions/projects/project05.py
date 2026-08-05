"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Project 05: Inventory Analysis System

Difficulty:
Intermediate

Estimated Completion Time:
60-75 Minutes

Objective:
Create an inventory analysis system using lambda functions, map(), filter(),
and sorted() to process product stock data, identify inventory issues, and
generate business insights.

This project demonstrates how functional programming techniques can be applied
to real-world inventory management workflows.

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

A retail company manages hundreds of products and needs a simple inventory
analysis tool.

The inventory team wants to:

- Calculate inventory value.
- Identify low-stock products.
- Classify products by stock status.
- Sort products according to inventory value.
- Generate an inventory report.


Functional Requirements:
-----------------------

The program must:

1. Store product inventory records.
2. Calculate total inventory value using map().
3. Assign stock status.
4. Filter low-stock products.
5. Sort products by inventory value.
6. Display an inventory analysis report.


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
Create inventory records.

Step 2:
Calculate inventory value using map().

Step 3:
Classify stock availability.

Step 4:
Filter products requiring restocking.

Step 5:
Sort products by inventory value.

Step 6:
Display the final report.

===============================================================================
"""


# =============================================================================
# Inventory Dataset
# =============================================================================

inventory = [
    {
        "product": "Laptop",
        "quantity": 15,
        "price": 120000
    },
    {
        "product": "Keyboard",
        "quantity": 50,
        "price": 5000
    },
    {
        "product": "Mouse",
        "quantity": 80,
        "price": 2500
    },
    {
        "product": "Monitor",
        "quantity": 8,
        "price": 45000
    },
    {
        "product": "Printer",
        "quantity": 4,
        "price": 30000
    }
]


# =============================================================================
# Step 1: Calculate Inventory Value
# =============================================================================

inventory_value = list(
    map(
        lambda item: {
            **item,
            "total_value": item["quantity"] * item["price"]
        },
        inventory
    )
)


# =============================================================================
# Step 2: Add Stock Status
# =============================================================================

stock_analysis = list(
    map(
        lambda item: {
            **item,
            "status": (
                "Low Stock"
                if item["quantity"] < 10
                else "Available"
            )
        },
        inventory_value
    )
)


# =============================================================================
# Step 3: Filter Low Stock Items
# =============================================================================

low_stock_items = list(
    filter(
        lambda item: item["quantity"] < 10,
        stock_analysis
    )
)


# =============================================================================
# Step 4: Sort Inventory By Value
# =============================================================================

ranked_inventory = sorted(
    stock_analysis,
    key=lambda item: item["total_value"],
    reverse=True
)


# =============================================================================
# Inventory Report
# =============================================================================

print("=" * 70)
print("INVENTORY ANALYSIS REPORT")
print("=" * 70)

for item in ranked_inventory:
    print(
        f"Product: {item['product']}\n"
        f"Quantity: {item['quantity']}\n"
        f"Unit Price: Rs. {item['price']}\n"
        f"Inventory Value: Rs. {item['total_value']}\n"
        f"Status: {item['status']}\n"
    )


print("=" * 70)
print(f"Total Products: {len(stock_analysis)}")
print(f"Low Stock Products: {len(low_stock_items)}")
print("=" * 70)


"""
===============================================================================
Sample Input:
===============================================================================

Inventory record:

{
    "product": "Laptop",
    "quantity": 15,
    "price": 120000
}


===============================================================================
Sample Output:
===============================================================================

======================================================================
INVENTORY ANALYSIS REPORT
======================================================================

Product: Laptop
Quantity: 15
Unit Price: Rs. 120000
Inventory Value: Rs. 1800000
Status: Available

Product: Monitor
Quantity: 8
Unit Price: Rs. 45000
Inventory Value: Rs. 360000
Status: Low Stock

Product: Keyboard
Quantity: 50
Unit Price: Rs. 5000
Inventory Value: Rs. 250000
Status: Available

Product: Printer
Quantity: 4
Unit Price: Rs. 30000
Inventory Value: Rs. 120000
Status: Low Stock

Product: Mouse
Quantity: 80
Unit Price: Rs. 2500
Inventory Value: Rs. 200000
Status: Available

======================================================================
Total Products: 5
Low Stock Products: 2
======================================================================


===============================================================================
Detailed Explanation:
===============================================================================

This project demonstrates how lambda functions can process inventory records.

The first map() operation calculates the total value of each product:

quantity × price


The second map() operation adds stock availability information.

The filter() function identifies products requiring attention:

filter(
    lambda item: item["quantity"] < 10,
    inventory
)


The sorted() function ranks products according to their inventory value:

sorted(
    inventory,
    key=lambda item: item["total_value"],
    reverse=True
)


===============================================================================
Code Walkthrough:
===============================================================================

1. Inventory Data

Stores product details including quantity and price.

2. Value Calculation

map() transforms product records by adding total value.

3. Stock Classification

lambda expressions determine stock status.

4. Filtering

filter() extracts low-stock products.

5. Sorting

sorted() creates a value-based ranking.


===============================================================================
Best Practices:
===============================================================================

- Keep data processing steps separate.
- Use lambda functions for simple calculations.
- Use meaningful names for processed data.
- Use sorted() key functions instead of manual comparisons.
- Keep business rules easy to understand.


===============================================================================
Common Mistakes:
===============================================================================

1. Incorrect inventory value calculation.

2. Filtering the wrong condition.

3. Sorting using quantity instead of total value.

4. Writing very large lambda expressions.


===============================================================================
Possible Improvements:
===============================================================================

- Add supplier information.
- Add automatic reorder suggestions.
- Store inventory history.
- Create sales forecasting features.
- Connect with inventory databases.


===============================================================================
Bonus Challenges:
===============================================================================

1. Use reduce() to calculate total inventory worth.

2. Find the most valuable product.

3. Create category-based inventory reports.

4. Add discount calculations.


===============================================================================
Real-World Applications:
===============================================================================

These concepts are used in:

- Warehouse management systems
- Retail platforms
- Supply chain analytics
- Business reporting systems
- Data engineering pipelines


===============================================================================
Key Learning Outcomes:
===============================================================================

After completing this project, learners should understand:

✓ Processing inventory data with lambda functions
✓ Transforming records using map()
✓ Filtering business conditions
✓ Sorting complex data structures
✓ Applying functional programming in practical systems

===============================================================================
"""