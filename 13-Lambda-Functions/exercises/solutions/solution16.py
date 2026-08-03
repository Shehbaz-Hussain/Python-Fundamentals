"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 16
Exercise Title: Employee Salary Transformation Using Lambda
Difficulty: Intermediate–Advanced

Objective:
    Practice applying lambda functions with map(), filter(), and sorted()
    to process employee records. Generate annual salaries, filter employees
    by salary, and sort employee records while keeping the original data
    unchanged.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a list of employee records.
employees = [
    ("Ali", "IT", 65000),
    ("Sara", "HR", 52000),
    ("Ahmed", "Finance", 71000),
    ("Ayesha", "IT", 85000),
    ("Usman", "Sales", 47000),
    ("Fatima", "Finance", 93000),
]

# Create a list containing each employee's annual salary.
annual_salaries = list(
    map(
        lambda employee: (
            employee[0],
            employee[1],
            employee[2] * 12,
        ),
        employees,
    )
)

# Filter employees earning more than 60,000 per month.
employees_above_60000 = list(
    filter(
        lambda employee: employee[2] > 60000,
        employees,
    )
)

# Sort employees by monthly salary in ascending order.
employees_sorted_by_salary = sorted(
    employees,
    key=lambda employee: employee[2],
)

# Challenge: Sort employees alphabetically by name.
employees_sorted_by_name = sorted(
    employees,
    key=lambda employee: employee[0],
)

# Display the results.
print("Original Employees:")
print(employees)

print("\nAnnual Salaries:")
print(annual_salaries)

print("\nEmployees Earning Above 60,000:")
print(employees_above_60000)

print("\nEmployees Sorted by Salary:")
print(employees_sorted_by_salary)

print("\nEmployees Sorted by Name:")
print(employees_sorted_by_name)


"""
===============================================================================
Expected Output
===============================================================================

Original Employees:
[('Ali', 'IT', 65000), ('Sara', 'HR', 52000), ('Ahmed', 'Finance', 71000),
 ('Ayesha', 'IT', 85000), ('Usman', 'Sales', 47000),
 ('Fatima', 'Finance', 93000)]

Annual Salaries:
[('Ali', 'IT', 780000), ('Sara', 'HR', 624000),
 ('Ahmed', 'Finance', 852000), ('Ayesha', 'IT', 1020000),
 ('Usman', 'Sales', 564000), ('Fatima', 'Finance', 1116000)]

Employees Earning Above 60,000:
[('Ali', 'IT', 65000), ('Ahmed', 'Finance', 71000),
 ('Ayesha', 'IT', 85000), ('Fatima', 'Finance', 93000)]

Employees Sorted by Salary:
[('Usman', 'Sales', 47000), ('Sara', 'HR', 52000),
 ('Ali', 'IT', 65000), ('Ahmed', 'Finance', 71000),
 ('Ayesha', 'IT', 85000), ('Fatima', 'Finance', 93000)]

Employees Sorted by Name:
[('Ahmed', 'Finance', 71000), ('Ali', 'IT', 65000),
 ('Ayesha', 'IT', 85000), ('Fatima', 'Finance', 93000),
 ('Sara', 'HR', 52000), ('Usman', 'Sales', 47000)]

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A list of employee records is created. Each tuple contains:
       - Employee name
       - Department
       - Monthly salary

2. The map() function applies a lambda expression to every employee record.
   The lambda creates a new tuple containing the employee's annual salary by
   multiplying the monthly salary by 12.

3. The filter() function applies a lambda expression that returns True only
   for employees whose monthly salary exceeds 60,000.

4. The sorted() function uses the key parameter with a lambda expression to
   sort employees by monthly salary in ascending order.

5. As a challenge, another call to sorted() orders employees
   alphabetically by name.

6. The original employee list remains unchanged because map(), filter(), and
   sorted() each produce new objects instead of modifying the original list.

How the Lambda Expressions Work
-------------------------------

First lambda expression:

    lambda employee: (
        employee[0],
        employee[1],
        employee[2] * 12,
    )

- Accepts one employee record.
- Calculates the annual salary.
- Returns a new tuple.

Second lambda expression:

    lambda employee: employee[2] > 60000

- Checks whether the monthly salary exceeds 60,000.
- Returns True for matching employees.

Third lambda expression:

    lambda employee: employee[2]

- Returns the monthly salary.
- sorted() uses this value to order the records.

Fourth lambda expression:

    lambda employee: employee[0]

- Returns the employee's name.
- sorted() uses the name for alphabetical ordering.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- map()
- filter()
- sorted()
- key parameter
- Lists
- Tuples
- Arithmetic operations
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(n log n)

Explanation:
- map() processes every employee once: O(n)
- filter() processes every employee once: O(n)
- sorted() performs sorting in O(n log n)

The sorting operation dominates the overall time complexity.

===============================================================================
Space Complexity
===============================================================================

O(n)

Explanation:
New lists are created for the mapped, filtered, and sorted results while the
original employee list remains unchanged.

===============================================================================
Best Practices
===============================================================================

- Preserve the original data by using map(), filter(), and sorted().
- Use descriptive variable names for transformed data.
- Keep each lambda expression focused on a single responsibility.
- Use the key parameter to customize sorting without modifying records.

===============================================================================
Common Mistakes
===============================================================================

- Forgetting to convert map() or filter() objects into lists.
- Using the wrong tuple index when accessing the salary or name.
- Sorting the original list with sort() instead of using sorted().
- Multiplying by an incorrect number when calculating annual salary.
- Returning the wrong value from a lambda expression.

===============================================================================
Alternative Approach
===============================================================================

Another valid implementation is to create the annual salary list using:

    lambda employee: employee + (employee[2] * 12,)

This appends the annual salary to each existing employee tuple instead of
replacing the monthly salary.

===============================================================================
Real-World Relevance
===============================================================================

These techniques are commonly used in:

- Human resource management systems
- Payroll processing
- Employee reporting dashboards
- Business analytics
- Data transformation pipelines

===============================================================================
Key Takeaways
===============================================================================

- map() transforms every element in an iterable.
- filter() selects elements that satisfy a condition.
- sorted() with the key parameter customizes sorting behavior.
- Lambda functions provide concise logic for data transformation, filtering,
  and sorting.
===============================================================================
"""