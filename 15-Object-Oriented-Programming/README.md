# Module 15 — Object-Oriented Programming

Object-Oriented Programming (OOP) is a programming paradigm that organizes software around **objects that combine state and behavior**.

Python supports object-oriented programming extensively. Classes and objects are used throughout the Python standard library and many widely used frameworks and libraries.

This module introduces OOP progressively. You will begin with classes, objects, attributes, methods, `self`, and `__init__`, then move toward class-level behavior, encapsulation, inheritance, polymorphism, abstraction, composition, and practical object-oriented design.

The objective is not to memorize class syntax. The objective is to understand **how objects model state and behavior, how responsibilities can be organized, and when object-oriented design is appropriate**.

---

## Learning Objectives

By the end of this module, you should be able to:

* Explain object-oriented programming accurately.
* Distinguish between classes, objects, and instances.
* Define classes in Python.
* Create and use objects.
* Manage object state using instance attributes.
* Define and call instance methods.
* Explain the purpose of `self`.
* Understand and use `__init__`.
* Distinguish instance attributes from class attributes.
* Use class methods appropriately.
* Use static methods appropriately.
* Explain encapsulation in the context of Python.
* Understand Python's conventions for non-public attributes.
* Implement inheritance.
* Use `super()` appropriately.
* Override inherited methods.
* Explain polymorphism and duck typing.
* Understand abstraction and abstract interfaces.
* Use composition to construct objects from other objects.
* Compare inheritance and composition.
* Understand separation of responsibilities.
* Recognize the relationship between cohesion and coupling.
* Determine when a function is more appropriate than a class.
* Design small object-oriented programs.
* Read and understand OOP-based Python libraries and frameworks.
* Recognize practical uses of OOP in AI and machine-learning software.

---

## Prerequisites

Before beginning this module, you should be comfortable with:

* Python syntax
* Variables
* Strings, numbers, and booleans
* Lists, tuples, sets, and dictionaries
* Input and output
* Type conversion
* Arithmetic operators
* Comparison operators
* Logical operators
* Conditional statements
* Loops
* Functions
* Parameters and arguments
* Return values
* Lambda expressions
* Basic built-in functions

These concepts will be used throughout the examples and exercises.

---

## Why Learn Object-Oriented Programming?

Small programs can often be written effectively with variables, functions, and built-in data structures.

As software grows, however, related state and behavior may become difficult to organize when they are scattered across unrelated parts of a program.

Consider a banking application.

An account may have:

* An account number
* An owner
* A balance

It may also support operations such as:

* Depositing money
* Withdrawing money
* Checking the balance

A class can provide a coherent definition for this type of entity, while individual objects can represent specific accounts.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

The class describes the structure and behavior.

An object represents a particular instance:

```python
account = BankAccount("Ali", 1000)
account.deposit(500)
```

The resulting object has its own state:

```text
owner   → "Ali"
balance → 1500
```

This illustrates an important OOP idea:

> A class defines a type of object, while an object is a particular instance of that type.

OOP can make larger programs easier to organize, maintain, test, and extend when the problem naturally involves objects with state and behavior.

However, OOP is **not automatically better than procedural or functional programming**. Python supports multiple programming paradigms, and good software design requires choosing the appropriate abstraction for the problem.

---

## Core Idea: State and Behavior

A useful way to understand OOP is through two related concepts.

### State

State represents information associated with an object.

For example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

A `Student` object might contain:

```text
name → "Sara"
age  → 21
```

These values represent the object's state.

### Behavior

Behavior represents operations an object can perform.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")
```

The `introduce()` method represents behavior associated with the object.

Therefore, a simplified model is:

```text
Object
├── State
│   ├── attributes
│   └── stored data
│
└── Behavior
    ├── methods
    └── operations
```

This model will be developed throughout the module.

---

## Classes and Objects

A **class** is a definition used to create objects.

An **object** is an instance of a class.

For example:

```python
class Car:
    pass
```

`Car` is a class.

We can create objects from it:

```python
car1 = Car()
car2 = Car()
```

Here:

* `Car` is the class.
* `car1` is an object.
* `car2` is another object.
* `car1` and `car2` are separate instances of `Car`.

The objects share the class definition but are distinct objects.

---

## Instance Attributes

Instance attributes store data belonging to a particular object.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Two objects can contain different state:

```python
person1 = Person("Ali", 20)
person2 = Person("Sara", 25)
```

Conceptually:

```text
person1
├── name → "Ali"
└── age  → 20

person2
├── name → "Sara"
└── age  → 25
```

The attributes belong to individual instances.

---

## Instance Methods

Methods are functions defined inside classes.

```python
class Calculator:
    def add(self, a, b):
        return a + b
```

An instance method can operate using the object's state:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

Calling:

```python
account.deposit(100)
```

changes the state of that particular account.

---

## The `self` Parameter

`self` refers to the current object instance when an instance method is called.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(self.name)
```

When:

```python
student = Student("Ali")
student.display_name()
```

is executed, `self` refers to `student` during that method call.

`self` is not a Python keyword. It is the standard naming convention for the first parameter of an instance method.

---

## The `__init__` Method

`__init__` is an initializer method that Python calls after a new instance has been created.

It is commonly used to initialize instance attributes.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

Creating:

```python
product = Product("Keyboard", 50)
```

causes the initializer to run with the supplied arguments.

A common beginner mistake is to call `__init__` a constructor without qualification.

Technically, Python's object creation process involves `__new__()` creating the instance and `__init__()` initializing it. For introductory OOP, `__init__()` is commonly described as the initializer.

---

## Class Attributes

Class attributes belong to the class and can be shared through the class definition.

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name
```

Here:

```python
Student.school
```

accesses the class attribute.

Instance attributes and class attributes serve different purposes and should not be treated as interchangeable.

---

## Class Methods

A class method receives the class as its first argument, conventionally named `cls`.

It is declared using `@classmethod`.

```python
class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, name):
        cls.school = name
```

Class methods are useful when an operation conceptually belongs to the class rather than to a particular instance.

They are also frequently used for alternative constructors.

---

## Static Methods

A static method does not automatically receive either an instance (`self`) or a class (`cls`).

It is declared using `@staticmethod`.

```python
class MathTools:
    @staticmethod
    def add(a, b):
        return a + b
```

Static methods are useful when a function is logically related to a class but does not need instance or class state.

However, not every utility function needs to be placed inside a class. Sometimes a normal module-level function is the clearer design.

---

## Encapsulation

Encapsulation concerns how data and behavior are organized behind an interface and how access to internal implementation details is controlled or discouraged.

Python does not provide the same strict private-field access mechanism found in some other languages.

Instead, Python uses conventions and mechanisms such as:

### Single leading underscore

```python
self._balance
```

A leading underscore conventionally indicates that an attribute or method is intended for internal or non-public use.

It does not technically prevent access.

### Double leading underscore

```python
self.__balance
```

A double leading underscore triggers **name mangling**.

It is primarily intended to reduce accidental name collisions in subclasses rather than to provide absolute privacy.

Understanding this distinction is important when discussing encapsulation in Python.

---

## Inheritance

Inheritance allows a class to derive from another class.

```python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    pass
```

`Dog` inherits from `Animal`.

Therefore:

```python
dog = Dog()
dog.speak()
```

can use the inherited method.

Inheritance can model an **is-a** relationship, but it should not be used merely to reuse code.

---

## `super()`

`super()` provides a way to access behavior from a parent class according to Python's method resolution order.

For example:

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

The child class reuses the parent initialization logic instead of duplicating it.

---

## Method Overriding

A subclass can provide its own implementation of an inherited method.

```python
class Animal:
    def speak(self):
        print("Some sound")


class Dog(Animal):
    def speak(self):
        print("Woof")
```

The `Dog` implementation overrides the inherited `speak()` implementation.

This is an important mechanism behind polymorphic behavior.

---

## Polymorphism

Polymorphism means that a common operation can work with different object types while each type provides an appropriate implementation.

For example:

```python
class Dog:
    def speak(self):
        print("Woof")


class Cat:
    def speak(self):
        print("Meow")
```

Code that calls:

```python
animal.speak()
```

can work with either object if the required interface is available.

Polymorphism does not necessarily require inheritance.

---

## Duck Typing

Python commonly uses **duck typing**.

The principle can be summarized as:

> What an object can do is often more important than what class it belongs to.

For example:

```python
def make_sound(animal):
    animal.speak()
```

The function does not need to know the exact class of `animal`.

It only needs the object passed to it to provide a compatible `speak()` operation.

This is one of the defining characteristics of Python's dynamic type system.

---

## Abstraction

Abstraction focuses on exposing the interface necessary to use a component while separating that interface from implementation details.

For example, a user of a banking class may need:

```python
account.deposit(500)
account.withdraw(100)
```

They do not necessarily need to know every internal detail of how the account maintains its state.

Python also provides formal mechanisms for abstract interfaces through the `abc` module and abstract base classes. These concepts will be introduced at an appropriate point in the module.

---

## Composition

Composition builds larger objects by giving them references to other objects.

For example:

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()
```

A `Car` contains an `Engine`.

This models a **has-a** relationship:

```text
Car
└── Engine
```

Composition is often preferable to inheritance when one object uses or contains another object rather than representing a specialized version of it.

---

## Composition vs Inheritance

A useful initial distinction is:

| Relationship                    | Typical Technique     |
| ------------------------------- | --------------------- |
| "Dog is an Animal"              | Inheritance           |
| "Car has an Engine"             | Composition           |
| "Order uses a PaymentProcessor" | Composition           |
| "Manager is an Employee"        | Potential inheritance |
| "Report uses a Formatter"       | Composition           |

The choice should depend on the domain model and the responsibilities of the objects.

A common design principle is:

> Prefer composition over inheritance when composition provides a simpler and more flexible design.

This is a guideline, not an absolute rule.

---

## Cohesion and Coupling

Good object-oriented design considers both cohesion and coupling.

### Cohesion

Cohesion describes how closely related the responsibilities within a component are.

A highly cohesive class generally has a focused responsibility.

### Coupling

Coupling describes the degree of dependency between components.

Lower unnecessary coupling generally makes software easier to change and maintain.

A useful design goal is:

```text
High cohesion
+
Low unnecessary coupling
=
More maintainable design
```

These principles become increasingly important as programs grow.

---

## Functions vs Classes

A class should not be introduced simply because a program can use one.

A function may be the better abstraction when:

* There is no meaningful persistent object state.
* The operation is simple and independent.
* A standalone transformation describes the problem clearly.
* Creating an object would add unnecessary complexity.

A class may be appropriate when:

* State needs to persist across multiple operations.
* Several operations naturally belong to the same entity.
* Multiple instances of the same conceptual type are required.
* The object has clear responsibilities and behavior.
* The abstraction improves organization and maintainability.

The objective is not to maximize the number of classes.

The objective is to create an appropriate design.

---

## OOP in AI and Machine Learning

Object-oriented programming appears throughout AI and machine-learning software.

Examples include objects representing:

* Datasets
* Models
* Training configurations
* Neural-network layers
* Optimizers
* Tokenizers
* Pipelines
* Evaluation components
* Data-processing components

A simplified machine-learning model might conceptually look like:

```python
class Model:
    def __init__(self):
        self.parameters = {}

    def train(self, data):
        pass

    def predict(self, data):
        pass
```

Real machine-learning frameworks use much more sophisticated designs, but the same fundamental ideas appear repeatedly:

```text
Object
├── State
│   ├── parameters
│   ├── configuration
│   └── metadata
│
└── Behavior
    ├── train()
    ├── predict()
    └── evaluate()
```

Understanding OOP therefore helps when reading and working with professional Python libraries used in AI and machine learning.

---

## Module Structure

This module is organized into the following sections:

### `theory/`

Conceptual explanations of OOP and object-oriented design.

Topics include:

* OOP fundamentals
* Classes and objects
* Attributes and methods
* `self`
* `__init__`
* Class attributes
* Class methods
* Static methods
* Encapsulation
* Inheritance
* Method overriding
* Polymorphism
* Abstraction
* Composition
* OOP best practices

### `syntax/`

Focused syntax references for common OOP constructs.

### `examples/`

Small, focused Python programs demonstrating individual concepts.

### `exercises/`

20 progressively challenging programming exercises.

### `solutions/`

Solutions corresponding to all 20 exercises.

### `projects/`

10 practical projects designed to apply OOP concepts in increasingly realistic scenarios.

### `quizzes/`

Knowledge checks, multiple-choice questions, and answer keys.

### `assignments/`

Larger practice tasks requiring design and implementation.

### `notes/`

Revision, examination, and interview-oriented notes.

### `cheat-sheet/`

A compact reference for frequently used OOP syntax and concepts.

### `assets/images/`

Visual learning resources used by the module.

---

## Recommended Learning Sequence

Follow the module in this order:

```text
OOP Fundamentals
       ↓
Classes and Objects
       ↓
Attributes and Methods
       ↓
self and __init__
       ↓
Class Attributes
       ↓
Class Methods and Static Methods
       ↓
Encapsulation
       ↓
Inheritance
       ↓
super() and Method Overriding
       ↓
Polymorphism
       ↓
Duck Typing
       ↓
Abstraction
       ↓
Composition
       ↓
Cohesion and Coupling
       ↓
OOP Design Decisions
       ↓
Practical Projects
       ↓
AI/ML Applications
```

Do not skip the conceptual material simply to reach the projects. Understanding why a design works is more important than memorizing its syntax.

---

## Important Principles

Keep the following principles in mind throughout the module:

1. **A class is a definition; an object is an instance.**
2. **Instance attributes represent object-specific state.**
3. **Instance methods operate in the context of an instance.**
4. **`self` refers to the current instance in an instance method.**
5. **`__init__()` initializes an already-created instance.**
6. **Class attributes belong to the class and can be shared.**
7. **Class methods receive the class through `cls`.**
8. **Static methods receive neither `self` nor `cls` automatically.**
9. **Python's encapsulation mechanisms do not provide absolute private fields.**
10. **Inheritance should model an appropriate subtype relationship, not merely provide code reuse.**
11. **Polymorphism can exist without inheritance.**
12. **Duck typing focuses on supported behavior rather than exact type.**
13. **Composition models relationships where one object contains or uses another.**
14. **High cohesion and low unnecessary coupling generally improve maintainability.**
15. **A function is sometimes a better abstraction than a class.**
16. **Good OOP design is about responsibilities and relationships, not class count.**

---

## Expected Outcome

After completing this module, you should be able to read a basic object-oriented Python program and explain:

* Which classes exist.
* Which objects are created.
* What state each object stores.
* Which methods define behavior.
* How `self` is used.
* How objects interact.
* Which attributes belong to instances or classes.
* Where inheritance is used.
* Where polymorphism occurs.
* Where composition is used.
* Why a particular design was chosen.

You should also be able to design and implement small object-oriented Python programs independently.

This foundation will support later work involving Python software engineering, machine learning, deep learning, AI applications, APIs, automation, and larger software systems.

---

## Module Completion Checklist

Before considering this module complete, verify that you can:

* [ ] Explain OOP and its purpose.
* [ ] Define a class.
* [ ] Create objects from a class.
* [ ] Explain the difference between a class and an instance.
* [ ] Create instance attributes.
* [ ] Define instance methods.
* [ ] Explain `self`.
* [ ] Use `__init__()` correctly.
* [ ] Explain class attributes.
* [ ] Use class methods.
* [ ] Use static methods.
* [ ] Explain Python's approach to encapsulation.
* [ ] Implement inheritance.
* [ ] Use `super()`.
* [ ] Override methods.
* [ ] Explain polymorphism.
* [ ] Demonstrate duck typing.
* [ ] Explain abstraction.
* [ ] Use composition.
* [ ] Compare composition and inheritance.
* [ ] Explain cohesion and coupling.
* [ ] Decide when a function is preferable to a class.
* [ ] Design a small object-oriented application.
* [ ] Recognize OOP patterns in AI/ML libraries.

---

## Next Steps

After completing Module 15, continue practicing by building increasingly realistic Python programs.

The next stage should focus on applying Python's object-oriented features in larger software systems and preparing for the engineering concepts required in machine-learning and AI development.
