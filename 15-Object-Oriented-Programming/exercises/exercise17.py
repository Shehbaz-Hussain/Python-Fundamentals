"""
Exercise 17: Duck Typing

Problem:
Create different classes that provide the same required
behavior and use them through a function without checking
their class types.

Requirements:
1. Define a class named Dog with a speak() method.
2. Define a class named Robot with a speak() method.
3. Define a class named Person with a speak() method.
4. Each speak() method should display a different message.
5. Define a function named make_speak() that accepts one object.
6. Inside make_speak(), call the object's speak() method.
7. Do not use inheritance between Dog, Robot, and Person.
8. Do not use isinstance() or explicit type checking.
9. Create one object from each class.
10. Pass each object to make_speak().

Expected Behavior:
The program should demonstrate that all three objects can be
used because they provide the required speak() behavior.
"""