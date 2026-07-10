# Example 05: Age Validation
# This program checks whether a person's age is within
# the valid range for registration.

age = int(input("Enter your age: "))

print()

print("Age:", age)

# Check whether the age is between 18 and 60 (inclusive).
is_valid_age = age >= 18 and age <= 60

print("Age is between 18 and 60:", is_valid_age)

# Check whether the person is under 18.
print("Age is below 18:", age < 18)

# Check whether the person is above 60.
print("Age is above 60:", age > 60)


# Expected Output:

# Enter your age: 25
# Age: 25   
# Age is between 18 and 60: True
# Age is below 18: False
# Age is above 60: False
