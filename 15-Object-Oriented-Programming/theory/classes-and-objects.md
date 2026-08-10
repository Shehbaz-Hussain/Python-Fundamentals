# Classes and Objects

Classes and objects are the foundational building blocks of object-oriented programming in Python.

A **class** defines a type and describes the structure and behavior that its instances can provide.

An **object** is a particular instance of a class.

Understanding this distinction is essential because most other OOP concepts—attributes, methods, inheritance, polymorphism, and composition—build upon it.

---

## 1. What Is a Class?

A class is a user-defined type created using the `class` statement.

At a conceptual level, a class can define:

* What data its objects can contain.
* What operations its objects can perform.
* How objects of that type behave.

A minimal class looks like this:

```python id="6i2yqo"
class Student:
    pass
```

Here:

```text id="9n1xwg"
Student
   ↓
Class
```

The class exists as a Python object representing the `Student` type.

The `pass` statement means that the class currently has no custom body.

Although this class is minimal, it can still be used to create objects.

---

## 2. What Is an Object?

An object is a particular instance of a class.

Using the previous class:

```python id="x3zqfd"
class Student:
    pass

student = Student()
```

The relationship is:

```text id="2z7z5r"
Student
   │
   └── student
        ↓
      object
```

More precisely:

* `Student` is a class.
* `student` refers to an object.
* The object is an instance of `Student`.

We can verify its type:

```python id="j2e5jo"
print(type(student))
```

The result will identify the object as an instance of `Student`.

---

## 3. Class vs Object

The distinction can be summarized as follows:

| Class                               | Object                         |
| ----------------------------------- | ------------------------------ |
| Defines a type                      | Is an instance of a type       |
| Describes structure and behavior    | Contains actual runtime state  |
| Used to create instances            | Created from a class           |
| Acts as a blueprint-like definition | Represents a particular entity |

Consider:

```python id="d6z0di"
class Car:
    pass

car1 = Car()
car2 = Car()
```

There is one class:

```text id="d6q1c8"
Car
```

and two separate objects:

```text id="g0b8xe"
car1 → Car instance
car2 → Car instance
```

The objects have the same type but are different instances.

---

## 4. Creating Multiple Objects

A major advantage of classes is that one class can be used to create many objects.

```python id="h9v1ba"
class Student:
    pass

student1 = Student()
student2 = Student()
student3 = Student()
```

Conceptually:

```text id="u2m9au"
             Student
                │
       ┌────────┼────────┐
       ↓        ↓        ↓
   student1  student2  student3
```

Each object is a separate instance.

This allows one class definition to represent many entities of the same general type.

---

## 5. Objects Have Identity

Every object has an identity.

The built-in `id()` function returns an integer identifying the object during its lifetime.

```python id="c7q2ac"
class Student:
    pass

student1 = Student()
student2 = Student()

print(id(student1))
print(id(student2))
```

The values will normally be different because the objects are distinct.

Do not treat the value returned by `id()` as a permanent identifier for application data.

Its purpose is to identify an object during its lifetime within the Python implementation.

---

## 6. Identity vs Equality

Object identity and equality are different concepts.

Consider:

```python id="bdz7mu"
class Student:
    pass

student1 = Student()
student2 = Student()

print(student1 is student2)
print(student1 == student2)
```

The first expression tests whether both variables refer to the exact same object.

```python id="8n0g9b"
student1 is student2
```

The result is:

```text id="pl4qsy"
False
```

By default, two separate instances of a user-defined class are also not equal unless the class provides different equality behavior.

The important distinction is:

```text id="4gh6rj"
is
↓
identity

==
↓
equality
```

Do not use `is` as a general replacement for `==`.

---

## 7. Variables Refer to Objects

A variable in Python does not contain an object in the simplistic sense often used in introductory explanations.

Instead, a variable name is bound to an object.

For example:

```python id="tq0ex0"
class Student:
    pass

student = Student()
```

Conceptually:

```text id="f9m2xe"
student
   │
   ↓
Student object
```

The name `student` refers to the object.

This distinction becomes important when working with multiple references to the same object.

---

## 8. Multiple References to the Same Object

Consider:

```python id="z8u5f5"
class Student:
    pass

student1 = Student()
student2 = student1
```

Now:

```text id="5x5w0q"
student1 ──┐
           ↓
       Student object
           ↑
student2 ──┘
```

Both names refer to the same object.

Therefore:

```python id="3vl9ez"
print(student1 is student2)
```

produces:

```text id="l5g6rc"
True
```

This is fundamentally different from:

```python id="3jhj5q"
student1 = Student()
student2 = Student()
```

which creates two separate objects.

---

## 9. Classes Define Behavior

A class can define methods that represent behavior.

```python id="plj03d"
class Dog:
    def bark(self):
        print("Woof!")
```

An object can use that behavior:

```python id="5v3hlf"
dog = Dog()
dog.bark()
```

Output:

```text id="0dx4s4"
Woof!
```

The class defines the method.

The object invokes the method.

---

## 10. Classes Define Object State

Classes can also define how object state is initialized.

```python id="h1ot5p"
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Now:

```python id="kz8g5j"
student = Student("Ali", 20)
```

The object contains:

```text id="h1xq4c"
student
├── name → "Ali"
└── age  → 20
```

The values are associated with that particular object.

---

## 11. Different Objects Can Have Different State

Consider:

```python id="b9r3mz"
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Ali", 20)
student2 = Student("Sara", 22)
```

The objects have the same type:

```text id="v0nqgz"
student1 → Student
student2 → Student
```

but different state:

```text id="v9b7ay"
student1
├── name → "Ali"
└── age  → 20

student2
├── name → "Sara"
└── age  → 22
```

This is one of the primary reasons classes are useful.

A single class can describe a general type while individual instances maintain different values.

---

## 12. Objects Can Have Behavior Based on Their State

Methods can operate on instance state.

```python id="y2ghs9"
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

Create an object:

```python id="3skp6h"
account = BankAccount(1000)
```

Then:

```python id="4f1s78"
account.deposit(500)
```

The object's state changes:

```text id="h7frq2"
Before:
balance → 1000

After:
balance → 1500
```

The method provides behavior that operates on the object's own state.

---

## 13. The `self` Parameter

Instance methods normally receive the current instance through their first parameter.

By convention, that parameter is named `self`.

```python id="6opg89"
class Student:
    def introduce(self):
        print("I am a student.")
```

When:

```python id="3svq7q"
student = Student()
student.introduce()
```

is called, Python effectively supplies the instance as the first argument.

Conceptually, this:

```python id="sp9fxb"
student.introduce()
```

is closely related to:

```python id="e2j4hy"
Student.introduce(student)
```

The second form demonstrates the underlying argument relationship.

The exact mechanics involve Python's method binding behavior, but this model is useful for understanding why `self` exists.

---

## 14. Accessing Object Attributes

Attributes can be accessed using dot notation.

```python id="h8ud8s"
class Student:
    def __init__(self, name):
        self.name = name

student = Student("Ali")

print(student.name)
```

Output:

```text id="o6l1mg"
Ali
```

The expression:

```python id="6m7c0e"
student.name
```

asks Python to retrieve the `name` attribute associated with that object.

---

## 15. Modifying Object Attributes

Object attributes can be reassigned.

```python id="7ivn8j"
class Student:
    def __init__(self, name):
        self.name = name

student = Student("Ali")

student.name = "Sara"

print(student.name)
```

Output:

```text id="6n4azc"
Sara
```

The object's state has changed.

This direct modification is possible in Python unless the class design provides mechanisms or conventions that discourage or prevent particular forms of modification.

---

## 16. Adding Attributes Dynamically

Python objects can sometimes receive new attributes after creation.

For example:

```python id="by0yqc"
class Student:
    pass

student = Student()

student.name = "Ali"
student.age = 20
```

The object now has those attributes.

This demonstrates Python's dynamic nature.

However, the ability to dynamically add attributes does not mean that arbitrary attributes should be added throughout an application.

A well-designed class should generally establish its expected state clearly.

For example:

```python id="r4j6x7"
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

This makes the intended object structure easier to understand.

---

## 17. Methods Belong to Classes

Methods are functions defined inside a class.

```python id="2v5vwu"
class Calculator:
    def add(self, a, b):
        return a + b
```

The method is defined once as part of the class.

Different instances can use that same method definition:

```python id="b3vv2g"
calculator1 = Calculator()
calculator2 = Calculator()

print(calculator1.add(2, 3))
print(calculator2.add(10, 20))
```

The method behavior is defined by the class, while the call operates through a particular instance.

---

## 18. Objects Can Interact

Real applications often contain multiple objects that communicate with one another.

For example:

```python id="t5s9av"
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
```

Now:

```python id="9e4xqg"
car = Car()
car.start()
```

The `Car` object delegates part of its behavior to its `Engine` object.

Conceptually:

```text id="8a3j8e"
Car
 │
 └── Engine
       │
       └── start()
```

This is an example of **composition**, which will be covered in greater detail later.

---

## 19. Objects Are Everywhere in Python

OOP is not limited to user-defined classes.

Python's built-in values are objects.

For example:

```python id="u2ml5f"
number = 10
text = "Python"
items = [1, 2, 3]
```

These objects have types:

```python id="2r8n5f"
print(type(number))
print(type(text))
print(type(items))
```

They also provide behavior.

For example:

```python id="x83zj1"
text.upper()
```

and:

```python id="1bq6px"
items.append(4)
```

Both involve calling methods on objects.

This is why understanding classes and objects helps explain ordinary Python code.

---

## 20. Built-in Types Are Objects

Consider an integer:

```python id="axj1h6"
number = 42
```

The value `42` is an object.

Its type is:

```python id="h4qv5f"
print(type(number))
```

which identifies `int`.

Strings are also objects:

```python id="b7a3u9"
text = "hello"

print(type(text))
```

Lists are objects:

```python id="l8y8ly"
items = [1, 2, 3]

print(type(items))
```

Therefore, the class/object model is not limited to classes you write yourself.

---

## 21. Objects Have Attributes and Methods

A useful conceptual distinction is:

### Attributes

Attributes provide information associated with an object.

```python id="7u1gpg"
student.name
```

### Methods

Methods provide behavior.

```python id="k9mb5x"
student.introduce()
```

The distinction is not always perfectly represented by a simple data-versus-function rule because Python's attribute system is more general than that.

Still, for introductory OOP, this distinction provides a useful mental model:

```text id="d1j0l7"
Object
├── Attributes → state/data
└── Methods    → behavior/operations
```

---

## 22. A Complete Basic Example

Consider the following class:

```python id="6q0b9g"
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")
```

Create two objects:

```python id="4z8f2m"
student1 = Student("Ali", 20)
student2 = Student("Sara", 22)
```

Each object has independent state:

```text id="t0v5bx"
student1
├── name → "Ali"
└── age  → 20

student2
├── name → "Sara"
└── age  → 22
```

Each can invoke the same method:

```python id="t6i6fh"
student1.introduce()
student2.introduce()
```

The method definition is shared through the class, but each call operates using the state of the particular instance.

---

## 23. Class-Level Definition vs Instance-Level State

A useful distinction is:

```text id="a9m1xx"
Class
├── Defines behavior
├── Defines structure
└── Can contain class-level attributes

Instance
├── Has its own state
└── Uses behavior defined by its class
```

For example:

```python id="5zz3v4"
class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name
```

Here:

```text id="a5zvqe"
Dog
└── species → "Canis familiaris"

dog
└── name → "Max"
```

The `species` attribute is class-level, while `name` is instance-specific.

Class attributes will be discussed separately later.

---

## 24. Object Creation Is a Runtime Operation

A class definition does not automatically create instances.

For example:

```python id="4ce5or"
class Student:
    pass
```

This defines the class.

An instance is created only when the class is called:

```python id="y8l5p4"
student = Student()
```

Conceptually:

```text id="k4m5qp"
class Student:
        │
        │ call
        ↓
Student()
        │
        ↓
new instance
```

This distinction becomes important when learning constructors, initialization, and object lifecycle.

---

## 25. Why Multiple Objects Matter

Suppose an application needs to represent 1,000 students.

Creating separate variables manually would be difficult to manage.

Instead, one class can describe the student type:

```python id="n5q6uc"
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Then many instances can be created:

```python id="z3q8sh"
student1 = Student("Ali", 20)
student2 = Student("Sara", 21)
student3 = Student("Hamza", 19)
```

A data structure such as a list can then organize those objects:

```python id="2yx9ju"
students = [student1, student2, student3]
```

This demonstrates how OOP and Python's built-in data structures can work together.

---

## 26. Classes Model Concepts

A class should ideally represent a meaningful concept in the problem domain or software design.

Examples include:

```text id="6c4t3d"
BankAccount
Student
Product
Order
Customer
File
Model
Dataset
Pipeline
```

The important question is not:

> "Can I make this a class?"

The better question is:

> "Does representing this concept as an object make the program easier to understand, maintain, or extend?"

This distinction helps prevent unnecessary object-oriented complexity.

---

## 27. Common Beginner Errors

### Error 1: Confusing a class with an object

Incorrect:

```text
Student and student are the same thing.
```

Correct:

```text
Student → class
student → instance
```

---

### Error 2: Forgetting parentheses during object creation

```python id="h6g0fl"
student = Student
```

This assigns the class itself to `student`.

It does not create an instance.

To create an instance:

```python id="07y9kn"
student = Student()
```

---

### Error 3: Forgetting `self`

Incorrect:

```python id="y3h1mg"
class Student:
    def introduce():
        print("Hello")
```

Calling:

```python id="5nt5ik"
student.introduce()
```

causes an argument mismatch because the bound instance is supplied automatically.

Correct:

```python id="s1f5p7"
class Student:
    def introduce(self):
        print("Hello")
```

---

### Error 4: Using `is` instead of `==`

Do not generally write:

```python id="x0r6x5"
if student1 is student2:
    ...
```

when you mean to compare values.

`is` checks identity.

`==` checks equality according to the objects' equality semantics.

---

### Error 5: Assuming every object has exactly the same state

Two instances of the same class can have different instance attributes and values.

For example:

```python id="y7m5zi"
student1 = Student("Ali", 20)
student2 = Student("Sara", 22)
```

They share the same class but not the same instance state.

---

## 28. Classes and Objects in AI/ML

Object-oriented programming is heavily used in AI and machine-learning software.

A model can be represented as an object:

```python id="x5f3v2"
class Model:
    def __init__(self, name):
        self.name = name

    def predict(self, data):
        pass
```

Then:

```python id="g9j5ba"
model = Model("Classifier")
```

The model object may eventually contain:

```text id="q0p4n8"
State:
- model parameters
- configuration
- metadata

Behavior:
- train()
- predict()
- evaluate()
```

Real frameworks are much more sophisticated, but the fundamental concept is the same.

Understanding classes and objects therefore provides a foundation for reading machine-learning libraries and frameworks.

---

## 29. A Practical Analysis Example

Consider:

```python id="4m9l5k"
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account = BankAccount("Ali", 1000)
account.deposit(250)
```

Analyze it step by step.

### Class

```python id="7f6n9r"
BankAccount
```

Defines the type.

### Object

```python id="4c9gqb"
account
```

References an instance of `BankAccount`.

### State

```text id="o8z6c4"
owner   → "Ali"
balance → 1250
```

### Behavior

```python id="8s7v2r"
deposit()
```

changes the object's state.

### Relationship

```text id="g2y9sa"
BankAccount
      ↓
   account
      ↓
  state + behavior
```

This is the fundamental pattern that the remainder of the module develops.

---

## Summary

The distinction between classes and objects is foundational to Python OOP.

Remember:

* A **class** defines a type.
* An **object** is an instance of a class.
* Multiple objects can be created from one class.
* Each object can maintain its own state.
* Methods provide behavior associated with a class.
* `self` provides access to the current instance in an instance method.
* Objects have identity and type.
* `is` checks identity, while `==` checks equality.
* Python's built-in values are also objects.
* Classes and data structures can be used together.
* Not every problem requires a class.

The central mental model is:

```text id="h0nq7b"
Class
  │
  ├── defines structure
  ├── defines behavior
  │
  └── creates instances
          │
          ├── object 1 → its own state
          ├── object 2 → its own state
          └── object 3 → its own state
```

Once this distinction is clear, attributes, methods, initialization, inheritance, polymorphism, and composition become much easier to understand.
