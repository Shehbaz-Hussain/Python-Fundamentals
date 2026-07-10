# Project: Employee Bonus Checker
# --------------------------------
# Objective:
# Determine whether an employee is eligible for a bonus.
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

print("===== Employee Bonus Checker =====")

years_of_service = int(input("Enter years of service: "))
performance_score = int(input("Enter performance score: "))

print()

bonus_eligible = (
    years_of_service >= 5 and
    performance_score >= 85
)

print("Years of Service:", years_of_service)
print("Performance Score:", performance_score)

print()

print("Service Requirement Met:", years_of_service >= 5)
print("Performance Requirement Met:", performance_score >= 85)

print()

print("Bonus Eligible:", bonus_eligible)


# Sample Output 1:

# ===== Employee Bonus Checker =====
# Enter years of service: 6
# Enter performance score: 90

# Years of Service: 6
# Performance Score: 90

# Service Requirement Met: True
# Performance Requirement Met: True

# Bonus Eligible: True


# Sample Output 2:

# ===== Employee Bonus Checker =====
# Enter years of service: 3
# Enter performance score: 92

# Years of Service: 3
# Performance Score: 92

# Service Requirement Met: False
# Performance Requirement Met: True

# Bonus Eligible: False


# Sample Output 3:

# ===== Employee Bonus Checker =====
# Enter years of service: 8
# Enter performance score: 80

# Years of Service: 8
# Performance Score: 80

# Service Requirement Met: True
# Performance Requirement Met: False

# Bonus Eligible: False