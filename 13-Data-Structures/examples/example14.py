"""
Module 13 - Data Structures
Example 14: Checking for Key Membership in a Dictionary

Purpose:
Demonstrate how to use the `in` and `not in` membership operators
to determine whether a key exists in a dictionary.
"""

# Create a dictionary containing country-capital pairs.
capitals = {
    "Pakistan": "Islamabad",
    "Japan": "Tokyo",
    "Canada": "Ottawa"
}

print("Dictionary:")
print(capitals)

# Check whether specific keys exist in the dictionary.
print("\nIs 'Japan' a key in the dictionary?")
print("Japan" in capitals)

print("\nIs 'Brazil' a key in the dictionary?")
print("Brazil" in capitals)

print("\nIs 'Canada' not a key in the dictionary?")
print("Canada" not in capitals)

# Expected Output:
# Dictionary:
# {'Pakistan': 'Islamabad', 'Japan': 'Tokyo', 'Canada': 'Ottawa'}
#
# Is 'Japan' a key in the dictionary?
# True
#
# Is 'Brazil' a key in the dictionary?
# False
#
# Is 'Canada' not a key in the dictionary?
# False