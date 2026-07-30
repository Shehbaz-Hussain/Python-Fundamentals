"""
File: example25.py
Topic: Combining Lambda Functions with Multiple Operations

Description:
This example demonstrates how lambda functions can be combined
with map(), filter(), and sorted() to process real-world data.

Concepts Covered:
- Lambda functions with filter()
- Lambda functions with map()
- Lambda functions with sorted()
- Multi-step data processing pipeline

Python Version:
Python 3.13+
"""


# Creating a list of employee salary records
employees = [
    ("Ali", 4500),
    ("Sara", 6200),
    ("Ahmed", 3500),
    ("Zain", 5400)
]


# Filtering employees with salaries above 4000
qualified_employees = filter(
    lambda employee: employee[1] > 4000,
    employees
)


# Increasing qualified employee salaries by 10%
updated_salaries = list(
    map(
        lambda employee: (
            employee[0],
            employee[1] * 1.10
        ),
        qualified_employees
    )
)


# Sorting employees by updated salary
sorted_employees = sorted(
    updated_salaries,
    key=lambda employee: employee[1],
    reverse=True
)


# Displaying the final processed data
print(sorted_employees)


"""
Expected Output:

[
    ('Sara', 6820.000000000001),
    ('Zain', 5940.000000000001),
    ('Ali', 4950.000000000001)
]


Explanation:

1. A list of employee records is created.
2. Each record contains:
   - Employee name
   - Employee salary

3. The filter() function selects employees whose salary is
   greater than 4000.

4. The map() function increases the selected employee salaries
   by 10%.

5. The sorted() function arranges employees from highest salary
   to lowest salary.

6. Lambda functions are used for:
   - Selecting employees
   - Transforming salary values
   - Sorting records

Best Practice:

Lambda functions are useful for short processing steps in a
data pipeline. However, if the logic becomes complex or requires
multiple conditions, use regular functions with meaningful names.

Real-World Relevance:

This type of data processing pattern is commonly used in:
- Employee management systems
- Financial applications
- Data analysis pipelines
- Machine learning data preparation
- Backend data processing workflows
"""