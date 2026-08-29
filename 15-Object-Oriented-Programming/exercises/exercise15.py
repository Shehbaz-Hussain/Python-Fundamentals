"""
Exercise 15: Using super()

Problem:
Create a parent class named Employee and a child class named
Manager. Use super() to reuse the parent's initialization
behavior.

Requirements:
1. Define a class named Employee.
2. Define an __init__() method in Employee that accepts name.
3. Store name as an instance attribute.
4. Define a method named display_info() that displays:
   "Name: <name>"
5. Define a class named Manager that inherits from Employee.
6. Define an __init__() method in Manager that accepts name
   and department.
7. Use super().__init__(name) to initialize the inherited
   name attribute.
8. Store department as an instance attribute.
9. Override display_info() in Manager.
10. Use super().display_info() inside the overridden method.
11. Display the department after displaying the inherited
    employee information.
12. Create a Manager object with:
    - Name: Ayesha
    - Department: Artificial Intelligence
13. Call display_info().

Expected Behavior:
The program should display:

Name: Ayesha
Department: Artificial Intelligence
"""