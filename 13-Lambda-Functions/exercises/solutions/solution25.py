"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 25
Exercise Title: AI Dataset Preparation and Report Generation
Difficulty: Advanced

Objective:
    Apply lambda functions to perform realistic data preprocessing,
    transformation, filtering, sorting, and report generation tasks commonly
    used in Artificial Intelligence and Machine Learning workflows.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

from functools import reduce


# -----------------------------------------------------------------------------
# Dataset Creation
# -----------------------------------------------------------------------------

employees = [
    ("Ali", 24, "AI", 2, 81),
    ("Sara", 28, "Data Science", 5, 94),
    ("Ahmed", 26, "Cybersecurity", 3, 76),
    ("Ayesha", 31, "AI", 7, 98),
    ("Usman", 23, "Backend", 1, 69),
    ("Fatima", 29, "Data Science", 6, 91),
    ("Bilal", 27, "AI", 4, 87),
    ("Hina", 25, "Backend", 2, 74),
]


# -----------------------------------------------------------------------------
# Performance Level Assignment
# -----------------------------------------------------------------------------

performance_level = lambda score: (
    "Excellent"
    if score >= 90
    else "Very Good"
    if score >= 80
    else "Good"
    if score >= 70
    else "Average"
)


# -----------------------------------------------------------------------------
# Main Tasks
# -----------------------------------------------------------------------------

# Add performance level information.
processed_employees = list(
    map(
        lambda employee: (
            employee[0],
            employee[2],
            employee[3],
            employee[4],
            performance_level(employee[4]),
        ),
        employees,
    )
)


# Filter employees with performance score >= 85.
high_performing_employees = list(
    filter(
        lambda employee: employee[4] >= 85,
        employees,
    )
)


# Calculate total performance score.
total_performance_score = reduce(
    lambda total, employee: total + employee[4],
    employees,
    0,
)


# Calculate average performance score.
average_performance_score = total_performance_score / len(employees)


# Sort employees by performance score descending.
employees_sorted_by_score = sorted(
    processed_employees,
    key=lambda employee: employee[3],
    reverse=True,
)


# Sort employees by department and experience descending.
employees_sorted_by_department = sorted(
    processed_employees,
    key=lambda employee: (employee[1], -employee[2]),
)


# -----------------------------------------------------------------------------
# Challenge Tasks
# -----------------------------------------------------------------------------

# Increase performance score by 5%, maximum value 100.
improved_performance_dataset = list(
    map(
        lambda employee: (
            employee[0],
            employee[1],
            employee[2],
            employee[3],
            min(employee[4] * 1.05, 100),
        ),
        employees,
    )
)


# Create uppercase employee names.
uppercase_names = list(
    map(
        lambda employee: employee[0].upper(),
        employees,
    )
)


# Count employees by department.
departments = list(
    map(
        lambda employee: employee[2],
        employees,
    )
)

department_count = {
    "AI": departments.count("AI"),
    "Data Science": departments.count("Data Science"),
    "Cybersecurity": departments.count("Cybersecurity"),
    "Backend": departments.count("Backend"),
}


# Generate report values.
highest_score = max(
    map(
        lambda employee: employee[4],
        employees,
    )
)

lowest_score = min(
    map(
        lambda employee: employee[4],
        employees,
    )
)


# Prepare AI/ML feature dataset.
ml_training_dataset = list(
    map(
        lambda employee: (
            employee[1],
            employee[3],
            employee[4],
        ),
        employees,
    )
)


# -----------------------------------------------------------------------------
# Display Results
# -----------------------------------------------------------------------------

print("Original Employee Dataset:")
print(employees)

print("\nEmployees With Performance Level:")
print(processed_employees)

print("\nEmployees With Performance Score >= 85:")
print(high_performing_employees)

print("\nTotal Performance Score:")
print(total_performance_score)

print("\nAverage Performance Score:")
print(average_performance_score)

print("\nEmployees Sorted By Performance Score:")
print(employees_sorted_by_score)

print("\nEmployees Sorted By Department And Experience:")
print(employees_sorted_by_department)

print("\nPerformance Score Increased By 5%:")
print(improved_performance_dataset)

print("\nEmployee Names In Uppercase:")
print(uppercase_names)

print("\nDepartment Count:")
print(department_count)

print("\nAI Dataset Report:")
print("-" * 30)
print(f"Total Employees: {len(employees)}")
print(
    f"Employees With Performance >= 85: "
    f"{len(high_performing_employees)}"
)
print(f"Highest Performance Score: {highest_score}")
print(f"Lowest Performance Score: {lowest_score}")
print(f"Average Performance Score: {average_performance_score}")

print("\nMachine Learning Feature Dataset:")
print(ml_training_dataset)


"""
===============================================================================
Expected Output
===============================================================================

Original Employee Dataset:
[('Ali', 24, 'AI', 2, 81), ('Sara', 28, 'Data Science', 5, 94),
 ('Ahmed', 26, 'Cybersecurity', 3, 76), ('Ayesha', 31, 'AI', 7, 98),
 ('Usman', 23, 'Backend', 1, 69), ('Fatima', 29, 'Data Science', 6, 91),
 ('Bilal', 27, 'AI', 4, 87), ('Hina', 25, 'Backend', 2, 74)]

Employees With Performance Level:
[
('Ali', 'AI', 2, 81, 'Very Good'),
('Sara', 'Data Science', 5, 94, 'Excellent'),
('Ahmed', 'Cybersecurity', 3, 76, 'Good'),
('Ayesha', 'AI', 7, 98, 'Excellent'),
('Usman', 'Backend', 1, 69, 'Average'),
('Fatima', 'Data Science', 6, 91, 'Excellent'),
('Bilal', 'AI', 4, 87, 'Very Good'),
('Hina', 'Backend', 2, 74, 'Good')
]

Employees With Performance Score >= 85:
[
('Sara', 28, 'Data Science', 5, 94),
('Ayesha', 31, 'AI', 7, 98),
('Fatima', 29, 'Data Science', 6, 91),
('Bilal', 27, 'AI', 4, 87)
]

Total Performance Score:
670

Average Performance Score:
83.75

Highest Performance Score:
98

Lowest Performance Score:
69

Machine Learning Feature Dataset:
[
(24, 2, 81),
(28, 5, 94),
(26, 3, 76),
(31, 7, 98),
(23, 1, 69),
(29, 6, 91),
(27, 4, 87),
(25, 2, 74)
]

===============================================================================
Step-by-Step Explanation
===============================================================================

1. The employee dataset stores raw information that can be used for analysis.

2. map() transforms every employee record by adding a calculated performance
   level.

3. filter() selects employees who satisfy the performance requirement.

4. reduce() combines all performance scores into one total value.

5. The average performance score is calculated from the total score.

6. sorted() creates customized rankings:
   - By performance score.
   - By department and experience.

7. Challenge tasks simulate common data preprocessing operations:
   - Score adjustment.
   - Text transformation.
   - Category counting.
   - Report generation.
   - Machine learning feature preparation.


===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- map()
- filter()
- reduce()
- sorted()
- key parameter
- Conditional expressions
- Lists
- Tuples
- Dictionary counting
- Arithmetic operations


===============================================================================
Time Complexity
===============================================================================

Overall Complexity: O(n log n)

Explanation:

- map(): O(n)
- filter(): O(n)
- reduce(): O(n)
- sorted(): O(n log n)

Sorting operations determine the overall complexity.


===============================================================================
Space Complexity
===============================================================================

Overall Complexity: O(n)

Explanation:

Additional lists are created for transformed datasets, filtered records,
and sorted results while preserving the original dataset.


===============================================================================
Best Practices
===============================================================================

- Keep raw datasets unchanged during preprocessing.
- Use lambda functions for short transformation logic.
- Use meaningful variable names for processed data.
- Separate each preprocessing step for readability.
- Prepare clean feature datasets before machine learning workflows.


===============================================================================
Common Mistakes
===============================================================================

- Using incorrect tuple indexes.
- Applying performance rules incorrectly.
- Forgetting reverse=True during descending sorting.
- Modifying the original employee dataset.
- Using loops instead of the required functional tools.
- Forgetting to import reduce from functools.


===============================================================================
Alternative Approach
===============================================================================

A class-based data processing pipeline could be used for larger enterprise
applications where preprocessing logic needs to be reused and extended.


===============================================================================
Real-World Relevance
===============================================================================

This workflow is commonly used in:

- Machine learning dataset preprocessing
- Feature engineering
- Employee analytics systems
- Business intelligence dashboards
- AI model preparation pipelines


===============================================================================
Key Takeaways
===============================================================================

- Lambda functions simplify small data transformation operations.
- map(), filter(), reduce(), and sorted() are useful for data processing.
- Dataset preprocessing is a critical step before AI model training.
- Clean feature extraction improves machine learning workflow quality.
- Functional programming techniques can make data pipelines concise and
  readable.

===============================================================================
"""