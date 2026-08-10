# Introduction to Object-Oriented Programming

Object-Oriented Programming (OOP) is a programming paradigm that organizes software around **objects that combine state and behavior**.

In Python, OOP is not a separate language feature layered on top of the language. Python's object model is fundamental to how the language works. Values such as integers, strings, lists, functions, and user-defined instances are all objects.

OOP provides a way to model related data and operations as coherent units. It can make larger programs easier to organize and maintain when the problem naturally contains entities with state, behavior, and relationships.

However, OOP is not automatically the best solution for every problem. Python supports procedural, functional, and object-oriented programming styles, and professional software commonly combines them.

---

## What Is Object-Oriented Programming?

Object-Oriented Programming is a programming paradigm in which software is structured around **objects** that represent state and provide behavior.

An object can conceptually be viewed as:

```text
Object
├── State
│   └── Data associated with the object
│
└── Behavior
    └── Operations the object can perform
```

For example, a bank account could have:

```text
State:
- account number
- owner
- balance

Behavior:
- deposit
- withdraw
- check balance
```

In Python, a class can define the structure and behavior of such objects.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

An individual account can then be represented by an object:

```python
account = BankAccount("Ali", 1000)
```

The object contains state:

```text
owner   → "Ali"
balance → 1000
```

and provides behavior:

```python
account.deposit(500)
```

After the operation:

```text
balance → 1500
```

The important idea is that the account's state and the operations that manipulate that state are represented together.

---

## OOP Is a Programming Paradigm

A programming paradigm is a general approach to structuring and thinking about programs.

Common programming paradigms include:

* Procedural programming
* Functional programming
* Object-oriented programming
* Declarative programming

OOP emphasizes objects and their relationships.

Procedural programming often emphasizes:

```text
Data
  ↓
Functions
  ↓
Operations
```

OOP often organizes the same problem around:

```text
Objects
├── State
└── Behavior
```

These are not mutually exclusive approaches in Python.

A Python program can contain:

* Functions
* Classes
* Objects
* Data structures
* Modules
* Higher-order functions
* Object-oriented abstractions

Professional Python code frequently combines several programming styles.

---

## Why Does OOP Exist?

OOP became particularly valuable as software systems grew larger and more complex.

Consider a small program that calculates the area of a rectangle:

```python
width = 10
height = 5

area = width * height
```

A class would probably be unnecessary here.

Now consider a graphics application containing hundreds of rectangles.

Each rectangle may need:

* Width
* Height
* Position
* Color
* Visibility state
* Movement behavior
* Resizing behavior
* Rendering behavior

Managing all of this as unrelated variables can become difficult.

A class can provide a coherent abstraction:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

Multiple objects can then represent multiple rectangles:

```python
rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(20, 8)
```

Each object maintains its own state while sharing the class's behavior definition.

This is one of the primary motivations for object-oriented design.

---

## Classes and Objects

Two foundational OOP concepts are **classes** and **objects**.

### Class

A class defines a type and provides the structure and behavior used by its instances.

```python
class Student:
    pass
```

`Student` is a class.

### Object

An object is a particular instance of a class.

```python
student = Student()
```

Here:

* `Student` is the class.
* `student` is an object.
* `student` is an instance of `Student`.

A useful mental model is:

```text
Class
  ↓
Defines a type
  ↓
Creates instances
  ↓
Objects
```

The class is not the object itself.

---

## Objects Have Identity, Type, and State

Python's object model can be understood through three important concepts:

### Identity

Identity answers:

> Which particular object is this?

Python provides the `id()` function to expose an object's identity value during its lifetime.

```python
student = Student()

print(id(student))
```

The exact numeric value is implementation-dependent and should not normally be used as application data.

The `is` operator checks object identity:

```python
a = []
b = a
c = []

print(a is b)
print(a is c)
```

The first comparison is `True` because `a` and `b` refer to the same object.

The second is `False` because `c` is a different object.

---

### Type

Every Python object has a type.

```python
number = 42

print(type(number))
```

The result identifies the object's type.

For user-defined objects:

```python
class Student:
    pass

student = Student()

print(type(student))
```

The object is an instance of `Student`.

---

### State

State refers to information associated with an object.

For example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

An instance might have:

```text
name → "Sara"
age  → 21
```

That information represents the object's current state.

---

## State and Behavior

One of the most useful ways to understand OOP is to separate **state** from **behavior**.

Consider a `BankAccount`.

### State

```text
owner
balance
account_number
```

### Behavior

```text
deposit()
withdraw()
transfer()
```

The class can combine them:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
```

This creates a meaningful relationship between the data and operations.

The `deposit()` method changes the balance belonging to the particular account object.

---

## Abstraction

Abstraction means representing a concept through a useful interface while hiding unnecessary implementation details.

For example, a user may interact with:

```python
account.deposit(500)
```

The user does not need to know every internal operation involved in updating the account's state.

The interface provides a meaningful operation:

```text
deposit()
```

instead of requiring the caller to manipulate internal implementation details directly.

Abstraction is not the same thing as simply "hiding code."

It is about choosing an appropriate interface that exposes what users of a component need while minimizing unnecessary implementation knowledge.

---

## Encapsulation

Encapsulation concerns how data and behavior are organized together and how internal implementation details are controlled or discouraged from external use.

Python approaches encapsulation differently from languages that enforce private fields through access modifiers.

For example:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
```

The leading underscore communicates:

> This attribute is intended for internal or non-public use.

However, Python does not prevent access:

```python
account._balance
```

This is a convention rather than strict access control.

Double leading underscores introduce name mangling:

```python
self.__balance
```

Name mangling is primarily useful for reducing accidental name collisions in subclasses.

Therefore, it is technically inaccurate to claim that Python's `_name` or `__name` syntax creates completely private fields.

---

## Inheritance

Inheritance allows one class to derive from another.

For example:

```python
class Animal:
    def speak(self):
        print("Some sound")


class Dog(Animal):
    pass
```

`Dog` inherits from `Animal`.

Therefore:

```python
dog = Dog()
dog.speak()
```

can use the inherited behavior.

Inheritance can be useful when a subclass genuinely represents a specialized form of its parent.

For example:

```text
Animal
├── Dog
├── Cat
└── Bird
```

This represents an **is-a** relationship.

However, inheritance should not be selected merely because it allows code reuse.

---

## Polymorphism

Polymorphism allows code to work with different object types through a common operation or interface.

Consider:

```python
class Dog:
    def speak(self):
        print("Woof")


class Cat:
    def speak(self):
        print("Meow")
```

Both objects support:

```python
speak()
```

A function can therefore operate on either:

```python
def make_sound(animal):
    animal.speak()
```

The function does not need to know whether the object is a `Dog` or `Cat`.

This is closely related to Python's duck typing.

---

## Duck Typing

Duck typing focuses on behavior rather than explicit type relationships.

The common informal expression is:

> If it behaves like the required object, it can be used as that object.

For example:

```python
def start_device(device):
    device.start()
```

The function does not require a specific class.

Any compatible object can be passed:

```python
class Car:
    def start(self):
        print("Car started")


class Computer:
    def start(self):
        print("Computer started")
```

Both provide the required `start()` behavior.

Therefore:

```python
start_device(Car())
start_device(Computer())
```

can work without inheritance between the classes.

This demonstrates an important characteristic of Python's dynamic type system.

---

## Composition

Composition allows objects to be constructed from other objects.

For example:

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()
```

The `Car` contains an `Engine` object.

The relationship is:

```text
Car
└── Engine
```

This represents a **has-a** relationship.

Composition is often useful when objects collaborate without one being a specialized subtype of another.

---

## OOP Does Not Mean "Everything Must Be a Class"

A common beginner misconception is:

> Good Python programs should put everything inside classes.

This is incorrect.

Python supports multiple programming paradigms, and a class should be introduced only when it provides a useful abstraction.

For example:

```python
def calculate_area(width, height):
    return width * height
```

A class may be unnecessary if there is no meaningful persistent state.

A class becomes more reasonable when the program needs to represent multiple objects with state and behavior:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

The design decision should be based on the problem, not on a rule that every piece of code must be object-oriented.

---

## OOP and Data Structures

OOP and data structures solve different but complementary problems.

A data structure organizes data.

For example:

```python
students = ["Ali", "Sara", "Hamza"]
```

A class can model an entity with both data and behavior:

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")
```

A program can use both:

```python
students = [
    Student("Ali"),
    Student("Sara"),
    Student("Hamza")
]
```

The list organizes multiple objects, while each object models an individual student's state and behavior.

This combination is common in real software.

---

## OOP and Software Design

OOP becomes more valuable when thinking about **responsibilities**.

Suppose an application contains:

```text
User
Order
Payment
Product
Invoice
```

A good design should determine:

* What responsibility belongs to each object?
* Which object owns each piece of state?
* Which operations should each object provide?
* Which objects need to communicate?
* Which relationships are inheritance relationships?
* Which relationships are composition or dependency relationships?

This is more important than simply knowing how to write:

```python
class MyClass:
    pass
```

The syntax is easy.

The design decisions are the difficult part.

---

## Cohesion

Cohesion describes how closely related the responsibilities within a component are.

Consider:

```python
class User:
    def create_account(self):
        pass

    def reset_password(self):
        pass

    def calculate_invoice_tax(self):
        pass

    def resize_image(self):
        pass
```

This class has unrelated responsibilities.

A better design may separate them into focused components.

High cohesion generally means that a class has a clear, related purpose.

---

## Coupling

Coupling describes dependencies between components.

If one class depends heavily on the internal implementation details of many other classes, changing one part of the system can cause changes throughout the application.

A useful design goal is to reduce unnecessary coupling while keeping the required relationships explicit.

This does not mean eliminating all dependencies.

Software components must communicate.

The objective is to create **manageable dependencies**.

---

## Advantages of OOP

When applied appropriately, OOP can provide several benefits.

### Organization

Related state and behavior can be grouped together.

### Reusability

A class can be instantiated multiple times.

### Maintainability

Well-designed classes can isolate responsibilities and reduce unnecessary changes across a codebase.

### Extensibility

Inheritance, composition, and polymorphism can support extending existing systems.

### Abstraction

Classes can provide meaningful interfaces over complex implementation details.

### Modeling

Classes can represent entities and relationships found in the problem domain.

These benefits depend on design quality. Poorly designed classes can make software more complicated rather than less complicated.

---

## Limitations of OOP

OOP also has potential disadvantages.

### Unnecessary Complexity

A simple problem can become unnecessarily complicated if classes are introduced without a clear reason.

### Excessive Abstraction

Too many layers of classes and abstractions can make code difficult to understand.

### Inappropriate Inheritance

Deep or poorly designed inheritance hierarchies can create tight coupling and fragile behavior.

### More Indirection

Object-oriented systems may require developers to navigate through several objects and methods to understand what happens.

### Overengineering

A small script does not necessarily need an elaborate object model.

Professional programming requires recognizing when OOP helps and when it does not.

---

## OOP in Python

Python's object model is broader than user-defined classes.

For example:

```python
number = 10
text = "Python"
items = [1, 2, 3]
```

These values are all objects.

They have types:

```python
print(type(number))
print(type(text))
print(type(items))
```

They also provide behavior through methods where applicable:

```python
text.upper()
items.append(4)
```

This means that object-oriented concepts are present throughout ordinary Python programming.

When you use:

```python
"python".upper()
```

you are already interacting with an object's behavior.

When you use:

```python
items.append(4)
```

you are calling a method on a list object.

OOP therefore becomes a deeper understanding of concepts that are already present in Python.

---

## OOP in AI and Machine Learning

OOP is particularly relevant when working with large Python libraries used in AI and machine learning.

A framework may represent a model as an object:

```python
model = Model()
```

The model may contain:

```text
State:
- parameters
- configuration
- learned values

Behavior:
- train()
- predict()
- evaluate()
```

A dataset object may contain:

```text
State:
- samples
- labels
- metadata

Behavior:
- load()
- transform()
- access()
```

A pipeline may combine several components:

```text
Pipeline
├── Preprocessor
├── Model
└── Evaluator
```

These designs rely heavily on the OOP concepts introduced in this module.

You will encounter similar structures when working with machine-learning and deep-learning libraries.

---

## A Practical Mental Model

When analyzing an object-oriented program, ask these questions:

### 1. What objects exist?

Identify the important entities.

```text
User
Order
Product
Payment
```

### 2. What state does each object own?

Identify the data associated with each entity.

```text
User
├── name
└── email
```

### 3. What behavior belongs to each object?

Identify operations related to that state.

```text
User
├── update_profile()
└── change_password()
```

### 4. How do objects interact?

Determine which objects communicate with one another.

```text
Order → Product
Order → Payment
```

### 5. Which relationships are inheritance?

Look for genuine subtype relationships.

```text
Animal
├── Dog
└── Cat
```

### 6. Which relationships are composition?

Look for objects that contain or use other objects.

```text
Car
└── Engine
```

### 7. Is a class actually necessary?

Before creating a class, consider whether a function or data structure would provide a simpler abstraction.

This reasoning process is more important than memorizing OOP terminology.

---

## Common Misconceptions

### Misconception 1: A class and object are the same thing.

They are not.

A class defines a type; an object is an instance of that type.

---

### Misconception 2: `self` is a keyword.

It is not.

`self` is the conventional name for the first parameter of an instance method.

---

### Misconception 3: `__init__()` creates the object.

Not precisely.

Object creation and initialization are separate stages. `__new__()` is responsible for creating the instance, while `__init__()` initializes it.

---

### Misconception 4: A leading underscore makes an attribute private.

It does not.

```python
self._value
```

is a naming convention indicating non-public intent.

---

### Misconception 5: Double underscores provide absolute privacy.

They do not.

```python
self.__value
```

uses name mangling to reduce accidental name conflicts.

It is not a security mechanism.

---

### Misconception 6: Inheritance is always better than composition.

Incorrect.

Inheritance should represent an appropriate subtype relationship. Composition is often a better solution when objects simply contain or use other objects.

---

### Misconception 7: Polymorphism requires inheritance.

Incorrect.

Python's duck typing allows polymorphic behavior without a shared inheritance hierarchy.

---

### Misconception 8: Every Python program should use classes.

Incorrect.

Functions and data structures are often sufficient for simpler problems.

---

## Key Terminology

| Term          | Meaning                                                                                   |
| ------------- | ----------------------------------------------------------------------------------------- |
| Object        | A runtime entity with identity, type, and state/behavior                                  |
| Class         | A user-defined type that describes object structure and behavior                          |
| Instance      | A particular object created from a class                                                  |
| Attribute     | Data or other value associated with an object or class                                    |
| Method        | A function defined as part of a class                                                     |
| State         | Information representing an object's current condition                                    |
| Behavior      | Operations an object can perform                                                          |
| Encapsulation | Organizing state and behavior behind an interface and controlling implementation exposure |
| Inheritance   | Deriving one class from another                                                           |
| Polymorphism  | Using different object types through compatible operations or interfaces                  |
| Duck typing   | Relying on supported behavior rather than exact type                                      |
| Abstraction   | Representing a concept through a useful interface while hiding unnecessary details        |
| Composition   | Building objects using other objects                                                      |
| Cohesion      | How closely related a component's responsibilities are                                    |
| Coupling      | The degree of dependency between components                                               |

---

## Summary

Object-Oriented Programming provides a way to structure software around objects that combine **state and behavior**.

The foundational concepts are:

```text
OOP
│
├── Classes
├── Objects
├── State
├── Behavior
├── Attributes
├── Methods
├── Encapsulation
├── Inheritance
├── Polymorphism
├── Abstraction
└── Composition
```

The most important lesson is not the syntax for creating a class.

The deeper question is:

> **What responsibilities should this software component own, and what is the simplest useful abstraction for those responsibilities?**

A well-designed object-oriented system should improve organization and maintainability rather than simply increase the number of classes.

As you progress through this module, you will learn each OOP mechanism individually and then combine them to design practical Python applications.
