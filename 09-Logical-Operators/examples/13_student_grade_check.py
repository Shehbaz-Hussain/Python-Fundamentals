# Example 13: Student Grade Check
# This program checks whether a student has passed
# based on marks and attendance.

marks = int(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))

print()

print("Marks:", marks)
print("Attendance:", attendance)

# Check whether the student has passed.
has_passed = marks >= 50 and attendance >= 75

print("Student passed:", has_passed)

# Display individual condition results.
print("Marks requirement met:", marks >= 50)
print("Attendance requirement met:", attendance >= 75)

# Check whether the student failed.
print("Student failed:", not has_passed)


# Sample Output 1:

# Enter marks: 72
# Enter attendance percentage: 85

# Marks: 72
# Attendance: 85.0
# Student passed: True
# Marks requirement met: True
# Attendance requirement met: True
# Student failed: False

# Sample Output 2:

# Enter marks: 45
# Enter attendance percentage: 80

# Marks: 45
# Attendance: 80.0
# Student passed: False
# Marks requirement met: False
# Attendance requirement met: True
# Student failed: True

# Sample Output 3:

# Enter marks: 68
# Enter attendance percentage: 60

# Marks: 68
# Attendance: 60.0
# Student passed: False
# Marks requirement met: True
# Attendance requirement met: False
# Student failed: True