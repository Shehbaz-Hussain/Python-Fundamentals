# Example 15: Practice Examples
# This program contains several beginner-friendly
# practice examples using logical operators.

print("========== Practice Example 1 ==========")

age = 22

print("Age:", age)
print("Eligible for a driving license:", age >= 18)

print()

print("========== Practice Example 2 ==========")

marks = 78
attendance = 82

print("Marks:", marks)
print("Attendance:", attendance)

eligible_for_exam = marks >= 50 and attendance >= 75

print("Eligible for final exam:", eligible_for_exam)

print()

print("========== Practice Example 3 ==========")

temperature = 39

print("Temperature:", temperature)

weather_alert = temperature < 0 or temperature > 35

print("Weather alert:", weather_alert)

print()

print("========== Practice Example 4 ==========")

number = -8

print("Number:", number)

positive_number = number > 0
even_number = number % 2 == 0

print("Positive Number:", positive_number)
print("Even Number:", even_number)
print("Positive and Even:", positive_number and even_number)

print()

print("========== Practice Example 5 ==========")

username = "admin"
password = "python123"

entered_username = "admin"
entered_password = "python123"

login_successful = (
    entered_username == username and
    entered_password == password
)

print("Username Correct:", entered_username == username)
print("Password Correct:", entered_password == password)
print("Login Successful:", login_successful)

print()

print("========== Practice Example 6 ==========")

is_holiday = False

print("Is Holiday:", is_holiday)
print("Not Holiday:", not is_holiday)

print()

print("========== Practice Example 7 ==========")

age = 17
has_permission = True

entry_allowed = age >= 18 or has_permission

print("Age:", age)
print("Has Permission:", has_permission)
print("Entry Allowed:", entry_allowed)

print()

print("========== Practice Example 8 ==========")

salary = 65000
years_of_service = 6

bonus_eligible = salary >= 50000 and years_of_service >= 5

print("Salary:", salary)
print("Years of Service:", years_of_service)
print("Bonus Eligible:", bonus_eligible)


# Expected Output:

# ========== Practice Example 1 ==========
# Age: 22
# Eligible for a driving license: True

# ========== Practice Example 2 ==========
# Marks: 78
# Attendance: 82
# Eligible for final exam: True

# ========== Practice Example 3 ==========
# Temperature: 39
# Weather alert: True

# ========== Practice Example 4 ==========
# Number: -8
# Positive Number: False
# Even Number: True
# Positive and Even: False

# ========== Practice Example 5 ==========
# Username Correct: True
# Password Correct: True
# Login Successful: True

# ========== Practice Example 6 ==========
# Is Holiday: False
# Not Holiday: True

# ========== Practice Example 7 ==========
# Age: 17
# Has Permission: True
# Entry Allowed: True

# ========== Practice Example 8 ==========
# Salary: 65000
# Years of Service: 6
# Bonus Eligible: True