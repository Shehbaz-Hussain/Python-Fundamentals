"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 24
Exercise Title: AI/ML Dataset Preprocessing Using Lambda Functions
Difficulty: Advanced

Objective:
    Use lambda functions to perform common preprocessing tasks on a small
    machine learning dataset before model training.

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

# Create the machine learning dataset.
dataset = [
    ("Ali", 20, 18, 82),
    ("Sara", 22, 25, 95),
    ("Ahmed", 19, 12, 68),
    ("Ayesha", 21, 20, 91),
    ("Usman", 23, 10, 63),
    ("Fatima", 20, 28, 97),
    ("Bilal", 24, 16, 74),
    ("Hina", 22, 14, 79),
]


# Create a function using lambda to assign grades.
assign_grade = lambda score: (
    "A"
    if score >= 90
    else "B"
    if score >= 80
    else "C"
    if score >= 70
    else "D"
    if score >= 60
    else "F"
)


# Add grade information to each record.
processed_dataset = list(
    map(
        lambda student: (
            student[0],
            student[1],
            student[2],
            student[3],
            assign_grade(student[3]),
        ),
        dataset,
    )
)


# Filter students who scored at least 80 marks.
high_scoring_students = list(
    filter(
        lambda student: student[3] >= 80,
        processed_dataset,
    )
)


# Calculate total exam score.
total_exam_score = reduce(
    lambda total, student: total + student[3],
    dataset,
    0,
)


# Calculate average exam score.
average_exam_score = total_exam_score / len(dataset)


# Sort students by exam score in descending order.
sorted_by_exam_score = sorted(
    processed_dataset,
    key=lambda student: student[3],
    reverse=True,
)


# -----------------------------------------------------------------------------
# Challenge Solutions
# -----------------------------------------------------------------------------

# Increase study hours by 10%.
increased_study_hours_dataset = list(
    map(
        lambda student: (
            student[0],
            student[1],
            student[2] * 1.10,
            student[3],
        ),
        dataset,
    )
)


# Select students with study hours >= 18.
students_with_required_hours = list(
    filter(
        lambda student: student[2] >= 18,
        dataset,
    )
)


# Sort students alphabetically by name.
sorted_by_name = sorted(
    processed_dataset,
    key=lambda student: student[0],
)


# Create a list containing only grades.
grades = list(
    map(
        lambda student: student[4],
        processed_dataset,
    )
)


# Count each grade.
grade_counts = {
    "A": grades.count("A"),
    "B": grades.count("B"),
    "C": grades.count("C"),
    "D": grades.count("D"),
    "F": grades.count("F"),
}


# -----------------------------------------------------------------------------
# Display Results
# -----------------------------------------------------------------------------

print("Original Dataset:")
print(dataset)

print("\nDataset with Grades:")
print(processed_dataset)

print("\nStudents Scoring 80 or Above:")
print(high_scoring_students)

print("\nTotal Exam Score:")
print(total_exam_score)

print("\nAverage Exam Score:")
print(average_exam_score)

print("\nDataset Sorted by Exam Score (Highest First):")
print(sorted_by_exam_score)

print("\nDataset with Study Hours Increased by 10%:")
print(increased_study_hours_dataset)

print("\nStudents with Study Hours >= 18:")
print(students_with_required_hours)

print("\nDataset Sorted Alphabetically by Name:")
print(sorted_by_name)

print("\nGrades:")
print(grades)

print("\nGrade Count:")
print(grade_counts)


"""
===============================================================================
Expected Output
===============================================================================

Original Dataset:
[('Ali', 20, 18, 82), ('Sara', 22, 25, 95),
 ('Ahmed', 19, 12, 68), ('Ayesha', 21, 20, 91),
 ('Usman', 23, 10, 63), ('Fatima', 20, 28, 97),
 ('Bilal', 24, 16, 74), ('Hina', 22, 14, 79)]

Dataset with Grades:
[('Ali', 20, 18, 82, 'B'),
 ('Sara', 22, 25, 95, 'A'),
 ('Ahmed', 19, 12, 68, 'D'),
 ('Ayesha', 21, 20, 91, 'A'),
 ('Usman', 23, 10, 63, 'D'),
 ('Fatima', 20, 28, 97, 'A'),
 ('Bilal', 24, 16, 74, 'C'),
 ('Hina', 22, 14, 79, 'C')]

Students Scoring 80 or Above:
[('Ali', 20, 18, 82, 'B'),
 ('Sara', 22, 25, 95, 'A'),
 ('Ayesha', 21, 20, 91, 'A')]

Total Exam Score:
649

Average Exam Score:
81.125

Dataset Sorted by Exam Score (Highest First):
[('Fatima', 20, 28, 97, 'A'),
 ('Sara', 22, 25, 95, 'A'),
 ('Ayesha', 21, 20, 91, 'A'),
 ('Ali', 20, 18, 82, 'B'),
 ('Hina', 22, 14, 79, 'C'),
 ('Bilal', 24, 16, 74, 'C'),
 ('Ahmed', 19, 12, 68, 'D'),
 ('Usman', 23, 10, 63, 'D')]

Dataset with Study Hours Increased by 10%:
[('Ali', 20, 19.8, 82), ('Sara', 22, 27.500000000000004, 95),
 ('Ahmed', 19, 13.200000000000001, 68),
 ('Ayesha', 21, 22.0, 91),
 ('Usman', 23, 11.0, 63),
 ('Fatima', 20, 30.800000000000004, 97),
 ('Bilal', 24, 17.6, 74),
 ('Hina', 22, 15.400000000000002, 79)]

Students with Study Hours >= 18:
[('Ali', 20, 18, 82),
 ('Sara', 22, 25, 95),
 ('Ayesha', 21, 20, 91),
 ('Fatima', 20, 28, 97)]

Grades:
['B', 'A', 'D', 'A', 'D', 'A', 'C', 'C']

Grade Count:
{'A': 3, 'B': 1, 'C': 2, 'D': 2, 'F': 0}

===============================================================================
Step-by-Step Explanation
===============================================================================

1. The dataset contains student information:
   - Name
   - Age
   - Study hours
   - Exam score

2. A lambda expression assigns grades based on exam scores.

3. map() transforms each student record by adding the calculated grade.

4. filter() selects students who achieved at least 80 marks.

5. reduce() calculates the total exam score of all students.

6. The average score is calculated using the total score divided by the
   number of students.

7. sorted() orders students by exam score from highest to lowest.

8. Challenge operations:
   - Increase study hours by 10%.
   - Select students meeting study hour requirements.
   - Sort students alphabetically.
   - Extract grades.
   - Count grade distribution.

How the Lambda Expressions Work
-------------------------------

Lambda 1:

    lambda score: (...)

Assigns a grade using conditional expressions.

Lambda 2:

    lambda student: (...)

Creates a new student record containing grade information.

Lambda 3:

    lambda student: student[3] >= 80

Filters students based on exam score.

Lambda 4:

    lambda total, student: total + student[3]

Adds exam scores together.

Lambda 5:

    lambda student: student[3]

Provides the sorting key for exam scores.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- map()
- filter()
- reduce()
- sorted()
- key parameter
- Conditional expressions
- Lists
- Tuples
- String operations
- Arithmetic operations

===============================================================================
Time Complexity
===============================================================================

Overall Complexity: O(n log n)

Explanation:
- map(): O(n)
- filter(): O(n)
- reduce(): O(n)
- sorted(): O(n log n)

Sorting dominates the overall complexity.

===============================================================================
Space Complexity
===============================================================================

Overall Complexity: O(n)

Explanation:
Additional datasets and lists are created while keeping the original dataset
unchanged.

===============================================================================
Best Practices
===============================================================================

- Keep preprocessing steps separate and readable.
- Avoid modifying raw datasets directly.
- Use descriptive names for transformed data.
- Apply lambda expressions only for simple operations.

===============================================================================
Common Mistakes
===============================================================================

- Incorrect grade boundaries.
- Using the wrong index for exam scores.
- Forgetting to convert map() and filter() results into lists.
- Modifying the original dataset.
- Calculating the average using the wrong number of records.

===============================================================================
Alternative Approach
===============================================================================

A dictionary-based grading system could replace nested conditional
expressions for easier maintenance in larger machine learning pipelines.

===============================================================================
Real-World Relevance
===============================================================================

These preprocessing techniques are commonly used in:

- Machine learning data preparation
- Feature engineering
- Student performance prediction systems
- Data cleaning pipelines
- Educational analytics

===============================================================================
Key Takeaways
===============================================================================

- Lambda functions are useful for compact preprocessing operations.
- map(), filter(), reduce(), and sorted() are powerful tools for dataset
  processing.
- Data preprocessing is an important step before machine learning model
  training.
- Keeping raw data unchanged improves reliability and reproducibility.
===============================================================================
"""