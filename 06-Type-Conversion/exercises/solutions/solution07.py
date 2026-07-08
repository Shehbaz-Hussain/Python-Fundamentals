"""
File: solution07.py

Solution to Exercise 07: Calculate the Average of Three Marks

This program demonstrates how to:
- Accept user input.
- Convert string input into integers.
- Calculate the average of three marks.
- Display the result and its data type.

Note:
The average is a float because the division (/) operator
always returns a floating-point number in Python.
"""

# Ask the user to enter marks for three subjects
mark1_text = input("Enter marks for Subject 1: ")
mark2_text = input("Enter marks for Subject 2: ")
mark3_text = input("Enter marks for Subject 3: ")

# Convert the string inputs into integers
mark1 = int(mark1_text)
mark2 = int(mark2_text)
mark3 = int(mark3_text)

# Calculate the average marks
average = (mark1 + mark2 + mark3) / 3

print()

# Display the entered marks
print("Subject 1 Marks:", mark1)
print("Subject 2 Marks:", mark2)
print("Subject 3 Marks:", mark3)

print()

# Display the calculated average
print("Average Marks:", average)

# Display the data type of the average
print("Average Type:", type(average))