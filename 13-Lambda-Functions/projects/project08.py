"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Project 08: Data Cleaning Pipeline

Difficulty:
Intermediate

Estimated Completion Time:
60-75 Minutes

Objective:
Build a simple data cleaning pipeline using lambda functions, map(), filter(),
and sorted() to clean, transform, validate, and organize raw dataset records.

This project demonstrates how functional programming techniques are used in
data preparation workflows commonly found in data science and machine learning.

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

A company collects customer data from different sources. The collected data
contains incomplete records and inconsistent values.

The data team needs a simple cleaning pipeline that can:

- Remove invalid records.
- Standardize customer information.
- Add data quality labels.
- Sort cleaned records.
- Generate a cleaned dataset report.


Functional Requirements:
-----------------------

The program must:

1. Store raw customer records.
2. Remove incomplete records using filter().
3. Transform data using map().
4. Add quality labels.
5. Sort records using sorted().
6. Display the cleaned dataset.


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
- Advanced data processing tools


Implementation Roadmap:
-----------------------

Step 1:
Create raw customer data.

Step 2:
Filter invalid records.

Step 3:
Clean and transform records.

Step 4:
Add quality information.

Step 5:
Sort cleaned data.

Step 6:
Display final results.

===============================================================================
"""


# =============================================================================
# Raw Customer Dataset
# =============================================================================

raw_data = [
    {
        "name": " ali ",
        "age": 25,
        "score": 85
    },
    {
        "name": "",
        "age": 30,
        "score": 90
    },
    {
        "name": "sara",
        "age": 22,
        "score": 75
    },
    {
        "name": "AHMED",
        "age": 28,
        "score": 95
    },
    {
        "name": "",
        "age": 20,
        "score": 60
    }
]


# =============================================================================
# Step 1: Remove Invalid Records Using filter()
# =============================================================================

clean_records = list(
    filter(
        lambda customer: customer["name"] != "",
        raw_data
    )
)


# =============================================================================
# Step 2: Transform Data Using map()
# =============================================================================

processed_records = list(
    map(
        lambda customer: {
            **customer,
            "name": customer["name"].strip().title()
        },
        clean_records
    )
)


# =============================================================================
# Step 3: Add Quality Label
# =============================================================================

quality_records = list(
    map(
        lambda customer: {
            **customer,
            "quality": (
                "High Quality"
                if customer["score"] >= 80
                else "Low Quality"
            )
        },
        processed_records
    )
)


# =============================================================================
# Step 4: Sort Records By Score
# =============================================================================

sorted_records = sorted(
    quality_records,
    key=lambda customer: customer["score"],
    reverse=True
)


# =============================================================================
# Clean Dataset Report
# =============================================================================

print("=" * 70)
print("DATA CLEANING PIPELINE REPORT")
print("=" * 70)

for customer in sorted_records:
    print(
        f"Name: {customer['name']}\n"
        f"Age: {customer['age']}\n"
        f"Score: {customer['score']}\n"
        f"Quality: {customer['quality']}\n"
    )


print("=" * 70)
print(f"Original Records: {len(raw_data)}")
print(f"Clean Records: {len(sorted_records)}")
print("=" * 70)


"""
===============================================================================
Sample Input:
===============================================================================

{
    "name": " ali ",
    "age": 25,
    "score": 85
}


===============================================================================
Sample Output:
===============================================================================

======================================================================
DATA CLEANING PIPELINE REPORT
======================================================================

Name: Ahmed
Age: 28
Score: 95
Quality: High Quality

Name: Ali
Age: 25
Score: 85
Quality: High Quality

Name: Sara
Age: 22
Score: 75
Quality: Low Quality

======================================================================
Original Records: 5
Clean Records: 3
======================================================================


===============================================================================
Detailed Explanation:
===============================================================================

This project represents a basic data preprocessing pipeline.

The filter() function removes invalid records.

Example:

filter(
    lambda customer: customer["name"] != "",
    data
)


The map() function transforms raw data into a cleaner format.

Example:

lambda customer:
    customer["name"].strip().title()


Another map() operation adds data quality information.

The sorted() function organizes records by score.


===============================================================================
Code Walkthrough:
===============================================================================

1. Raw Data Collection

The dataset contains unclean customer information.

2. Data Filtering

filter() removes records without names.

3. Data Transformation

map() cleans text values.

4. Quality Classification

lambda expressions assign quality labels.

5. Sorting

sorted() ranks records by score.


===============================================================================
Best Practices:
===============================================================================

- Clean data before analysis.
- Separate filtering and transformation steps.
- Use lambda functions for simple operations.
- Keep data pipelines readable.
- Validate data before processing.


===============================================================================
Common Mistakes:
===============================================================================

1. Forgetting to remove invalid records.

2. Changing data without checking values.

3. Using complex lambda expressions.

4. Sorting before cleaning data.


===============================================================================
Possible Improvements:
===============================================================================

- Add missing value handling.
- Add duplicate detection.
- Connect with machine learning preprocessing.
- Process larger datasets.


===============================================================================
Bonus Challenges:
===============================================================================

1. Add email validation rules.

2. Create data quality scores.

3. Filter customers by age.

4. Create a complete preprocessing workflow.


===============================================================================
Real-World Applications:
===============================================================================

Similar techniques are used in:

- Machine learning data preparation
- Data engineering pipelines
- Analytics systems
- Business intelligence tools
- ETL workflows


===============================================================================
Key Learning Outcomes:
===============================================================================

After completing this project, learners should understand:

✓ Cleaning data using filter()
✓ Transforming data using map()
✓ Sorting processed records
✓ Building simple data pipelines
✓ Applying lambda functions in data workflows

===============================================================================
"""