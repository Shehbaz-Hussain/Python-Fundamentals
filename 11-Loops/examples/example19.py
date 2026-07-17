"""
Module: 11-Loops
File: example19.py

Title: Searching for a Number Using for Loop and else

Description:
This example demonstrates how a for loop can be combined
with an else block to perform an action when a value is not
found.
"""

# Store the number to search for.
search_number = 9

# Search numbers from 1 to 5.
for number in range(1, 6):

    if number == search_number:
        print("Number found.")
        break

else:
    print("Number not found.")