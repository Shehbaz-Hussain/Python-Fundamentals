"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Project 02: Product Price Transformation System

Difficulty:
Beginner

Estimated Completion Time:
45-60 Minutes

Objective:
Create a product price processing system using lambda functions,
map(), filter(), and sorted() to transform product prices, apply discounts,
filter products, and generate organized reports.

This project demonstrates how lambda functions can simplify common business
data processing operations.

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

An online shopping company needs a simple system to process product information.

The company wants to:

- Apply discounts to product prices.
- Calculate final prices.
- Identify affordable products.
- Sort products according to price.
- Generate a pricing report.

The objective is to practice functional programming techniques using
lambda functions and Python built-in functions.


Functional Requirements:
-----------------------

The program must:

1. Store product information.
2. Apply a discount percentage using map().
3. Calculate final prices.
4. Filter products based on price range.
5. Sort products by final price.
6. Display a formatted product report.


Prerequisites:
--------------

Learners should understand:

- Variables
- Lists
- Dictionaries
- Lambda functions
- map()
- filter()
- sorted()
- key parameter


Constraints:
------------

Do not use:

- Classes
- External packages
- File handling
- Database systems


Implementation Roadmap:
-----------------------

Step 1:
Create a product dataset.

Step 2:
Use map() with lambda to apply discounts.

Step 3:
Calculate final product prices.

Step 4:
Use filter() to find affordable products.

Step 5:
Sort products by price.

Step 6:
Display the final report.

===============================================================================
"""


# =============================================================================
# Product Dataset
# =============================================================================

products = [
    {
        "name": "Laptop",
        "price": 120000,
        "discount": 10
    },
    {
        "name": "Keyboard",
        "price": 5000,
        "discount": 15
    },
    {
        "name": "Mouse",
        "price": 2500,
        "discount": 20
    },
    {
        "name": "Monitor",
        "price": 45000,
        "discount": 5
    },
    {
        "name": "Headphones",
        "price": 8000,
        "discount": 25
    }
]


# =============================================================================
# Step 1: Apply Discounts Using map()
# =============================================================================

discounted_products = list(
    map(
        lambda product: {
            **product,
            "final_price": (
                product["price"]
                -
                (product["price"] * product["discount"] / 100)
            )
        },
        products
    )
)


# =============================================================================
# Step 2: Add Price Category
# =============================================================================

categorized_products = list(
    map(
        lambda product: {
            **product,
            "category": (
                "Premium"
                if product["final_price"] >= 50000
                else "Standard"
                if product["final_price"] >= 10000
                else "Budget"
            )
        },
        discounted_products
    )
)


# =============================================================================
# Step 3: Filter Affordable Products
# =============================================================================

affordable_products = list(
    filter(
        lambda product: product["final_price"] <= 10000,
        categorized_products
    )
)


# =============================================================================
# Step 4: Sort Products By Final Price
# =============================================================================

sorted_products = sorted(
    categorized_products,
    key=lambda product: product["final_price"]
)


# =============================================================================
# Product Report
# =============================================================================

print("=" * 65)
print("PRODUCT PRICE REPORT")
print("=" * 65)

for product in sorted_products:
    print(
        f"Product: {product['name']}\n"
        f"Original Price: Rs. {product['price']}\n"
        f"Discount: {product['discount']}%\n"
        f"Final Price: Rs. {product['final_price']:.0f}\n"
        f"Category: {product['category']}\n"
    )


print("=" * 65)
print(f"Total Products: {len(categorized_products)}")
print(f"Affordable Products: {len(affordable_products)}")
print("=" * 65)


"""
===============================================================================
Sample Input:
===============================================================================

The program uses predefined product records:

[
    {
        "name": "Laptop",
        "price": 120000,
        "discount": 10
    }
]


===============================================================================
Sample Output:
===============================================================================

=================================================================
PRODUCT PRICE REPORT
=================================================================

Product: Mouse
Original Price: Rs. 2500
Discount: 20%
Final Price: Rs. 2000
Category: Budget

Product: Keyboard
Original Price: Rs. 5000
Discount: 15%
Final Price: Rs. 4250
Category: Budget

Product: Headphones
Original Price: Rs. 8000
Discount: 25%
Final Price: Rs. 6000
Category: Budget

Product: Monitor
Original Price: Rs. 45000
Discount: 5%
Final Price: Rs. 42750
Category: Standard

Product: Laptop
Original Price: Rs. 120000
Discount: 10%
Final Price: Rs. 108000
Category: Premium

=================================================================
Total Products: 5
Affordable Products: 3
=================================================================


===============================================================================
Detailed Explanation:
===============================================================================

The project uses lambda functions to process product information without
creating separate functions.

The first map() operation applies discounts to every product.

Example:

lambda product:
    product["price"] - discount amount


The second map() operation classifies products based on their final price.

The filter() function identifies products that match the affordable price
condition.

The sorted() function organizes products by their final price:

sorted(
    products,
    key=lambda product: product["final_price"]
)


The key parameter extracts the value Python should use for comparison.


===============================================================================
Code Walkthrough:
===============================================================================

1. Product Dataset

Contains product name, original price, and discount percentage.

2. Discount Processing

map() creates updated product records with final prices.

3. Product Classification

lambda assigns price categories.

4. Filtering

filter() selects affordable products.

5. Sorting

sorted() arranges products from lowest to highest price.


===============================================================================
Best Practices:
===============================================================================

- Keep lambda expressions short.
- Use descriptive dictionary keys.
- Separate transformation and filtering steps.
- Use key functions instead of custom sorting logic.
- Avoid unnecessary complexity in lambda expressions.


===============================================================================
Common Mistakes:
===============================================================================

1. Incorrect discount calculation.

2. Forgetting that map() returns an iterator.

3. Sorting using the wrong dictionary key.

4. Mixing multiple operations into one unclear lambda function.


===============================================================================
Possible Improvements:
===============================================================================

- Add customer-specific discounts.
- Add product categories.
- Generate shopping recommendations.
- Store products in a database.
- Create a complete shopping cart system.


===============================================================================
Bonus Challenges:
===============================================================================

1. Use reduce() to calculate total inventory value.

2. Find the most expensive product.

3. Add tax calculation using lambda functions.

4. Create a discount recommendation system.


===============================================================================
Real-World Applications:
===============================================================================

These techniques are commonly used in:

- E-commerce platforms
- Inventory management systems
- Pricing engines
- Sales analytics tools
- Business data processing pipelines


===============================================================================
Key Learning Outcomes:
===============================================================================

After completing this project, learners should understand:

✓ Applying transformations with map()
✓ Filtering business data using filter()
✓ Sorting records with key functions
✓ Using lambda functions in real applications
✓ Building simple data processing workflows

===============================================================================
"""