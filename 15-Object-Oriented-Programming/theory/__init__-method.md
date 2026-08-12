# The `__init__()` Method

The `__init__()` method is a special method commonly used to initialize an object's state immediately after an instance is created.

It is one of the most frequently used methods in Python classes because it provides a convenient place to assign initial instance attributes.

Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

When an object is created:

```python
student = Student("Ali", 20)
```

Python invokes `__init__()` for that newly created instance.

The resulting object has:

```python
student.name
student.age
```

---

## 1. What Does `__init__()` Mean?

The name `__init__` contains double underscores on both sides.

```python
__init__
```

Methods with this naming convention are commonly called **special methods** or **dunder methods**.

The purpose of `__init__()` is to initialize an already-created instance.

A simplified conceptual sequence is:

```text
Create instance
      ↓
Initialize instance
      ↓
__init__()
      ↓
Object ready for use
```

This distinction matters because `__init__()` is technically an **initializer**, not the method responsible for allocating the instance itself.

---

## 2. Basic Syntax

The general pattern is:

```python
class ClassName:
    def __init__(self, parameters):
        self.attribute = value
```

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

Create an object:

```python
student = Student("Ali")
```

Now:

```python
print(student.name)
```

produces:

```text
Ali
```

---

## 3. Why Use `__init__()`?

Without `__init__()`, attributes can still technically be assigned after an object is created:

```python
class Student:
    pass


student = Student()
student.name = "Ali"
student.age = 20
```

Although valid, this approach does not guarantee that every `Student` object is initialized consistently.

Using `__init__()` provides a predictable initialization interface:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Now:

```python
student = Student("Ali", 20)
```

creates an object with the expected initial state.

---

## 4. `__init__()` and `self`

The first parameter of `__init__()` is conventionally `self`.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

Here:

```text
self
 ↓
current instance

name
 ↓
argument supplied by caller
```

When:

```python
student = Student("Ali")
```

is executed, conceptually:

```text
self → student
name → "Ali"
```

Therefore:

```python
self.name = name
```

means:

```text
store "Ali" in the student's name attribute
```

---

## 5. `__init__()` Is Called Automatically

You normally do not call `__init__()` directly.

When:

```python
student = Student("Ali")
```

is executed, Python handles the initialization process automatically.

You should normally write:

```python
student = Student("Ali")
```

rather than:

```python
student.__init__("Ali")
```

The second form is technically callable but is not the normal way to initialize an object.

---

## 6. Constructor vs Initializer

Python terminology requires some precision here.

In many introductory tutorials, `__init__()` is called a **constructor**.

Strictly speaking, this is not completely accurate.

Python's object creation process involves `__new__()` and `__init__()`:

```text
__new__()
   ↓
creates the instance
   ↓
__init__()
   ↓
initializes the instance
```

Therefore:

* `__new__()` is responsible for creating the instance.
* `__init__()` initializes the already-created instance.

For ordinary classes, you will usually work with `__init__()` and rarely need to override `__new__()`.

For beginner and practical Python programming, the phrase "constructor" is commonly used for `__init__()`, but **initializer** is technically more precise.

---

## 7. A Simple Example

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
```

Create an object:

```python
car = Car("Toyota", "Corolla")
```

The object now contains:

```text
brand → "Toyota"
model → "Corolla"
```

Access the attributes:

```python
print(car.brand)
print(car.model)
```

Output:

```text
Toyota
Corolla
```

---

## 8. Multiple Parameters

`__init__()` can accept multiple parameters.

```python
class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
```

Create an object:

```python
employee = Employee(
    "Sara",
    "Engineering",
    75000
)
```

The instance now stores three pieces of state.

```python
print(employee.name)
print(employee.department)
print(employee.salary)
```

---

## 9. Default Parameters in `__init__()`

You can use default values.

```python
class User:
    def __init__(self, name, active=True):
        self.name = name
        self.active = active
```

Now:

```python
user1 = User("Ali")
user2 = User("Sara", False)
```

Their state differs:

```text
user1.active → True
user2.active → False
```

Default arguments can make object creation more flexible.

---

## 10. Required vs Optional Initialization Data

Consider:

```python
class Product:
    def __init__(self, name, price, category="General"):
        self.name = name
        self.price = price
        self.category = category
```

Here:

```text
name
price
```

are required.

```text
category
```

has a default value.

Therefore:

```python
product = Product("Keyboard", 50)
```

is valid.

Python assigns:

```python
product.category
```

the value:

```text
General
```

---

## 11. `__init__()` Can Validate Input

Initialization is a useful place to validate an object's initial state.

```python
class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.balance = balance
```

Valid:

```python
account = BankAccount(1000)
```

Invalid:

```python
account = BankAccount(-100)
```

The second call raises a `ValueError`.

Validation helps prevent objects from beginning in an invalid state.

---

## 12. `__init__()` Can Normalize Data

Initialization can also normalize incoming values.

```python
class User:
    def __init__(self, username):
        self.username = username.strip().lower()
```

If:

```python
user = User("  Alice  ")
```

then:

```python
print(user.username)
```

produces:

```text
alice
```

The class stores a normalized representation.

---

## 13. `__init__()` Should Initialize Object State

A common responsibility of `__init__()` is establishing the attributes required by the object's design.

For example:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
```

The object now has the state required by methods such as:

```python
def area(self):
    return self.width * self.height
```

A well-designed class generally initializes the state that its methods depend on.

---

## 14. Calling Methods After Initialization

`__init__()` can establish state that instance methods later use.

```python
class Counter:
    def __init__(self, start=0):
        self.value = start

    def increment(self):
        self.value += 1

    def get_value(self):
        return self.value
```

Usage:

```python
counter = Counter(10)

counter.increment()

print(counter.get_value())
```

Output:

```text
11
```

The relationship is:

```text
__init__()
   ↓
establish initial state
   ↓
instance methods
   ↓
use or modify state
```

---

## 15. `__init__()` Does Not Return the Object

A critical rule is that `__init__()` must return `None`.

Correct:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

Incorrect:

```python
class Student:
    def __init__(self, name):
        self.name = name
        return self
```

This causes a `TypeError` when object construction is attempted.

The object itself is created separately, and `__init__()` initializes it.

---

## 16. `__init__()` Must Not Return Another Value

For example:

```python
class Student:
    def __init__(self, name):
        self.name = name
        return "Student"
```

This is invalid.

Python expects `__init__()` to return `None`.

Do not use `return` to return an object from `__init__()`.

If an object-producing operation is required, use a normal method or an appropriate class-level construction technique.

---

## 17. `__init__()` Can Contain Conditional Logic

Normal Python statements can be used in `__init__()`.

```python
class Student:
    def __init__(self, name, age):
        self.name = name

        if age >= 18:
            self.status = "Adult"
        else:
            self.status = "Minor"
```

Create:

```python
student = Student("Ali", 20)
```

Then:

```python
print(student.status)
```

Output:

```text
Adult
```

---

## 18. `__init__()` Can Initialize Collections

An object can contain lists, dictionaries, sets, or other data structures.

```python
class ShoppingCart:
    def __init__(self):
        self.items = []
```

Now:

```python
cart1 = ShoppingCart()
cart2 = ShoppingCart()
```

Each object receives its own list.

This is important because mutable values should normally be created per instance rather than shared unintentionally.

---

## 19. Avoid Mutable Default Arguments

A common mistake is:

```python
class ShoppingCart:
    def __init__(self, items=[]):
        self.items = items
```

The default list is created once and can be shared across instances.

Prefer:

```python
class ShoppingCart:
    def __init__(self, items=None):
        if items is None:
            items = []

        self.items = items
```

Now each call without `items` creates a new list.

An even simpler version is:

```python
class ShoppingCart:
    def __init__(self):
        self.items = []
```

When initialization requires mutable state, create the mutable object inside `__init__()` when appropriate.

---

## 20. Multiple Instances Get Separate State

Consider:

```python
class Counter:
    def __init__(self):
        self.value = 0
```

Create:

```python
counter1 = Counter()
counter2 = Counter()
```

Then:

```python
counter1.value = 10
```

does not change:

```python
counter2.value
```

The result is:

```text
counter1.value → 10
counter2.value → 0
```

The `self` reference ensures that the attribute belongs to the current instance.

---

## 21. `__init__()` and Instance Independence

Consider:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

Create:

```python
student1 = Student("Ali")
student2 = Student("Sara")
```

The state is:

```text
student1.name → "Ali"
student2.name → "Sara"
```

The class defines the structure, while each object maintains its own instance state.

---

## 22. Calling `__init__()` Explicitly

Technically, you can do:

```python
student.__init__("Sara")
```

However, this is not normal object initialization.

It directly invokes the initializer on an existing object.

For example:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

Then:

```python
student = Student("Ali")
student.__init__("Sara")
```

The object's state may now be:

```text
student.name → "Sara"
```

This is valid Python behavior, but it should not generally be used as a replacement for constructing a new object.

---

## 23. Reinitializing an Existing Object

Calling `__init__()` manually effectively reinitializes the object according to the initializer's code.

This can produce surprising results if the class has complex state.

For example:

```python
class Counter:
    def __init__(self, value=0):
        self.value = value
```

Then:

```python
counter = Counter(10)
counter.__init__()
```

changes:

```text
counter.value
```

from:

```text
10
```

to:

```text
0
```

This demonstrates why direct calls to `__init__()` should generally be avoided in ordinary application code.

---

## 24. `__init__()` and Inheritance

When inheritance is introduced, a subclass may define its own `__init__()`.

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
```

Here, the subclass's initializer replaces the inherited initializer for normal construction.

However, this duplicates initialization logic.

A more maintainable approach can use `super()`:

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

`super()` will be covered in detail in the inheritance section.

---

## 25. Parent Initialization Matters

Consider:

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed
```

Now:

```python
dog = Dog("Max", "Labrador")
```

The subclass initializer does not initialize `name`.

Therefore:

```python
print(dog.name)
```

will fail because the attribute was never established by `Dog.__init__()`.

If the parent initialization is required, use:

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

---

## 26. `__init__()` and Composition

An initializer can create or receive other objects.

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self, engine):
        self.engine = engine
```

Usage:

```python
engine = Engine()
car = Car(engine)
```

Now:

```python
car.engine
```

refers to the `Engine` object.

This is a basic example of dependency injection and composition.

Alternatively:

```python
class Car:
    def __init__(self):
        self.engine = Engine()
```

creates the dependency internally.

The appropriate approach depends on the design and desired coupling.

---

## 27. Dependency Injection Through `__init__()`

Consider:

```python
class Logger:
    def log(self, message):
        print(message)


class Application:
    def __init__(self, logger):
        self.logger = logger

    def run(self):
        self.logger.log("Application started")
```

Usage:

```python
logger = Logger()
app = Application(logger)

app.run()
```

The `Application` receives its dependency instead of constructing it itself.

This can improve testability and reduce tight coupling.

---

## 28. `__init__()` and AI/ML Configuration

In machine-learning software, `__init__()` commonly establishes configuration.

For example:

```python
class Model:
    def __init__(self, learning_rate, epochs):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
```

Create:

```python
model = Model(
    learning_rate=0.01,
    epochs=100
)
```

The object now retains its configuration:

```text
learning_rate → 0.01
epochs        → 100
weights       → None
```

Later methods can use this state:

```python
model.train(data)
model.predict(data)
```

This pattern is common in object-oriented ML APIs.

---

## 29. Configuration vs Learned State

A useful distinction in ML-oriented classes is:

```text
Configuration
    ↓
learning_rate
epochs
batch_size

Learned state
    ↓
weights
biases
parameters
```

`__init__()` may establish both initial configuration and placeholders for state that will be populated later.

For example:

```python
class Model:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
        self.weights = None
```

Then:

```python
def train(self, data):
    self.weights = ...
```

The exact implementation depends on the model.

---

## 30. `__init__()` and Object Invariants

An **invariant** is a condition that should remain true for a valid object.

For example:

```python
class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.balance = balance
```

This establishes the invariant:

```text
balance >= 0
```

If later methods also preserve this invariant, the object remains valid.

This is an important aspect of object-oriented design.

---

## 31. Keep Initialization Focused

A good `__init__()` generally establishes the object's initial state.

Avoid putting excessive unrelated work into it.

For example, an initializer that:

* Connects to several external services
* Downloads large datasets
* Trains a machine-learning model
* Sends emails
* Starts background processes

may create difficult construction behavior.

Prefer explicit operations when work is expensive or has significant external side effects.

For example:

```python
model = Model(config)
model.load_weights()
model.train(data)
```

can be clearer than performing all of these operations automatically inside `__init__()`.

---

## 32. `__init__()` and Side Effects

Initialization can have side effects, but they should be considered carefully.

Compare:

```python
class Model:
    def __init__(self, path):
        self.path = path
        self.load_model()
```

with:

```python
class Model:
    def __init__(self, path):
        self.path = path

    def load_model(self):
        ...
```

The second design makes object construction cheaper and more predictable.

There is no universal rule that `__init__()` must have no side effects, but expensive or failure-prone operations should not be placed there without a clear reason.

---

## 33. `__init__()` and Class Attributes

Instance initialization and class attributes are different concepts.

Example:

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name
```

Here:

```text
school
    ↓
class attribute

self.name
    ↓
instance attribute
```

Each object receives its own `name`, while `school` is defined at the class level.

Class attributes are covered separately in this module.

---

## 34. `__init__()` Without Parameters

Not every class needs external initialization data.

```python
class Counter:
    def __init__(self):
        self.value = 0
```

Usage:

```python
counter = Counter()
```

The initializer establishes the default state.

---

## 35. `__init__()` Can Initialize Multiple Related Attributes

For example:

```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.active = True
        self.login_count = 0
```

The initializer establishes the initial state in one predictable place.

This makes the class easier to understand because readers can quickly identify which attributes exist immediately after construction.

---

## 36. A Complete Example

Consider:

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount

    def get_balance(self):
        return self.balance
```

Create:

```python
account = BankAccount("Ali", 1000)
```

`__init__()` establishes:

```text
owner   → "Ali"
balance → 1000
```

Then:

```python
account.deposit(500)
```

changes:

```text
balance → 1500
```

The initializer establishes the initial state, while the instance methods manage subsequent behavior.

---

## 37. Common Errors

### Error 1: Incorrect spelling

Incorrect:

```python
def _init_(self):
    ...
```

Correct:

```python
def __init__(self):
    ...
```

There are **two underscores before and after** `init`.

---

### Error 2: Missing `self`

Incorrect:

```python
class Student:
    def __init__(name):
        self.name = name
```

Correct:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

---

### Error 3: Forgetting `self.`

Incorrect:

```python
class Student:
    def __init__(self, name):
        name = name
```

This does not create instance state.

Correct:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

---

### Error 4: Returning a value

Incorrect:

```python
class Student:
    def __init__(self, name):
        self.name = name
        return self
```

`__init__()` must return `None`.

---

### Error 5: Mutable default argument

Avoid:

```python
class Cart:
    def __init__(self, items=[]):
        self.items = items
```

Prefer:

```python
class Cart:
    def __init__(self, items=None):
        self.items = [] if items is None else items
```

---

### Error 6: Assuming `__init__()` creates the object

Technically, this is inaccurate.

The simplified lifecycle is:

```text
__new__()
   ↓
instance creation
   ↓
__init__()
   ↓
instance initialization
```

For ordinary classes, you generally only need to define `__init__()`.

---

## 38. `__init__()` vs Ordinary Methods

Compare:

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")
```

The roles are different.

### `__init__()`

```text
Called during object construction
↓
Establishes initial state
```

### `introduce()`

```text
Called explicitly by the program
↓
Performs normal object behavior
```

This distinction helps clarify the purpose of special methods.

---

## 39. `__init__()` vs `__new__()`

For technical accuracy:

```text
__new__()
    ↓
creates/returns an instance

__init__()
    ↓
initializes that instance
```

A simplified example:

```python
class Student:
    def __new__(cls, name):
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        self.name = name
```

`__new__()` is an advanced mechanism and is not normally needed for ordinary class design.

The important beginner-level rule is:

> Use `__init__()` to initialize instance state.

---

## 40. AI/ML-Oriented Example

A simplified model class might look like:

```python
class LinearModel:
    def __init__(self, learning_rate=0.01, epochs=100):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = 0.0
        self.is_trained = False

    def train(self, X, y):
        print("Training model...")
        self.weights = []
        self.is_trained = True

    def predict(self, X):
        if not self.is_trained:
            raise RuntimeError("Model has not been trained")

        return []
```

When:

```python
model = LinearModel()
```

the initializer establishes:

```text
learning_rate → 0.01
epochs        → 100
weights       → None
bias          → 0.0
is_trained    → False
```

After:

```python
model.train(X, y)
```

the object's state changes.

This illustrates an important OOP pattern used in stateful machine-learning APIs:

```text
Construction
    ↓
Configuration
    ↓
Training
    ↓
Updated model state
    ↓
Prediction
```

---

## Summary

`__init__()` is Python's standard instance initializer.

Key points:

* `__init__()` is a special method.
* It is called automatically during normal object construction.
* Its primary purpose is to initialize instance state.
* The first parameter is conventionally `self`.
* Parameters supplied during object creation are received by `__init__()`.
* `self.attribute = value` creates or initializes instance attributes.
* Initialization can validate and normalize input.
* `__init__()` can establish object invariants.
* `__init__()` must return `None`.
* `__init__()` is technically an initializer, not the method that creates the instance.
* `__new__()` participates in instance creation.
* Mutable default arguments should generally be avoided.
* Each instance can receive independent state through `self`.
* Subclasses may need to call parent initialization with `super()`.
* `__init__()` should generally establish state rather than perform excessive unrelated work.
* In AI and ML software, `__init__()` frequently establishes model configuration and initial state.

The central lifecycle is:

```text
Class()
   ↓
__new__()
   ↓
instance created
   ↓
__init__()
   ↓
instance initialized
   ↓
object ready for use
```

And the fundamental initialization pattern is:

```python
class ClassName:
    def __init__(self, value):
        self.value = value
```

When:

```python
object = ClassName(value)
```

is executed, the supplied value becomes part of that particular object's state.
