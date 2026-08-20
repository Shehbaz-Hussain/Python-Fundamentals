"super()" Syntax

Introduction

"super()" is a built-in function used in inheritance to access attributes and methods from a parent class or, more precisely, from the next class in the method resolution order (MRO).

It is commonly used when a child class wants to extend the behavior of a parent class instead of completely replacing it.

One of the most common uses of "super()" is calling the parent class's "__init__()" method.

---

Basic Syntax

class Parent:
    def method(self):
        print("Parent method")


class Child(Parent):
    def method(self):
        super().method()

Syntax Breakdown

- "super()" provides access to the next class in the MRO.
- ".method()" calls the relevant method.
- The child class can extend the parent behavior without duplicating its implementation.

---

Simple Example

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")


dog1 = Dog()

dog1.sound()

Output:

Animal makes a sound
Dog barks

The statement:

super().sound()

calls the inherited implementation before the child class adds its own behavior.

---

Calling the Parent "__init__()" Method

A common use of "super()" is calling the parent class's initializer.

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog1 = Dog("Buddy", "German Shepherd")

print(dog1.name)
print(dog1.breed)

Output:

Buddy
German Shepherd

The statement:

super().__init__(name)

allows the parent class to initialize "name".

The child class then initializes its own "breed" attribute.

---

Why Use "super()"?

Without "super()", the child class might duplicate initialization logic.

For example:

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

This works, but the child class duplicates the parent's initialization logic.

Using "super()" is cleaner:

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

The parent remains responsible for initializing the state defined by the parent class.

---

Extending a Parent Method

A child class can use "super()" to extend an inherited method.

class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def start(self):
        super().start()
        print("Car is ready to drive")


car1 = Car()

car1.start()

Output:

Vehicle started
Car is ready to drive

The child method performs both the parent behavior and its additional behavior.

---

"super()" with Instance Methods

"super()" is commonly used inside instance methods.

class Parent:
    def display(self):
        print("Parent")


class Child(Parent):
    def display(self):
        super().display()
        print("Child")


child1 = Child()

child1.display()

Output:

Parent
Child

The child method calls the parent implementation first.

---

"super()" with Multiple Attributes

A parent class can initialize several attributes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university


student1 = Student("Shehbaz", 21, "KIU")

print(student1.name)
print(student1.age)
print(student1.university)

Output:

Shehbaz
21
KIU

The parent class initializes "name" and "age", while the child class initializes "university".

---

"super()" Does Not Mean Simply "Parent"

A common misconception is that:

super()

always means "my direct parent."

That description is incomplete.

More precisely, "super()" delegates attribute or method lookup to the next class in the method resolution order (MRO).

This distinction becomes particularly important when using multiple inheritance.

---

Method Resolution Order

Python determines the order in which classes are searched using the method resolution order.

Consider:

class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")
        super().show()


class C(A):
    def show(self):
        print("C")
        super().show()


class D(B, C):
    def show(self):
        print("D")
        super().show()


object1 = D()

object1.show()

Output:

D
B
C
A

The relevant MRO is:

D → B → C → A → object

Therefore, each "super()" call moves to the next class in that order.

---

Viewing the MRO

The "mro()" method can be used to inspect the method resolution order.

print(D.mro())

A simplified representation of the result is:

D
B
C
A
object

The exact printed representation includes Python's class notation.

---

"super()" with an Overridden Method

When a child overrides a method, "super()" allows it to reuse the inherited implementation.

class Animal:
    def move(self):
        print("Animal is moving")


class Dog(Animal):
    def move(self):
        super().move()
        print("Dog is running")


dog1 = Dog()

dog1.move()

Output:

Animal is moving
Dog is running

This allows the child class to extend rather than completely replace the parent behavior.

---

General Syntax

The most common syntax is:

class Child(Parent):
    def method(self):
        super().method()

For an initializer:

class Child(Parent):
    def __init__(self, value):
        super().__init__(value)

---

Common Mistake

A common mistake is directly calling the parent class by name when "super()" is more appropriate.

For example:

class Parent:
    def show(self):
        print("Parent")


class Child(Parent):
    def show(self):
        Parent.show(self)
        print("Child")

This can work for simple single inheritance, but it tightly couples the child implementation to the specific "Parent" class.

Using:

class Child(Parent):
    def show(self):
        super().show()
        print("Child")

is generally preferable because it works with Python's MRO and supports cooperative inheritance.

---

Important Points

- "super()" is used with inheritance.
- It provides access to the next class in the MRO.
- It is commonly used to call inherited methods.
- It is frequently used to call a parent initializer.
- "super()" helps avoid duplicating parent-class logic.
- It allows a child class to extend inherited behavior.
- "super()" does not simply mean "direct parent."
- Understanding MRO is important when using "super()" with multiple inheritance.
- The zero-argument form "super()" is the normal modern Python syntax inside methods.

---

Summary

The basic syntax is:

class Child(Parent):
    def method(self):
        super().method()

For an initializer:

class Child(Parent):
    def __init__(self, value):
        super().__init__(value)

"super()" is an important part of Python inheritance because it allows child classes to reuse and extend inherited behavior while respecting Python's method resolution order.