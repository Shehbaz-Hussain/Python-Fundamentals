"""
Module 13 - Data Structures
Example 13: Removing a Dictionary Item Using del

Purpose:
Demonstrate how to remove a key-value pair from a dictionary
using the del statement.
"""

# Create a dictionary containing product information.
product = {
    "id": 1001,
    "name": "Laptop",
    "price": 85000,
    "stock": 15
}

print("Original dictionary:")
print(product)

# Remove the "stock" key and its associated value.
del product["stock"]

print("\nDictionary after removing the 'stock' key:")
print(product)

# Expected Output:
# Original dictionary:
# {'id': 1001, 'name': 'Laptop', 'price': 85000, 'stock': 15}
#
# Dictionary after removing the 'stock' key:
# {'id': 1001, 'name': 'Laptop', 'price': 85000}