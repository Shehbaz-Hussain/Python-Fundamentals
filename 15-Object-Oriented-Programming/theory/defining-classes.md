# Defining Classes

A class is a user-defined Python type that describes the structure and behavior of its instances.

Defining a class is one of the first practical steps in object-oriented programming. However, professional OOP requires more than knowing the `class` keyword. You must understand what belongs inside a class, how class definitions are executed, how methods are declared, and how class design affects maintainability.

---

## 1. Basic Class Syntax

A class is defined using the `class` statement:

```python
class ClassName:
    pass
```

For example:

```python
class Student:
    pass
```

Here:

* `class` is the Python keyword.
* `Student` is the class name.
* `:` begins the class body.
* `pass` provides an empty statement so the class can have an empty body.

Python conventionally uses **PascalCase** for class names:

```python
class BankAccount:
    pass


class MachineLearningModel:
    pass
```

PEP 8 recommends CapWords-style naming for classes.

---

## 2. The Class Body

The indented block after the `class` statement is the class body.

It can contain:

* Methods
* Class attributes
* Documentation strings
* Nested definitions
* Other executable statements

Example:

```python
class Student:
    school = "ABC School"

    def introduce(self):
        print("Hello")
```

The class body defines information and behavior associated with the class.

---

## 3. Classes Are Executed When Defined

One important Python detail is that a class definition is executable code.

For example:

```python
class Student:
    print("Class body executed")
```

When Python executes this definition, the statement inside the class body runs.

Output:

```text
Class body executed
```

This differs from the body of a method.

A method body does not execute merely because the class is defined:

```python
class Student:
    def introduce(self):
        print("Hello")
```

The `print()` executes when the method is called:

```python
student = Student()
student.introduce()
```

This distinction becomes important when understanding Python's class creation process.

---

## 4. A Class Creates a Class Object

After Python executes:

```python
class Student:
    pass
```

the name `Student` refers to a class object.

You can inspect it:

```python
print(Student)
print(type(Student))
```

The class itself is an object.

Typically:

```text
Student
   ↓
class object
   ↓
instance of type
```

This is part of Python's object model.

You do not need to study metaclasses to use ordinary classes, but understanding that classes themselves are objects helps explain Python's flexibility.

---

## 5. Defining a Class with a Method

A class can contain methods.

```python
class Student:
    def introduce(self):
        print("I am a student.")
```

The method is defined inside the class body.

To use it:

```python
student = Student()
student.introduce()
```

Output:

```text
I am a student.
```

The method receives the current object through `self`.

---

## 6. The `self` Parameter

Instance methods normally define the current instance as their first parameter.

By convention, that parameter is called `self`.

```python
class Student:
    def introduce(self):
        print("I am a student.")
```

When called:

```python
student = Student()
student.introduce()
```

Python binds `student` to the method's first parameter.

Conceptually:

```python
Student.introduce(student)
```

This is why `self` is required in an ordinary instance method.

---

## 7. `self` Is a Convention, Not a Keyword

Python does not reserve `self` as a keyword.

Technically, this is possible:

```python
class Student:
    def introduce(current_student):
        print("I am a student.")
```

The method can be called:

```python
student = Student()
student.introduce()
```

However, this is poor style.

The standard convention is:

```python
class Student:
    def introduce(self):
        print("I am a student.")
```

Always use `self` for the first parameter of an instance method unless there is a highly unusual reason not to.

---

## 8. Defining Instance Attributes

Instance attributes are usually created in `__init__()`.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

When an object is created:

```python
student = Student("Ali", 20)
```

the instance receives:

```text
name → "Ali"
age  → 20
```

The expression:

```python
self.name = name
```

means:

* `name` on the right is the parameter.
* `self.name` on the left is an attribute of the current instance.

This distinction is fundamental.

---

## 9. Parameters and Attributes Are Different

Consider:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

There are two different identifiers:

```text
name
```

and:

```text
self.name
```

The parameter:

```python
name
```

exists during the method call.

The attribute:

```python
self.name
```

is stored on the object.

Therefore:

```python
student = Student("Ali")
```

results in the object retaining:

```text
student.name → "Ali"
```

after `__init__()` finishes.

---

## 10. Defining Multiple Attributes

A class can initialize multiple pieces of state:

```python
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
```

Create an instance:

```python
product = Product("Keyboard", 50, "Electronics")
```

The object now has:

```text
product
├── name     → "Keyboard"
├── price    → 50
└── category → "Electronics"
```

This is a common pattern for modeling entities.

---

## 11. Defining Methods That Use State

Methods can read instance attributes through `self`.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")
```

Create an object:

```python
student = Student("Ali")
student.introduce()
```

Output:

```text
My name is Ali.
```

The method accesses the state of the specific object through `self`.

---

## 12. Defining Methods That Modify State

Methods can also modify instance state.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

Create:

```python
account = BankAccount(1000)
```

Then:

```python
account.deposit(250)
```

The state becomes:

```text
balance → 1250
```

The method provides controlled behavior for changing the object's state.

---

## 13. Defining Methods with Parameters

Instance methods can accept additional parameters after `self`.

```python
class Calculator:
    def add(self, a, b):
        return a + b
```

Calling:

```python
calculator = Calculator()

result = calculator.add(10, 20)

print(result)
```

produces:

```text
30
```

The first parameter is the instance:

```text
self
```

Additional parameters represent information required for the operation:

```text
a
b
```

---

## 14. Defining Methods with Return Values

Methods can return values just like ordinary functions.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

Usage:

```python
rectangle = Rectangle(10, 5)

area = rectangle.area()

print(area)
```

Output:

```text
50
```

Methods do not need to print their results.

Returning values often provides greater flexibility because the caller can decide what to do with the result.

---

## 15. Class Attributes

A class can define attributes at class scope.

```python
class Student:
    school = "ABC School"
```

`school` is a class attribute.

It can be accessed through the class:

```python
print(Student.school)
```

It may also be accessible through an instance:

```python
student = Student()

print(student.school)
```

However, instance attribute lookup and class attribute lookup follow Python's attribute-resolution rules. The two concepts should not be treated as identical.

Class attributes are covered in detail in a later theory section.

---

## 16. Class Documentation Strings

A class can have a docstring describing its purpose.

```python
class BankAccount:
    """Represent a bank account with a balance."""
```

The docstring can be inspected:

```python
print(BankAccount.__doc__)
```

Docstrings are useful because they communicate the purpose of the class to developers and documentation tools.

A good class docstring should explain what the class represents and, where useful, its important responsibilities.

---

## 17. Method Documentation Strings

Methods can also have docstrings:

```python
class Calculator:
    def add(self, a, b):
        """Return the sum of two numbers."""
        return a + b
```

This documents the method's purpose.

For public classes and methods, clear documentation becomes increasingly important as the project grows.

---

## 18. Naming Classes

PEP 8 recommends CapWords-style names for classes.

Preferred:

```python
class BankAccount:
    pass


class MachineLearningModel:
    pass


class DataProcessor:
    pass
```

Avoid unclear names:

```python
class bankaccount:
    pass
```

or:

```python
class my_class:
    pass
```

The conventional Python style is:

```text
BankAccount
DataProcessor
MachineLearningModel
```

Method and attribute names normally use `snake_case`:

```python
class BankAccount:
    def check_balance(self):
        pass
```

---

## 19. Class Names Should Describe Concepts

A class name should communicate what the object represents.

Good:

```python
class Customer:
    pass


class Invoice:
    pass


class NeuralNetwork:
    pass
```

Poor:

```python
class Thing:
    pass


class DataStuff:
    pass
```

The purpose of a class should be understandable from its name whenever possible.

---

## 20. Defining a Class with Multiple Methods

A class can provide several related behaviors.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(self.balance)
```

All three methods relate to the bank account's responsibilities.

This is preferable to placing unrelated functionality inside the same class.

---

## 21. Class Responsibilities

A class should have a coherent responsibility.

For example:

```python
class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32
```

This class has a clear responsibility.

A poorly designed class might combine unrelated concerns:

```python
class Everything:
    def calculate_tax(self):
        pass

    def resize_image(self):
        pass

    def send_email(self):
        pass

    def train_model(self):
        pass
```

Technically, Python can execute such code.

Architecturally, it is difficult to justify the class as a coherent abstraction.

Good OOP design is concerned with responsibility, not merely syntax.

---

## 22. Empty Classes

An empty class can be useful in limited situations.

```python
class Student:
    pass
```

This creates a valid type without custom behavior.

An object can then be created:

```python
student = Student()
```

Attributes can technically be added dynamically:

```python
student.name = "Ali"
```

However, if the object's expected state is known in advance, explicitly initializing it through `__init__()` is usually clearer.

---

## 23. Using `pass`

`pass` is a statement that does nothing.

It can be used when a syntactically valid block is required but no implementation is currently provided.

Example:

```python
class Student:
    pass
```

It can also appear in methods:

```python
class Student:
    def study(self):
        pass
```

This can be useful for placeholders during early development, but production code should normally replace placeholders with meaningful implementations.

---

## 24. Defining Methods in the Correct Scope

Methods must be indented inside the class body.

Correct:

```python
class Student:
    def introduce(self):
        print("Hello")
```

Incorrect:

```python
class Student:
def introduce(self):
    print("Hello")
```

Python's indentation is syntactically meaningful.

The method must belong to the class's indented block.

---

## 25. Defining Multiple Classes

A Python module can contain multiple classes.

```python
class Student:
    pass


class Teacher:
    pass
```

This is valid.

However, classes should generally be grouped in a module when they have a meaningful relationship or belong to the same conceptual area.

If a file becomes too large, classes can be separated into modules.

---

## 26. Classes and Modules

A module is a Python file.

A module can contain one or more classes.

For example:

```text
school.py
```

could contain:

```python
class Student:
    pass


class Teacher:
    pass
```

Another module can import them:

```python
from school import Student, Teacher
```

This allows larger applications to organize related classes across multiple files.

Module organization becomes especially important in professional software projects.

---

## 27. Defining a Class Does Not Create an Instance

Consider:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

At this point, no `Student` instance has been created merely because the class exists.

An instance is created with:

```python
student = Student("Ali")
```

Conceptually:

```text
Class definition
      ↓
Student
      ↓
Student("Ali")
      ↓
Instance
```

This distinction is fundamental.

---

## 28. Class Definition vs Class Call

These two operations are different:

### Defining the class

```python
class Student:
    pass
```

### Calling the class

```python
student = Student()
```

The first creates the class object.

The second invokes the class object to create an instance.

For ordinary Python classes, the process involves `type` and object creation machinery, but you do not need to understand those internals to use classes effectively.

---

## 29. Defining a Class with Default Values

Methods can use default parameter values just like ordinary functions.

```python
class Student:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
```

Now:

```python
student1 = Student("Ali")
student2 = Student("Sara", 21)
```

The resulting states are:

```text
student1
├── name → "Ali"
└── age  → 18

student2
├── name → "Sara"
└── age  → 21
```

The same rules for default arguments that you learned with functions apply here.

---

## 30. Defining Methods That Call Other Methods

Methods can call other methods through `self`.

```python
class Student:
    def introduce(self):
        print("I am a student.")

    def welcome(self):
        self.introduce()
        print("Welcome.")
```

Calling:

```python
student = Student()
student.welcome()
```

causes `welcome()` to invoke `introduce()` on the same instance.

The expression:

```python
self.introduce()
```

means that the current object should execute its `introduce()` method.

---

## 31. Defining Properties Through Methods

At this stage, avoid overcomplicating class design.

If an attribute is simple state:

```python
self.name = name
```

that is often sufficient.

More advanced mechanisms such as `@property` can provide controlled attribute-style access to computed or validated values.

For example:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2
```

Then:

```python
circle = Circle(5)

print(circle.area)
```

This is useful, but properties are not required for every attribute.

They will become more relevant when discussing encapsulation and interface design.

---

## 32. Defining Classes for AI/ML Concepts

Classes can represent concepts commonly found in AI and machine-learning systems.

For example:

```python
class Model:
    def __init__(self, name):
        self.name = name

    def predict(self, data):
        print(f"Running {self.name} prediction.")
```

An instance:

```python
model = Model("Classifier")
```

can then expose behavior:

```python
model.predict(data)
```

Real ML frameworks are much more complex, but the design pattern is familiar:

```text
Model
├── State
│   └── configuration / parameters
│
└── Behavior
    └── predict()
```

This is one reason OOP is important for AI engineering.

---

## 33. Good Class Design Guidelines

When defining a class, ask:

### 1. What does the class represent?

The answer should be concrete.

### 2. What state should the object own?

Identify the attributes that belong to each instance.

### 3. What behavior belongs to the object?

Identify operations that naturally operate on that state.

### 4. Are the responsibilities related?

Avoid unrelated functionality.

### 5. Is a class actually necessary?

A function or data structure may sometimes be simpler.

### 6. Can another developer understand the class?

Clear naming and focused responsibilities matter.

---

## 34. A Complete Example

Consider a simple product class:

```python
class Product:
    """Represent a product with a name and price."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name}: ${self.price}")

    def apply_discount(self, percentage):
        self.price -= self.price * percentage / 100
```

Create an object:

```python
product = Product("Keyboard", 100)
```

Display it:

```python
product.display()
```

Apply a discount:

```python
product.apply_discount(10)
```

Display the updated state:

```python
product.display()
```

The class provides:

```text
Product
├── State
│   ├── name
│   └── price
│
└── Behavior
    ├── display()
    └── apply_discount()
```

The class has a coherent responsibility: representing a product and its related operations.

---

## 35. Common Errors

### Error 1: Incorrect indentation

```python
class Student:
def introduce(self):
    print("Hello")
```

Correct:

```python
class Student:
    def introduce(self):
        print("Hello")
```

---

### Error 2: Forgetting `self`

Incorrect:

```python
class Student:
    def introduce():
        print("Hello")
```

Correct:

```python
class Student:
    def introduce(self):
        print("Hello")
```

---

### Error 3: Confusing parameters and attributes

Incorrect reasoning:

```python
class Student:
    def __init__(self, name):
        name = name
```

This does not store the value on the instance.

Correct:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

---

### Error 4: Putting unrelated responsibilities into one class

Avoid classes that become general-purpose containers for unrelated functions.

Prefer focused responsibilities.

---

### Error 5: Creating classes unnecessarily

Not every small operation requires a class.

If this is sufficient:

```python
def square(number):
    return number ** 2
```

there is no obvious reason to replace it with:

```python
class MathUtility:
    def square(self, number):
        return number ** 2
```

The second design adds object-management overhead without providing meaningful state or abstraction.

---

## 36. Summary

Defining a class involves more than writing:

```python
class ClassName:
    pass
```

A useful class should define a coherent concept with appropriate state and behavior.

Important points:

* Use the `class` statement to define a class.
* Class names conventionally use CapWords.
* The class body is executable during class definition.
* Classes themselves are objects.
* Instance methods conventionally use `self`.
* Instance state is commonly initialized in `__init__()`.
* `self.attribute` refers to state associated with the current instance.
* Methods can read and modify instance state.
* Class attributes belong to the class.
* Docstrings can document classes and methods.
* A module can contain multiple related classes.
* Classes should have focused responsibilities.
* A class should not be created merely because OOP syntax is available.
* Functions and data structures remain appropriate tools for many problems.

A useful design model is:

```text
Class
│
├── What does it represent?
│
├── What state does it own?
│
├── What behavior does it provide?
│
└── Why should this be a class?
```

These questions form the foundation for the more advanced OOP concepts that follow.
