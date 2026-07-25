"""
Module 13 - Data Structures
Project 02: Inventory Management System

Objective:
Build a simple inventory management system that demonstrates the
combined use of lists, tuples, sets, dictionaries, indexing,
membership operators, iteration, nested data structures, and
built-in functions.

Problem Statement:
A small shop wants to maintain information about its products.
The program should store product details, display the inventory,
identify unique categories, and calculate the total inventory value.

Requirements:
- Use a list to store inventory records.
- Use a dictionary for each product.
- Use a tuple to store supplier information.
- Use a set to store unique product categories.
- Display all product information.
- Calculate the inventory value of each product.
- Display the total inventory value.
- Display the total number of products and unique categories.
"""

# Inventory records
inventory = [
    {
        "name": "Keyboard",
        "category": "Accessories",
        "price": 2500,
        "quantity": 8,
        "supplier": ("Tech Solutions", "Gilgit"),
    },
    {
        "name": "Mouse",
        "category": "Accessories",
        "price": 1200,
        "quantity": 12,
        "supplier": ("Digital Store", "Skardu"),
    },
    {
        "name": "Monitor",
        "category": "Displays",
        "price": 28000,
        "quantity": 4,
        "supplier": ("Vision Electronics", "Islamabad"),
    },
    {
        "name": "USB Flash Drive",
        "category": "Storage",
        "price": 1800,
        "quantity": 15,
        "supplier": ("Memory Hub", "Lahore"),
    },
]

unique_categories = set()
total_inventory_value = 0

print("=" * 50)
print("Inventory Management System")
print("=" * 50)

for product in inventory:
    unique_categories.add(product["category"])

    inventory_value = product["price"] * product["quantity"]
    total_inventory_value += inventory_value

    supplier_name, supplier_city = product["supplier"]

    print(f"Product       : {product['name']}")
    print(f"Category      : {product['category']}")
    print(f"Price         : PKR {product['price']}")
    print(f"Quantity      : {product['quantity']}")
    print(f"Supplier      : {supplier_name}")
    print(f"Supplier City : {supplier_city}")
    print(f"Inventory Value: PKR {inventory_value}")
    print("-" * 50)

print("Unique Categories:")
# The order of elements in a set is not guaranteed.
print(unique_categories)

print()

print("Keyboard Available:", "Keyboard" in [item["name"] for item in inventory])
print("Laptop Available:", "Laptop" in [item["name"] for item in inventory])

print()

print("Total Products:", len(inventory))
print("Unique Categories:", len(unique_categories))
print("Total Inventory Value: PKR", total_inventory_value)

# Expected Output:
# ==================================================
# Inventory Management System
# ==================================================
# Product       : Keyboard
# Category      : Accessories
# Price         : PKR 2500
# Quantity      : 8
# Supplier      : Tech Solutions
# Supplier City : Gilgit
# Inventory Value: PKR 20000
# --------------------------------------------------
# ...
# Unique Categories:
# {'Accessories', 'Displays', 'Storage'}
# The order of elements in a set is not guaranteed.
#
# Keyboard Available: True
# Laptop Available: False
#
# Total Products: 4
# Unique Categories: 3
# Total Inventory Value: PKR 166600

# Possible Improvements:
# - Allow users to add, update, and remove products.
# - Search for products by name or category.
# - Sort products by price or quantity.
# - Save inventory data to a file.
# - Generate sales and inventory reports.