"""
Module 13 - Data Structures
Example 07: Modifying a List

Purpose:
Demonstrate how to modify a list by adding, updating,
and removing elements using common list methods.
"""

# Create a list of fruits
fruits = [
    "Apple",
    "Banana",
    "Orange"
]

# Display the original list
print("Original List:")
print(fruits)

# Add a new element to the end of the list
fruits.append("Mango")

print("\nAfter append():")
print(fruits)

# Modify an existing element
fruits[1] = "Grapes"

print("\nAfter updating an element:")
print(fruits)

# Remove an element by value
fruits.remove("Orange")

print("\nAfter remove():")
print(fruits)

# Display the final number of elements
print("\nTotal fruits:", len(fruits))

# Expected Output:
# Original List:
# ['Apple', 'Banana', 'Orange']
#
# After append():
# ['Apple', 'Banana', 'Orange', 'Mango']
#
# After updating an element:
# ['Apple', 'Grapes', 'Orange', 'Mango']
#
# After remove():
# ['Apple', 'Grapes', 'Mango']
#
# Total fruits: 3