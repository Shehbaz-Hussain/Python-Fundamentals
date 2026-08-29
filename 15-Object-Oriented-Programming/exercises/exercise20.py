"""
Exercise 20: Integrated OOP Design

Problem:
Design a small employee system that demonstrates inheritance,
method overriding, polymorphism, and object state.

Requirements:
1. Define a class named Employee.
2. Employee must have an __init__() method that accepts name
   and salary.
3. Store name and salary as instance attributes.
4. Define a method named display_info() that displays the
   employee's name and salary.
5. Define a class named Developer that inherits from Employee.
6. Developer must accept name, salary, and programming_language.
7. Use super().__init__() to initialize the inherited attributes.
8. Store programming_language as an instance attribute.
9. Override display_info() in Developer.
10. The overridden method must display the employee's name,
    salary, and programming language.
11. Define a class named Manager that inherits from Employee.
12. Manager must accept name, salary, and team_size.
13. Use super().__init__() to initialize the inherited attributes.
14. Store team_size as an instance attribute.
15. Override display_info() in Manager.
16. The overridden method must display the employee's name,
    salary, and team size.
17. Create at least one Employee, one Developer, and one Manager.
18. Store all objects in the same collection.
19. Use a loop to call display_info() on every object.
20. Do not use explicit type checking such as isinstance().
21. The program must demonstrate that different employee
    objects can be used through the same display_info() interface.

Expected Behavior:
The program should display appropriate information for each
employee, developer, and manager, for example:

Name: Ali
Salary: $50000.00

Name: Ayesha
Salary: $70000.00
Programming Language: Python

Name: Hamza
Salary: $80000.00
Team Size: 8

The exact formatting may be chosen by the implementation,
provided all required information is displayed.

Concepts Practiced:
- Classes
- Objects
- Instance attributes
- Inheritance
- Method overriding
- super()
- Polymorphism
- Object state
"""