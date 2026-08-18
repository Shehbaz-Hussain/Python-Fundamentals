"__init__()" Method Syntax

Introduction

The "__init__()" method is a special method in Python that is commonly used to initialize an object's state when an instance is created.

It is often called the initializer method.

The "__init__()" method allows a class to receive values during object creation and store those values as instance attributes.

---

Basic Syntax

class ClassName:
    def __init__(self):
        # initialization code
        pass

Syntax Breakdown

- "def" defines the method.
- "__init__" is the name of the initializer method.
- "self" refers to the current instance.
- The method body contains the initialization logic.

The name "__init__" contains two underscores before and after "init".

---

Simple Example

class Student:
    def __init__(self):
        print("Student object initialized")


student1 = Student()

Output:

Student object initialized

When "Student()" creates an instance, Python automatically invokes the "__init__()" method for that instance.

---

"__init__()" with a Parameter

The initializer can receive values during object creation.

class Student:
    def __init__(self, name):
        self.name = name


student1 = Student("Shehbaz")

print(student1.name)

Output:

Shehbaz

The value ""Shehbaz"" is passed to the "name" parameter.

The statement:

self.name = name

stores that value in the object's "name" instance attribute.

---

Multiple Parameters

An initializer can accept multiple parameters.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Shehbaz", 21)

print(student1.name)
print(student1.age)

Output:

Shehbaz
21

The object is initialized with two pieces of data:

- "name"
- "age"

---

Creating Multiple Objects

The same initializer is executed for every object created from the class.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Shehbaz", 21)
student2 = Student("Ali", 22)

print(student1.name)
print(student2.name)

Output:

Shehbaz
Ali

Each object receives its own instance attributes.

---

Default Parameter Values

The "__init__()" method can use default parameter values.

class Student:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age


student1 = Student("Shehbaz")

print(student1.name)
print(student1.age)

Output:

Shehbaz
18

The default value "18" is used because an "age" argument was not provided.

---

Providing the Optional Value

The default value can be replaced by providing an argument.

class Student:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age


student1 = Student("Shehbaz", 21)

print(student1.age)

Output:

21

---

"__init__()" and Instance Attributes

One of the most common uses of "__init__()" is initializing instance attributes.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)

Output:

Toyota
Corolla

The initializer establishes the initial state of the object.

---

"__init__()" with Different Data Types

Parameters passed to "__init__()" can represent different types of data.

class Student:
    def __init__(self, name, age, enrolled):
        self.name = name
        self.age = age
        self.enrolled = enrolled


student1 = Student("Shehbaz", 21, True)

print(student1.name)
print(student1.age)
print(student1.enrolled)

Output:

Shehbaz
21
True

---

"__init__()" with Methods

An object can use methods that work with the state initialized by "__init__()".

class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


student1 = Student("Shehbaz")

student1.introduce()

Output:

My name is Shehbaz

The "__init__()" method initializes "self.name", and "introduce()" uses that attribute.

---

Calling "__init__()" Automatically

Normally, you do not call "__init__()" directly.

Instead, create an object:

class Student:
    def __init__(self, name):
        self.name = name


student1 = Student("Shehbaz")

Python handles the normal initialization process automatically.

---

"__init__()" Must Not Return Another Value

The "__init__()" method is expected to return "None".

Correct:

class Student:
    def __init__(self, name):
        self.name = name

Incorrect:

class Student:
    def __init__(self, name):
        self.name = name
        return self.name

The second example raises a "TypeError" when the object is created because "__init__()" must return "None".

---

"__init__()" Is Not the Object-Creation Method

It is important to distinguish object creation from object initialization.

Python's instance creation process involves "__new__()", which creates the instance, followed by "__init__()", which initializes it.

For normal Python programming, the important distinction is:

__new__()  → creates the instance
__init__() → initializes the instance

Most Python developers only need to define "__init__()" for ordinary object initialization.

---

General Syntax

The common pattern is:

class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2

An object can then be created with:

object1 = ClassName(value1, value2)

For example:

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Shehbaz", 21)

print(student1.name)
print(student1.age)

Output:

Shehbaz
21

---

Important Points

- "__init__()" is a special method.
- It is commonly called the initializer method.
- It is automatically invoked during normal instance creation.
- "self" refers to the current instance.
- It is commonly used to initialize instance attributes.
- Values can be passed to "__init__()" during object creation.
- Default parameter values can be used.
- Each object receives its own initialized instance state.
- "__init__()" must return "None".
- "__init__()" initializes an instance; it does not technically create the instance itself.

---

Summary

The basic syntax of "__init__()" is:

class ClassName:
    def __init__(self):
        # initialization code
        pass

With parameters:

class ClassName:
    def __init__(self, parameter):
        self.attribute = parameter

The "__init__()" method is fundamental to Python classes because it provides a standard way to initialize the state of each object when it is created.