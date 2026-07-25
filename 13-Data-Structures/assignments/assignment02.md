# Module 13 - Data Structures

# Assignment 02 — Library Inventory Management System

## Difficulty

Intermediate

---

# Objective

Develop a Python program that manages a small library inventory using multiple Python data structures. The assignment focuses on applying lists, tuples, sets, dictionaries, indexing, slicing, membership operators, unpacking, nested data structures, iteration, and built-in functions in a practical scenario.

---

# Learning Outcomes

After completing this assignment, you should be able to:

- Select appropriate data structures for different types of data.
- Store related information using nested data structures.
- Access and modify data using indexing and slicing.
- Use membership operators to search for data.
- Iterate through lists, tuples, sets, and dictionaries.
- Apply common built-in functions such as `len()`, `sorted()`, `min()`, and `max()`.
- Write clean, readable, and well-organized Python code.

---

# Requirements

Create a Python program that performs the following tasks:

1. Create a list containing at least six book titles.
2. Create a tuple representing book categories.
3. Create a set containing unique author names.
4. Create a dictionary where:
   - The key is a book title.
   - The value is another dictionary containing:
     - Author
     - Category
     - Number of available copies
5. Display all book information in a readable format.
6. Print:
   - The first book.
   - The last book.
   - A slice containing three consecutive books.
7. Check whether a specific book exists using the `in` operator.
8. Iterate through:
   - The list of books.
   - The tuple of categories.
   - The set of authors.
   - The inventory dictionary.
9. Display:
   - Total number of books using `len()`.
   - Categories in sorted order using `sorted()`.
10. Use tuple unpacking to store any two category names into separate variables and display them.

---

# Constraints

- Use only concepts covered in Module 13.
- Do not use functions or classes.
- Do not use file handling or external libraries.
- Follow PEP 8 guidelines.
- Use descriptive variable names.
- Add comments explaining each major section.

---

# Sample Output

```text
Library Inventory

Book: Python Basics
Author: Eric
Category: Programming
Available Copies: 5

Book: Data Science Essentials
Author: Sara
Category: Data Science
Available Copies: 3

...

First Book:
Python Basics

Last Book:
Artificial Intelligence

Selected Books:
['Python Basics', 'Data Science Essentials', 'Machine Learning']

Book Found: True

Categories:
Programming
Data Science
Artificial Intelligence

Authors:
Eric
Sara
Ali

Total Books: 6

Sorted Categories:
['Artificial Intelligence', 'Data Science', 'Programming']

Unpacked Categories:
Programming
Data Science
```

> **Note:** The order of elements in a set is not guaranteed.

---

# Submission Guidelines

- Save the program as `assignment02.py`.
- Ensure it executes successfully using Python 3.13 or later.
- Include meaningful comments throughout the code.
- Test the program before submission.
- Submit only your own original work.

---

# Evaluation Criteria

| Criterion | Marks |
|-----------|------:|
| Correct use of lists | 15 |
| Correct use of tuples and unpacking | 15 |
| Correct use of sets | 10 |
| Correct use of dictionaries and nested structures | 20 |
| Correct use of indexing, slicing, and membership operators | 15 |
| Proper iteration and use of built-in functions | 15 |
| Code quality, comments, and PEP 8 compliance | 10 |
| **Total** | **100** |