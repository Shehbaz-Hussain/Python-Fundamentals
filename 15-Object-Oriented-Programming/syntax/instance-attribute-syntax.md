Instance Attribute Syntax

Introduction

An instance attribute is an attribute that belongs to a specific object of a class.

Instance attributes are used to store data that can be different for each object.

They are commonly created inside the "__init__()" method using the "self" parameter.

---

Basic Syntax

class ClassName:
    def __init__(self, value):
        self.attribute_name = value

Syntax Breakdown

- "class ClassName:" defines the class.
- "__init__()" initializes the object.
- "self" refers to the current object.
- "attribute_name" is the name of the instance attribute.
- "value" is assigned to the instance attribute.

---

Example

class Student:
    def __init__(self, name):
        self.name = name


student1 = Student("Shehbaz")

print(student1.name)

Output:

Shehbaz

Here, "name" is an instance attribute.

The statement:

self.name = name

stores the value provided during object creation in the current object.

---

Using Multiple Instance Attributes

A class can have multiple instance attributes.

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

The object now contains two instance attributes:

- "name"
- "age"

---

Creating Different Values for Different Objects

Each object can have different values for its instance attributes.

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

Both objects have a "name" attribute, but each object stores its own value.

---

Accessing Instance Attributes

Instance attributes are accessed using dot notation.

Syntax

object_name.attribute_name

Example

class Student:
    def __init__(self, name):
        self.name = name


student1 = Student("Shehbaz")

print(student1.name)

Output:

Shehbaz

---

Modifying an Instance Attribute

An instance attribute can be modified after the object has been created.

class Student:
    def __init__(self, name):
        self.name = name


student1 = Student("Shehbaz")

student1.name = "Ali"

print(student1.name)

Output:

Ali

The assignment:

student1.name = "Ali"

changes the "name" attribute of "student1".

---

Instance Attributes Are Independent

Instance attributes belong to individual objects.

Changing an attribute of one object does not automatically change the corresponding attribute of another object.

class Student:
    def __init__(self, name):
        self.name = name


student1 = Student("Shehbaz")
student2 = Student("Ali")

student1.name = "Ahmed"

print(student1.name)
print(student2.name)

Output:

Ahmed
Ali

Only "student1.name" was changed.

---

Instance Attribute Created Outside "__init__()"

Python also allows an instance attribute to be created directly through an object.

class Student:
    pass


student1 = Student()

student1.name = "Shehbaz"

print(student1.name)

Output:

Shehbaz

However, when an attribute is part of the normal state of every object, it is generally better to initialize it inside "__init__()".

---

Using Instance Attributes in Methods

Instance methods can access instance attributes using "self".

class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


student1 = Student("Shehbaz")

student1.introduce()

Output:

My name is Shehbaz

Here, "self.name" refers to the "name" attribute belonging to the current object.

---

"self" and Instance Attributes

Consider the following code:

class Student:
    def __init__(self, name):
        self.name = name

The parameter "name" and the instance attribute "self.name" are different things.

When this object is created:

student1 = Student("Shehbaz")

the value ""Shehbaz"" is passed to the parameter "name".

Then:

self.name = name

stores that value in the current object's "name" attribute.

Conceptually:

name              → local parameter
self.name         → instance attribute

---

Instance Attributes with Different Data Types

Instance attributes can store values of different data types.

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

The attributes can contain values such as strings, integers, booleans, and other Python objects.

---

General Syntax

The general pattern for creating instance attributes is:

class ClassName:
    def __init__(self, parameter):
        self.attribute = parameter

For multiple attributes:

class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2

---

Important Points

- An instance attribute belongs to a specific object.
- Instance attributes are commonly created inside "__init__()".
- "self" refers to the current instance.
- Instance attributes are accessed using dot notation.
- Different objects can have different values for the same instance attribute.
- Changing an instance attribute normally affects only that particular object.
- Instance attributes can be modified after object creation.
- Instance methods can access instance attributes through "self".
- Attributes that represent an object's individual state are commonly implemented as instance attributes.

---

Summary

The basic syntax for an instance attribute is:

class ClassName:
    def __init__(self, value):
        self.attribute_name = value

For example:

class Student:
    def __init__(self, name):
        self.name = name

Each object created from the class can then have its own value:

student1 = Student("Shehbaz")
student2 = Student("Ali")

Therefore, instance attributes are the primary mechanism for storing object-specific state in Python classes.