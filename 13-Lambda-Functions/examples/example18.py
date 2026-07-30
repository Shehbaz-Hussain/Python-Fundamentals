"""
File: example18.py
Topic: Lambda Function for Sorting Real-World Records

Description:
This example demonstrates how lambda functions can be used with
sorted() to organize records based on a specific value.

Concepts Covered:
- Lambda functions with sorted()
- key parameter
- Sorting records by a field

Python Version:
Python 3.13+
"""


# Creating a list of student records
students = [
    ("Ali", 85),
    ("Sara", 92),
    ("Ahmed", 78),
    ("Zain", 88)
]


# Sorting students based on their marks
sorted_students = sorted(
    students,
    key=lambda student: student[1]
)


# Displaying sorted records
print(sorted_students)


"""
Expected Output:

[('Ahmed', 78), ('Ali', 85), ('Zain', 88), ('Sara', 92)]


Explanation:

1. A list of student records is created.
2. Each record contains:
   - Student name
   - Student marks

3. The sorted() function arranges the records.
4. The key parameter receives a lambda function.
5. The lambda function returns the second item of each tuple,
   which represents the student's marks.
6. Python uses those marks to determine the sorting order.

Best Practice:

Use lambda functions with sorted() when sorting requires a
simple extraction rule. If the sorting logic becomes complex,
create a separate function.

Real-World Relevance:

Sorting records is common in student management systems,
employee databases, ranking systems, analytics applications,
and machine learning dataset preparation.
"""