"""
File: example16.py
Topic: Lambda Function for Data Transformation

Description:
This example demonstrates how lambda functions can transform
data by modifying values inside a collection.

Concepts Covered:
- Lambda functions for practical transformations
- map() with lambda
- Data processing

Python Version:
Python 3.13+
"""


# Creating a list of temperatures in Celsius
temperatures_celsius = [0, 10, 20, 30, 40]


# Converting Celsius values to Fahrenheit
temperatures_fahrenheit = list(
    map(
        lambda temperature: (temperature * 9 / 5) + 32,
        temperatures_celsius
    )
)


# Displaying converted temperatures
print(temperatures_fahrenheit)


"""
Expected Output:

[32.0, 50.0, 68.0, 86.0, 104.0]


Explanation:

1. A list containing temperature values in Celsius is created.
2. The map() function applies the lambda function to every value.
3. The lambda expression converts Celsius into Fahrenheit using:

   (Celsius × 9 / 5) + 32

4. Each converted value is added to the new list.
5. The final transformed data is stored in
   'temperatures_fahrenheit'.

Best Practice:

Use lambda functions for simple data transformations.
For complex calculations involving multiple steps, use a
regular function to improve readability.

Real-World Relevance:

Data transformation is a common task in data science,
machine learning preprocessing, automation systems, and
software applications that process measurements or records.
"""