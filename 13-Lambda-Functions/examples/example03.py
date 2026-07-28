"""
File: example03.py
Topic: Lambda Function with Multiple Parameters

Description:
This example demonstrates how lambda functions can accept multiple
parameters and use them in a single expression.

Concepts Covered:
- Multiple lambda parameters
- Passing multiple arguments
- Automatic return values

Python Version:
Python 3.13+
"""


# Creating a lambda function with two parameters
add_numbers = lambda first_number, second_number: first_number + second_number


# Passing two arguments to the lambda function
result = add_numbers(15, 25)


# Displaying the returned value
print(result)


"""
Expected Output:

40


Explanation:

1. The lambda function has two parameters:
   - first_number
   - second_number

2. The values 15 and 25 are passed as arguments.

3. The expression:
   
   first_number + second_number

   calculates the sum of both values.

4. Lambda functions automatically return the result
   of their expression.

5. The final result is stored in the variable 'result'.

Best Practice:

Use multiple parameters in lambda functions only when the
operation remains simple and easy to understand.

Real-World Relevance:

Lambda functions with multiple parameters are useful for
small calculations, sorting rules, data transformations,
and functional programming operations.
"""