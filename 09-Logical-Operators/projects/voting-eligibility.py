# Project: Voting Eligibility Checker
# -----------------------------------
# Objective:
# Determine whether a person is eligible to vote.
#
# Concepts Used:
# - Variables
# - Input and Output
# - Type Conversion
# - Comparison Operators
# - Logical Operators
#
# Note:
# This project uses only concepts covered up to Module 09.

print("===== Voting Eligibility Checker =====")

age = int(input("Enter your age: "))
citizenship = input("Are you a citizen? (yes/no): ")

print()

eligible_to_vote = (
    age >= 18 and
    citizenship == "yes"
)

print("Age:", age)
print("Citizen:", citizenship)

print()

print("Age Requirement Met:", age >= 18)
print("Citizenship Requirement Met:", citizenship == "yes")

print()

print("Eligible to Vote:", eligible_to_vote)


# Sample Output 1:

# ===== Voting Eligibility Checker =====
# Enter your age: 22
# Are you a citizen? (yes/no): yes

# Age: 22
# Citizen: yes

# Age Requirement Met: True
# Citizenship Requirement Met: True

# Eligible to Vote: True

# Sample Output 2:

# ===== Voting Eligibility Checker =====
# Enter your age: 16
# Are you a citizen? (yes/no): yes

# Age: 16
# Citizen: yes

# Age Requirement Met: False
# Citizenship Requirement Met: True

# Eligible to Vote: False

# Sample Output 3:

# ===== Voting Eligibility Checker =====
# Enter your age: 25
# Are you a citizen? (yes/no): no

# Age: 25
# Citizen: no

# Age Requirement Met: True
# Citizenship Requirement Met: False

# Eligible to Vote: False
