"""
Exercise 09: Instance vs Class Attributes

Problem:
Create a Python class named Employee that demonstrates the
difference between an instance attribute and a class attribute.

Requirements:
1. Define a class named Employee.
2. Define a class attribute named company and set it to
   "Tech Solutions".
3. Define an __init__() method that accepts name and salary.
4. Store name and salary as instance attributes.
5. Define an instance method named display_info().
6. Create two Employee objects with different names and salaries.
7. Display each employee's name, salary, and company.
8. Change the company class attribute to "AI Solutions" through
   the Employee class.
9. Display the information again to show that both objects
   observe the updated class attribute.

Expected Behavior:
Initially, both employees should display:

Company: Tech Solutions

After changing the class attribute, both employees should display:

Company: AI Solutions
"""