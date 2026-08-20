Inheritance Syntax

Introduction

Inheritance is an object-oriented programming mechanism that allows one class to acquire attributes and methods from another class.

The class being inherited from is commonly called the parent class, base class, or superclass.

The class that inherits from it is commonly called the child class, derived class, or subclass.

Inheritance promotes code reuse and allows a subclass to extend or specialize existing behavior.

---

Basic Syntax

class ParentClass:
    pass


class ChildClass(ParentClass):
    pass

Syntax Breakdown

- "ParentClass" is the base class.
- "ChildClass" is the derived class.
- "ChildClass(ParentClass)" specifies that "ChildClass" inherits from "ParentClass".
- The child class can use accessible attributes and methods inherited from the parent class.

---

Simple Example

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    pass


dog1 = Dog()

dog1.eat()

Output:

Animal is eating

Although "eat()" is defined in "Animal", the "Dog" object can use it because "Dog" inherits from "Animal".

---

Parent Class and Child Class

Consider:

class Animal:
    pass


class Dog(Animal):
    pass

The relationship is:

Animal
   ↓
Dog

"Animal" is the parent class, and "Dog" is the child class.

---

Adding a Method to the Child Class

A child class can define its own methods in addition to inherited methods.

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog1 = Dog()

dog1.eat()
dog1.bark()

Output:

Animal is eating
Dog is barking

The "Dog" object can use both:

- the inherited "eat()" method
- the child-defined "bark()" method

---

Inheritance with Instance Attributes

A child class can have its own instance attributes.

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    pass


dog1 = Dog("Buddy")

print(dog1.name)

Output:

Buddy

Because "Dog" does not define its own "__init__()" method, the inherited initializer from "Animal" can be used.

---

Child Class with Its Own "__init__()"

A child class can define its own initializer.

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


dog1 = Dog("Buddy", "German Shepherd")

print(dog1.name)
print(dog1.breed)

Output:

Buddy
German Shepherd

Here, "Dog" defines its own "__init__()" method.

---

Method Overriding

A child class can provide its own implementation of a method inherited from the parent class.

This is called method overriding.

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


dog1 = Dog()

dog1.sound()

Output:

Dog barks

The "Dog" implementation replaces the inherited behavior when "sound()" is called on a "Dog" object.

---

Inheritance and Class Attributes

Class attributes can also be inherited.

class Animal:
    category = "Animal"


class Dog(Animal):
    pass


dog1 = Dog()

print(dog1.category)
print(Dog.category)

Output:

Animal
Animal

The child class can access the inherited class attribute.

---

Multilevel Inheritance

Python supports inheritance across multiple levels.

class Animal:
    def eat(self):
        print("Animal is eating")


class Mammal(Animal):
    def walk(self):
        print("Mammal is walking")


class Dog(Mammal):
    def bark(self):
        print("Dog is barking")


dog1 = Dog()

dog1.eat()
dog1.walk()
dog1.bark()

Output:

Animal is eating
Mammal is walking
Dog is barking

The inheritance relationship is:

Animal
   ↓
Mammal
   ↓
Dog

"Dog" can access behavior inherited through both levels.

---

Multiple Inheritance

Python also supports multiple inheritance.

A class can inherit from more than one parent class.

class Father:
    def work(self):
        print("Father is working")


class Mother:
    def cook(self):
        print("Mother is cooking")


class Child(Father, Mother):
    pass


child1 = Child()

child1.work()
child1.cook()

Output:

Father is working
Mother is cooking

The syntax is:

class Child(Parent1, Parent2):
    pass

---

Checking an Inheritance Relationship

The built-in "isinstance()" function can check whether an object is an instance of a particular class or its subclass.

class Animal:
    pass


class Dog(Animal):
    pass


dog1 = Dog()

print(isinstance(dog1, Dog))
print(isinstance(dog1, Animal))

Output:

True
True

A "Dog" object is both a "Dog" instance and, through inheritance, an "Animal" instance.

---

Checking a Class Relationship with "issubclass()"

The built-in "issubclass()" function can check whether one class inherits from another.

class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog, Animal))

Output:

True

The expression:

issubclass(Dog, Animal)

checks whether "Dog" is a subclass of "Animal".

---

Inheritance and Method Reuse

Inheritance allows a child class to reuse behavior without redefining it.

class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    pass


car1 = Car()

car1.start()

Output:

Vehicle started

The "Car" class does not need to redefine "start()".

---

Inheritance and Extension

A child class can reuse inherited behavior and add additional behavior.

class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


car1 = Car()

car1.start()
car1.drive()

Output:

Vehicle started
Car is driving

This is one of the main purposes of inheritance: extending an existing abstraction.

---

General Syntax

The general syntax for single inheritance is:

class Parent:
    # parent class body
    pass


class Child(Parent):
    # child class body
    pass

For multiple inheritance:

class Parent1:
    pass


class Parent2:
    pass


class Child(Parent1, Parent2):
    pass

---

Important Points

- Inheritance allows a class to acquire behavior and attributes from another class.
- The inherited class is called the parent, base, or superclass.
- The inheriting class is called the child, derived, or subclass.
- Inheritance is specified using parentheses after the child class name.
- A child class can use inherited methods.
- A child class can define additional methods and attributes.
- A child class can override inherited methods.
- Python supports single, multilevel, and multiple inheritance.
- "isinstance()" checks an object's relationship to a class.
- "issubclass()" checks a relationship between two classes.
- Inheritance should represent a meaningful is-a relationship.

---

Summary

The basic syntax for inheritance is:

class Parent:
    pass


class Child(Parent):
    pass

Inheritance allows a child class to reuse and extend functionality from a parent class.

For example:

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")

The "Dog" class inherits "eat()" from "Animal" and adds its own "bark()" behavior.

Inheritance is a fundamental OOP mechanism for building related classes and organizing reusable behavior.