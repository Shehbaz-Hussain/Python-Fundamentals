# Method Overriding

Method overriding occurs when a subclass provides its own implementation of a method that is already defined in its parent class.

It allows a child class to **specialize or replace inherited behavior** while maintaining the same method name.

Method overriding is an important mechanism behind runtime polymorphism and is commonly used in object-oriented Python programs.

---

## 1. What Is Method Overriding?

Consider:

```python
class Animal:
    def speak(self):
        print("Some animal sound")
```

A `Dog` inherits `speak()`:

```python
class Dog(Animal):
    pass
```

The inherited behavior is:

```python
dog = Dog()
dog.speak()
```

Output:

```text
Some animal sound
```

But a dog has a more specific implementation of `speak()`.

We can override the method:

```python
class Dog(Animal):
    def speak(self):
        print("Woof!")
```

Now:

```python
dog = Dog()
dog.speak()
```

Output:

```text
Woof!
```

The `Dog` implementation takes precedence over the inherited `Animal` implementation.

---

## 2. Basic Syntax

The general pattern is:

```python
class Parent:
    def method(self):
        # Parent implementation
        ...


class Child(Parent):
    def method(self):
        # Child implementation
        ...
```

The child method has the same name as the inherited method.

Python's attribute lookup finds the method on `Child` before searching its parent classes.

---

## 3. Simple Example

```python
class Vehicle:
    def start(self):
        print("Starting vehicle")


class Car(Vehicle):
    def start(self):
        print("Starting car")
```

Now:

```python
vehicle = Vehicle()
car = Car()

vehicle.start()
car.start()
```

Output:

```text
Starting vehicle
Starting car
```

The same method name produces different behavior depending on the object's actual type.

---

## 4. Why Override Methods?

Method overriding is useful when a subclass needs to:

* Provide more specific behavior.
* Replace a generic implementation.
* Adapt inherited behavior.
* Customize an operation for a particular type.
* Participate in polymorphic behavior.

For example:

```text
Animal
  │
  ├── Dog → speak() → Woof
  ├── Cat → speak() → Meow
  └── Cow → speak() → Moo
```

The base class defines a common operation, while subclasses specialize it.

---

## 5. Overriding Is Not Overloading

These concepts are different.

### Method overriding

A subclass redefines an inherited method:

```python
class Parent:
    def show(self):
        print("Parent")


class Child(Parent):
    def show(self):
        print("Child")
```

### Method overloading

Traditional method overloading means defining multiple methods with the same name but different parameter signatures.

Python does **not** support traditional compile-time method overloading in the same way as languages such as Java or C++.

For example, this does not create two overloaded methods:

```python
class Example:
    def add(self, a):
        ...

    def add(self, a, b):
        ...
```

The second definition replaces the first one in the class namespace.

Therefore:

```text
Overriding ≠ Overloading
```

---

## 6. Overriding an Inherited Method

```python
class Animal:
    def move(self):
        print("Animal is moving")


class Dog(Animal):
    def move(self):
        print("Dog is running")
```

Now:

```python
dog = Dog()
dog.move()
```

Output:

```text
Dog is running
```

The parent method is still defined in `Animal`, but it is not the implementation selected for this `Dog` object.

---

## 7. What Happens During Method Lookup?

When Python evaluates:

```python
dog.move()
```

Python must locate `move`.

A simplified lookup is:

```text
Dog object
    ↓
Dog class
    ↓
Does Dog define move?
    ↓
Yes
    ↓
Use Dog.move()
```

If `Dog` did not define `move`, Python would continue searching through the inheritance hierarchy.

For:

```python
class Dog(Animal):
    pass
```

the search would continue to `Animal`.

---

## 8. Overriding With Different Behavior

A subclass can completely replace the parent behavior:

```python
class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending email")
```

Usage:

```python
notification = EmailNotification()
notification.send()
```

Output:

```text
Sending email
```

The subclass has replaced the inherited implementation for its objects.

---

## 9. Calling the Parent Implementation

Sometimes a subclass should extend the parent's behavior instead of completely replacing it.

Use `super()`:

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog says woof")
```

Now:

```python
dog = Dog()
dog.speak()
```

Output:

```text
Animal makes a sound
Dog says woof
```

The child method performs both the inherited and specialized behavior.

---

## 10. `super()` and Method Overriding

The general pattern is:

```python
class Child(Parent):
    def method(self):
        super().method()
        # additional child behavior
```

This is useful when the parent implementation contains behavior that should not be duplicated.

Instead of:

```python
class Child(Parent):
    def method(self):
        # duplicated parent logic
        ...
        # child logic
        ...
```

prefer:

```python
class Child(Parent):
    def method(self):
        super().method()
        # child logic
```

when the parent behavior should remain part of the operation.

---

## 11. Overriding `__init__()`

`__init__()` is also a method and can be overridden.

Example:

```python
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
```

Here, `Student` provides its own initializer.

However, duplicating the parent's initialization is usually unnecessary.

A better approach is:

```python
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
```

This allows `Person` to remain responsible for initializing `name`.

---

## 12. Why `super().__init__()` Matters

Suppose:

```python
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, student_id):
        self.student_id = student_id
```

Now:

```python
student = Student("Ali", 101)

print(student.name)
```

raises:

```text
AttributeError
```

because `Person.__init__()` never executed.

Using:

```python
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
```

properly initializes the inherited state.

---

## 13. Overriding While Preserving the Parent Contract

A subclass should generally preserve the expected behavior of the parent method.

For example:

```python
class Model:
    def predict(self, data):
        ...
```

A subclass might implement:

```python
class LinearModel(Model):
    def predict(self, data):
        return "prediction"
```

The subclass should still satisfy the conceptual contract of `predict()`.

This is related to the **Liskov Substitution Principle**.

---

## 14. Method Signatures and Overriding

Consider:

```python
class Parent:
    def process(self, data):
        print(data)


class Child(Parent):
    def process(self, data):
        print(data)
```

The subclass maintains the same basic method interface.

This is usually easier to use polymorphically.

Changing the interface in an incompatible way can create problems:

```python
class Child(Parent):
    def process(self):
        print("Processing")
```

Code expecting:

```python
obj.process(data)
```

may fail when `obj` is a `Child`.

Therefore, overriding should preserve the expectations associated with the inherited interface.

---

## 15. Return Values in Overridden Methods

An overridden method can return a value:

```python
class Animal:
    def sound(self):
        return "Unknown"


class Dog(Animal):
    def sound(self):
        return "Woof"
```

Then:

```python
dog = Dog()

result = dog.sound()

print(result)
```

Output:

```text
Woof
```

When designing polymorphic classes, consistent return semantics are generally important.

---

## 16. Overriding and Polymorphism

Method overriding is one way to achieve polymorphic behavior.

Example:

```python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("Meow")
```

Then:

```python
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```

Output:

```text
Woof
Meow
```

The loop does not need separate logic for each subclass.

It simply calls:

```python
animal.speak()
```

The object's implementation determines what happens.

---

## 17. Runtime Method Selection

Consider:

```python
animal = Dog()
animal.speak()
```

The variable may conceptually be treated as an `Animal`, but the actual object is a `Dog`.

Python resolves the method according to the object's runtime type and class hierarchy.

Conceptually:

```text
animal
  ↓
Dog object
  ↓
Dog.speak()
```

This is why overriding supports runtime polymorphism.

---

## 18. Parent Reference and Child Object

Consider:

```python
class Animal:
    def speak(self):
        print("Animal")


class Dog(Animal):
    def speak(self):
        print("Dog")
```

Then:

```python
animal = Dog()
animal.speak()
```

Output:

```text
Dog
```

The variable name `animal` does not change the object's actual class.

The object is still a `Dog`.

---

## 19. Overriding Class Attributes

The concept also applies to class attributes.

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

The subclass defines its own value for the inherited name.

This is attribute overriding or shadowing rather than method overriding specifically.

---

## 20. Overriding Does Not Modify the Parent

Consider:

```python
class Animal:
    def speak(self):
        print("Animal")


class Dog(Animal):
    def speak(self):
        print("Dog")
```

Calling:

```python
dog = Dog()
dog.speak()
```

does not change:

```python
Animal.speak
```

The parent class remains unchanged.

You can verify:

```python
animal = Animal()
animal.speak()
```

Output:

```text
Animal
```

The overridden implementation exists in the subclass.

---

## 21. Multiple Levels of Overriding

Methods can be overridden across several inheritance levels.

```python
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")


class C(B):
    def show(self):
        print("C")
```

Now:

```python
C().show()
```

outputs:

```text
C
```

The most specific implementation takes precedence.

---

## 22. Using `super()` Across Multiple Levels

Consider:

```python
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        super().show()
        print("B")


class C(B):
    def show(self):
        super().show()
        print("C")
```

Calling:

```python
C().show()
```

produces:

```text
A
B
C
```

The calls proceed through the relevant method resolution order.

---

## 23. `super()` Is MRO-Based

It is inaccurate to define `super()` simply as:

> Call the parent class.

A more precise explanation is:

> `super()` returns a proxy that delegates attribute lookup to the next class in the method resolution order.

This becomes particularly important with multiple inheritance.

For simple single inheritance:

```text
Child → Parent
```

the distinction may not be visible.

With multiple inheritance, it becomes essential.

---

## 24. Multiple Inheritance and Overriding

Consider:

```python
class A:
    def show(self):
        print("A")


class B:
    def show(self):
        print("B")


class C(A, B):
    pass
```

Then:

```python
C().show()
```

produces:

```text
A
```

because `A` appears before `B` in the MRO for `C`.

You can inspect it:

```python
print(C.mro())
```

---

## 25. Cooperative Multiple Inheritance

Multiple inheritance works most reliably when classes cooperate using `super()`.

Example:

```python
class A:
    def process(self):
        print("A")
        super().process()


class B:
    def process(self):
        print("B")
        super().process()


class C(A, B):
    def process(self):
        print("C")
        super().process()
```

This pattern requires careful design and an appropriate terminal implementation.

It is an advanced use of inheritance, but understanding the concept is important when reading sophisticated Python code.

---

## 26. Overriding Built-in Special Methods

Python classes can override special methods such as:

```python
__str__
__len__
__eq__
```

For example:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
```

Now:

```python
person = Person("Ali")

print(person)
```

uses the custom `__str__()` implementation.

Special methods allow objects to integrate with Python's language protocols.

---

## 27. Example: Overriding `__str__()`

A parent class:

```python
class Person:
    def __str__(self):
        return "Person"
```

A child class:

```python
class Student(Person):
    def __str__(self):
        return "Student"
```

Then:

```python
print(Person())
print(Student())
```

Output:

```text
Person
Student
```

The subclass overrides the parent's string representation.

---

## 28. Overriding and `__len__()`

A parent can define:

```python
class Collection:
    def __len__(self):
        return 0
```

A subclass can specialize:

```python
class Numbers(Collection):
    def __init__(self, numbers):
        self.numbers = numbers

    def __len__(self):
        return len(self.numbers)
```

Now:

```python
numbers = Numbers([10, 20, 30])

print(len(numbers))
```

Output:

```text
3
```

This demonstrates how overriding can customize Python's built-in operations.

---

## 29. Overriding in AI Software

Method overriding is especially useful when several AI components share a common interface.

Consider:

```python
class Model:
    def predict(self, inputs):
        raise NotImplementedError
```

Then:

```python
class Classifier(Model):
    def predict(self, inputs):
        return "class prediction"
```

and:

```python
class Regressor(Model):
    def predict(self, inputs):
        return "numeric prediction"
```

Both provide:

```python
predict(inputs)
```

but their implementations differ.

---

## 30. Example: Training Components

A simplified design might be:

```python
class Trainer:
    def train(self, model, data):
        raise NotImplementedError
```

A subclass can specialize:

```python
class NeuralNetworkTrainer(Trainer):
    def train(self, model, data):
        print("Training neural network")
```

Another can implement:

```python
class TreeTrainer(Trainer):
    def train(self, model, data):
        print("Training decision tree")
```

The common interface allows higher-level code to work with different trainers.

---

## 31. Example: Data Processing

```python
class DataProcessor:
    def process(self, data):
        raise NotImplementedError


class TextProcessor(DataProcessor):
    def process(self, data):
        return data.lower()


class ImageProcessor(DataProcessor):
    def process(self, data):
        return "Processed image"
```

The subclasses specialize the common `process()` operation.

This pattern is common in extensible software systems.

---

## 32. Method Overriding and Duck Typing

Python does not require inheritance for polymorphism.

For example:

```python
class Dog:
    def speak(self):
        print("Woof")


class Robot:
    def speak(self):
        print("Beep")
```

Neither class needs to inherit from the other.

Both support:

```python
speak()
```

A function can operate on either object:

```python
def make_speak(obj):
    obj.speak()
```

This is duck typing.

Therefore:

```text
Method overriding → usually inheritance-based specialization
Duck typing → compatible behavior without requiring inheritance
```

Both can support polymorphism.

---

## 33. Overriding vs Duck Typing

### Method overriding

```text
Parent
  ↓
Child
```

The child redefines an inherited method.

### Duck typing

```text
Dog → speak()
Robot → speak()
```

The classes do not need a shared parent.

Python focuses heavily on behavior and protocols rather than requiring explicit inheritance relationships.

---

## 34. Overriding and Abstract Base Classes

Abstract base classes can define required methods.

For example:

```python
from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def predict(self, data):
        pass
```

A concrete subclass must provide an implementation:

```python
class LinearModel(Model):
    def predict(self, data):
        return "Prediction"
```

Here, overriding is used to satisfy an abstract interface.

---

## 35. What Happens If the Method Is Not Implemented?

Suppose:

```python
from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def predict(self, data):
        pass
```

Then:

```python
class LinearModel(Model):
    pass
```

`LinearModel` remains abstract because it has not implemented `predict()`.

Attempting:

```python
model = LinearModel()
```

raises a `TypeError`.

The abstract base class therefore enforces an interface contract.

---

## 36. Overriding With Additional Validation

A subclass can add validation while preserving parent behavior.

```python
class User:
    def set_name(self, name):
        self.name = name


class Admin(User):
    def set_name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")

        super().set_name(name)
```

The child adds a rule before delegating to the parent.

This can be appropriate when the specialization truly belongs in the subclass.

---

## 37. Overriding With Additional Logging

Another pattern is:

```python
class Service:
    def run(self):
        print("Running service")


class LoggedService(Service):
    def run(self):
        print("Starting log")
        super().run()
        print("Finished log")
```

This extends the operation without duplicating the parent implementation.

---

## 38. Overriding Should Preserve Meaning

Suppose:

```python
class FileStorage:
    def save(self, data):
        ...
```

A subclass overriding `save()` should still behave like a storage implementation.

If the subclass instead:

```python
def save(self, data):
    print("I do not save anything")
```

then the subclass may violate the expectations associated with the parent abstraction.

Method overriding is not merely about matching method names.

It should preserve the semantic contract of the operation.

---

## 39. Common Mistake: Forgetting `self`

Incorrect:

```python
class Dog(Animal):
    def speak():
        print("Woof")
```

Correct:

```python
class Dog(Animal):
    def speak(self):
        print("Woof")
```

Instance methods require the instance parameter.

---

## 40. Common Mistake: Incorrect `super()` Usage

Incorrect:

```python
super(Dog)
```

This does not call the parent method.

For modern Python code, the usual form inside an instance method is:

```python
super().method()
```

For example:

```python
class Dog(Animal):
    def speak(self):
        super().speak()
```

---

## 41. Common Mistake: Assuming Parent `__init__()` Runs Automatically

This:

```python
class Child(Parent):
    def __init__(self):
        self.value = 10
```

does not automatically execute:

```python
Parent.__init__()
```

If required:

```python
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value = 10
```

---

## 42. Common Mistake: Calling the Parent Class Directly

You may sometimes see:

```python
Parent.__init__(self)
```

This can work in simple cases, but it is generally less flexible than:

```python
super().__init__()
```

`super()` supports cooperative inheritance and respects Python's method resolution order.

For maintainable inheritance hierarchies, `super()` is generally preferable.

---

## 43. Common Mistake: Changing the Method Contract

Suppose:

```python
class Model:
    def predict(self, data):
        ...
```

Then:

```python
class BadModel(Model):
    def predict(self):
        ...
```

Code that expects:

```python
model.predict(data)
```

can fail.

An overriding method should generally preserve compatible calling expectations unless the design intentionally changes the abstraction.

---

## 44. Common Mistake: Overriding Unnecessarily

Do not override a method simply because you can.

If the inherited behavior is already correct:

```python
class Dog(Animal):
    pass
```

is preferable to:

```python
class Dog(Animal):
    def eat(self):
        super().eat()
```

when the subclass adds no meaningful behavior.

Unnecessary overrides add noise without providing value.

---

## 45. Common Mistake: Using Inheritance for Unrelated Behavior

Suppose:

```python
class Logger:
    def log(self, message):
        print(message)
```

and:

```python
class Model(Logger):
    pass
```

This may be inappropriate if a model is not conceptually a logger.

Composition may be better:

```python
class Model:
    def __init__(self):
        self.logger = Logger()
```

The correct design depends on the actual responsibilities and relationships.

---

## 46. Best Practices

### 1. Override for specialization

Use overriding when the child genuinely needs different behavior.

### 2. Preserve the parent contract

Keep method semantics compatible with the base abstraction.

### 3. Use `super()` when extending behavior

Avoid duplicating parent implementation.

### 4. Keep method signatures compatible

Especially when subclasses are used polymorphically.

### 5. Avoid unnecessary overrides

Inherited behavior should be reused when it is already correct.

### 6. Keep inheritance hierarchies coherent

Do not create artificial relationships merely for code reuse.

### 7. Understand MRO

This becomes essential with multiple inheritance and `super()`.

---

## 47. Method Overriding and Software Design

Method overriding is not simply a syntax feature.

It supports a broader design principle:

```text
Common interface
       ↓
Specialized implementations
       ↓
Polymorphic behavior
```

For example:

```text
Model
 │
 ├── LinearModel
 ├── TreeModel
 └── NeuralNetworkModel
```

Each model can implement:

```python
predict()
```

while providing its own internal behavior.

This allows higher-level code to depend on the abstraction rather than each implementation.

---

## 48. Key Takeaways

Method overriding occurs when a subclass defines a method with the same name as an inherited method.

Important points:

* A subclass can replace inherited behavior.
* A subclass can extend inherited behavior.
* `super()` allows access to the next implementation in the MRO.
* Overriding supports polymorphism.
* Overriding is different from traditional method overloading.
* `__init__()` can also be overridden.
* Parent initialization is not automatically executed when a child defines its own `__init__()`.
* Overridden methods should generally preserve the parent contract.
* Python supports polymorphism without inheritance through duck typing.
* Multiple inheritance makes understanding MRO particularly important.
* Inheritance should model meaningful relationships, not merely provide code reuse.

The essential pattern is:

```python
class Parent:
    def action(self):
        print("Parent behavior")


class Child(Parent):
    def action(self):
        print("Child behavior")
```

Or, when extending the parent behavior:

```python
class Child(Parent):
    def action(self):
        super().action()
        print("Additional child behavior")
```

The central principle is:

> **Override inherited behavior when a subclass needs a specialized implementation, while preserving the behavioral contract of the abstraction.**
