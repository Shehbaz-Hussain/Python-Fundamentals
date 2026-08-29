"""
Exercise 18: Composition

Problem:
Model a Car that contains an Engine object using composition.

Requirements:
1. Define a class named Engine.
2. Add a method named start() to Engine.
3. The start() method should display:
   "Engine started."
4. Define a class named Car.
5. Define an __init__() method in Car that accepts brand.
6. Store brand as an instance attribute.
7. Create an Engine object inside the Car object and store it
   in an instance attribute named engine.
8. Define a method named start() in Car.
9. The Car start() method should display:
   "<brand> is starting."
10. The Car start() method should then call the Engine object's
    start() method.
11. Create a Car object with the brand "Toyota".
12. Call the Car start() method.

Expected Behavior:
The program should display:

Toyota is starting.
Engine started.
"""