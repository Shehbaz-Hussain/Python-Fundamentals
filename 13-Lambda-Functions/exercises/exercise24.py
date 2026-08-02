"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Exercise 24: AI/ML Dataset Preprocessing Using Lambda Functions

Difficulty:
Advanced

Estimated Time:
40–50 Minutes

Objective:
Use lambda functions to perform common preprocessing tasks on a small
machine learning dataset before model training.

Instructions:
A dataset contains the following records:

(Name, Age, Study Hours per Week, Exam Score)

Create the following list:

dataset = [
    ("Ali", 20, 18, 82),
    ("Sara", 22, 25, 95),
    ("Ahmed", 19, 12, 68),
    ("Ayesha", 21, 20, 91),
    ("Usman", 23, 10, 63),
    ("Fatima", 20, 28, 97),
    ("Bilal", 24, 16, 74),
    ("Hina", 22, 14, 79)
]

Perform the following tasks:

1. Display the original dataset.

2. Use map() with a lambda function to create a new dataset containing:

   (
       Name,
       Age,
       Study Hours,
       Exam Score,
       Grade
   )

   Assign grades using the following rules:

   - A : Score ≥ 90
   - B : Score ≥ 80
   - C : Score ≥ 70
   - D : Score ≥ 60
   - F : Score < 60

3. Use filter() with a lambda function to extract students who scored
   at least 80 marks.

4. Import reduce from functools and calculate the total exam score of
   all students.

5. Calculate the average exam score.

6. Use sorted() with a lambda function to sort the dataset by exam score
   in descending order.

7. Display every generated result with appropriate headings.

Requirements:
- Use lambda functions.
- Use map(), filter(), reduce(), and sorted().
- Keep the original dataset unchanged.
- Follow PEP 8 style guidelines.

Challenge:

1. Create another dataset where study hours are increased by 10%.
2. Display only students whose study hours are greater than or equal to
   18 hours per week.
3. Sort the dataset alphabetically by student name.
4. Create a list containing only grades.
5. Count how many students received each grade.
===============================================================================
"""