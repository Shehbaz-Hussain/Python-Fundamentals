# Example 02: OR Operator
# This program demonstrates how the 'or' logical operator works.

# Example 1
marks = 45

print("Example 1")
print("Marks:", marks)
print("Marks are 50 or above, or at least 40:", marks >= 50 or marks >= 40)

print()

# Example 2
temperature = 38

print("Example 2")
print("Temperature:", temperature)
print("Temperature is below 0 or above 35:", temperature < 0 or temperature > 35)

print()

# Example 3
number = -5

print("Example 3")
print("Number:", number)
print("Number is positive or even:", number > 0 or number % 2 == 0)

print()

# Example 4
age = 16

print("Example 4")
print("Age:", age)
print("Age is 18 or above, or 21 or above:", age >= 18 or age >= 21)

# Expected Output:

# Example 1
# Marks: 45
# Marks are 50 or above, or at least 40: True

# Example 2
# Temperature: 38
# Temperature is below 0 or above 35: True

# Example 3
# Number: -5
# Number is positive or even: False

# Example 4
# Age: 16
# Age is 18 or above, or 21 or above: False