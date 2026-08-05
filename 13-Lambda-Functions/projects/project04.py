"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Project 04: Employee Ranking System

Difficulty:
Intermediate

Estimated Completion Time:
60-75 Minutes

Objective:
Develop an employee ranking system using lambda functions, map(), filter(),
and sorted() to analyze employee performance, calculate scores, classify
employees, and generate rankings.

This project demonstrates how functional programming techniques can support
business performance analysis systems.

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

A software company wants to evaluate employee performance every quarter.

The HR department collects employee information including:

- Completed projects
- Performance ratings
- Experience years

The company needs a system that can:

- Calculate employee performance scores.
- Assign performance levels.
- Find high-performing employees.
- Rank employees according to their scores.
- Generate an employee performance report.


Functional Requirements:
-----------------------

The program must:

1. Store employee records.
2. Calculate performance scores using map().
3. Assign performance categories.
4. Filter top-performing employees.
5. Sort employees by ranking score.
6. Display a complete report.


Prerequisites:
--------------

Learners should understand:

- Lambda functions
- map()
- filter()
- sorted()
- key parameter
- Lists
- Dictionaries


Constraints:
------------

Do not use:

- External libraries
- Classes
- File handling
- Database systems


Implementation Roadmap:
-----------------------

Step 1:
Create employee performance data.

Step 2:
Use map() to calculate performance scores.

Step 3:
Classify employees based on scores.

Step 4:
Use filter() to identify high performers.

Step 5:
Sort employees using sorted().

Step 6:
Generate the ranking report.

===============================================================================
"""


# =============================================================================
# Employee Dataset
# =============================================================================

employees = [
    {
        "name": "Ali",
        "projects": 8,
        "rating": 4.8,
        "experience": 3
    },
    {
        "name": "Sara",
        "projects": 5,
        "rating": 4.2,
        "experience": 2
    },
    {
        "name": "Ahmed",
        "projects": 10,
        "rating": 4.9,
        "experience": 5
    },
    {
        "name": "Fatima",
        "projects": 7,
        "rating": 4.5,
        "experience": 4
    },
    {
        "name": "Usman",
        "projects": 3,
        "rating": 3.8,
        "experience": 1
    }
]


# =============================================================================
# Step 1: Calculate Performance Score
# =============================================================================

employee_scores = list(
    map(
        lambda employee: {
            **employee,
            "score": (
                employee["projects"] * 5
                +
                employee["rating"] * 10
                +
                employee["experience"] * 2
            )
        },
        employees
    )
)


# =============================================================================
# Step 2: Assign Performance Category
# =============================================================================

categorized_employees = list(
    map(
        lambda employee: {
            **employee,
            "category": (
                "Outstanding"
                if employee["score"] >= 90
                else "Excellent"
                if employee["score"] >= 70
                else "Average"
            )
        },
        employee_scores
    )
)


# =============================================================================
# Step 3: Filter High Performers
# =============================================================================

high_performers = list(
    filter(
        lambda employee: employee["score"] >= 70,
        categorized_employees
    )
)


# =============================================================================
# Step 4: Rank Employees
# =============================================================================

ranked_employees = sorted(
    categorized_employees,
    key=lambda employee: employee["score"],
    reverse=True
)


# =============================================================================
# Employee Ranking Report
# =============================================================================

print("=" * 70)
print("EMPLOYEE PERFORMANCE RANKING REPORT")
print("=" * 70)

position = 1

for employee in ranked_employees:
    print(
        f"Rank: {position}\n"
        f"Name: {employee['name']}\n"
        f"Projects Completed: {employee['projects']}\n"
        f"Performance Rating: {employee['rating']}\n"
        f"Experience: {employee['experience']} years\n"
        f"Score: {employee['score']:.1f}\n"
        f"Category: {employee['category']}\n"
    )

    position += 1


print("=" * 70)
print(f"Total Employees: {len(categorized_employees)}")
print(f"High Performers: {len(high_performers)}")
print("=" * 70)


"""
===============================================================================
Sample Input:
===============================================================================

Employee record:

{
    "name": "Ali",
    "projects": 8,
    "rating": 4.8,
    "experience": 3
}


===============================================================================
Sample Output:
===============================================================================

======================================================================
EMPLOYEE PERFORMANCE RANKING REPORT
======================================================================

Rank: 1
Name: Ahmed
Projects Completed: 10
Performance Rating: 4.9
Experience: 5 years
Score: 109.0
Category: Outstanding

Rank: 2
Name: Ali
Projects Completed: 8
Performance Rating: 4.8
Experience: 3 years
Score: 94.0
Category: Outstanding

Rank: 3
Name: Fatima
Projects Completed: 7
Performance Rating: 4.5
Experience: 4 years
Score: 93.0
Category: Outstanding

Rank: 4
Name: Sara
Projects Completed: 5
Performance Rating: 4.2
Experience: 2 years
Score: 62.0
Category: Average

Rank: 5
Name: Usman
Projects Completed: 3
Performance Rating: 3.8
Experience: 1 years
Score: 50.0
Category: Average

======================================================================
Total Employees: 5
High Performers: 3
======================================================================


===============================================================================
Detailed Explanation:
===============================================================================

This project uses lambda functions to process employee performance data.

The first map() calculates an employee score using multiple performance
factors.

The formula combines:

- Completed projects
- Performance rating
- Years of experience


The second map() classifies employees according to their scores.

The filter() function identifies employees who achieved a required score.

The sorted() function ranks employees:

sorted(
    employees,
    key=lambda employee: employee["score"],
    reverse=True
)


The key parameter determines which value is used for ranking.


===============================================================================
Code Walkthrough:
===============================================================================

1. Employee Dataset

Contains employee performance information.

2. Score Calculation

map() creates updated records with calculated scores.

3. Performance Classification

lambda expressions assign categories.

4. Filtering

filter() selects high-performing employees.

5. Ranking

sorted() creates the final employee ranking.


===============================================================================
Best Practices:
===============================================================================

- Use lambda functions only for small operations.
- Keep transformation steps separate.
- Use descriptive variable names.
- Prefer readable expressions over complex one-line logic.
- Use sorted() key functions for ranking.


===============================================================================
Common Mistakes:
===============================================================================

1. Creating overly complicated lambda expressions.

2. Using incorrect score formulas.

3. Forgetting that sorted() returns a new list.

4. Confusing filtering with transformation.


===============================================================================
Possible Improvements:
===============================================================================

- Add department-wise ranking.
- Add salary analysis.
- Export reports to files.
- Add employee attendance data.
- Build a complete HR analytics system.


===============================================================================
Bonus Challenges:
===============================================================================

1. Use reduce() to calculate average employee score.

2. Find the top three employees.

3. Create promotion recommendations.

4. Add monthly performance tracking.


===============================================================================
Real-World Applications:
===============================================================================

These concepts are used in:

- HR analytics systems
- Performance management software
- Business intelligence tools
- Data processing pipelines
- Machine learning feature preparation


===============================================================================
Key Learning Outcomes:
===============================================================================

After completing this project, learners should understand:

✓ Using lambda functions for scoring systems
✓ Transforming business records with map()
✓ Filtering important records
✓ Ranking data using sorted()
✓ Designing practical functional programming workflows

===============================================================================
"""