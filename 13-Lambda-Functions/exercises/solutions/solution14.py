"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 14
Exercise Title: Sorting Data with sorted() and the key Parameter
Difficulty: Intermediate

Objective:
    Practice using the built-in sorted() function together with the key
    parameter and a lambda function to sort a list of names based on their
    length. Keep the original list unchanged and complete the challenge by
    sorting the names in descending order of length.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a list of names.
names = [
    "Ali",
    "Muhammad",
    "Sara",
    "Zain",
    "Ayesha",
    "Usman",
    "Hina",
]

# Sort the names by their length.
names_sorted_by_length = sorted(
    names,
    key=lambda name: len(name),
)

# Challenge: Sort the names by length in descending order.
names_sorted_by_length_descending = sorted(
    names,
    key=lambda name: len(name),
    reverse=True,
)

# Display the results.
print("Original Names:")
print(names)

print("\nNames Sorted by Length:")
print(names_sorted_by_length)

print("\nNames Sorted by Length (Descending):")
print(names_sorted_by_length_descending)


"""
===============================================================================
Expected Output
===============================================================================

Original Names:
['Ali', 'Muhammad', 'Sara', 'Zain', 'Ayesha', 'Usman', 'Hina']

Names Sorted by Length:
['Ali', 'Sara', 'Zain', 'Hina', 'Usman', 'Ayesha', 'Muhammad']

Names Sorted by Length (Descending):
['Muhammad', 'Ayesha', 'Usman', 'Sara', 'Zain', 'Hina', 'Ali']

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A list of names is created.
2. The sorted() function is used to create a new sorted list.
3. The key parameter receives a lambda function.
4. The lambda function returns the length of each name using len().
5. The names are sorted in ascending order based on their length.
6. The original list remains unchanged because sorted() returns a new list.
7. For the challenge, another call to sorted() uses reverse=True to sort the
   names in descending order of length.
8. The original list and both sorted lists are displayed.

How the Lambda Expression Works
-------------------------------

Lambda expression:

    lambda name: len(name)

- 'lambda' creates an anonymous function.
- 'name' represents each element in the list.
- The len() function returns the number of characters in each name.
- The returned length is used by sorted() as the sorting key.
- Elements are ordered according to the value returned by the lambda function.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- sorted()
- key parameter
- Lists
- String functions
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(n log n)

Explanation:
The sorted() function uses an efficient sorting algorithm with a time
complexity of O(n log n), where n is the number of elements in the list.

===============================================================================
Space Complexity
===============================================================================

O(n)

Explanation:
The sorted() function creates and returns a new list containing the sorted
elements.

===============================================================================
Best Practices
===============================================================================

- Use sorted() when you want to preserve the original list.
- Use descriptive variable names for sorted results.
- Keep lambda expressions simple and focused on a single key.
- Use the key parameter instead of modifying the original data.

===============================================================================
Common Mistakes
===============================================================================

- Using sort() instead of sorted(), which modifies the original list.
- Forgetting to use the key parameter.
- Returning the string itself instead of its length.
- Forgetting to use reverse=True for descending order.
- Assuming sorted() changes the original list.

===============================================================================
Alternative Approach
===============================================================================

Another valid implementation is:

    names_sorted_by_length = sorted(
        names,
        key=len,
    )

Since len() already accepts one argument and returns the required key, it can
be passed directly without a lambda function. However, this exercise
specifically requires using a lambda function as the key.

===============================================================================
Real-World Relevance
===============================================================================

Custom sorting with the key parameter is widely used in:

- Data analysis
- Report generation
- User interface development
- Search result organization
- Business and inventory management systems

===============================================================================
Key Takeaways
===============================================================================

- The key parameter customizes how sorted() orders elements.
- Lambda functions provide concise custom sorting logic.
- The sorted() function returns a new list and leaves the original list
  unchanged.
- The reverse=True argument sorts elements in descending order.
===============================================================================
"""