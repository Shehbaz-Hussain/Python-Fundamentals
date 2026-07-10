# Example 14: Real-World Examples
# This program demonstrates practical uses of
# logical operators in everyday situations.

# --------------------------------------------------
# Example 1: Voting Eligibility
# --------------------------------------------------

age = 20

print("Example 1: Voting Eligibility")
print("Age:", age)
print("Eligible to vote:", age >= 18)

print()

# --------------------------------------------------
# Example 2: Bank Account Eligibility
# --------------------------------------------------

age = 25
minimum_balance = 6000

print("Example 2: Bank Account Eligibility")
print("Age:", age)
print("Minimum Balance:", minimum_balance)

eligible_for_account = age >= 18 and minimum_balance >= 5000

print("Eligible:", eligible_for_account)

print()

# --------------------------------------------------
# Example 3: Employee Bonus
# --------------------------------------------------

years_of_service = 6
performance_score = 90

print("Example 3: Employee Bonus")

bonus_eligible = (
    years_of_service >= 5 and
    performance_score >= 85
)

print("Years of Service:", years_of_service)
print("Performance Score:", performance_score)
print("Bonus Eligible:", bonus_eligible)

print()

# --------------------------------------------------
# Example 4: Security Check
# --------------------------------------------------

has_id_card = True
has_access_card = False

print("Example 4: Security Check")

access_allowed = has_id_card or has_access_card

print("Has ID Card:", has_id_card)
print("Has Access Card:", has_access_card)
print("Access Allowed:", access_allowed)

print()

# --------------------------------------------------
# Example 5: Admission Eligibility
# --------------------------------------------------

marks = 82
age = 19

print("Example 5: Admission Eligibility")

admission_allowed = marks >= 80 and age >= 18

print("Marks:", marks)
print("Age:", age)
print("Admission Allowed:", admission_allowed)


# Expected Output:

# Example 1: Voting Eligibility
# Age: 20
# Eligible to vote: True

# Example 2: Bank Account Eligibility
# Age: 25
# Minimum Balance: 6000
# Eligible: True

# Example 3: Employee Bonus
# Years of Service: 6
# Performance Score: 90
# Bonus Eligible: True

# Example 4: Security Check
# Has ID Card: True
# Has Access Card: False
# Access Allowed: True

# Example 5: Admission Eligibility
# Marks: 82
# Age: 19
# Admission Allowed: True