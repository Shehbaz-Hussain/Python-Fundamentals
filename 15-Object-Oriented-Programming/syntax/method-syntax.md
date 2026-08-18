Method Syntax

Introduction

A method is a function defined inside a class.

Methods are used to define the behavior of objects. They can perform operations, access instance attributes, modify object state, accept arguments, and return values.

In Python, an instance method normally receives "self" as its first parameter.

---

Basic Syntax

class ClassName:
    def method_name(self):
        # method body
        pass

Syntax Breakdown

- "class ClassName:" defines the class.
- "def" defines the method.
- "method_name" is the name of the method.
- "self" refers to the current object.
- The indented block contains the method body.

---

Defining a Simple Method

class Student:
    def study(self):
        print("Student is studying")

Here, "study()" is an instance method of the "Student" class.

The method can be called through an object:

student1 = Student()

student1.study()

Output:

Student is studying

---

Method Calling Syntax

The general syntax for calling an instance method is:

object_name.method_name()

For example:

class Student:
    def study(self):
        print("Student is studying")


student1 = Student()

student1.study()

The expression:

student1.study()

calls the "study()" method for the "student1" object.

---

The "self" Parameter

The "self" parameter refers to the current instance.

class Student:
    def introduce(self):
        print("This is a student")


student1 = Student()

student1.introduce()

When the method is called through "student1", Python provides the instance as the first argument automatically.

The name "self" is the standard Python convention for this parameter.

---

Method with Instance Attributes

Methods can access instance attributes through "self".

class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


student1 = Student("Shehbaz")

student1.introduce()

Output:

My name is Shehbaz

The expression:

self.name

refers to the "name" attribute of the current object.

---

Method with Parameters

A method can receive additional parameters after "self".

class Student:
    def introduce(self, message):
        print(message)


student1 = Student()

student1.introduce("I am studying Python")

Output:

I am studying Python

The general syntax is:

def method_name(self, parameter):
    # method body

---

Method with Multiple Parameters

A method can accept multiple arguments.

class Calculator:
    def add(self, number1, number2):
        print(number1 + number2)


calculator = Calculator()

calculator.add(10, 20)

Output:

30

The "self" parameter represents the object, while "number1" and "number2" receive the values supplied when the method is called.

---

Method with a Return Value

A method can return a value using the "return" statement.

class Calculator:
    def add(self, number1, number2):
        return number1 + number2


calculator = Calculator()

result = calculator.add(10, 20)

print(result)

Output:

30

The returned value can be stored in a variable and used later.

---

Method Modifying an Instance Attribute

A method can modify the state of an object.

class Student:
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name


student1 = Student("Shehbaz")

student1.change_name("Ali")

print(student1.name)

Output:

Ali

The method changes the "name" instance attribute of "student1".

---

Multiple Methods in a Class

A class can contain multiple methods.

class Student:
    def study(self):
        print("Student is studying")

    def attend_class(self):
        print("Student is attending class")


student1 = Student()

student1.study()
student1.attend_class()

Output:

Student is studying
Student is attending class

Each method represents a different behavior of the object.

---

One Method Calling Another Method

An instance method can call another method of the same object using "self".

class Student:
    def start(self):
        print("Student started studying")

    def study(self):
        self.start()
        print("Student is studying")


student1 = Student()

student1.study()

Output:

Student started studying
Student is studying

The expression:

self.start()

calls the "start()" method for the current object.

---

Methods with Default Parameters

Methods can use default parameter values.

class Student:
    def introduce(self, name="Student"):
        print("Hello", name)


student1 = Student()

student1.introduce()
student1.introduce("Shehbaz")

Output:

Hello Student
Hello Shehbaz

---

Methods and Object State

Methods can read and modify the state stored in instance attributes.

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count = self.count + 1


counter1 = Counter()

counter1.increment()
counter1.increment()

print(counter1.count)

Output:

2

The "increment()" method changes the object's "count" attribute.

---

General Method Syntax

A typical instance method has the following structure:

class ClassName:
    def method_name(self, parameter1, parameter2):
        # method body
        return value

Not every method requires parameters or a return statement.

For example:

class Student:
    def study(self):
        print("Studying")

---

Common Mistake: Forgetting "self"

A normal instance method should have an instance parameter.

Incorrect:

class Student:
    def study():
        print("Studying")


student1 = Student()
student1.study()

This produces a "TypeError" because Python passes the instance automatically, but the method does not have a parameter to receive it.

Correct:

class Student:
    def study(self):
        print("Studying")


student1 = Student()
student1.study()

Output:

Studying

---

Important Points

- A method is a function defined inside a class.
- Instance methods normally have "self" as their first parameter.
- "self" refers to the current object.
- Methods are called using dot notation.
- Methods can access instance attributes through "self".
- Methods can accept additional parameters.
- Methods can return values.
- Methods can modify instance attributes.
- A class can contain multiple methods.
- One instance method can call another using "self".

---

Summary

The basic syntax for an instance method is:

class ClassName:
    def method_name(self):
        # method body
        pass

A method with parameters can be written as:

class ClassName:
    def method_name(self, parameter):
        # method body
        pass

Methods define the behavior of objects and work together with instance attributes to represent the state and behavior of an object.