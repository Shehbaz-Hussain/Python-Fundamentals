"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Exercise 11: Applying map() with Lambda Functions

Difficulty:
Intermediate

Estimated Time:
15–20 Minutes

Objective:
Practice using the built-in map() function together with a lambda function
to transform every element in an iterable.

Instructions:
1. Create a list of temperatures in Celsius:
   [0, 15, 25, 30, 40]

2. Use map() with a lambda function to convert every temperature to
   Fahrenheit using the formula:

       Fahrenheit = (Celsius × 9 / 5) + 32

3. Store the converted temperatures in a new list.

4. Display:
   - Original Celsius temperatures
   - Converted Fahrenheit temperatures

Expected Output Format (Values should match your calculation):

Original Celsius:
[0, 15, 25, 30, 40]

Converted Fahrenheit:
[32.0, 59.0, 77.0, 86.0, 104.0]

Requirements:
- Use map().
- Use a lambda function.
- Convert the map object into a list.
- Do not use a traditional for loop for the conversion.
- Write clean and readable code following PEP 8.

Challenge:
Round each Fahrenheit value to one decimal place using another lambda
expression.
===============================================================================
"""