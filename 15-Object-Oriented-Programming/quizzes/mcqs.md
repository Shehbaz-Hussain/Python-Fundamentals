# Object-Oriented Programming Quiz


## Overview

This assessment evaluates your understanding of the core Object-Oriented Programming concepts covered in Module 15.

The quiz assesses:

* Classes and objects
* Instance attributes
* Class attributes
* Instance methods
* `self`
* `__init__()`
* Class methods
* Static methods
* Object state
* Inheritance
* Method overriding
* `super()`
* Composition
* Polymorphism
* Duck typing
* Encapsulation
* Name mangling
* Abstraction
* Attribute lookup
* Object-oriented design reasoning

## Instructions

* Answer all 60 questions.
* Select one answer for each multiple-choice question.
* For True/False questions, determine whether the statement is correct.
* For code-output questions, determine the exact output before checking the answer key.
* Do not execute the code while attempting the assessment.
* Assume Python 3.13+.
* Review the answer key only after completing the quiz.
* Pay attention to the reasoning behind each answer.

---

# Part 1 — Multiple Choice

## Classes and Objects

### 1. What is a class in Python?

A. A specific object stored in memory
B. A definition used to create instances and describe their behavior
C. A function that must return an object
D. A module containing only related functions

---

### 2. What is an object?

A. An instance of a class
B. A class definition
C. A method definition
D. A variable name

---

### 3. Which statement best describes instantiation?

A. Modifying a class definition
B. Creating an instance of a class
C. Defining a method
D. Inheriting from another class

---

### 4. Which syntax creates an instance of `Student`?

```python
class Student:
    pass
```

A.

```python
Student = student()
```

B.

```python
student = Student
```

C.

```python
student = Student()
```

D.

```python
student = new Student()
```

---

## Instance State and Attributes

### 5. Which statement best describes an instance attribute?

A. State associated with a particular instance
B. State that must be shared by every instance
C. A method belonging to the class
D. A variable that can only exist outside a class

---

### 6. Which statement correctly describes a class attribute?

A. It can only be accessed through `self`
B. It is defined in the class namespace and is associated with the class
C. Every instance must create an independent copy of it
D. It must always be immutable

---

### 7. Consider the following code:

```python
class Employee:
    company = "Nexa"

    def __init__(self, name):
        self.name = name
```

Which statement is correct?

A. `name` is a class attribute and `company` is an instance attribute
B. Both are instance attributes
C. `company` is a class attribute and `name` is an instance attribute
D. Both are local variables

---

### 8. Why can two instances of the same class have different values for an instance attribute?

A. Each instance can maintain its own state
B. Instance attributes are always class attributes
C. Python automatically creates a new class for each object
D. Instance attributes cannot be changed

---

### 9. What happens when an instance does not contain an attribute being accessed?

A. Python always returns `None`
B. Python searches according to its attribute lookup rules, including the class
C. Python automatically creates the attribute
D. Python converts the attribute into a method

---

### 10. What happens when an instance defines an attribute with the same name as a class attribute?

A. The class attribute is deleted
B. The instance attribute generally takes precedence for that instance
C. Both values are automatically merged
D. Python raises a syntax error

---

## `self` and Methods

### 11. What does `self` conventionally refer to inside an instance method?

A. The class
B. The current instance
C. The superclass
D. The module

---

### 12. Which statement about `self` is technically correct?

A. `self` is a Python keyword
B. `self` must be used because Python reserves the name
C. `self` is the conventional name for the instance parameter
D. `self` always refers to the class

---

### 13. Why is `self.name` different from `name` inside an instance method?

A. `self.name` refers to instance state, while `name` may refer to a local or other variable depending on scope
B. `self.name` is always a class attribute
C. `name` always refers to the current object
D. Python treats both expressions identically

---

### 14. What is the primary purpose of `__init__()`?

A. Initialize an already-created instance
B. Define inheritance
C. Destroy an object
D. Allocate memory directly

---

### 15. Which statement about `__init__()` is correct?

A. It must always return the newly created object
B. It initializes instance state after object creation
C. It is required for every class
D. It can only initialize class attributes

---

## Class Methods and Static Methods

### 16. Which decorator defines a class method?

A. `@staticmethod`
B. `@classmethod`
C. `@class`
D. `@method`

---

### 17. What does a class method conventionally receive as its first parameter?

A. `self`
B. `object`
C. `cls`
D. `class`

---

### 18. What does a static method automatically receive?

A. `self`
B. `cls`
C. Both `self` and `cls`
D. Neither an implicit instance nor an implicit class argument

---

### 19. Which situation is generally appropriate for a static method?

A. Behavior that needs the current instance
B. Behavior that needs the class object
C. Utility-like behavior logically grouped with a class but requiring no implicit instance or class state
D. Every method in a class

---

### 20. Which situation is commonly appropriate for a class method?

A. Creating alternative instances of a class
B. Accessing an individual object's state
C. Requiring `self` for every operation
D. Replacing every instance method

---

## Inheritance and Polymorphism

### 21. Which relationship is generally represented by inheritance?

A. Has-a
B. Is-a
C. Uses-a
D. Contains-a

---

### 22. What is method overriding?

A. Defining a subclass implementation for an inherited method
B. Calling a method twice
C. Defining two local variables with the same name
D. Creating a class attribute

---

### 23. What is the primary purpose of `super()`?

A. Create a new superclass
B. Access behavior through the method resolution order
C. Make an attribute private
D. Convert a method into a static method

---

### 24. What does polymorphism allow?

A. Only objects from the same class to be used together
B. Different objects to be used through compatible behavior or interfaces
C. Every class to inherit from `object` manually
D. Classes to contain only one method

---

### 25. What is duck typing?

A. Requiring objects to inherit from the same superclass
B. Focusing on whether an object supports the required operations
C. Requiring every object to have exactly the same attributes
D. Restricting polymorphism to built-in types

---

# Part 2 — True or False

### 26. A class and an object are the same thing.

**True / False**

---

### 27. Multiple instances can be created from the same class.

**True / False**

---

### 28. Two instances of the same class can maintain different instance attribute values.

**True / False**

---

### 29. `self` is a Python keyword.

**True / False**

---

### 30. `__init__()` initializes an instance after the instance has been created.

**True / False**

---

### 31. A class attribute can be accessed through an instance if the instance does not provide an attribute with the same name.

**True / False**

---

### 32. A static method automatically receives `self`.

**True / False**

---

### 33. A class method conventionally receives `cls` as its first parameter.

**True / False**

---

### 34. Duck typing requires classes to share the same superclass.

**True / False**

---

### 35. Composition commonly represents a has-a relationship.

**True / False**

---

# Part 3 — Code Output

Determine the exact output of each program.

### 36. What is the output?

```python
class Student:
    def __init__(self, name):
        self.name = name


student = Student("Aisha")

print(student.name)
```

A. `Student`
B. `name`
C. `Aisha`
D. `None`

---

### 37. What is the output?

```python
class Counter:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1


counter = Counter(4)
counter.increment()

print(counter.value)
```

A. `4`
B. `5`
C. `1`
D. `None`

---

### 38. What is the output?

```python
class Device:
    category = "Electronic"


phone = Device()
laptop = Device()

print(phone.category)
print(laptop.category)
```

A.

```text
None
None
```

B.

```text
Electronic
Electronic
```

C.

```text
phone
laptop
```

D.

```text
Device
Device
```

---

### 39. What is the output?

```python
class Device:
    category = "Electronic"


phone = Device()
phone.category = "Mobile"

print(phone.category)
print(Device.category)
```

A.

```text
Electronic
Electronic
```

B.

```text
Mobile
Mobile
```

C.

```text
Mobile
Electronic
```

D.

```text
Electronic
Mobile
```

---

### 40. What is the output?

```python
class Employee:
    count = 0

    def __init__(self):
        Employee.count += 1


Employee()
Employee()

print(Employee.count)
```

A. `0`
B. `1`
C. `2`
D. An error occurs

---

### 41. What is the output?

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(3, 4))
```

A. `3`
B. `4`
C. `7`
D. An error occurs

---

### 42. What is the output?

```python
class Person:
    species = "Human"

    @classmethod
    def get_species(cls):
        return cls.species


print(Person.get_species())
```

A. `Person`
B. `Human`
C. `species`
D. `None`

---

### 43. What is the output?

```python
class Animal:
    def speak(self):
        print("Animal")


class Dog(Animal):
    def speak(self):
        print("Dog")


dog = Dog()
dog.speak()
```

A. `Animal`
B. `Dog`
C.

```text
Animal
Dog
```

D. An error occurs

---

### 44. What is the output?

```python
class Animal:
    def speak(self):
        print("Animal")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog")


dog = Dog()
dog.speak()
```

A.

```text
Animal
```

B.

```text
Dog
```

C.

```text
Animal
Dog
```

D.

```text
Dog
Animal
```

---

### 45. What is the output?

```python
class Printer:
    def print_document(self):
        print("Printing")


class Scanner:
    def print_document(self):
        print("Scanning")


def process(device):
    device.print_document()


process(Printer())
process(Scanner())
```

A.

```text
Printing
Printing
```

B.

```text
Scanning
Scanning
```

C.

```text
Printing
Scanning
```

D. An error occurs because the classes are unrelated

---

### 46. What is the output?

```python
class Parent:
    value = "Parent"


class Child(Parent):
    value = "Child"


child = Child()

print(child.value)
```

A. `Parent`
B. `Child`
C. `None`
D. An error occurs

---

### 47. What is the output?

```python
class Parent:
    def message(self):
        return "Parent"


class Child(Parent):
    def message(self):
        return super().message() + " Child"


print(Child().message())
```

A. `Parent`
B. `Child`
C. `Parent Child`
D. `Child Parent`

---

### 48. What is the output?

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = Account(500)

print(account.get_balance())
```

A. `0`
B. `500`
C. `__balance`
D. An error occurs

---

### 49. What is the output?

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()


car = Car()
car.start()
```

A. `Car`
B. `Engine started`
C. `None`
D. An error occurs because `Car` does not inherit from `Engine`

---

### 50. What is the output?

```python
class Parent:
    def show(self):
        print("Parent")


class Child(Parent):
    pass


Child().show()
```

A. `Parent`
B. `Child`
C. `None`
D. An error occurs

---

# Part 4 — Conceptual Reasoning

### 51. Why is the distinction between instance attributes and class attributes important?

A. They have identical ownership semantics
B. They represent different kinds of state and have different lookup behavior
C. Class attributes cannot contain strings
D. Instance attributes cannot be modified

---

### 52. Why can an instance attribute hide a class attribute with the same name?

A. Python deletes the class attribute
B. Instance-level lookup can take precedence over the class attribute
C. Python combines both values
D. The class is automatically modified

---

### 53. A `Car` object contains an `Engine` object and delegates engine-related operations to it. Which relationship is most appropriate?

A. Inheritance
B. Composition
C. Method overriding
D. Class inheritance

---

### 54. Which situation generally favors composition over inheritance?

A. One type is genuinely a specialized form of another type
B. An object needs to collaborate with another object without being a subtype of it
C. A subclass must override a method
D. A class needs a constructor

---

### 55. Which statement best describes method overriding?

A. A subclass replaces or specializes inherited behavior by defining a method with the same name
B. A class creates two objects
C. An instance creates a class
D. A method becomes static

---

### 56. Which statement best describes duck typing?

A. The object's exact class is more important than its behavior
B. Objects are accepted based on whether they support the required operations
C. Every object must inherit from a common application-specific base class
D. Duck typing is only available for built-in types

---

### 57. What is the purpose of name mangling for names beginning with two leading underscores?

A. It makes attributes completely inaccessible
B. It helps reduce accidental name collisions in subclasses
C. It converts attributes into constants
D. It automatically makes attributes read-only

---

### 58. Which statement best describes encapsulation?

A. Combining related state and behavior while providing appropriate interfaces for interaction
B. Making every attribute completely inaccessible
C. Replacing all composition with inheritance
D. Using only private attributes

---

### 59. Which statement best distinguishes abstraction from encapsulation?

A. Abstraction focuses on essential interfaces and behavior, while encapsulation focuses on organizing and controlling access to state and behavior
B. Abstraction means inheritance, while encapsulation means polymorphism
C. They are exactly the same concept
D. Abstraction only applies to static methods

---

### 60. Which design best demonstrates polymorphism?

A. A function that accepts different objects because each object provides the required method
B. A class containing only class attributes
C. Two variables referencing the same integer
D. A class with no methods

---

# End of Quiz

Complete all 60 questions before reviewing the answer key.

See `oop-quiz-answer-key.md` for the correct answers and explanations.
