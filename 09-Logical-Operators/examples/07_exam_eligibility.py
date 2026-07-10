# Example 07: Exam Eligibility
# This program checks whether a student is eligible
# to appear in an exam based on attendance and fee status.

attendance = float(input("Enter attendance percentage: "))
fee_paid = input("Have you paid the examination fee? (yes/no): ")

print()

print("Attendance:", attendance)
print("Fee Paid:", fee_paid)

# Check whether the student is eligible.
is_eligible = attendance >= 75 and fee_paid == "yes"

print("Eligible for exam:", is_eligible)

# Display individual condition results.
print("Attendance requirement met:", attendance >= 75)
print("Fee requirement met:", fee_paid == "yes")

# Sample Output 1:

# Enter attendance percentage: 82
# Have you paid the examination fee? (yes/no): yes

# Attendance: 82.0
# Fee Paid: yes
# Eligible for exam: True
# Attendance requirement met: True
# Fee requirement met: True

# Sample Output 2:

# Enter attendance percentage: 68
# Have you paid the examination fee? (yes/no): no

# Attendance: 68.0
# Fee Paid: yes
# Eligible for exam: False
# Attendance requirement met: False 
# Fee requirement met: True


# Sample Output 3:

# Enter attendance percentage: 80
# Have you paid the examination fee? (yes/no): no
# Attendance: 80.0
# Fee Paid: no
# Eligible for exam: False
# Attendance requirement met: True
# Fee requirement met: False
