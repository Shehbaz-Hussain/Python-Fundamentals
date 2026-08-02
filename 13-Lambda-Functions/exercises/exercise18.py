"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Exercise 18: Student Marks Analysis Using Lambda Functions

Difficulty:
Intermediate–Advanced

Estimated Time:
25–35 Minutes

Objective:
Practice analyzing student records using lambda functions together with
map(), filter(), sorted(), and reduce().

Instructions:
A school stores student records in the following format:

(Name, Subject, Marks)

Create the following list:

students = [
    ("Ali", "Mathematics", 82),
    ("Sara", "Physics", 95),
    ("Ahmed", "Chemistry", 68),
    ("Ayesha", "Biology", 91),
    ("Usman", "Mathematics", 74),
    ("Fatima", "Physics", 88)
]

Perform the following tasks:

1. Display the original student records.

2. Use map() with a lambda function to create a list containing only
   student names.

3. Use filter() with a lambda function to create a list of students
   who scored at least 80 marks.

4. Import reduce from functools and use reduce() with a lambda
   function to calculate the total marks of all students.

5. Use sorted() with the key parameter and a lambda function to sort
   the student records by marks in descending order.

6. Display all generated results with meaningful headings.

Expected Output Format:

Original Student Records:
...

Student Names:
...

Students Scoring 80 or Above:
...

Total Marks:
...

Students Sorted by Marks (Highest First):
...

Requirements:
- Use lambda functions.
- Use map().
- Use filter().
- Use reduce().
- Use sorted().
- Do not modify the original list.
- Follow PEP 8 style guidelines.

Challenge:
1. Calculate the average marks using the total obtained from reduce().
2. Create another sorted list ordered alphabetically by subject and
   then by student name using a lambda expression.
===============================================================================
"""