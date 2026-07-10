# Project: Admission Checker
# -----------------------------------
# Objective:
# Check whether a student is eligible for admission.
#
# Concepts Used:
# - Variables
# - Input and Output
# - Type Conversion
# - Comparison Operators
# - Logical Operators (and)
#
# Note:
# This project uses only concepts covered up to Module 09.

print("===== Admission Eligibility Checker =====")

age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))

print()

admission_eligible = (
    age >= 18 and
    marks >= 80
)

print("Age:", age)
print("Marks:", marks)

print()

print("Age Requirement Met:", age >= 18)
print("Marks Requirement Met:", marks >= 80)

print()

print("Admission Eligible:", admission_eligible)


# Sample Output 1:

# ===== Admission Eligibility Checker =====
# Enter your age: 19
# Enter your marks: 85

# Age: 19
# Marks: 85

# Age Requirement Met: True
# Marks Requirement Met: True

# Admission Eligible: True

# Sample Output 2:

# ===== Admission Eligibility Checker =====
# Enter your age: 17
# Enter your marks: 92

# Age: 17
# Marks: 92

# Age Requirement Met: False
# Marks Requirement Met: True

# Admission Eligible: False

# Sample Output 3:

# ===== Admission Eligibility Checker =====
# Enter your age: 20
# Enter your marks: 75

# Age: 20
# Marks: 75

# Age Requirement Met: True
# Marks Requirement Met: False

# Admission Eligible: False