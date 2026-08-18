Object Creation Syntax

Introduction

An object is an instance of a class. After defining a class, objects can be created from that class.

Creating an object is also called instantiation.

In Python, an object is created by calling the class name followed by parentheses.

---

Basic Syntax

object_name = ClassName()

Syntax Breakdown

- "object_name" is the variable that refers to the object.
- "ClassName" is the class from which the object is created.
- "()" calls the class and creates an instance.
- "=" assigns the created object to the variable.

---

Example

class Student:
    pass


student1 = Student()

print(student1)

The statement:

student1 = Student()

creates an object of the "Student" class.

The variable "student1" refers to that object.

---

Creating Multiple Objects

A single class can be used to create multiple objects.

class Student:
    pass


student1 = Student()
student2 = Student()
student3 = Student()

Here, three separate "Student" objects are created.

Each object is an independent instance of the same class.

---

Checking the Type of an Object

The built-in "type()" function can be used to determine the type of an object.

class Student:
    pass


student1 = Student()

print(type(student1))

Output:

<class '__main__.Student'>

The exact module name displayed by "type()" can vary depending on where the code is executed, but the important part is that "student1" is an instance of "Student".

---

Creating an Object from a Class with a Method

A class can contain methods, and its objects can use those methods.

class Student:
    def study(self):
        print("Student is studying")


student1 = Student()

student1.study()

Output:

Student is studying

Here:

1. "Student" defines the class.
2. "student1 = Student()" creates an object.
3. "student1.study()" calls the object's method.

---

Creating Objects with "__init__()"

When a class contains an "__init__()" method that requires arguments, those arguments are provided when the object is created.

class Student:
    def __init__(self, name):
        self.name = name


student1 = Student("Shehbaz")

print(student1.name)

Output:

Shehbaz

The value ""Shehbaz"" is passed to the "name" parameter during object creation.

---

Creating Multiple Objects with Different Values

Objects created from the same class can contain different data.

class Student:
    def __init__(self, name):
        self.name = name


student1 = Student("Shehbaz")
student2 = Student("Ali")

print(student1.name)
print(student2.name)

Output:

Shehbaz
Ali

Both objects belong to the same class, but their instance data is different.

---

Object Identity

Each object created from a class is a separate instance.

class Student:
    pass


student1 = Student()
student2 = Student()

print(student1 is student2)

Output:

False

The expression "student1 is student2" checks whether both variables refer to the exact same object.

Since two separate objects were created, the result is "False".

---

Assigning One Object to Another Variable

Assigning an existing object to another variable does not create a new object.

class Student:
    pass


student1 = Student()
student2 = student1

print(student1 is student2)

Output:

True

Both variables refer to the same object.

This is different from:

student1 = Student()
student2 = Student()

because that statement creates two separate objects.

---

General Object Creation Syntax

The general form is:

object_name = ClassName(arguments)

If the class does not require arguments:

object_name = ClassName()

If the class requires arguments:

object_name = ClassName(value1, value2)

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

Common Mistake

A common mistake is trying to create an object without providing required arguments.

For example:

class Student:
    def __init__(self, name):
        self.name = name


student1 = Student()

This produces an error because the required "name" argument was not provided.

The correct syntax is:

student1 = Student("Shehbaz")

---

Important Points

- An object is an instance of a class.
- Creating an object is called instantiation.
- Objects are created by calling the class.
- The basic syntax is "object_name = ClassName()".
- Arguments can be passed during object creation when required by "__init__()".
- Multiple objects can be created from the same class.
- Each separately created object is an independent instance.
- Assigning one object to another variable does not create a new object.
- The "is" operator can be used to check whether two variables refer to the same object.

---

Summary

The basic syntax for creating an object is:

object_name = ClassName()

When a class requires initialization arguments:

object_name = ClassName(value1, value2)

Object creation is an essential part of object-oriented programming because classes define the structure and behavior, while objects represent individual instances of that structure.