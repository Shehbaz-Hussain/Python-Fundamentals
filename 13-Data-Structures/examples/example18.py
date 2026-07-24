"""
Module 13 - Data Structures
Example 18: List Unpacking

Purpose:
Demonstrate how to unpack the elements of a list into
individual variables.
"""

# Create a list containing three values.
coordinates = [10, 20, 30]

print("Original list:")
print(coordinates)

# Unpack the list into separate variables.
x_coordinate, y_coordinate, z_coordinate = coordinates

print("\nValues after unpacking:")
print("x_coordinate =", x_coordinate)
print("y_coordinate =", y_coordinate)
print("z_coordinate =", z_coordinate)

# Expected Output:
# Original list:
# [10, 20, 30]
#
# Values after unpacking:
# x_coordinate = 10
# y_coordinate = 20
# z_coordinate = 30