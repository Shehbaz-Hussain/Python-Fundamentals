# Example 04: Multiple Conditions
# This program demonstrates how multiple logical conditions
# can be combined using logical operators.

# Example 1
age = 20
marks = 85

print("Example 1")
print("Age:", age)
print("Marks:", marks)
print("Eligible for admission:", age >= 18 and marks >= 80)

print()

# Example 2
temperature = 38
is_raining = False

print("Example 2")
print("Temperature:", temperature)
print("Is Raining:", is_raining)
print("Weather warning:", temperature > 35 or is_raining)

print()

# Example 3
number = 12

print("Example 3")
print("Number:", number)
print("Positive and even:", number > 0 and number % 2 == 0)

print()

# Example 4
age = 16
has_permission = True

print("Example 4")
print("Age:", age)
print("Has Permission:", has_permission)
print("Entry allowed:", age >= 18 or has_permission)

print()

# Example 5
marks = 45

print("Example 5")
print("Marks:", marks)
print("Did not pass:", not (marks >= 50))


# Expected Output:

# Example 1
# Age: 20   
# Marks: 85
# Eligible for admission: True

# Example 2
# Temperature: 38
# Is Raining: False
# Weather warning: True

# Example 3
# Number: 12
# Positive and even: True

# Example 4
# Age: 16
# Has Permission: True
# Entry allowed: True

# Example 5
# Marks: 45
# Did not pass: True