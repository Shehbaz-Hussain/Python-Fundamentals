"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 15
Exercise Title: Sorting Records Using the key Parameter and Lambda
Difficulty: Intermediate

Objective:
    Practice sorting a collection of student records using the key parameter
    together with lambda functions. Sort the records by exam score while
    keeping the original list unchanged, then complete the challenge by
    sorting in descending order of score and alphabetically by student name.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a list of student records.
students = [
    ("Ali", 82),
    ("Sara", 95),
    ("Ahmed", 76),
    ("Zain", 88),
    ("Ayesha", 91),
]

# Sort student records by exam score in ascending order.
students_sorted_by_score = sorted(
    students,
    key=lambda student: student[1],
)

# Challenge 1: Sort student records by exam score in descending order.
students_sorted_by_score_descending = sorted(
    students,
    key=lambda student: student[1],
    reverse=True,
)

# Challenge 2: Sort student records alphabetically by student name.
students_sorted_by_name = sorted(
    students,
    key=lambda student: student[0],
)

# Display the results.
print("Original Student Records:")
print(students)

print("\nSorted by Score:")
print(students_sorted_by_score)

print("\nSorted by Score (Descending):")
print(students_sorted_by_score_descending)

print("\nSorted by Name:")
print(students_sorted_by_name)


"""
===============================================================================
Expected Output
===============================================================================

Original Student Records:
[('Ali', 82), ('Sara', 95), ('Ahmed', 76), ('Zain', 88), ('Ayesha', 91)]

Sorted by Score:
[('Ahmed', 76), ('Ali', 82), ('Zain', 88), ('Ayesha', 91), ('Sara', 95)]

Sorted by Score (Descending):
[('Sara', 95), ('Ayesha', 91), ('Zain', 88), ('Ali', 82), ('Ahmed', 76)]

Sorted by Name:
[('Ahmed', 76), ('Ali', 82), ('Ayesha', 91), ('Sara', 95), ('Zain', 88)]

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A list of student records is created using tuples.
2. Each tuple contains:
       - Student name
       - Exam score
3. The sorted() function creates a new list sorted by exam score.
4. The key parameter uses a lambda function that returns the second element
   of each tuple (the score).
5. The original list remains unchanged because sorted() returns a new list.
6. For the first challenge, reverse=True sorts the records in descending
   order of score.
7. For the second challenge, another lambda function returns the student's
   name, allowing the records to be sorted alphabetically.
8. All lists are displayed using the print() function.

How the Lambda Expressions Work
-------------------------------

First lambda expression:

    lambda student: student[1]

- 'student' represents one tuple from the list.
- 'student[1]' accesses the exam score.
- sorted() uses the score as the sorting key.

Second lambda expression:

    lambda student: student[1]

- Returns the exam score again.
- Combined with reverse=True to sort scores in descending order.

Third lambda expression:

    lambda student: student[0]

- 'student[0]' accesses the student's name.
- sorted() uses the name as the sorting key for alphabetical ordering.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- sorted()
- key parameter
- Lists
- Tuples
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(n log n)

Explanation:
Each call to sorted() uses an efficient sorting algorithm with a time
complexity of O(n log n), where n is the number of student records.

===============================================================================
Space Complexity
===============================================================================

O(n)

Explanation:
Each call to sorted() creates and returns a new list while leaving the
original list unchanged.

===============================================================================
Best Practices
===============================================================================

- Keep the original data unchanged by using sorted() instead of sort().
- Use descriptive variable names for each sorted result.
- Use tuple indexing consistently when selecting sort keys.
- Keep lambda expressions focused on returning only the required key.

===============================================================================
Common Mistakes
===============================================================================

- Using the wrong tuple index for the sorting key.
- Using sort() instead of sorted(), which modifies the original list.
- Forgetting to use reverse=True for descending order.
- Returning the entire tuple instead of the required field.
- Assuming sorted() changes the original list.

===============================================================================
Alternative Approach
===============================================================================

Another valid implementation is to sort by score and then by name when scores
are equal:

    students_sorted = sorted(
        students,
        key=lambda student: (student[1], student[0]),
    )

This uses a tuple as the sorting key to apply multiple sorting criteria.

===============================================================================
Real-World Relevance
===============================================================================

Sorting records with custom keys is commonly used in:

- Student management systems
- Employee databases
- Business reporting
- Inventory management
- Data analysis and visualization

===============================================================================
Key Takeaways
===============================================================================

- Lambda functions can define custom sorting keys.
- The key parameter determines how elements are ordered.
- The sorted() function preserves the original list.
- Tuple indexing allows specific fields within records to be used for sorting.
===============================================================================
"""