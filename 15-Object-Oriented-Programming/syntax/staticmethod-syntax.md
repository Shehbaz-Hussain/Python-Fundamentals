"@staticmethod" Syntax

Introduction

A static method is a method defined inside a class that does not automatically receive the instance or the class as its first argument.

Python uses the "@staticmethod" decorator to define a static method.

Unlike an instance method, a static method does not require "self".

Unlike a class method, a static method does not require "cls".

Static methods are useful for operations that are logically related to a class but do not need to access instance-specific or class-specific data.

---

Basic Syntax

class ClassName:
    @staticmethod
    def method_name():
        # method body
        pass

Syntax Breakdown

- "@staticmethod" is the decorator that creates a static method.
- "def" defines the method.
- "method_name" is the name of the method.
- A static method does not receive "self" or "cls" automatically.
- The method body contains the required operation.

---

Simple Example

class Calculator:
    @staticmethod
    def show_message():
        print("This is a static method")


Calculator.show_message()

Output:

This is a static method

The method can be called directly through the class.

---

Static Method with Parameters

A static method can accept normal parameters.

class Calculator:
    @staticmethod
    def add(number1, number2):
        return number1 + number2


result = Calculator.add(10, 20)

print(result)

Output:

30

The parameters "number1" and "number2" are explicitly provided by the caller.

There is no automatic "self" or "cls" parameter.

---

Calling a Static Method Through an Instance

A static method can also be accessed through an instance.

class Calculator:
    @staticmethod
    def add(number1, number2):
        return number1 + number2


calculator = Calculator()

result = calculator.add(10, 20)

print(result)

Output:

30

The method still does not receive the "calculator" object automatically.

---

Static Method Does Not Require "self"

An instance method normally has "self":

class Calculator:
    def add(self, number1, number2):
        return number1 + number2

A static method does not:

class Calculator:
    @staticmethod
    def add(number1, number2):
        return number1 + number2

The difference is important because a static method does not operate automatically on a particular object.

---

Static Method Does Not Require "cls"

A class method receives "cls":

class Calculator:
    @classmethod
    def show_class(cls):
        print(cls)

A static method does not:

class Calculator:
    @staticmethod
    def show_message():
        print("Calculator")

There is no automatically supplied class reference.

---

Static Method for Validation

Static methods can be useful for validation operations that do not require object or class state.

class Student:
    @staticmethod
    def is_valid_age(age):
        return age >= 18


print(Student.is_valid_age(21))
print(Student.is_valid_age(16))

Output:

True
False

The method only needs the explicitly provided "age" value.

---

Static Method for Calculation

A static method can perform calculations using its parameters.

class Mathematics:
    @staticmethod
    def square(number):
        return number * number


result = Mathematics.square(5)

print(result)

Output:

25

The calculation does not depend on any particular object or class state.

---

Static Method with Multiple Parameters

class Calculator:
    @staticmethod
    def multiply(number1, number2):
        return number1 * number2

    @staticmethod
    def subtract(number1, number2):
        return number1 - number2


print(Calculator.multiply(5, 4))
print(Calculator.subtract(10, 3))

Output:

20
7

A class can contain multiple static methods.

---

Static Method and Instance Attributes

A static method does not automatically have access to instance attributes because it does not receive "self".

For example:

class Student:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def show_message():
        print("Student information")

The static method cannot directly use:

self.name

because "self" is not automatically available inside a static method.

---

Static Method and Class Attributes

A static method also does not automatically receive "cls".

For example:

class Student:
    university = "KIU"

    @staticmethod
    def show_message():
        print("Student information")

The static method does not automatically receive the class reference.

If access to class-level state is required, a class method is usually more appropriate.

---

Static Method as a Utility Operation

A static method is appropriate when an operation is logically related to the class but does not require object or class state.

class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32


temperature = Temperature.celsius_to_fahrenheit(25)

print(temperature)

Output:

77.0

The conversion depends only on the supplied value.

---

Instance Method vs Class Method vs Static Method

Instance Method

class Student:
    def method(self):
        pass

Receives:

self → current instance

Class Method

class Student:
    @classmethod
    def method(cls):
        pass

Receives:

cls → current class

Static Method

class Student:
    @staticmethod
    def method():
        pass

Receives:

no automatic instance or class argument

---

General Syntax

The general syntax is:

class ClassName:
    @staticmethod
    def method_name(parameter1, parameter2):
        # method body
        pass

For a method that returns a value:

class ClassName:
    @staticmethod
    def method_name(parameter1, parameter2):
        return parameter1 + parameter2

---

Common Mistake

A common mistake is defining a static method with "self" when it is not needed.

For example:

class Calculator:
    @staticmethod
    def add(self, number1, number2):
        return number1 + number2

This does not make "self" an automatically supplied instance parameter. In a static method, all parameters are ordinary explicit parameters.

The clearer and correct version is:

class Calculator:
    @staticmethod
    def add(number1, number2):
        return number1 + number2


print(Calculator.add(10, 20))

Output:

30

---

Important Points

- A static method is defined using "@staticmethod".
- A static method does not automatically receive "self".
- A static method does not automatically receive "cls".
- All parameters of a static method are explicit parameters.
- A static method can be called through the class.
- A static method can also be accessed through an instance.
- Static methods are useful for operations that do not require instance or class state.
- Static methods are often suitable for validation, calculations, conversions, and other utility operations.

---

Summary

The basic syntax for a static method is:

class ClassName:
    @staticmethod
    def method_name():
        # method body
        pass

A static method differs from other method types because it receives no implicit instance or class reference.

Instance method → self
Class method    → cls
Static method   → no automatic reference

Understanding this distinction is important when deciding whether a method should operate on an object, on a class, or only on explicitly provided data.