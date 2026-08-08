"""
Module 13 - Data Structures
Solution 13: Accessing Values in a Nested Dictionary

Solution:
"""

# Create the employee dictionary.
employee = {
    "name": "Sara",
    "department": "IT",
    "address": {
        "city": "Gilgit",
        "country": "Pakistan"
    }
}

# Print the complete dictionary.
print(employee)

# Print the employee's name.
print(employee["name"])

# Print the city.
print(employee["address"]["city"])

# Print the country.
print(employee["address"]["country"])