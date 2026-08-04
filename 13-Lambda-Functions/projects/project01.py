"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Project 01: Student Data Processing System

Difficulty:
Beginner

Estimated Completion Time:
45-60 Minutes

Objective:
Build a simple student data processing system using lambda functions,
map(), filter(), and sorted() to transform, analyze, and organize student
records.

This project introduces how functional programming techniques can be used
for common data processing tasks.

Python Version:
3.13+

===============================================================================
"""


# =============================================================================
# Project Description
# =============================================================================

"""
Problem Statement:
------------------

A school administration department stores student information and wants a small
program to process student performance data.

The system should:

- Calculate student grades
- Filter students based on performance
- Sort students by marks
- Generate processed reports

The goal is to practice using lambda functions with built-in functional tools.


Functional Requirements:
-----------------------

The program must:

1. Store student records.
2. Calculate percentage values using map().
3. Assign performance categories using lambda functions.
4. Filter students who passed.
5. Sort students according to marks.
6. Display a formatted student report.


Prerequisites:
--------------

Before starting this project, learners should understand:

- Variables
- Lists
- Dictionaries
- Lambda functions
- map()
- filter()
- sorted()
- key parameter


Constraints:
------------

Do not use:

- Classes
- External libraries
- File handling
- Database systems

Use only Python built-in features.


Implementation Roadmap:
-----------------------

Step 1:
Create student data records.

Step 2:
Use map() with lambda to calculate percentages.

Step 3:
Use lambda expressions to classify performance.

Step 4:
Use filter() to select passing students.

Step 5:
Use sorted() with key parameter to rank students.

Step 6:
Generate the final report.

===============================================================================
"""


# =============================================================================
# Student Dataset
# =============================================================================

students = [
    {
        "name": "Ali",
        "marks": 450,
        "total": 500
    },
    {
        "name": "Sara",
        "marks": 380,
        "total": 500
    },
    {
        "name": "Ahmed",
        "marks": 290,
        "total": 500
    },
    {
        "name": "Fatima",
        "marks": 470,
        "total": 500
    },
    {
        "name": "Usman",
        "marks": 330,
        "total": 500
    }
]


# =============================================================================
# Step 1: Calculate Percentages Using map()
# =============================================================================

student_percentages = list(
    map(
        lambda student: {
            **student,
            "percentage": (student["marks"] / student["total"]) * 100
        },
        students
    )
)


# =============================================================================
# Step 2: Add Performance Category
# =============================================================================

processed_students = list(
    map(
        lambda student: {
            **student,
            "grade": (
                "Excellent"
                if student["percentage"] >= 90
                else "Good"
                if student["percentage"] >= 75
                else "Average"
                if student["percentage"] >= 60
                else "Needs Improvement"
            )
        },
        student_percentages
    )
)


# =============================================================================
# Step 3: Filter Passing Students
# =============================================================================

passing_students = list(
    filter(
        lambda student: student["percentage"] >= 50,
        processed_students
    )
)


# =============================================================================
# Step 4: Sort Students by Percentage
# =============================================================================

ranked_students = sorted(
    processed_students,
    key=lambda student: student["percentage"],
    reverse=True
)


# =============================================================================
# Student Report
# =============================================================================

print("=" * 60)
print("STUDENT PERFORMANCE REPORT")
print("=" * 60)

for student in ranked_students:
    print(
        f"Name: {student['name']}\n"
        f"Marks: {student['marks']}/{student['total']}\n"
        f"Percentage: {student['percentage']:.2f}%\n"
        f"Performance: {student['grade']}\n"
    )


print("=" * 60)
print(f"Total Students: {len(processed_students)}")
print(f"Passing Students: {len(passing_students)}")
print("=" * 60)


"""
===============================================================================
Sample Input:
===============================================================================

The program uses predefined student records:

[
    {"name": "Ali", "marks": 450, "total": 500},
    {"name": "Sara", "marks": 380, "total": 500}
]


===============================================================================
Sample Output:
===============================================================================

============================================================
STUDENT PERFORMANCE REPORT
============================================================
Name: Fatima
Marks: 470/500
Percentage: 94.00%
Performance: Excellent

Name: Ali
Marks: 450/500
Percentage: 90.00%
Performance: Excellent

Name: Sara
Marks: 380/500
Percentage: 76.00%
Performance: Good

Name: Usman
Marks: 330/500
Percentage: 66.00%
Performance: Average

Name: Ahmed
Marks: 290/500
Percentage: 58.00%
Performance: Average

============================================================
Total Students: 5
Passing Students: 5
============================================================


===============================================================================
Detailed Explanation:
===============================================================================

This project demonstrates how lambda functions can simplify small data
processing operations.

The first map() operation creates new student records by calculating each
student's percentage.

Example:

lambda student: (student["marks"] / student["total"]) * 100

The second map() operation adds performance categories based on percentages.

The filter() function removes students who do not meet the passing criteria.

The sorted() function uses a lambda expression as a key function:

sorted(
    students,
    key=lambda student: student["percentage"]
)

The key parameter tells Python which value should be used for comparison
during sorting.


===============================================================================
Code Walkthrough:
===============================================================================

1. Student Data

The program starts with a list containing student dictionaries.

2. Percentage Calculation

map() applies the lambda function to every student.

3. Performance Classification

A lambda expression creates a performance label.

4. Filtering

filter() keeps only students meeting the required condition.

5. Ranking

sorted() organizes students from highest to lowest percentage.


===============================================================================
Best Practices:
===============================================================================

- Use lambda functions for short and simple operations.
- Use meaningful dictionary keys.
- Keep data processing steps separated.
- Use sorted() key functions instead of manual sorting logic.
- Avoid writing complex expressions inside lambda functions.


===============================================================================
Common Mistakes:
===============================================================================

1. Writing long complicated lambda functions.

2. Forgetting to convert map() and filter() results into lists when required.

3. Using incorrect dictionary keys.

4. Forgetting reverse=True when ranking in descending order.


===============================================================================
Possible Improvements:
===============================================================================

- Add user input for student records.
- Store results in files.
- Add subject-wise analysis.
- Create graphical reports.
- Connect with a database system.


===============================================================================
Bonus Challenges:
===============================================================================

1. Find the top three students using sorted().

2. Calculate average class percentage using reduce().

3. Add attendance information and filter students based on attendance.

4. Create a scholarship eligibility system.


===============================================================================
Real-World Applications:
===============================================================================

Similar processing techniques are used in:

- Student management systems
- Learning management platforms
- Data analysis pipelines
- Machine learning dataset preparation
- Educational reporting systems


===============================================================================
Key Learning Outcomes:
===============================================================================

After completing this project, learners should understand:

✓ How lambda functions process data
✓ How map() transforms collections
✓ How filter() selects data
✓ How sorted() uses key functions
✓ How functional programming concepts apply to real applications

===============================================================================
"""