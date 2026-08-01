"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Exercise 15: Sorting Records Using the key Parameter and Lambda

Difficulty:
Intermediate

Estimated Time:
20–30 Minutes

Objective:
Practice sorting a collection of records using the key parameter with a
lambda function.

Instructions:
1. Create the following list of student records:

students = [
    ("Ali", 82),
    ("Sara", 95),
    ("Ahmed", 76),
    ("Zain", 88),
    ("Ayesha", 91)
]

Each tuple contains:
- Student name
- Exam score

2. Use sorted() with a lambda function to sort the records by exam score
   in ascending order.

3. Store the sorted records in a new list.

4. Display:
   - Original student records
   - Student records sorted by score

Expected Output Format:

Original Student Records:
[('Ali', 82), ('Sara', 95), ('Ahmed', 76), ('Zain', 88), ('Ayesha', 91)]

Sorted by Score:
[('Ahmed', 76), ('Ali', 82), ('Zain', 88), ('Ayesha', 91), ('Sara', 95)]

Requirements:
- Use sorted().
- Use the key parameter.
- Use a lambda function to access the score.
- Do not modify the original list.
- Follow PEP 8 style guidelines.

Challenge:
1. Create another sorted list in descending order of scores.
2. Create another sorted list sorted alphabetically by student name
   using a different lambda expression.
===============================================================================
"""