"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Exercise 16: Employee Salary Transformation Using Lambda

Difficulty:
Intermediate–Advanced

Estimated Time:
25–30 Minutes

Objective:
Practice applying lambda functions to realistic employee data using
map(), filter(), and sorted().

Instructions:
A company stores employee records as tuples in the following format:

(Name, Department, Monthly Salary)

Create the following list:

employees = [
    ("Ali", "IT", 65000),
    ("Sara", "HR", 52000),
    ("Ahmed", "Finance", 71000),
    ("Ayesha", "IT", 85000),
    ("Usman", "Sales", 47000),
    ("Fatima", "Finance", 93000)
]

Perform the following tasks:

1. Display the original employee records.

2. Use map() with a lambda function to create a new list containing
   each employee's annual salary.

3. Use filter() with a lambda function to create a list containing
   employees whose monthly salary is greater than 60,000.

4. Use sorted() with the key parameter and a lambda function to sort
   employees by monthly salary in ascending order.

5. Display all generated results clearly.

Expected Output Format:

Original Employees:
...

Annual Salaries:
...

Employees Earning Above 60,000:
...

Employees Sorted by Salary:
...

Requirements:
- Use lambda functions.
- Use map().
- Use filter().
- Use sorted().
- Keep the original employee list unchanged.
- Follow PEP 8 style guidelines.

Challenge:
Create another sorted list ordered by employee name instead of salary.
===============================================================================
"""