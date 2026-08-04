"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 18
Exercise Title: Student Marks Analysis Using Lambda Functions
Difficulty: Intermediate–Advanced

Objective:
    Practice analyzing student records using lambda functions together with
    map(), filter(), reduce(), and sorted(). Extract student names, filter
    high-scoring students, calculate total and average marks, and sort the
    records while keeping the original list unchanged.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

from functools import reduce

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a list of student records.
students = [
    ("Ali", "Mathematics", 82),
    ("Sara", "Physics", 95),
    ("Ahmed", "Chemistry", 68),
    ("Ayesha", "Biology", 91),
    ("Usman", "Mathematics", 74),
    ("Fatima", "Physics", 88),
]

# Create a list containing only student names.
student_names = list(
    map(
        lambda student: student[0],
        students,
    )
)

# Filter students who scored at least 80 marks.
students_scoring_80_or_above = list(
    filter(
        lambda student: student[2] >= 80,
        students,
    )
)

# Calculate the total marks using reduce().
total_marks = reduce(
    lambda total, student: total + student[2],
    students,
    0,
)

# Challenge: Calculate the average marks.
average_marks = total_marks / len(students)

# Sort student records by marks in descending order.
students_sorted_by_marks = sorted(
    students,
    key=lambda student: student[2],
    reverse=True,
)

# Challenge: Sort student records by subject and then by student name.
students_sorted_by_subject_and_name = sorted(
    students,
    key=lambda student: (student[1], student[0]),
)

# Display the results.
print("Original Student Records:")
print(students)

print("\nStudent Names:")
print(student_names)

print("\nStudents Scoring 80 or Above:")
print(students_scoring_80_or_above)

print("\nTotal Marks:")
print(total_marks)

print("\nAverage Marks:")
print(average_marks)

print("\nStudents Sorted by Marks (Highest First):")
print(students_sorted_by_marks)

print("\nStudents Sorted by Subject and Name:")
print(students_sorted_by_subject_and_name)


"""
===============================================================================
Expected Output
===============================================================================

Original Student Records:
[('Ali', 'Mathematics', 82), ('Sara', 'Physics', 95),
 ('Ahmed', 'Chemistry', 68), ('Ayesha', 'Biology', 91),
 ('Usman', 'Mathematics', 74), ('Fatima', 'Physics', 88)]

Student Names:
['Ali', 'Sara', 'Ahmed', 'Ayesha', 'Usman', 'Fatima']

Students Scoring 80 or Above:
[('Ali', 'Mathematics', 82), ('Sara', 'Physics', 95),
 ('Ayesha', 'Biology', 91), ('Fatima', 'Physics', 88)]

Total Marks:
498

Average Marks:
83.0

Students Sorted by Marks (Highest First):
[('Sara', 'Physics', 95), ('Ayesha', 'Biology', 91),
 ('Fatima', 'Physics', 88), ('Ali', 'Mathematics', 82),
 ('Usman', 'Mathematics', 74), ('Ahmed', 'Chemistry', 68)]

Students Sorted by Subject and Name:
[('Ayesha', 'Biology', 91), ('Ahmed', 'Chemistry', 68),
 ('Ali', 'Mathematics', 82), ('Usman', 'Mathematics', 74),
 ('Fatima', 'Physics', 88), ('Sara', 'Physics', 95)]

===============================================================================
Step-by-Step Explanation
===============================================================================

1. The reduce() function is imported from the functools module.
2. A list of student records is created. Each tuple contains:
       - Student name
       - Subject
       - Marks
3. The map() function extracts only the student names.
4. The filter() function selects students whose marks are 80 or greater.
5. The reduce() function adds the marks of all students to calculate the
   total marks.
6. The average marks are calculated by dividing the total marks by the
   number of students.
7. The sorted() function orders the student records by marks in descending
   order.
8. As a challenge, another sorted() call orders the records first by
   subject and then alphabetically by student name.
9. The original list and all generated results are displayed.

How the Lambda Expressions Work
-------------------------------

First lambda expression:

    lambda student: student[0]

- Returns the student's name.
- map() collects all names into a new list.

Second lambda expression:

    lambda student: student[2] >= 80

- Returns True for students who scored at least 80 marks.
- filter() keeps only those records.

Third lambda expression:

    lambda total, student: total + student[2]

- 'total' stores the running sum.
- 'student[2]' accesses the student's marks.
- reduce() combines all marks into a single total.

Fourth lambda expression:

    lambda student: student[2]

- Returns the marks.
- sorted() uses the marks to order the records.

Fifth lambda expression:

    lambda student: (student[1], student[0])

- Returns a tuple containing:
      - Subject
      - Student name
- sorted() first sorts by subject and then by student name.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- map()
- filter()
- reduce()
- sorted()
- key parameter
- Lists
- Tuples
- Arithmetic operations
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(n log n)

Explanation:
- map() processes each record once: O(n)
- filter() processes each record once: O(n)
- reduce() processes each record once: O(n)
- sorted() performs sorting in O(n log n)

The sorting operation dominates the overall time complexity.

===============================================================================
Space Complexity
===============================================================================

O(n)

Explanation:
New lists are created for the mapped, filtered, and sorted results while the
original student list remains unchanged.

===============================================================================
Best Practices
===============================================================================

- Use descriptive variable names for transformed and filtered data.
- Keep lambda expressions short and focused on one task.
- Use reduce() only for cumulative calculations.
- Use sorted() instead of sort() when the original data should remain
  unchanged.

===============================================================================
Common Mistakes
===============================================================================

- Forgetting to import reduce() from functools.
- Using the wrong tuple index when accessing names, subjects, or marks.
- Forgetting to convert map() or filter() objects into lists.
- Omitting reverse=True when sorting in descending order.
- Dividing by the wrong number when calculating the average.

===============================================================================
Alternative Approach
===============================================================================

Another valid implementation is to calculate the average directly using:

    average_marks = reduce(
        lambda total, student: total + student[2],
        students,
        0,
    ) / len(students)

This combines the total calculation and average calculation into one
expression.

===============================================================================
Real-World Relevance
===============================================================================

These techniques are commonly used in:

- Student information systems
- Academic performance analysis
- Educational reporting
- Data analytics
- Machine learning data preprocessing

===============================================================================
Key Takeaways
===============================================================================

- map() transforms data into a new form.
- filter() selects records that satisfy a condition.
- reduce() combines multiple values into a single result.
- sorted() with the key parameter provides flexible custom sorting.
- Lambda functions make data processing concise and readable.
===============================================================================
"""