"""
Exercise 13: Student Result Checker

Problem Statement:
Write a Python program that asks the user to enter marks (out of 100) for
three subjects. Calculate the total marks, percentage, and determine the
student's result.

Result Rules:
- A student passes only if they score at least 40 marks in each subject.
- If the student scores less than 40 in any subject, the result is "Fail".
- If the student passes all subjects, determine the grade using the percentage:

Grade Criteria:
- 90% and above      -> Grade A+
- 80% to 89%         -> Grade A
- 70% to 79%         -> Grade B
- 60% to 69%         -> Grade C
- 50% to 59%         -> Grade D
- Below 50%          -> Grade E

Expected Output Example:

Enter marks for Subject 1: 85
Enter marks for Subject 2: 78
Enter marks for Subject 3: 92

Total Marks: 255
Percentage: 85.0%
Result: Pass
Grade: A
"""

# Ask the user to enter marks for three subjects
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

# Calculate total marks
total_marks = subject1 + subject2 + subject3

# Calculate percentage
percentage = (total_marks / 300) * 100

# Display total marks and percentage
print("\nTotal Marks:", total_marks)
print("Percentage:", round(percentage, 2), "%")

# Check whether the student has passed all subjects
if subject1 >= 40 and subject2 >= 40 and subject3 >= 40:
    print("Result: Pass")

    # Determine the grade
    if percentage >= 90:
        print("Grade: A+")
    elif percentage >= 80:
        print("Grade: A")
    elif percentage >= 70:
        print("Grade: B")
    elif percentage >= 60:
        print("Grade: C")
    elif percentage >= 50:
        print("Grade: D")
    else:
        print("Grade: E")
else:
    print("Result: Fail")