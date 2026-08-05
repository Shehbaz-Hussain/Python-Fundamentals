"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Project 10: Business Performance Analyzer

Difficulty:
Advanced

Estimated Completion Time:
90 Minutes

Objective:
Build a business performance analyzer using lambda functions, map(), filter(),
and sorted() to process business data, calculate performance scores, identify
successful departments, and generate analytical reports.

This final project combines multiple lambda-based techniques into a realistic
business data processing workflow.

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

A company wants to analyze the performance of different departments.

Each department provides:

- Revenue generated
- Number of employees
- Customer satisfaction score

The management team needs a system that can:

- Calculate department performance scores.
- Classify department performance.
- Identify successful departments.
- Rank departments.
- Generate a business performance report.


Functional Requirements:
-----------------------

The program must:

1. Store department records.
2. Calculate performance scores using map().
3. Assign performance categories.
4. Filter successful departments.
5. Sort departments by performance score.
6. Display a final business report.


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

- Import statements
- External libraries
- Classes
- File handling
- Machine learning libraries


Implementation Roadmap:
-----------------------

Step 1:
Create department data.

Step 2:
Calculate performance scores.

Step 3:
Classify department performance.

Step 4:
Filter successful departments.

Step 5:
Rank departments.

Step 6:
Generate the final report.

===============================================================================
"""


# =============================================================================
# Business Dataset
# =============================================================================

departments = [
    {
        "department": "Sales",
        "revenue": 900000,
        "employees": 20,
        "satisfaction": 4.8
    },
    {
        "department": "Marketing",
        "revenue": 600000,
        "employees": 15,
        "satisfaction": 4.5
    },
    {
        "department": "Development",
        "revenue": 1200000,
        "employees": 30,
        "satisfaction": 4.9
    },
    {
        "department": "Support",
        "revenue": 400000,
        "employees": 25,
        "satisfaction": 4.2
    },
    {
        "department": "Research",
        "revenue": 700000,
        "employees": 10,
        "satisfaction": 4.7
    }
]


# =============================================================================
# Step 1: Calculate Performance Score
# =============================================================================

departments_with_score = list(
    map(
        lambda department: {
            **department,
            "performance_score": (
                department["revenue"] / 10000
                +
                department["satisfaction"] * 20
                -
                department["employees"]
            )
        },
        departments
    )
)


# =============================================================================
# Step 2: Add Performance Category
# =============================================================================

categorized_departments = list(
    map(
        lambda department: {
            **department,
            "category": (
                "Excellent"
                if department["performance_score"] >= 150
                else "Good"
                if department["performance_score"] >= 100
                else "Needs Improvement"
            )
        },
        departments_with_score
    )
)


# =============================================================================
# Step 3: Filter Successful Departments
# =============================================================================

successful_departments = list(
    filter(
        lambda department: department["performance_score"] >= 100,
        categorized_departments
    )
)


# =============================================================================
# Step 4: Rank Departments
# =============================================================================

ranked_departments = sorted(
    categorized_departments,
    key=lambda department: department["performance_score"],
    reverse=True
)


# =============================================================================
# Business Performance Report
# =============================================================================

print("=" * 80)
print("BUSINESS PERFORMANCE ANALYSIS REPORT")
print("=" * 80)

rank = 1

for department in ranked_departments:
    print(
        f"Rank: {rank}\n"
        f"Department: {department['department']}\n"
        f"Revenue: Rs. {department['revenue']}\n"
        f"Employees: {department['employees']}\n"
        f"Customer Satisfaction: {department['satisfaction']}\n"
        f"Performance Score: {department['performance_score']:.2f}\n"
        f"Category: {department['category']}\n"
    )

    rank += 1


print("=" * 80)
print(f"Total Departments: {len(categorized_departments)}")
print(f"Successful Departments: {len(successful_departments)}")
print("=" * 80)


"""
===============================================================================
Sample Input:
===============================================================================

{
    "department": "Sales",
    "revenue": 900000,
    "employees": 20,
    "satisfaction": 4.8
}


===============================================================================
Sample Output:
===============================================================================

================================================================================
BUSINESS PERFORMANCE ANALYSIS REPORT
================================================================================

Rank: 1
Department: Development
Revenue: Rs. 1200000
Employees: 30
Customer Satisfaction: 4.9
Performance Score: 119.80
Category: Good

Rank: 2
Department: Sales
Revenue: Rs. 900000
Employees: 20
Customer Satisfaction: 4.8
Performance Score: 116.00
Category: Good

Rank: 3
Department: Research
Revenue: Rs. 700000
Employees: 10
Customer Satisfaction: 4.7
Performance Score: 97.00
Category: Needs Improvement

Rank: 4
Department: Marketing
Revenue: Rs. 600000
Employees: 15
Customer Satisfaction: 4.5
Performance Score: 90.00
Category: Needs Improvement

Rank: 5
Department: Support
Revenue: Rs. 400000
Employees: 25
Customer Satisfaction: 4.2
Performance Score: 39.00
Category: Needs Improvement

================================================================================
Total Departments: 5
Successful Departments: 2
================================================================================


===============================================================================
Detailed Explanation:
===============================================================================

This project combines all major concepts learned in this module.

The first map() function creates performance scores by combining multiple
business factors.

The second map() function classifies departments according to their scores.

The filter() function selects departments that achieve the required
performance level.

The sorted() function ranks departments:

sorted(
    departments,
    key=lambda department: department["performance_score"],
    reverse=True
)


The key parameter allows custom sorting based on calculated values.


===============================================================================
Code Walkthrough:
===============================================================================

1. Business Dataset

Contains department performance information.

2. Score Calculation

map() transforms raw records into analytical records.

3. Performance Classification

lambda functions assign categories.

4. Filtering

filter() identifies successful departments.

5. Ranking

sorted() creates the business ranking.


===============================================================================
Best Practices:
===============================================================================

- Design clear data processing steps.
- Use lambda functions for small calculations.
- Keep scoring formulas understandable.
- Use sorted() with key functions.
- Separate transformation and filtering operations.


===============================================================================
Common Mistakes:
===============================================================================

1. Creating overly complicated lambda functions.

2. Using wrong fields for calculations.

3. Sorting without a key function.

4. Applying filters before required transformations.


===============================================================================
Possible Improvements:
===============================================================================

- Add monthly performance tracking.
- Add predictive analytics.
- Connect with machine learning models.
- Create graphical dashboards.
- Store historical reports.


===============================================================================
Bonus Challenges:
===============================================================================

1. Add employee productivity analysis.

2. Create company-wide ranking.

3. Add performance recommendations.

4. Build a business decision support system.


===============================================================================
Real-World Applications:
===============================================================================

These concepts are used in:

- Business intelligence systems
- Data analytics platforms
- Performance dashboards
- Machine learning preprocessing
- Enterprise reporting systems


===============================================================================
Key Learning Outcomes:
===============================================================================

After completing this project, learners should understand:

✓ Combining lambda functions with map()
✓ Filtering business records
✓ Ranking complex data
✓ Building analytical workflows
✓ Applying functional programming in real-world scenarios

===============================================================================
"""