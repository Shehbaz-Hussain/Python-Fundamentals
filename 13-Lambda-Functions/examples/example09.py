"""
File: example09.py
Topic: Lambda Function with Conditional Expression

Description:
This example demonstrates how lambda functions can use conditional
expressions to return different values based on a condition.

Concepts Covered:
- Lambda functions with conditions
- Conditional expressions
- Boolean evaluation

Python Version:
Python 3.13+
"""


# Creating a lambda function with a conditional expression
check_age = lambda age: "Adult" if age >= 18 else "Minor"


# Passing different arguments to test the condition
first_result = check_age(25)
second_result = check_age(14)


# Displaying the returned values
print(first_result)
print(second_result)


"""
Expected Output:

Adult
Minor


Explanation:

1. The lambda function receives one parameter named 'age'.
2. The conditional expression checks whether age is greater than
   or equal to 18.
3. If the condition is True, the function returns "Adult".
4. If the condition is False, the function returns "Minor".
5. Lambda functions automatically return the result of the expression.

Best Practice:

Conditional expressions inside lambda functions should remain
short and readable. Avoid writing complex decision-making logic
inside lambda functions.

Real-World Relevance:

Lambda functions with conditional expressions are useful for
simple classification tasks, data labeling, filtering conditions,
and quick decision rules in data processing applications.
"""