"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Exercise 25: AI Dataset Preparation and Report Generation

Difficulty:
Advanced

Estimated Time:
45–60 Minutes

Objective:
Apply lambda functions to perform realistic data preprocessing,
transformation, filtering, sorting, and report generation tasks commonly
used in Artificial Intelligence and Machine Learning workflows.

Instructions:
A data scientist is preparing a dataset before training a machine
learning model. Each record has the following format:

(Name, Age, Department, Experience (Years), Performance Score)

Create the following list:

employees = [
    ("Ali", 24, "AI", 2, 81),
    ("Sara", 28, "Data Science", 5, 94),
    ("Ahmed", 26, "Cybersecurity", 3, 76),
    ("Ayesha", 31, "AI", 7, 98),
    ("Usman", 23, "Backend", 1, 69),
    ("Fatima", 29, "Data Science", 6, 91),
    ("Bilal", 27, "AI", 4, 87),
    ("Hina", 25, "Backend", 2, 74)
]

Perform the following tasks:

1. Display the original dataset.

2. Use map() with a lambda function to create a new dataset in the
   following format:

   (
       Name,
       Department,
       Experience,
       Performance Score,
       Performance Level
   )

   Assign the Performance Level according to the rules below:

   - Excellent : Score >= 90
   - Very Good : Score >= 80
   - Good      : Score >= 70
   - Average   : Score < 70

3. Use filter() with a lambda function to create a list containing only
   employees whose performance score is 85 or higher.

4. Import reduce from functools and calculate the total performance
   score of all employees.

5. Calculate the average performance score.

6. Use sorted() with the key parameter and a lambda function to sort the
   employee records by performance score in descending order.

7. Create another sorted list ordered by:
   - Department
   - Experience (highest first within each department)

8. Display all generated results with clear and meaningful headings.

Requirements:
- Use lambda functions.
- Use map().
- Use filter().
- Use reduce().
- Use sorted().
- Keep the original dataset unchanged.
- Follow PEP 8 style guidelines.
- Produce clean and readable output.

Challenge:

1. Create a new dataset where each employee's performance score is
   increased by 5%, but the maximum score cannot exceed 100.

2. Create a list containing only employee names in uppercase.

3. Count the number of employees in each department.

4. Generate a simple textual report showing:
   - Total employees
   - Employees with performance >= 85
   - Highest performance score
   - Lowest performance score
   - Average performance score

5. Prepare a new dataset suitable for AI model training containing only:

   (
       Age,
       Experience,
       Performance Score
   )

   This represents a simplified feature set that could be used for
   machine learning experiments.

Learning Outcomes:

After completing this exercise, you should be able to:

- Apply lambda functions to realistic datasets.
- Combine map(), filter(), reduce(), and sorted() effectively.
- Implement business rules using lambda expressions.
- Perform basic dataset preprocessing.
- Prepare structured data for AI/ML workflows.
- Write clean, maintainable, and PEP 8-compliant Python code.

===============================================================================
"""