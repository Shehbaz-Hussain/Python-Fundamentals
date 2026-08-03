"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 12
Exercise Title: Filtering Data with filter() and Lambda
Difficulty: Intermediate

Objective:
    Practice using the built-in filter() function together with a lambda
    function to extract elements that satisfy a specified condition. Filter
    even numbers from a list and complete the challenge by filtering numbers
    greater than 30.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a list of integers.
numbers = [12, 7, 25, 18, 31, 42, 55, 60, 73, 84]

# Filter only the even numbers using filter() and a lambda function.
even_numbers = list(
    filter(
        lambda number: number % 2 == 0,
        numbers,
    )
)

# Challenge: Filter numbers greater than 30.
numbers_greater_than_30 = list(
    filter(
        lambda number: number > 30,
        numbers,
    )
)

# Display the results.
print("Original Numbers:")
print(numbers)

print("\nEven Numbers:")
print(even_numbers)

print("\nNumbers Greater Than 30:")
print(numbers_greater_than_30)


"""
===============================================================================
Expected Output
===============================================================================

Original Numbers:
[12, 7, 25, 18, 31, 42, 55, 60, 73, 84]

Even Numbers:
[12, 18, 42, 60, 84]

Numbers Greater Than 30:
[31, 42, 55, 60, 73, 84]

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A list of integers is created.
2. The filter() function processes each element in the list.
3. A lambda function checks whether each number is even by evaluating:

       number % 2 == 0

4. Only numbers that satisfy the condition are included in the filtered
   result.
5. The filter object is converted into a list using the list() constructor.
6. As an additional challenge, another filter() function with a lambda
   expression selects numbers greater than 30.
7. The original list, the list of even numbers, and the list of numbers
   greater than 30 are displayed.

How the Lambda Expressions Work
-------------------------------

First lambda expression:

    lambda number: number % 2 == 0

- Accepts one integer.
- Checks whether the number is evenly divisible by 2.
- Returns True for even numbers and False for odd numbers.

Second lambda expression:

    lambda number: number > 30

- Accepts one integer.
- Checks whether the number is greater than 30.
- Returns True only for numbers that satisfy the condition.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- filter()
- Lists
- Comparison operators
- Modulus operator
- Boolean return values
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(n)

Explanation:
Each call to filter() examines every element in the list once. Since two
filter() operations are performed sequentially, the overall time complexity
remains O(n).

===============================================================================
Space Complexity
===============================================================================

O(n)

Explanation:
New lists are created to store the filtered results.

===============================================================================
Best Practices
===============================================================================

- Use filter() when selecting elements based on a condition.
- Keep lambda expressions simple and easy to understand.
- Convert filter objects to lists when the results need to be reused or
  displayed.
- Use descriptive variable names that clearly indicate the filtering criteria.

===============================================================================
Common Mistakes
===============================================================================

- Forgetting to convert the filter object into a list.
- Using assignment (=) instead of the equality operator (==).
- Using map() instead of filter() for selecting elements.
- Writing an incorrect filtering condition.
- Using a traditional for loop instead of filter() when the exercise requires
  filter().

===============================================================================
Alternative Approach
===============================================================================

Another valid implementation is to filter numbers greater than 30 first and
then filter even numbers from that result, depending on the desired logic.

===============================================================================
Real-World Relevance
===============================================================================

Filtering data is commonly used in:

- Data preprocessing
- Business analytics
- Report generation
- Data validation
- Machine learning data preparation

===============================================================================
Key Takeaways
===============================================================================

- filter() selects only the elements that satisfy a condition.
- Lambda functions provide a concise way to define filtering criteria.
- Converting a filter object to a list makes the filtered data easy to use.
- Combining filter() with lambda functions simplifies data selection tasks.
===============================================================================
"""