# Inheritance

Inheritance is an object-oriented programming mechanism that allows one class to derive behavior and attributes from another class.

It is commonly used when there is a genuine **is-a relationship** between types.

For example:

```text
Vehicle
   │
   ├── Car
   └── Motorcycle
```

A `Car` is a `Vehicle`, and a `Motorcycle` is a `Vehicle`.

Inheritance can help avoid duplication and establish relationships between related classes. However, it should not be used merely to reuse code. In many situations, **composition is a better design choice**.

---

## 1. What Is Inheritance?

Suppose several classes share common behavior.

Without inheritance:

```python
class Dog:
    def eat(self):
        print("Eating")


class Cat:
    def eat(self):
        print("Eating")
```

Both classes contain duplicated behavior.

With inheritance:

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


class Cat(Animal):
    pass
```

Both `Dog` and `Cat` inherit the `eat()` method from `Animal`.

---

## 2. Parent and Child Classes

Inheritance introduces terminology.

```python
class Animal:
    pass


class Dog(Animal):
    pass
```

Here:

* `Animal` is the **parent class**.
* `Animal` is also called the **base class** or **superclass**.
* `Dog` is the **child class**.
* `Dog` is also called the **derived class** or **subclass**.

The terminology is interchangeable in most Python discussions.

---

## 3. Basic Inheritance Syntax

The syntax is:

```python
class Child(Parent):
    pass
```

Example:

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    pass
```

The class name of the parent is written inside parentheses.

```text
class Dog(Animal):
          ^^^^^^^
          parent class
```

---

## 4. Creating an Object of a Child Class

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


dog = Dog()

dog.eat()
```

Output:

```text
Eating
```

Although `eat()` is defined in `Animal`, the `Dog` object can use it because `Dog` inherits from `Animal`.

---

## 5. What Does a Child Class Inherit?

A subclass can inherit accessible attributes and methods from its parent class.

For example:

```python
class Animal:
    species = "Animal"

    def eat(self):
        print("Eating")
```

A subclass can use both:

```python
class Dog(Animal):
    pass
```

Then:

```python
dog = Dog()

print(dog.species)
dog.eat()
```

The inherited members are available through the `Dog` instance.

---

## 6. Inheritance Represents an "Is-A" Relationship

A good inheritance relationship should normally represent:

```text
Child IS-A Parent
```

Examples:

```text
Dog IS-A Animal
Car IS-A Vehicle
Manager IS-A Employee
CNN IS-A Model
```

This is different from:

```text
Car HAS-A Engine
Model HAS-A Optimizer
Student HAS-A Address
```

Those relationships usually suggest **composition**, not inheritance.

---

## 7. Inheritance Example: Vehicles

```python
class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    pass


car = Car()

car.start()
```

Output:

```text
Vehicle started
```

The `Car` inherits `start()` from `Vehicle`.

---

## 8. Adding New Behavior

A subclass does not have to contain only inherited behavior.

It can add its own methods.

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Woof!")
```

Now:

```python
dog = Dog()

dog.eat()
dog.bark()
```

Output:

```text
Eating
Woof!
```

The `Dog` has both inherited and newly defined behavior.

---

## 9. Adding Attributes to a Subclass

A subclass can define additional state.

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self, name):
        self.name = name
```

Usage:

```python
dog = Dog("Max")

print(dog.name)
dog.eat()
```

The `Dog` object has:

```text
name
eat()
```

where `eat()` comes from the parent.

---

## 10. Parent Initialization

Consider:

```python
class Animal:
    def __init__(self, species):
        self.species = species


class Dog(Animal):
    def __init__(self, name):
        self.name = name
```

Creating:

```python
dog = Dog("Max")
```

does **not automatically call `Animal.__init__()`** merely because `Dog` inherits from `Animal`.

Therefore, `species` is not initialized by this `Dog.__init__()`.

This is an important point.

Inheritance of a method does not mean that a subclass's custom `__init__()` automatically executes the parent initializer.

---

## 11. Using `super()`

A subclass can explicitly call the parent implementation using `super()`.

```python
class Animal:
    def __init__(self, species):
        self.species = species


class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")
        self.name = name
```

Now:

```python
dog = Dog("Max")

print(dog.species)
print(dog.name)
```

Output:

```text
Dog
Max
```

`super()` is particularly important when extending parent behavior.

---

## 12. Understanding `super()`

Inside:

```python
class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")
```

`super()` provides a proxy object used to access appropriate superclass behavior according to Python's method resolution order.

In simple single inheritance, this commonly means:

```text
Dog
 ↓
Animal
```

and:

```python
super().__init__(...)
```

calls the relevant parent implementation.

However, `super()` is more general than simply meaning "call my immediate parent."

---

## 13. Extending Parent Initialization

A common inheritance pattern is:

```python
class Parent:
    def __init__(self, value):
        self.value = value


class Child(Parent):
    def __init__(self, value, extra):
        super().__init__(value)
        self.extra = extra
```

The child extends the initialization performed by the parent.

Conceptually:

```text
Parent initialization
        +
Child-specific initialization
        =
Complete Child initialization
```

This avoids duplicating parent initialization logic.

---

## 14. Method Inheritance

A child class can use methods from its parent without redefining them.

```python
class Animal:
    def sleep(self):
        print("Sleeping")


class Dog(Animal):
    pass
```

Then:

```python
dog = Dog()

dog.sleep()
```

Output:

```text
Sleeping
```

The method is inherited.

---

## 15. Method Overriding

A subclass can provide its own implementation of an inherited method.

```python
class Animal:
    def speak(self):
        print("Some sound")


class Dog(Animal):
    def speak(self):
        print("Woof!")
```

Now:

```python
animal = Animal()
dog = Dog()

animal.speak()
dog.speak()
```

Output:

```text
Some sound
Woof!
```

The `Dog` implementation overrides the inherited implementation.

---

## 16. Why Override Methods?

Method overriding allows subclasses to specialize behavior.

A parent class can define a general interface:

```python
class Model:
    def predict(self, inputs):
        ...
```

Different subclasses can implement their own prediction behavior:

```python
class LinearModel(Model):
    def predict(self, inputs):
        ...


class TreeModel(Model):
    def predict(self, inputs):
        ...
```

The same conceptual operation can have different implementations.

This connects inheritance with **polymorphism**.

---

## 17. Calling the Parent Implementation After Overriding

A subclass can override a method while still using the parent's behavior.

```python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof!")
```

Calling:

```python
dog = Dog()
dog.speak()
```

produces:

```text
Animal sound
Woof!
```

The subclass extends rather than completely replaces the parent behavior.

---

## 18. Inheritance and `super()`

A common pattern is:

```python
class Parent:
    def action(self):
        print("Parent action")


class Child(Parent):
    def action(self):
        super().action()
        print("Child action")
```

The execution is:

```text
Child.action()
     ↓
super().action()
     ↓
Parent.action()
     ↓
Child-specific behavior
```

This pattern is useful when the parent's behavior should remain part of the child's behavior.

---

## 19. Single Inheritance

Single inheritance means a class directly inherits from one parent class.

```python
class Animal:
    pass


class Dog(Animal):
    pass
```

The relationship is:

```text
Animal
   │
   ▼
 Dog
```

This is the simplest inheritance structure.

---

## 20. Multilevel Inheritance

Inheritance can form multiple levels.

```python
class Animal:
    pass


class Mammal(Animal):
    pass


class Dog(Mammal):
    pass
```

The hierarchy is:

```text
Animal
   │
   ▼
Mammal
   │
   ▼
Dog
```

`Dog` inherits from `Mammal`, which itself inherits from `Animal`.

---

## 21. Multilevel Inheritance Example

```python
class Vehicle:
    def start(self):
        print("Starting")


class Car(Vehicle):
    def drive(self):
        print("Driving")


class ElectricCar(Car):
    def charge(self):
        print("Charging")
```

An `ElectricCar` object can use:

```python
car = ElectricCar()

car.start()
car.drive()
car.charge()
```

The methods come from different levels of the hierarchy.

---

## 22. Multiple Inheritance

Python supports multiple inheritance.

A class can inherit from more than one base class:

```python
class A:
    pass


class B:
    pass


class C(A, B):
    pass
```

The relationship is:

```text
A ──┐
    ├──> C
B ──┘
```

Multiple inheritance is powerful but can make class relationships more complex.

It should be used deliberately.

---

## 23. Multiple Inheritance Example

```python
class Flyable:
    def fly(self):
        print("Flying")


class Swimmable:
    def swim(self):
        print("Swimming")


class Duck(Flyable, Swimmable):
    pass
```

Now:

```python
duck = Duck()

duck.fly()
duck.swim()
```

Output:

```text
Flying
Swimming
```

The `Duck` receives behavior from both base classes.

---

## 24. Method Resolution Order

Multiple inheritance creates a fundamental question:

> If multiple classes provide a method with the same name, which implementation should Python use?

Python solves this using the **Method Resolution Order (MRO)**.

The MRO determines the order in which Python searches classes for attributes and methods.

You can inspect it with:

```python
ClassName.mro()
```

or:

```python
ClassName.__mro__
```

---

## 25. Simple MRO Example

```python
class A:
    def show(self):
        print("A")


class B(A):
    pass


class C(B):
    pass
```

The MRO can be inspected:

```python
print(C.mro())
```

Conceptually:

```text
C
↓
B
↓
A
↓
object
```

Python searches this sequence when resolving inherited attributes.

---

## 26. The `object` Base Class

Python classes ultimately inherit from `object` unless they are built on a different hierarchy that eventually leads to it.

For example:

```python
class Person:
    pass
```

is effectively based on:

```python
class Person(object):
    pass
```

in modern Python terms.

Therefore:

```text
Person
  ↓
object
```

The built-in `object` class is the root of Python's ordinary class hierarchy.

---

## 27. Checking Inheritance with `isinstance()`

Python provides:

```python
isinstance(object, class)
```

Example:

```python
class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
```

Output:

```text
True
True
```

A `Dog` instance is also considered an instance of `Animal` because `Dog` inherits from `Animal`.

---

## 28. Checking Class Relationships with `issubclass()`

Python also provides:

```python
issubclass(class, classinfo)
```

Example:

```python
class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog, Animal))
```

Output:

```text
True
```

This checks a class-level relationship rather than a particular object.

---

## 29. `isinstance()` vs `issubclass()`

Use:

```python
isinstance(value, Type)
```

when you want to ask:

> Is this object an instance of this type or one of its subclasses?

Use:

```python
issubclass(TypeA, TypeB)
```

when you want to ask:

> Is this class derived from this other class?

Example:

```python
dog = Dog()

isinstance(dog, Animal)
```

versus:

```python
issubclass(Dog, Animal)
```

The first operates on an object; the second operates on classes.

---

## 30. Inheritance of Class Attributes

Class attributes can also be inherited.

```python
class Animal:
    category = "Animal"


class Dog(Animal):
    pass
```

Then:

```python
dog = Dog()

print(dog.category)
```

Output:

```text
Animal
```

The attribute is found through the class hierarchy.

---

## 31. Child Attributes Can Override Parent Attributes

A subclass can define an attribute with the same name.

```python
class Animal:
    category = "Animal"


class Dog(Animal):
    category = "Dog"
```

Then:

```python
print(Animal.category)
print(Dog.category)
```

Output:

```text
Animal
Dog
```

The subclass's attribute takes precedence when accessed through `Dog`.

---

## 32. Attribute Lookup and Inheritance

When Python evaluates:

```python
dog.category
```

it performs attribute lookup through the object's class hierarchy and other mechanisms.

A simplified conceptual search is:

```text
Instance
   ↓
Dog
   ↓
Animal
   ↓
object
```

The actual lookup rules are more sophisticated, particularly when descriptors, properties, and multiple inheritance are involved.

For foundational OOP, the key idea is that inheritance participates in attribute lookup.

---

## 33. Inheritance Does Not Copy Code

A common misconception is:

> When a class inherits from another class, Python copies all parent methods into the child class.

That is not an accurate model.

Instead, attribute lookup searches the class hierarchy.

Conceptually:

```text
dog.eat()
   ↓
Does Dog provide eat?
   ↓ no
Does Animal provide eat?
   ↓ yes
Use Animal.eat
```

This distinction becomes important when understanding MRO and dynamic behavior.

---

## 34. Inheritance and Constructors

Consider:

```python
class Parent:
    def __init__(self):
        print("Parent")


class Child(Parent):
    pass
```

Since `Child` does not define its own `__init__()`, the inherited constructor can be used.

```python
child = Child()
```

Output:

```text
Parent
```

But if `Child` defines its own `__init__()`, Python uses the child's implementation.

---

## 35. Constructor Override

```python
class Parent:
    def __init__(self):
        print("Parent")


class Child(Parent):
    def __init__(self):
        print("Child")
```

Then:

```python
child = Child()
```

Output:

```text
Child
```

The parent's initializer is not automatically executed.

If the child needs the parent's initialization, it can call:

```python
super().__init__()
```

---

## 36. Inheritance and Encapsulation

Inheritance interacts with encapsulation.

For example:

```python
class Account:
    def __init__(self, balance):
        self._balance = balance
```

A subclass can access `_balance`:

```python
class SavingsAccount(Account):
    def add_interest(self):
        self._balance *= 1.05
```

The single underscore communicates that `_balance` is non-public, but subclasses can still access it.

This can be useful when subclasses are considered part of the implementation hierarchy.

---

## 37. Double Underscores and Inheritance

Consider:

```python
class Parent:
    def __init__(self):
        self.__value = 10
```

The attribute is name-mangled approximately as:

```text
_Parent__value
```

A child class using:

```python
self.__value
```

creates a different mangled name:

```text
_Child__value
```

This prevents accidental collisions between parent and child attributes.

---

## 38. Inheritance for AI/ML Models

Inheritance appears frequently in software architecture for machine-learning systems.

A conceptual design might be:

```text
BaseModel
   │
   ├── LinearModel
   ├── TreeModel
   └── NeuralNetworkModel
```

The base class might define a conceptual interface:

```python
class BaseModel:
    def predict(self, inputs):
        raise NotImplementedError
```

Subclasses provide specific implementations.

This allows software components to work with a common model abstraction.

---

## 39. Example: Base Model

```python
class BaseModel:
    def predict(self, inputs):
        raise NotImplementedError
```

Then:

```python
class LinearModel(BaseModel):
    def predict(self, inputs):
        return "Linear prediction"
```

and:

```python
class TreeModel(BaseModel):
    def predict(self, inputs):
        return "Tree prediction"
```

Both models provide `predict()`.

This design can support polymorphic code.

---

## 40. Inheritance Is Not Just Code Reuse

A major design mistake is:

> Use inheritance whenever two classes share code.

Shared code alone does not establish an inheritance relationship.

For example, suppose:

```text
Car
Engine
```

Both might have a method named `start()`, but:

```text
Car IS-A Engine
```

is false.

Instead:

```text
Car HAS-A Engine
```

suggests composition.

Inheritance should generally represent a meaningful subtype relationship.

---

## 41. Inheritance vs Composition

Compare:

```text
Inheritance:
Dog IS-A Animal
```

with:

```text
Composition:
Car HAS-A Engine
```

Inheritance expresses a type hierarchy.

Composition expresses that one object contains or uses another object.

Example:

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()
```

The `Car` contains an `Engine`.

This is composition.

---

## 42. Why Composition Is Often Preferred

Inheritance can create strong coupling between parent and child classes.

If a subclass depends heavily on parent implementation details, changes to the parent can unexpectedly affect subclasses.

Composition often provides greater flexibility:

```text
Car
 │
 └── Engine
```

The `Car` can use an engine without becoming a subtype of `Engine`.

This supports the principle:

> Favor composition over inheritance when inheritance does not represent a genuine subtype relationship.

This does not mean inheritance is bad. It means the relationship should be chosen deliberately.

---

## 43. A Good Inheritance Hierarchy

A useful inheritance hierarchy generally has:

* A meaningful subtype relationship.
* A coherent shared interface.
* Clear responsibilities.
* Minimal unnecessary coupling.
* Predictable inherited behavior.

Example:

```text
Shape
 │
 ├── Circle
 └── Rectangle
```

Both are shapes.

A questionable hierarchy would be created solely because two unrelated classes happen to share one method.

---

## 44. Liskov Substitution Principle

Inheritance is closely related to the **Liskov Substitution Principle (LSP)**.

The principle states, in practical terms:

> Objects of a subtype should be usable wherever objects of the base type are expected without violating the expected behavior of the program.

Suppose:

```python
class Bird:
    def fly(self):
        ...
```

Then creating:

```python
class Penguin(Bird):
    def fly(self):
        raise NotImplementedError
```

may indicate a problematic hierarchy.

A penguin is a bird biologically, but if the software's `Bird` abstraction specifically means "a bird that can fly," then `Penguin` does not satisfy the expected contract.

The issue is the abstraction, not biology.

---

## 45. Designing Better Abstractions

Instead of:

```python
class Bird:
    def fly(self):
        ...
```

you might separate capabilities:

```text
Bird
 │
 ├── FlyingBird
 └── Penguin
```

or use another interface design.

The important lesson is:

> Inheritance should model behavioral substitutability, not merely classification.

---

## 46. Inheritance and Polymorphism

Inheritance often enables polymorphism.

For example:

```python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")
```

Then:

```python
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```

Output:

```text
Woof!
Meow!
```

The same operation:

```python
animal.speak()
```

produces behavior appropriate to the actual object.

---

## 47. Inheritance Hierarchies Can Become Deep

Consider:

```text
A
│
└── B
    │
    └── C
        │
        └── D
            │
            └── E
```

Deep inheritance hierarchies can become difficult to understand.

A change in a high-level parent can affect many descendants.

Therefore, inheritance depth should be kept reasonable.

A flat or composition-based design may sometimes be easier to maintain.

---

## 48. Fragile Base Class Problem

A **fragile base class** problem occurs when changes to a parent class unexpectedly break or alter the behavior of subclasses.

For example, a parent class may change:

```python
class Parent:
    def process(self):
        ...
```

and a subclass may rely on assumptions about how `process()` works.

Changing the parent can then cause unintended effects.

This is one reason inheritance creates stronger coupling than composition in many designs.

---

## 49. Multiple Inheritance and Complexity

Multiple inheritance can produce powerful designs but introduces additional complexity.

For example:

```python
class A:
    def run(self):
        print("A")


class B:
    def run(self):
        print("B")


class C(A, B):
    pass
```

When:

```python
c = C()
c.run()
```

is executed, Python follows the MRO.

Understanding the MRO is therefore essential when using multiple inheritance.

---

## 50. Mixins

A **mixin** is a class designed to provide a focused piece of reusable behavior rather than represent a primary domain type.

Example:

```python
class LoggingMixin:
    def log(self, message):
        print(message)
```

A class can combine it with another class:

```python
class Service:
    pass


class LoggingService(LoggingMixin, Service):
    pass
```

Mixins are commonly used with multiple inheritance to add orthogonal capabilities.

A mixin generally should be small and focused.

---

## 51. Inheritance and Frameworks

Inheritance is common in frameworks.

A framework may provide a base class:

```python
class BaseProcessor:
    def process(self, data):
        raise NotImplementedError
```

An application developer can create:

```python
class ImageProcessor(BaseProcessor):
    def process(self, data):
        ...
```

The framework can then work with `BaseProcessor` while allowing specialized implementations.

This pattern appears in many software systems.

---

## 52. Inheritance in Python Libraries

When reading Python libraries, you may encounter structures such as:

```text
BaseClass
    ↓
SpecializedClass
```

or:

```text
BaseClass
 ├── ImplementationA
 ├── ImplementationB
 └── ImplementationC
```

Understanding inheritance helps you determine:

* Which methods are inherited.
* Which methods are overridden.
* Which behavior is shared.
* Which behavior is specialized.
* What interface the subclasses are expected to implement.

This is particularly important when working with large frameworks.

---

## 53. Practical Example: Dataset Classes

A simplified AI-oriented hierarchy might be:

```python
class Dataset:
    def __len__(self):
        return 0

    def get_item(self, index):
        raise NotImplementedError
```

A specialized dataset could implement:

```python
class ImageDataset(Dataset):
    def __init__(self, images):
        self.images = images

    def __len__(self):
        return len(self.images)

    def get_item(self, index):
        return self.images[index]
```

The base class establishes a conceptual interface, while the subclass provides concrete behavior.

---

## 54. Practical Example: Optimizers

A conceptual optimizer hierarchy might be:

```text
Optimizer
   │
   ├── SGD
   └── Adam
```

The base class might define a common operation:

```python
class Optimizer:
    def step(self):
        raise NotImplementedError
```

Subclasses can implement:

```python
class SGD(Optimizer):
    def step(self):
        print("SGD update")


class Adam(Optimizer):
    def step(self):
        print("Adam update")
```

This supports a common interface for different algorithms.

---

## 55. When Inheritance Is Appropriate

Inheritance is often appropriate when:

1. There is a genuine subtype relationship.
2. The child satisfies the behavioral expectations of the parent.
3. The parent provides a meaningful abstraction.
4. Shared behavior is conceptually part of the same hierarchy.
5. Polymorphism is useful.
6. The hierarchy remains understandable.

For example:

```text
Model
 │
 ├── LinearModel
 └── TreeModel
```

can be reasonable if all model types share a meaningful model interface.

---

## 56. When Inheritance Is Not Appropriate

Avoid inheritance when:

* You only want code reuse.
* The classes are unrelated.
* The relationship is actually "has-a."
* The hierarchy becomes unnecessarily deep.
* The subclass violates the parent's behavioral assumptions.
* Composition provides a simpler design.
* Parent implementation details become a required dependency.

For example:

```text
Car → Engine
```

should normally be composition rather than inheritance.

---

## 57. Inheritance Design Checklist

Before creating:

```python
class Child(Parent):
```

ask:

### Relationship

Is `Child` genuinely a `Parent`?

### Behavior

Can a `Child` safely be used wherever a `Parent` is expected?

### Responsibility

Does the parent abstraction represent behavior that belongs naturally to the child?

### Coupling

Will the child become tightly dependent on parent implementation details?

### Alternative

Would composition produce a simpler and more flexible design?

If these questions have poor answers, inheritance may not be the correct tool.

---

## 58. Common Mistake: Forgetting `super().__init__()`

Example:

```python
class Parent:
    def __init__(self):
        self.value = 10


class Child(Parent):
    def __init__(self):
        self.other = 20
```

Here the parent initializer does not run automatically.

Therefore:

```python
child = Child()
print(child.value)
```

raises an `AttributeError`.

If parent initialization is required:

```python
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.other = 20
```

---

## 59. Common Mistake: Assuming `super()` Means "Parent"

A simplified explanation often says:

> `super()` calls the parent class.

This is useful initially but technically incomplete.

`super()` provides access to the next implementation according to the relevant **MRO**.

This distinction matters especially in multiple inheritance.

Therefore, the more accurate description is:

> `super()` delegates method lookup to the next class in the method resolution order.

---

## 60. Common Mistake: Using Inheritance Only for Code Reuse

Incorrect:

```text
Class A has useful method X.
Class B also needs X.
Therefore B should inherit A.
```

Shared code is insufficient evidence for inheritance.

Instead ask:

```text
Is B an A?
```

If not, consider:

* Composition
* A helper function
* A separate utility abstraction
* A mixin, when appropriate

---

## 61. Common Mistake: Creating Deep Hierarchies

This:

```text
A → B → C → D → E → F
```

can become difficult to reason about.

Prefer simpler structures when possible.

The goal is not to maximize inheritance.

The goal is to create clear, maintainable relationships between abstractions.

---

## 62. Common Mistake: Confusing Inheritance With Polymorphism

Inheritance and polymorphism are related but distinct.

Inheritance:

```text
Child derives from Parent
```

Polymorphism:

```text
Different objects can respond to a common operation appropriately
```

Python can support polymorphism without inheritance through duck typing.

Therefore:

```text
Inheritance ≠ Polymorphism
```

Inheritance is one mechanism that can support polymorphic designs.

---

## 63. Common Mistake: Treating Biological Classification as Software Design

A real-world relationship does not automatically justify inheritance.

For example:

```text
Penguin IS-A Bird
```

may be biologically true.

But if the software abstraction is:

```text
Bird = object that can fly
```

then a penguin may not satisfy the behavioral contract.

Software inheritance should be based on the behavior and abstractions required by the program.

---

## 64. Best Practices

### 1. Model genuine subtype relationships

Use inheritance when the child is meaningfully a subtype of the parent.

### 2. Prefer shallow hierarchies

Avoid unnecessary inheritance depth.

### 3. Use `super()` when extending parent behavior

Do not duplicate parent initialization or logic unnecessarily.

### 4. Understand MRO

Especially when multiple inheritance is involved.

### 5. Keep parent classes coherent

A parent should define a meaningful abstraction.

### 6. Respect behavioral substitutability

Subclasses should honor the expectations established by their base class.

### 7. Prefer composition when appropriate

Do not use inheritance merely to reuse implementation.

### 8. Keep subclasses focused

Avoid creating subclasses that accumulate unrelated responsibilities.

---

## Summary

Inheritance allows one class to derive behavior and attributes from another class.

Important concepts include:

* Parent class
* Child class
* Base class
* Subclass
* Derived class
* Method inheritance
* Method overriding
* `super()`
* Single inheritance
* Multilevel inheritance
* Multiple inheritance
* Method Resolution Order
* `isinstance()`
* `issubclass()`
* Polymorphism
* Composition vs inheritance
* Liskov Substitution Principle
* Mixins

The basic syntax is:

```python
class Parent:
    pass


class Child(Parent):
    pass
```

A subclass can add behavior:

```python
class Child(Parent):
    def new_method(self):
        ...
```

It can override behavior:

```python
class Child(Parent):
    def existing_method(self):
        ...
```

It can extend parent behavior:

```python
class Child(Parent):
    def existing_method(self):
        super().existing_method()
        ...
```

The most important design rule is:

```text
Use inheritance for genuine "is-a" relationships.
Use composition for "has-a" relationships.
```

Inheritance is powerful, but it introduces coupling. A professional Python developer should therefore treat inheritance as a design decision rather than simply a mechanism for avoiding duplicated code.
