# Example 08: Even and Positive Number
# This program checks whether a number is both
# positive and even.

number = int(input("Enter a number: "))

print()

print("Number:", number)

# Check whether the number is positive and even.
is_positive_and_even = number > 0 and number % 2 == 0

print("Positive and even:", is_positive_and_even)

# Display individual condition results.
print("Positive number:", number > 0)
print("Even number:", number % 2 == 0)


# Sample Output 1:

# Enter a number: 8

# Number: -8
# Positive and even: False
# Positive number: False
# Even number: True

# Sample Output 2:

# Enter a number: 7

# Number: -8
# Positive and even: False
# Positive number: False
# Even number: Tru