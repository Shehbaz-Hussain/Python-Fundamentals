# Module 15 - Object-Oriented Programming Assignment 01

## Intermediate Level Assignment

**Python Programming Foundation**

**Module:** 15 - Object-Oriented Programming

**Difficulty:** Intermediate

**Python Version:** 3.13+

---

# Assignment Overview

This assignment is designed to strengthen practical understanding of:

* Classes
* Objects
* Constructors
* Instance attributes
* Instance methods
* Class attributes
* Object state
* Encapsulation
* Inheritance
* Method overriding
* Polymorphism
* Abstraction
* Composition

You will solve realistic programming problems by designing and implementing object-oriented Python programs.

---

# Instructions

* Complete all problems using Python 3.13+.
* Use classes and objects wherever appropriate.
* Use `__init__()` to initialize object attributes where required.
* Keep each class focused on a clear responsibility.
* Write clean and readable code.
* Use meaningful class, method, and variable names.
* Test your programs with multiple inputs and objects.
* Avoid unnecessary complexity.
* Do not use external libraries.
* Do not use global variables unnecessarily.
* Make sure every program runs without errors.

---

# Problem 01: Student Class

Create a `Student` class.

Requirements:

* Define a `Student` class.
* Add `name`, `age`, and `program` attributes.
* Use `__init__()` to initialize the attributes.
* Create at least three student objects.
* Display the information of each student.

Example:

```python
student1 = Student("Ali", 20, "BS Artificial Intelligence")
```

Expected output:

```text
Name: Ali
Age: 20
Program: BS Artificial Intelligence
```

---

# Problem 02: Student Information Method

Extend the `Student` class from Problem 01.

Requirements:

* Create a method named `display_info()`.
* The method should display all student information.
* Create multiple student objects.
* Call `display_info()` for each object.

---

# Problem 03: Rectangle Calculator

Create a `Rectangle` class.

Requirements:

* Store `length`.
* Store `width`.
* Create an `area()` method.
* Create a `perimeter()` method.
* Create a rectangle object.
* Display the area and perimeter.

Formulas:

```text
Area = length × width

Perimeter = 2 × (length + width)
```

Example:

```python
rectangle = Rectangle(10, 5)
```

Expected output:

```text
Area: 50
Perimeter: 30
```

---

# Problem 04: Bank Account

Create a `BankAccount` class.

Requirements:

* Store account holder name.
* Store account balance.
* Create a `deposit()` method.
* Create a `withdraw()` method.
* Create a `display_balance()` method.
* Prevent withdrawals greater than the available balance.

Example:

```python
account = BankAccount("Ali", 50000)
account.deposit(10000)
account.withdraw(15000)
account.display_balance()
```

Expected output:

```text
Account Holder: Ali
Balance: 45000
```

---

# Problem 05: Employee Salary Manager

Create an `Employee` class.

Requirements:

* Store employee name.
* Store employee position.
* Store employee salary.
* Create a `give_raise()` method.
* Create a `display_info()` method.
* Increase the salary by a specified amount.

Example:

```python
employee = Employee("Sara", "Developer", 80000)
employee.give_raise(10000)
```

Expected output:

```text
Name: Sara
Position: Developer
Salary: 90000
```

---

# Problem 06: Product Inventory

Create a `Product` class.

Requirements:

* Store product name.
* Store product price.
* Store product quantity.
* Create an `increase_quantity()` method.
* Create a `decrease_quantity()` method.
* Create a `display_product()` method.
* Prevent quantity from becoming negative.

Example:

```python
product = Product("Laptop", 120000, 10)
product.increase_quantity(5)
product.decrease_quantity(2)
```

---

# Problem 07: Class Attribute

Create a `Student` class with a class attribute named:

```python
school_name
```

Requirements:

* Set one common school name.
* Create multiple student objects.
* Display each student's name and school name.
* Demonstrate the difference between a class attribute and an instance attribute.

---

# Problem 08: Employee Object Counter

Create an `Employee` class that keeps track of the number of employee objects created.

Requirements:

* Create a class attribute named `employee_count`.
* Increase the count whenever a new employee object is created.
* Create at least five employee objects.
* Display the total number of employees.

Expected output:

```text
Total Employees: 5
```

---

# Problem 09: Encapsulated Bank Account

Create a secure `BankAccount` class.

Requirements:

* Store the balance as an internal attribute.
* Provide a method for depositing money.
* Provide a method for withdrawing money.
* Provide a method for checking the balance.
* Do not allow invalid withdrawals.
* Do not directly modify the balance from outside the class.

The objective is to demonstrate **encapsulation** and controlled access to object state.

---

# Problem 10: Animal Inheritance

Create a base class named `Animal`.

Create two child classes:

* `Dog`
* `Cat`

Requirements:

* The `Animal` class should contain a common attribute such as `name`.
* `Dog` should have a `make_sound()` method.
* `Cat` should have a `make_sound()` method.
* Create objects from both child classes.
* Display their sounds.

Example output:

```text
Dog: Bark
Cat: Meow
```

---

# Problem 11: Vehicle Inheritance

Create a base class named `Vehicle`.

Create the following child classes:

* `Car`
* `Motorcycle`
* `Truck`

Requirements:

* Add appropriate attributes to the parent class.
* Add specific behavior to each child class.
* Use inheritance correctly.
* Create objects of all three child classes.
* Display their information.

---

# Problem 12: Method Overriding

Create a base class named `Employee`.

Create two child classes:

* `Developer`
* `Manager`

Requirements:

* Define a method named `work()` in the parent class.
* Override `work()` in both child classes.
* Give each child class different behavior.
* Create objects and call the `work()` method.

Example output:

```text
Developer is writing code.
Manager is managing the team.
```

---

# Problem 13: Polymorphism

Create multiple classes:

* `Dog`
* `Cat`
* `Bird`

Each class should implement:

```python
make_sound()
```

Requirements:

* Create objects from all three classes.
* Store the objects in a collection.
* Loop through the collection.
* Call `make_sound()` on every object.

The same method call should produce different behavior depending on the object.

---

# Problem 14: Shape System

Create a base class named `Shape`.

Create child classes:

* `Circle`
* `Rectangle`
* `Triangle`

Requirements:

* Each class should implement an `area()` method.
* Use appropriate formulas.
* Create objects for each shape.
* Display their areas.

Demonstrate **inheritance and polymorphism**.

---

# Problem 15: Payment System

Create the following classes:

* `CashPayment`
* `CardPayment`
* `OnlinePayment`

Requirements:

* Each class must implement a `pay(amount)` method.
* Each class should provide different payment behavior.
* Create objects from all payment classes.
* Call the same `pay()` method for each object.

The program should demonstrate **polymorphism**.

---

# Problem 16: Library Management System

Create a simple library management system using OOP.

Create appropriate classes for:

* `Book`
* `Member`
* `Library`

The system should support:

* Adding books.
* Registering members.
* Borrowing books.
* Returning books.
* Displaying available books.

Each class should have a clear responsibility.

---

# Problem 17: Shopping Cart

Create a `ShoppingCart` class.

Requirements:

* Store multiple products.
* Add products to the cart.
* Remove products from the cart.
* Display all products.
* Calculate the total price.

Use appropriate classes such as:

```text
Product
ShoppingCart
```

---

# Problem 18: Composition

Create an `Engine` class.

Create a `Car` class that contains an `Engine` object.

Requirements:

* Create an `Engine` class.
* Create a `Car` class.
* Pass an `Engine` object to the `Car`.
* Allow the car to start its engine.
* Demonstrate the relationship between the two objects.

The objective is to understand **composition**.

---

# Problem 19: Abstract Shape

Create an abstract `Shape` design.

Create:

* `Circle`
* `Rectangle`

Requirements:

* Define an abstract `area()` method.
* Implement `area()` in each child class.
* Create objects from both classes.
* Display their areas.

Use Python's `abc` module for abstraction.

---

# Problem 20: AI Model Class

Create a class named `AIModel`.

The class should contain:

* `name`
* `model_type`
* `version`
* `accuracy`
* `status`

Create methods:

* `load()`
* `unload()`
* `display_info()`

Example:

```python
model = AIModel(
    "GPT Model",
    "Generative AI",
    "1.0",
    95.5
)
```

The program should allow the model status to change between loaded and unloaded states.

---

# Final Project: AI Model Management System

Build a complete command-line **AI Model Management System** using Object-Oriented Programming.

## Requirements

The system should allow users to:

* Add an AI model.
* Display all models.
* Search for a model.
* Update model information.
* Activate a model.
* Deactivate a model.
* Remove a model.
* Display model statistics.

## AI Model Attributes

Each model should contain:

* Model name
* Model type
* Version
* Accuracy
* Status

Example:

```text
Model Name: ImageClassifier
Model Type: Computer Vision
Version: 1.0
Accuracy: 94.5%
Status: Active
```

## Suggested Classes

At minimum, use:

```text
AIModel
ModelRegistry
```

You may create additional classes if they improve the design.

## OOP Requirements

The final project should demonstrate:

* Classes
* Objects
* Constructors
* Instance attributes
* Instance methods
* Class attributes where appropriate
* Encapsulation
* Inheritance
* Method overriding
* Polymorphism
* Abstraction
* Composition where appropriate

---

# Learning Objectives

After completing this assignment, you should be able to:

* Create classes and objects in Python.
* Use constructors with `__init__()`.
* Define and modify instance attributes.
* Create instance methods.
* Understand the `self` parameter.
* Distinguish between class and instance attributes.
* Encapsulate object data.
* Implement inheritance.
* Override methods in child classes.
* Apply polymorphism.
* Understand abstraction.
* Use composition between objects.
* Design classes with clear responsibilities.
* Build small applications using OOP.
* Apply OOP concepts to AI-related software problems.

---

# Submission Requirements

Submit:

* Python source files.
* Proper comments where necessary.
* Sample input.
* Sample output.
* Clean formatting.
* Meaningful class and method names.
* Tested and working programs.

---

# Challenge Extension

For additional practice:

1. Add input validation to the programs.
2. Add exception handling where appropriate.
3. Implement `__str__()` in selected classes.
4. Implement `__repr__()` where appropriate.
5. Refactor one procedural program from an earlier module into an OOP design.
6. Build a larger system by combining multiple classes.
7. Compare inheritance and composition and explain when each should be used.
8. Add file-based data storage to the final AI Model Management System as an advanced extension.

---