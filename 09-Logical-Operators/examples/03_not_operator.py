# Example 03: NOT Operator
# This program demonstrates how the 'not' logical operator works.

# Example 1
is_logged_in = False

print("Example 1")
print("Is Logged In:", is_logged_in)
print("Result of not:", not is_logged_in)

print()

# Example 2
age = 15

print("Example 2")
print("Age:", age)
print("Age is NOT 18 or above:", not (age >= 18))

print()

# Example 3
number = 8

print("Example 3")
print("Number:", number)
print("Number is NOT negative:", not (number < 0))

print()

# Example 4
temperature = 35

print("Example 4")
print("Temperature:", temperature)
print("Temperature is NOT 30 or below:", not (temperature <= 30))


# Expected Output:

# Example 1
# Is Logged In: False
# Result of not: True

# Example 2
# Age: 15
# Age is NOT 18 or above: True

# Example 3
# Number: 8
# Number is NOT negative: True

# Example 4
# Temperature: 35
# Temperature is NOT 30 or below: True