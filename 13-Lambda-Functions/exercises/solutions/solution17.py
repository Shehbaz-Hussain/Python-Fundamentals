"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 17
Exercise Title: Product Data Processing with Lambda Functions
Difficulty: Intermediate–Advanced

Objective:
    Practice processing product information using lambda functions together
    with map(), filter(), and sorted(). Transform product names, filter
    products by price, and sort product records while keeping the original
    list unchanged.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a list of product records.
products = [
    ("Laptop", "Electronics", 95000),
    ("Keyboard", "Electronics", 3500),
    ("Chair", "Furniture", 12000),
    ("Mouse", "Electronics", 1800),
    ("Desk", "Furniture", 22000),
    ("Monitor", "Electronics", 38000),
]

# Create a list containing product names in uppercase.
uppercase_product_names = list(
    map(
        lambda product: product[0].upper(),
        products,
    )
)

# Filter products with a price greater than 20,000.
products_above_20000 = list(
    filter(
        lambda product: product[2] > 20000,
        products,
    )
)

# Sort products by price in descending order.
products_sorted_by_price = sorted(
    products,
    key=lambda product: product[2],
    reverse=True,
)

# Challenge: Sort products by category and then by product name.
products_sorted_by_category_and_name = sorted(
    products,
    key=lambda product: (product[1], product[0]),
)

# Display the results.
print("Original Products:")
print(products)

print("\nProduct Names (Uppercase):")
print(uppercase_product_names)

print("\nProducts Above 20,000:")
print(products_above_20000)

print("\nProducts Sorted by Price (High to Low):")
print(products_sorted_by_price)

print("\nProducts Sorted by Category and Name:")
print(products_sorted_by_category_and_name)


"""
===============================================================================
Expected Output
===============================================================================

Original Products:
[('Laptop', 'Electronics', 95000), ('Keyboard', 'Electronics', 3500),
 ('Chair', 'Furniture', 12000), ('Mouse', 'Electronics', 1800),
 ('Desk', 'Furniture', 22000), ('Monitor', 'Electronics', 38000)]

Product Names (Uppercase):
['LAPTOP', 'KEYBOARD', 'CHAIR', 'MOUSE', 'DESK', 'MONITOR']

Products Above 20,000:
[('Laptop', 'Electronics', 95000),
 ('Desk', 'Furniture', 22000),
 ('Monitor', 'Electronics', 38000)]

Products Sorted by Price (High to Low):
[('Laptop', 'Electronics', 95000),
 ('Monitor', 'Electronics', 38000),
 ('Desk', 'Furniture', 22000),
 ('Chair', 'Furniture', 12000),
 ('Keyboard', 'Electronics', 3500),
 ('Mouse', 'Electronics', 1800)]

Products Sorted by Category and Name:
[('Keyboard', 'Electronics', 3500),
 ('Laptop', 'Electronics', 95000),
 ('Monitor', 'Electronics', 38000),
 ('Mouse', 'Electronics', 1800),
 ('Chair', 'Furniture', 12000),
 ('Desk', 'Furniture', 22000)]

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A list of product records is created. Each tuple contains:
       - Product name
       - Category
       - Price

2. The map() function applies a lambda expression to every product record.
   The lambda converts each product name to uppercase using the upper()
   string method.

3. The filter() function applies a lambda expression that returns True only
   for products priced above 20,000.

4. The sorted() function uses the key parameter with a lambda expression to
   sort the products by price in descending order.

5. For the challenge, another call to sorted() uses a tuple as the sorting
   key. Products are first sorted by category and then alphabetically by
   product name.

6. The original product list remains unchanged because map(), filter(), and
   sorted() each return new objects.

How the Lambda Expressions Work
-------------------------------

First lambda expression:

    lambda product: product[0].upper()

- Accesses the product name.
- Converts it to uppercase.
- Returns the transformed string.

Second lambda expression:

    lambda product: product[2] > 20000

- Accesses the product price.
- Returns True for products costing more than 20,000.

Third lambda expression:

    lambda product: product[2]

- Returns the product price.
- sorted() uses the price to order the records.

Fourth lambda expression:

    lambda product: (product[1], product[0])

- Returns a tuple containing:
      - Category
      - Product name
- sorted() first orders by category and then by product name.

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
- String methods
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(n log n)

Explanation:
- map() processes each product once: O(n)
- filter() processes each product once: O(n)
- sorted() performs sorting in O(n log n)

The sorting operation dominates the overall time complexity.

===============================================================================
Space Complexity
===============================================================================

O(n)

Explanation:
New lists are created for the mapped, filtered, and sorted results while the
original product list remains unchanged.

===============================================================================
Best Practices
===============================================================================

- Preserve the original data by using sorted() instead of sort().
- Use descriptive variable names for transformed and filtered data.
- Keep lambda expressions concise and focused on one task.
- Use tuple keys when sorting by multiple fields.

===============================================================================
Common Mistakes
===============================================================================

- Forgetting to convert the map() or filter() object into a list.
- Using the wrong tuple index for the product name, category, or price.
- Forgetting reverse=True when sorting in descending order.
- Using sort() instead of sorted(), which modifies the original list.
- Returning the wrong tuple order when sorting by multiple fields.

===============================================================================
Alternative Approach
===============================================================================

Another valid implementation is to transform the entire product record with
map(), for example:

    lambda product: (
        product[0].upper(),
        product[1],
        product[2],
    )

This preserves all product information while converting only the product
name to uppercase.

===============================================================================
Real-World Relevance
===============================================================================

These techniques are commonly used in:

- E-commerce platforms
- Inventory management systems
- Product catalog management
- Business analytics
- Data processing pipelines

===============================================================================
Key Takeaways
===============================================================================

- map() transforms each element of an iterable.
- filter() selects elements that satisfy a condition.
- sorted() with the key parameter supports custom sorting logic.
- Lambda functions provide concise solutions for transforming, filtering,
  and sorting structured data.
===============================================================================
"""