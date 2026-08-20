# Class Syntax

## Introduction

A **class** is a blueprint for creating objects in object-oriented programming.

A class defines the structure and behavior that objects created from it can have. It can contain **attributes**, which represent data, and **methods**, which define behavior.

In Python, a class is defined using the `class` keyword.

This file explains the syntax used to define a class and introduces the basic components that can appear inside a class.

---

## Basic Syntax

```python
class ClassName:
    pass
```

### Syntax Breakdown

- `class` is the keyword used to define a class.
- `ClassName` is the name of the class.
- `:` marks the beginning of the class body.
- The indented block contains the class definition.
- `pass` is used when the class does not yet contain any implementation.

---

## Class Naming Convention

Python class names conventionally use **PascalCase**.

```python
class Student:
    pass


class BankAccount:
    pass


class EmployeeRecord:
    pass
```

PascalCase means that each word begins with an uppercase letter without using underscores between words.

Using consistent class naming conventions improves code readability and follows common Python development practices.

---

## Empty Class

A class can initially be defined without any attributes or methods.

The `pass` statement can be used when no implementation is required yet.

```python
class Student:
    pass
```

The class is valid Python code and can be used to create objects.

```python
student1 = Student()

print(student1)
```

---

## Class with a Class Attribute

A class can contain a **class attribute**.

A class attribute belongs to the class and can be shared by objects created from that class.

```python
class Student:
    university = "KIU"
```

The attribute can be accessed through the class:

```python
print(Student.university)
```

Output:

```text
KIU
```

The general syntax is:

```python
class ClassName:
    attribute_name = value
```

---

## Class with an Instance Method

A class can contain an **instance method**.

An instance method normally receives `self` as its first parameter.

```python
class Student:
    def study(self):
        print("Student is studying")
```

An object can call the method:

```python
student1 = Student()

student1.study()
```

Output:

```text
Student is studying
```

The general syntax is:

```python
class ClassName:
    def method_name(self):
        # method body
        pass
```

---

## Class with an `__init__()` Method

A class can define an `__init__()` method to initialize instance attributes when an object is created.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

An object can then be created by providing the required argument:

```python
student1 = Student("Shehbaz")

print(student1.name)
```

Output:

```text
Shehbaz
```

The general syntax is:

```python
class ClassName:
    def __init__(self, parameter):
        self.attribute = parameter
```

---

## Class with Multiple Instance Attributes

A class can initialize multiple instance attributes.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

An object can be created by providing values for both parameters:

```python
student1 = Student("Shehbaz", 21)

print(student1.name)
print(student1.age)
```

Output:

```text
Shehbaz
21
```

Each object can have its own values for these instance attributes.

---

## Class with Multiple Methods

A class can contain multiple methods.

```python
class Student:
    def study(self):
        print("Student is studying")

    def attend_class(self):
        print("Student is attending class")
```

The methods can be called through an object:

```python
student1 = Student()

student1.study()
student1.attend_class()
```

Output:

```text
Student is studying
Student is attending class
```

---

## Class with Attributes and Methods

A class can contain both attributes and methods.

```python
class Student:
    university = "KIU"

    def study(self):
        print("Student is studying")
```

In this example:

- `university` is a class attribute.
- `study()` is an instance method.

---

## Complete Class Structure

A commonly used class structure is:

```python
class ClassName:
    class_attribute = value

    def __init__(self, parameter):
        self.instance_attribute = parameter

    def method_name(self):
        pass
```

This structure demonstrates the relationship between:

- the class definition
- class attributes
- the `__init__()` method
- instance attributes
- instance methods

---

## Complete Example

```python
class Student:
    university = "KIU"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("University:", self.university)


student1 = Student("Shehbaz", 21)

student1.introduce()
```

Output:

```text
Name: Shehbaz
Age: 21
University: KIU
```

This example demonstrates a class containing:

- a class attribute
- an initializer
- instance attributes
- an instance method

---

## Class Definition and Object Creation

Defining a class does not create an object automatically.

For example:

```python
class Student:
    pass
```

This statement only defines the class.

An object is created separately:

```python
student1 = Student()
```

Therefore:

```text
Class definition → defines the structure
Object creation  → creates an instance
```

---

## Creating Multiple Objects

Multiple objects can be created from the same class.

```python
class Student:
    def __init__(self, name):
        self.name = name


student1 = Student("Shehbaz")
student2 = Student("Ali")

print(student1.name)
print(student2.name)
```

Output:

```text
Shehbaz
Ali
```

The two objects are separate instances of the same class.

Each object maintains its own instance attributes.

---

## Class Body Indentation

Python uses indentation to define the body of a class.

Correct syntax:

```python
class Student:
    university = "KIU"

    def study(self):
        print("Student is studying")
```

Incorrect syntax:

```python
class Student:
university = "KIU"
```

The incorrect example produces an `IndentationError` because the class body must be indented.

---

## Accessing a Class Attribute

A class attribute can be accessed through the class name.

```python
class Student:
    university = "KIU"


print(Student.university)
```

Output:

```text
KIU
```

The general syntax is:

```python
ClassName.attribute_name
```

---

## Accessing an Instance Attribute

An instance attribute is accessed through an object.

```python
class Student:
    def __init__(self, name):
        self.name = name


student1 = Student("Shehbaz")

print(student1.name)
```

Output:

```text
Shehbaz
```

The general syntax is:

```python
object_name.attribute_name
```

---

## Calling an Instance Method

An instance method is normally called through an object.

```python
class Student:
    def study(self):
        print("Student is studying")


student1 = Student()

student1.study()
```

Output:

```text
Student is studying
```

The general syntax is:

```python
object_name.method_name()
```

---

## Class Syntax with User Input

A class can also be used with values obtained through `input()`.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Student name:", self.name)


name = input("Enter student name: ")

student1 = Student(name)

student1.introduce()
```

Example output:

```text
Enter student name: Shehbaz
Student name: Shehbaz
```

The class itself does not require `input()`. The input is simply used to provide a value when creating the object.

---

## Important Points

- A class is defined using the `class` keyword.
- A class provides a blueprint for creating objects.
- Class names conventionally use PascalCase.
- The class body must be indented.
- A class can contain attributes and methods.
- `pass` can be used when a class has no implementation.
- Class attributes belong to the class.
- Instance attributes belong to individual objects.
- The `__init__()` method is commonly used to initialize instance attributes.
- Instance methods normally receive `self` as their first parameter.
- Defining a class and creating an object are separate operations.
- Multiple objects can be created from the same class.
- Objects can access the attributes and methods defined by their class.

---

## Summary

The basic syntax for defining a class is:

```python
class ClassName:
    pass
```

A class can contain attributes, an initializer, and methods:

```python
class ClassName:
    class_attribute = value

    def __init__(self, parameter):
        self.instance_attribute = parameter

    def method_name(self):
        pass
```

The class definition provides the structure and behavior that objects created from the class can use.

Understanding class syntax is fundamental to understanding the remaining concepts of object-oriented programming, including object creation, instance attributes, methods, class attributes, inheritance, and method overriding.