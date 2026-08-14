# Class Methods

A **class method** is a method that receives the class itself as its first argument rather than a particular instance.

Python defines class methods using the `@classmethod` decorator.

The conventional first parameter of a class method is `cls`.

```python
class ClassName:
    @classmethod
    def method_name(cls):
        ...
```

Class methods are useful when behavior logically belongs to the class and needs access to class-level state.

---

## 1. What Is a Class Method?

An ordinary instance method receives an instance:

```python
class Student:
    def display(self):
        print(self)
```

A class method receives the class:

```python
class Student:
    @classmethod
    def display_class(cls):
        print(cls)
```

The distinction is:

```text
Instance method
    ↓
self
    ↓
specific object

Class method
    ↓
cls
    ↓
class
```

---

## 2. The `@classmethod` Decorator

The `@classmethod` decorator tells Python that a method should behave as a class method.

Example:

```python
class Student:
    school = "ABC School"

    @classmethod
    def get_school(cls):
        return cls.school
```

Call it through the class:

```python
print(Student.get_school())
```

Output:

```text
ABC School
```

---

## 3. The `cls` Parameter

The first parameter of a class method is conventionally named `cls`.

```python
class Student:
    @classmethod
    def show_class(cls):
        print(cls)
```

When:

```python
Student.show_class()
```

is called, Python supplies the class automatically.

Conceptually:

```text
cls → Student
```

This is analogous to how `self` refers to an instance in an instance method.

The names `self` and `cls` are conventions, but following them is strongly recommended because they make the code immediately understandable.

---

## 4. Instance Method vs Class Method

Compare:

```python
class Student:
    school = "ABC School"

    def show_name(self):
        print(self.name)

    @classmethod
    def show_school(cls):
        print(cls.school)

    def __init__(self, name):
        self.name = name
```

Here:

```text
show_name()
    ↓
instance method
    ↓
uses self
    ↓
works with individual object state

show_school()
    ↓
class method
    ↓
uses cls
    ↓
works with class-level state
```

---

## 5. Calling a Class Method Through the Class

The most direct form is:

```python
Student.show_school()
```

Example:

```python
class Student:
    school = "ABC School"

    @classmethod
    def get_school(cls):
        return cls.school


print(Student.get_school())
```

Output:

```text
ABC School
```

No instance is required.

This is one of the main advantages of class methods.

---

## 6. Calling a Class Method Through an Instance

A class method can also be accessed through an instance:

```python
student = Student()

print(student.get_school())
```

Python still passes the class to the method, not the instance.

Conceptually:

```text
student.get_school()
       ↓
Student.get_school()
       ↓
cls = Student
```

Therefore, class methods do not become instance methods simply because they are accessed through an instance.

For clarity, class methods are usually called through the class when no instance is required.

---

## 7. Class Methods Can Access Class Attributes

Consider:

```python
class Employee:
    company = "TechCorp"

    @classmethod
    def get_company(cls):
        return cls.company
```

Then:

```python
print(Employee.get_company())
```

returns:

```text
TechCorp
```

The method accesses:

```python
cls.company
```

because `cls` represents the class.

---

## 8. Class Methods Can Modify Class State

A class method can also modify class attributes.

Example:

```python
class User:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1
```

Call:

```python
User.increment_count()
```

Then:

```python
print(User.count)
```

produces:

```text
1
```

The method operates on class-level state.

---

## 9. Class-Level Counter

A common educational example is counting created objects:

```python
class User:
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
```

Create objects:

```python
user1 = User("Ali")
user2 = User("Sara")
user3 = User("Ahmed")
```

Then:

```python
print(User.get_count())
```

produces:

```text
3
```

The counter belongs to the class, so a class method is a natural interface for retrieving it.

---

## 10. Why Use `cls` Instead of the Class Name?

You could write:

```python
class User:
    count = 0

    @classmethod
    def get_count(cls):
        return User.count
```

But this is less flexible.

Prefer:

```python
class User:
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count
```

Using `cls` allows the method to work naturally with subclasses.

---

## 11. Class Methods and Inheritance

Consider:

```python
class Animal:
    category = "Animal"

    @classmethod
    def get_category(cls):
        return cls.category


class Dog(Animal):
    category = "Dog"
```

Then:

```python
print(Animal.get_category())
print(Dog.get_category())
```

Output:

```text
Animal
Dog
```

Why?

Because:

```python
Dog.get_category()
```

passes:

```text
cls → Dog
```

rather than:

```text
cls → Animal
```

This is an important advantage of using `cls`.

---

## 12. `cls` Refers to the Calling Class

Consider:

```python
class Parent:
    @classmethod
    def identify(cls):
        print(cls.__name__)


class Child(Parent):
    pass
```

Calling:

```python
Parent.identify()
```

produces:

```text
Parent
```

Calling:

```python
Child.identify()
```

produces:

```text
Child
```

The inherited class method receives the class through which it was invoked.

---

## 13. Class Methods as Alternative Constructors

One of the most important practical uses of class methods is implementing **alternative constructors**.

Suppose:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

The normal construction interface is:

```python
person = Person("Ali", 20)
```

But suppose the data is available as a string:

```text
Ali,20
```

A class method can provide another construction path:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))
```

Now:

```python
person = Person.from_string("Ali,20")
```

The class method constructs and returns a new object.

---

## 14. Why Use `cls()` in Alternative Constructors?

Notice:

```python
return cls(name, int(age))
```

rather than:

```python
return Person(name, int(age))
```

Using `cls()` makes the method inheritance-friendly.

Consider:

```python
class Employee(Person):
    pass
```

Then:

```python
employee = Employee.from_string("Ali,20")
```

Because `cls` is `Employee`, the method can construct an `Employee` instance.

This is a major reason alternative constructors use `cls`.

---

## 15. Alternative Constructor Example

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_string(cls, data):
        name, price = data.split(",")
        return cls(name, float(price))
```

Normal construction:

```python
product1 = Product("Keyboard", 50.0)
```

Alternative construction:

```python
product2 = Product.from_string("Mouse,25.5")
```

Both create `Product` instances but accept different input formats.

---

## 16. Alternative Constructor from a Dictionary

Class methods can also construct objects from dictionaries.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["age"]
        )
```

Then:

```python
data = {
    "name": "Ali",
    "age": 20
}

student = Student.from_dict(data)
```

This pattern is common when converting external data into domain objects.

---

## 17. Alternative Constructor from JSON-Like Data

For example:

```python
class ModelConfig:
    def __init__(self, learning_rate, epochs):
        self.learning_rate = learning_rate
        self.epochs = epochs

    @classmethod
    def from_dict(cls, data):
        return cls(
            learning_rate=data["learning_rate"],
            epochs=data["epochs"]
        )
```

Usage:

```python
config_data = {
    "learning_rate": 0.01,
    "epochs": 100
}

config = ModelConfig.from_dict(config_data)
```

This is a common pattern in configuration-driven software.

---

## 18. Class Methods and AI/ML APIs

Many machine-learning systems need multiple ways to create configuration or model objects.

For example:

```python
class ModelConfig:
    def __init__(self, learning_rate, epochs):
        self.learning_rate = learning_rate
        self.epochs = epochs

    @classmethod
    def default(cls):
        return cls(
            learning_rate=0.01,
            epochs=100
        )
```

Then:

```python
config = ModelConfig.default()
```

This provides a meaningful named construction method.

---

## 19. Class Method vs Static Method

These two decorators are often confused.

### Class method

```python
@classmethod
def method(cls):
    ...
```

Receives the class automatically.

### Static method

```python
@staticmethod
def method():
    ...
```

Receives neither the instance nor the class automatically.

The distinction is:

```text
Instance method
    self → instance

Class method
    cls → class

Static method
    no automatic self/cls
```

Static methods are covered in the next section.

---

## 20. Class Method vs Instance Method

Use an instance method when behavior depends on a particular object's state.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

`deposit()` needs:

```python
self.balance
```

Therefore it should be an instance method.

Use a class method when behavior operates on class-level state or constructs instances through the class.

```python
class BankAccount:
    @classmethod
    def from_balance(cls, balance):
        return cls(balance)
```

The construction logic does not require an existing account instance.

---

## 21. Class Methods Do Not Need an Existing Instance

This:

```python
class User:
    @classmethod
    def create_default(cls):
        return cls("Unknown")
```

can be called as:

```python
user = User.create_default()
```

No `User` instance existed before the call.

This makes class methods useful for class-level factories and alternative constructors.

---

## 22. Class Method as a Factory

A **factory method** is a method that creates and returns an object.

Example:

```python
class Model:
    def __init__(self, model_type):
        self.model_type = model_type

    @classmethod
    def classifier(cls):
        return cls("classifier")

    @classmethod
    def regressor(cls):
        return cls("regressor")
```

Usage:

```python
classifier = Model.classifier()
regressor = Model.regressor()
```

The class method provides a descriptive construction interface.

---

## 23. Factory Methods Can Improve Readability

Compare:

```python
model = Model("classifier")
```

with:

```python
model = Model.classifier()
```

The second form communicates intent more explicitly.

This can be useful when object construction involves meaningful configuration choices.

---

## 24. Class Methods and Validation

A class method can validate or transform external input before constructing an object.

```python
class User:
    def __init__(self, username):
        self.username = username

    @classmethod
    def from_email(cls, email):
        username = email.split("@")[0]
        return cls(username)
```

Then:

```python
user = User.from_email("ali@example.com")
```

The class method acts as a controlled construction path.

For production systems, validation should also consider malformed input and edge cases.

---

## 25. Class Methods and `cls.__name__`

Because `cls` refers to the class, you can access class metadata.

```python
class Model:
    @classmethod
    def describe(cls):
        return f"Class: {cls.__name__}"
```

Then:

```python
print(Model.describe())
```

produces:

```text
Class: Model
```

A subclass:

```python
class NeuralNetwork(Model):
    pass
```

can call:

```python
print(NeuralNetwork.describe())
```

and receive:

```text
Class: NeuralNetwork
```

---

## 26. Class Methods and Inheritance-Friendly Construction

Consider:

```python
class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        return cls(name)
```

Then:

```python
class Student(Person):
    pass
```

Calling:

```python
student = Student.create("Ali")
```

creates a `Student`.

This works because:

```python
cls
```

is `Student` during the call.

If the method instead used:

```python
return Person(name)
```

it would always create a `Person`, preventing the construction method from naturally adapting to subclasses.

---

## 27. Class Methods and Class-Level Counters

A class method can expose shared state without requiring direct attribute access.

```python
class Connection:
    active_connections = 0

    @classmethod
    def get_active_connections(cls):
        return cls.active_connections
```

Then:

```python
print(Connection.get_active_connections())
```

This provides a method-based interface to class-level state.

Whether direct attribute access or a method is better depends on the design.

---

## 28. Class Methods and Encapsulation

A class method can control how class-level state is accessed or modified.

For example:

```python
class Configuration:
    _environment = "development"

    @classmethod
    def get_environment(cls):
        return cls._environment

    @classmethod
    def set_environment(cls, environment):
        cls._environment = environment
```

Usage:

```python
print(Configuration.get_environment())

Configuration.set_environment("production")
```

The underscore communicates that `_environment` is intended to be non-public.

Python does not enforce private access in the same way as some languages.

---

## 29. Class Method Naming

Use descriptive names for class-level operations.

Good examples:

```python
from_string()
from_dict()
from_json()
create_default()
create_from_config()
get_count()
reset_counter()
```

Names such as these communicate the method's purpose.

---

## 30. Class Methods and State Reset

A class method can reset class-level state:

```python
class User:
    count = 0

    @classmethod
    def reset_count(cls):
        cls.count = 0
```

Then:

```python
User.reset_count()
```

This can be useful in controlled contexts such as tests.

However, global class-level state should be used carefully because it can introduce hidden dependencies between operations.

---

## 31. Class Methods in Testing

Suppose:

```python
class Registry:
    items = []

    @classmethod
    def reset(cls):
        cls.items.clear()
```

A test suite may call:

```python
Registry.reset()
```

to return the shared registry to a known state.

This is one example of a class-level operation.

In larger applications, dependency injection and isolated state are often preferable to extensive global class state.

---

## 32. Class Methods and `super()`

Class methods can also participate in inheritance and use `super()`.

Example:

```python
class Parent:
    value = 10

    @classmethod
    def show(cls):
        print(cls.value)


class Child(Parent):
    value = 20

    @classmethod
    def show_parent_value(cls):
        print(super().value)
```

Here, `super()` provides access to the parent part of the inheritance relationship.

The details of `super()` become more important when inheritance and method resolution order are covered.

---

## 33. Class Method Decorator Order

Decorators can be combined with other decorators, and order can matter.

For beginner-level class methods, the standard form is:

```python
class Example:
    @classmethod
    def method(cls):
        ...
```

Do not confuse:

```python
@classmethod
```

with:

```python
@staticmethod
```

They create different method binding behavior.

---

## 34. Class Method and Descriptor Behavior

Technically, `classmethod` is implemented through Python's descriptor protocol.

The decorator changes how the function is bound when accessed through the class or an instance.

For example:

```python
class Example:
    @classmethod
    def method(cls):
        ...
```

When accessed:

```python
Example.method
```

Python produces a bound method whose first argument is the class.

This is an implementation detail that becomes useful when studying Python's data model and descriptors.

For practical OOP programming, remember:

> `@classmethod` automatically binds the class as the first argument.

---

## 35. A Complete Example

Consider:

```python
class Student:
    school = "ABC School"
    student_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.student_count += 1

    @classmethod
    def get_school(cls):
        return cls.school

    @classmethod
    def get_student_count(cls):
        return cls.student_count

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))
```

Normal construction:

```python
student1 = Student("Ali", 20)
```

Alternative construction:

```python
student2 = Student.from_string("Sara,21")
```

Class-level information:

```python
print(Student.get_school())
print(Student.get_student_count())
```

Output:

```text
ABC School
2
```

This single class demonstrates three common uses:

```text
get_school()
    ↓
read class state

get_student_count()
    ↓
read shared class state

from_string()
    ↓
alternative constructor
```

---

## 36. AI/ML Example: Model Configuration

Consider:

```python
class ModelConfig:
    DEFAULT_EPOCHS = 100

    def __init__(self, learning_rate, epochs):
        self.learning_rate = learning_rate
        self.epochs = epochs

    @classmethod
    def default(cls, learning_rate=0.01):
        return cls(
            learning_rate=learning_rate,
            epochs=cls.DEFAULT_EPOCHS
        )
```

Then:

```python
config = ModelConfig.default()
```

creates a configuration using the class's default epoch count.

This is cleaner than requiring callers to know every default value.

---

## 37. AI/ML Example: Constructing Models

Consider:

```python
class Model:
    def __init__(self, model_type, learning_rate):
        self.model_type = model_type
        self.learning_rate = learning_rate

    @classmethod
    def classifier(cls, learning_rate=0.01):
        return cls("classifier", learning_rate)

    @classmethod
    def regressor(cls, learning_rate=0.01):
        return cls("regressor", learning_rate)
```

Usage:

```python
classifier = Model.classifier()
regressor = Model.regressor(0.001)
```

The class methods provide meaningful construction interfaces.

This pattern is conceptually similar to factory-style APIs frequently encountered in software libraries.

---

## 38. When Should You Use a Class Method?

A class method is appropriate when:

1. The operation needs the class itself.
2. The operation accesses or modifies class-level state.
3. The operation creates instances in an inheritance-friendly way.
4. The operation provides an alternative construction interface.
5. The behavior logically belongs to the class rather than an individual object.

Examples include:

```text
from_string()
from_dict()
from_config()
create_default()
get_count()
reset_state()
```

---

## 39. When Should You Not Use a Class Method?

Do not use `@classmethod` merely because a method happens not to need `self`.

If a method performs a generic calculation and needs neither instance nor class state, a static method may be more appropriate.

For example:

```python
class MathTools:
    @staticmethod
    def square(value):
        return value * value
```

There is no reason for this operation to receive `cls`.

The distinction should be based on semantics and dependencies, not preference.

---

## 40. Common Mistake: Forgetting `@classmethod`

Incorrect:

```python
class Student:
    def get_school(cls):
        return cls.school
```

Calling:

```python
Student.get_school()
```

does not automatically pass the class in the way a class method expects.

Correct:

```python
class Student:
    school = "ABC School"

    @classmethod
    def get_school(cls):
        return cls.school
```

---

## 41. Common Mistake: Using `self` in a Class Method

Incorrect:

```python
class Student:
    @classmethod
    def get_school(self):
        return self.school
```

This may technically execute because parameter names are not enforced, but it is misleading.

Use:

```python
class Student:
    @classmethod
    def get_school(cls):
        return cls.school
```

The `cls` convention communicates that the parameter refers to the class.

---

## 42. Common Mistake: Constructing the Base Class Directly

Consider:

```python
class Person:
    @classmethod
    def create(cls, name):
        return Person(name)
```

This defeats the inheritance-friendly behavior of `cls`.

Prefer:

```python
class Person:
    @classmethod
    def create(cls, name):
        return cls(name)
```

Now subclasses can inherit the construction behavior naturally.

---

## 43. Common Mistake: Treating Class Methods as Static Methods

This:

```python
class Model:
    @classmethod
    def create(cls):
        return cls()
```

depends on the class.

This:

```python
class MathTools:
    @staticmethod
    def square(value):
        return value * value
```

does not.

Do not select decorators based on syntax alone.

Ask what the method actually depends on.

---

## 44. Decision Guide

Use this simplified decision process:

```text
Does the method need instance state?
        │
       Yes
        ↓
   Instance method
       self

        No
        │
        ↓
Does it need class state
or class-aware construction?
        │
       Yes
        ↓
    Class method
       cls

        No
        ↓
    Static method
```

This is not a complete model of every Python design possibility, but it is a useful practical guideline.

---

## Summary

A class method is a method bound to a class rather than a particular instance.

Key points:

* Use the `@classmethod` decorator.
* The first parameter is conventionally `cls`.
* `cls` refers to the class involved in the call.
* Class methods can be called without creating an instance first.
* They can access class attributes.
* They can modify class-level state.
* They can work naturally with inheritance.
* They are commonly used as alternative constructors.
* `cls(...)` allows inheritance-friendly object creation.
* They can implement factory-style construction interfaces.
* They differ from instance methods because they receive the class rather than an object.
* They differ from static methods because static methods receive neither `self` nor `cls` automatically.
* Class methods should be used when the operation logically depends on the class.

The fundamental syntax is:

```python
class ClassName:
    @classmethod
    def method_name(cls, ...):
        ...
```

A common alternative-constructor pattern is:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))
```

Then:

```python
person = Person.from_string("Ali,20")
```

The essential distinction is:

```text
Instance method
    → self
    → individual object

Class method
    → cls
    → class

Static method
    → no automatic self/cls
    → independent operation
```

Understanding this distinction prepares you for the next topic: **static methods**.
