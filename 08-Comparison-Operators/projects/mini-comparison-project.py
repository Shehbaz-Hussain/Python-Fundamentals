# Mini Comparison Project

student_name = input("Enter the student name: ")

marks = int(input("Enter the student's marks: "))
passing_marks = int(input("Enter the passing marks: "))

print("\nComparison Results")
print("------------------")
print("Student Name:", student_name)
print("Marks:", marks)
print("Passing Marks:", passing_marks)

print("Equal to Passing Marks:", marks == passing_marks)
print("Not Equal to Passing Marks:", marks != passing_marks)
print("Greater Than Passing Marks:", marks > passing_marks)
print("Less Than Passing Marks:", marks < passing_marks)
print("Greater Than or Equal To Passing Marks:", marks >= passing_marks)
print("Less Than or Equal To Passing Marks:", marks <= passing_marks)