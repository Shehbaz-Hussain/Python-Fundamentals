"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 05
Exercise Title: Convert Text to Uppercase Using a Lambda Function
Difficulty: Beginner

Objective:
    Create a lambda function that accepts a string and returns its uppercase
    version. Store the lambda function in a meaningful variable and test it
    with different words and short sentences.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a lambda function that converts text to uppercase.
convert_to_uppercase = lambda text: text.upper()

# Call the lambda function with different strings.
print(convert_to_uppercase("python"))
print(convert_to_uppercase("Lambda Functions"))
print(convert_to_uppercase("Hello, World!"))


"""
===============================================================================
Expected Output
===============================================================================

PYTHON
LAMBDA FUNCTIONS
HELLO, WORLD!

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A lambda function is created using the 'lambda' keyword.
2. The function accepts one parameter named 'text'.
3. The '.upper()' string method converts all lowercase letters to uppercase.
4. The lambda function is stored in the variable 'convert_to_uppercase'.
5. The function is called with three different string values:
       - A lowercase word
       - A mixed-case phrase
       - A short sentence with punctuation
6. Each converted string is displayed using the print() function.

How the Lambda Expression Works
-------------------------------

Lambda expression:

    lambda text: text.upper()

- 'lambda' creates an anonymous function.
- 'text' is the input string.
- The '.upper()' method creates and returns a new uppercase string.
- The original string is not modified because strings are immutable in Python.
- The lambda function automatically returns the converted string.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- Anonymous functions
- String methods
- Function parameters
- Return values
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(n)

Explanation:
The '.upper()' method processes each character in the string once, where
'n' is the length of the string.

===============================================================================
Space Complexity
===============================================================================

O(n)

Explanation:
A new uppercase string is created, requiring additional memory proportional
to the length of the input string.

===============================================================================
Best Practices
===============================================================================

- Use descriptive variable names such as 'convert_to_uppercase'.
- Use built-in string methods instead of manually converting characters.
- Keep lambda expressions simple and limited to a single operation.
- Test the function with different types of text, including sentences.

===============================================================================
Common Mistakes
===============================================================================

- Forgetting the parentheses when calling '.upper()'.
- Using the 'def' keyword instead of a lambda function.
- Assuming '.upper()' modifies the original string.
- Passing a non-string value to the lambda function.
- Forgetting to print the returned value.

===============================================================================
Alternative Approach
===============================================================================

A regular function can also perform the same task:

    def convert_to_uppercase(text):
        return text.upper()

However, for this exercise, a lambda function is required.

===============================================================================
Real-World Relevance
===============================================================================

Converting text to uppercase is commonly used in:

- Data preprocessing
- User input normalization
- Report generation
- Log formatting
- Automation scripts

===============================================================================
Key Takeaways
===============================================================================

- Lambda functions can work with strings as well as numbers.
- The '.upper()' method converts all alphabetic characters to uppercase.
- Strings are immutable, so '.upper()' returns a new string.
- Lambda functions are well suited for short string transformation tasks.
===============================================================================
"""