"@classmethod" Syntax

Introduction

A class method is a method that is bound to a class rather than to a particular instance.

Python uses the "@classmethod" decorator to define a class method.

A class method receives the class itself as its first argument. By convention, this parameter is named "cls".

Class methods are commonly used when a method needs to work with class-level data or provide an alternative way to create objects.

---

Basic Syntax

class ClassName:
    @classmethod
    def method_name(cls):
        # method body
        pass

Syntax Breakdown

- "@classmethod" is the decorator that creates a class method.
- "def" defines the method.
- "method_name" is the name of the method.
- "cls" refers to the class.
- The indented block contains the method body.

---

Simple Example

class Student:
    @classmethod
    def show_message(cls):
        print("This is a class method")


Student.show_message()

Output:

This is a class method

The method is called directly through the class.

---

The "cls" Parameter

The first parameter of a class method is conventionally named "cls".

class Student:
    @classmethod
    def show_class(cls):
        print(cls)


Student.show_class()

Output:

<class '__main__.Student'>

The exact module name may vary depending on where the code is executed.

The important point is that "cls" refers to the "Student" class.

---

Accessing a Class Attribute

Class methods can access class attributes through "cls".

class Student:
    university = "KIU"

    @classmethod
    def show_university(cls):
        print(cls.university)


Student.show_university()

Output:

KIU

The expression:

cls.university

accesses the "university" attribute belonging to the class.

---

Modifying a Class Attribute

A class method can also modify a class attribute.

class Student:
    university = "KIU"

    @classmethod
    def change_university(cls, university):
        cls.university = university


Student.change_university("COMSATS")

print(Student.university)

Output:

COMSATS

The class method changes the class attribute through "cls".

---

Calling a Class Method Through an Instance

A class method can also be called through an instance.

class Student:
    university = "KIU"

    @classmethod
    def show_university(cls):
        print(cls.university)


student1 = Student()

student1.show_university()

Output:

KIU

Even though the method is called through "student1", the first argument received by the class method is still the class.

---

Class Method with Parameters

A class method can accept additional parameters.

class Student:
    university = "KIU"

    @classmethod
    def set_university(cls, university):
        cls.university = university


Student.set_university("COMSATS")

print(Student.university)

Output:

COMSATS

The "cls" parameter is automatically provided, while "university" is provided explicitly.

---

Class Method vs Instance Method

An instance method normally uses "self":

class Student:
    def show_name(self):
        print("Student")

A class method uses "cls":

class Student:
    @classmethod
    def show_class(cls):
        print(cls)

The difference is:

self → current instance
cls  → current class

---

Class Method as an Alternative Constructor

One important use of class methods is creating an alternative constructor.

Consider:

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))

The object can be created normally:

student1 = Student("Shehbaz", 21)

Or through the class method:

student2 = Student.from_string("Ali,22")

Both objects are instances of "Student".

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)

Output:

Shehbaz
21
Ali
22

---

Why Use "cls()" in an Alternative Constructor?

Consider:

return cls(name, int(age))

Here, "cls" represents the class on which the class method was called.

Using "cls()" allows the class method to create an instance of that class.

This is preferable to hard-coding:

return Student(name, int(age))

because "cls()" is designed to work with inheritance and subclasses more appropriately.

---

Class Method with a Class Attribute

A class method can work with multiple class attributes.

class Student:
    university = "KIU"
    department = "Artificial Intelligence"

    @classmethod
    def show_information(cls):
        print(cls.university)
        print(cls.department)


Student.show_information()

Output:

KIU
Artificial Intelligence

---

General Syntax

The general syntax for a class method is:

class ClassName:
    @classmethod
    def method_name(cls, parameter):
        # method body
        pass

For a method that modifies class-level state:

class ClassName:
    class_attribute = value

    @classmethod
    def change_attribute(cls, new_value):
        cls.class_attribute = new_value

---

Common Mistake

A common mistake is forgetting the "@classmethod" decorator.

For example:

class Student:
    def show_university(cls):
        print(cls.university)

This is an ordinary instance method, not a class method.

The correct syntax is:

class Student:
    university = "KIU"

    @classmethod
    def show_university(cls):
        print(cls.university)

Now it can be called as:

Student.show_university()

---

Important Points

- A class method is defined using the "@classmethod" decorator.
- The first parameter is conventionally named "cls".
- "cls" refers to the class.
- Class methods can access class attributes through "cls".
- Class methods can modify class attributes.
- Class methods can be called through the class.
- Class methods can also be accessed through instances.
- Class methods are commonly used for alternative constructors.
- "cls()" can be used to create an instance of the relevant class.

---

Summary

The basic syntax for a class method is:

class ClassName:
    @classmethod
    def method_name(cls):
        # method body
        pass

A class method works with the class itself rather than requiring a specific instance.

The key distinction is:

Instance method → self
Class method    → cls

Understanding "@classmethod" is important for working with class-level state and implementing alternative object-construction patterns in Python.