# Instance Attributes

Instance attributes are data values associated with a particular object. They represent the **state of an individual instance**.

If a class represents a general concept such as a student, bank account, product, or machine-learning model, instance attributes store the information that makes one instance different from another.

For example, two `Student` objects may have the same structure but different names and ages.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Here:

* `name` and `age` are instance attributes.
* Each `Student` object can have different values for those attributes.
* `self` identifies the particular instance whose state is being accessed.

---

## 1. What Is an Instance Attribute?

An instance attribute is an attribute associated with a specific object.

Consider:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Create an object:

```python
student = Student("Ali", 20)
```

The object has:

```text
student
├── name → "Ali"
└── age  → 20
```

The attributes belong to this particular `student` instance.

Another object can contain different values:

```python
student2 = Student("Sara", 22)
```

Now:

```text
student
├── name → "Ali"
└── age  → 20

student2
├── name → "Sara"
└── age  → 22
```

The class defines the general structure, while each instance maintains its own state.

---

## 2. The `self.attribute` Pattern

Instance attributes are commonly created with:

```python
self.attribute_name = value
```

For example:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

The left side:

```python
self.name
```

refers to an attribute on the current instance.

The right side:

```python
name
```

refers to the parameter passed into `__init__()`.

Therefore:

```python
self.name = name
```

means:

> Store the value received through `name` as the current object's `name` attribute.

---

## 3. Parameters vs Instance Attributes

This distinction is fundamental.

Consider:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

There are two separate names:

```text
name
```

and:

```text
self.name
```

`name` is a local parameter.

`self.name` is an attribute stored on the instance.

When:

```python
student = Student("Ali")
```

executes, the parameter temporarily receives:

```text
name → "Ali"
```

Then:

```python
self.name = name
```

stores that value on the object:

```text
student.name → "Ali"
```

After `__init__()` returns, the parameter no longer exists as a local variable, but the instance attribute remains.

---

## 4. Creating Instance Attributes in `__init__()`

The most common place to initialize instance attributes is `__init__()`.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
```

Create an instance:

```python
car = Car("Toyota", "Corolla")
```

The object now has:

```text
brand → "Toyota"
model → "Corolla"
```

This makes the expected initial state explicit.

---

## 5. Instance Attributes Can Have Different Values

Each instance can have its own values.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
```

Create multiple objects:

```python
employee1 = Employee("Ali", 50000)
employee2 = Employee("Sara", 70000)
```

Their state is independent:

```text
employee1
├── name   → "Ali"
└── salary → 50000

employee2
├── name   → "Sara"
└── salary → 70000
```

The class does not force every instance to have identical attribute values.

---

## 6. Accessing Instance Attributes

Use dot notation:

```python
student.name
```

For example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Ali", 20)

print(student.name)
print(student.age)
```

Output:

```text
Ali
20
```

The expression:

```python
student.name
```

asks Python to retrieve the `name` attribute associated with `student`.

---

## 7. Modifying Instance Attributes

Instance attributes can generally be modified using assignment:

```python
student.age = 21
```

For example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Ali", 20)

student.age = 21

print(student.age)
```

Output:

```text
21
```

The object's state has changed.

---

## 8. Adding an Attribute After Object Creation

Python allows attributes to be added to an instance after it has been created.

```python
class Student:
    def __init__(self, name):
        self.name = name


student = Student("Ali")

student.age = 20
```

The object now contains:

```text
student
├── name → "Ali"
└── age  → 20
```

This is valid Python.

However, it should not automatically be considered good design.

If every `Student` object is expected to have an `age`, it is generally clearer to initialize it in `__init__()`:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Explicit initialization makes the object's expected state easier to understand.

---

## 9. Different Instances Can Have Different Attribute Sets

Because Python objects can often receive attributes dynamically, this is technically possible:

```python
class Student:
    pass


student1 = Student()
student2 = Student()

student1.name = "Ali"
student2.name = "Sara"
student2.age = 22
```

Now `student2` has an `age` attribute while `student1` does not.

This flexibility is part of Python's dynamic object model.

However, classes should normally establish a predictable interface.

If all students require `name` and `age`, define those attributes consistently:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

## 10. Accessing a Missing Attribute

If an object does not contain an attribute and no suitable class-level attribute can satisfy the lookup, Python raises `AttributeError`.

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name


student = Student("Ali")

print(student.age)
```

This raises an error similar to:

```text
AttributeError: 'Student' object has no attribute 'age'
```

This means Python could not find the requested attribute through its attribute lookup process.

---

## 11. Instance Attributes and `self`

Inside an instance method, `self` refers to the current instance.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
```

Create two instances:

```python
student1 = Student("Ali")
student2 = Student("Sara")
```

Calling:

```python
student1.display()
```

causes `self` to refer to `student1`.

Calling:

```python
student2.display()
```

causes `self` to refer to `student2`.

Therefore, the same method can operate on different object state.

---

## 12. Instance Attributes Inside Methods

Methods can read instance attributes:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

Create:

```python
rectangle = Rectangle(10, 5)
```

Then:

```python
print(rectangle.area())
```

Output:

```text
50
```

The method uses:

```python
self.width
self.height
```

to access the state belonging to the current object.

---

## 13. Modifying State Through Methods

Methods can change instance attributes.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

Create:

```python
account = BankAccount(1000)
```

Then:

```python
account.deposit(500)
```

The state changes:

```text
Before:
balance → 1000

After:
balance → 1500
```

This pattern is central to OOP:

```text
Object
├── State
│   └── balance
│
└── Behavior
    └── deposit()
```

The behavior operates on the object's own state.

---

## 14. Instance Attributes Can Store Different Data Types

An instance attribute can reference values of different Python types.

```python
class User:
    def __init__(self, name, age, active):
        self.name = name
        self.age = age
        self.active = active
```

The resulting state may be:

```text
name   → str
age    → int
active → bool
```

Python's dynamic typing means attributes are not required to have a statically declared type.

---

## 15. Instance Attributes Can Store Collections

Instance attributes can also reference lists, dictionaries, sets, tuples, or other objects.

For example:

```python
class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects
```

Create:

```python
student = Student(
    "Ali",
    ["Python", "Mathematics", "AI"]
)
```

Now:

```text
student
├── name     → "Ali"
└── subjects → list
```

The attribute stores a reference to the list object.

This leads to an important distinction between an attribute and the object it references.

---

## 16. Attributes Store References

Python variables and attributes do not conceptually contain the entire object value directly. They reference objects.

Consider:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

When:

```python
student = Student("Ali")
```

the attribute:

```python
student.name
```

references the string object `"Ali"`.

Conceptually:

```text
student
   │
   ↓
Student object
   │
   └── name ─────→ "Ali"
```

This reference model becomes particularly important when instance attributes point to mutable objects.

---

## 17. Mutable Instance Attributes

Consider:

```python
class Student:
    def __init__(self, subjects):
        self.subjects = subjects
```

Create:

```python
subjects = ["Python", "AI"]

student = Student(subjects)
```

Now both:

```python
subjects
```

and:

```python
student.subjects
```

refer to the same list.

Therefore:

```python
subjects.append("ML")
```

also changes what the student sees:

```python
print(student.subjects)
```

Output:

```text
['Python', 'AI', 'ML']
```

The attribute stores a reference to the list; it does not automatically create a copy.

---

## 18. Avoiding Unintended Shared Mutable State

Suppose:

```python
subjects = ["Python", "AI"]

student1 = Student(subjects)
student2 = Student(subjects)
```

Both instances now reference the same list.

Therefore:

```python
student1.subjects.append("ML")
```

can affect:

```python
student2.subjects
```

because both attributes refer to the same mutable object.

If independent lists are required, create separate lists:

```python
student1 = Student(["Python", "AI"])
student2 = Student(["Python", "AI"])
```

or make an explicit copy where appropriate.

This is an important state-management issue in object-oriented Python.

---

## 19. Instance Attributes and Default Mutable Arguments

A related issue can occur when mutable default arguments are used incorrectly.

Avoid:

```python
class Student:
    def __init__(self, subjects=[]):
        self.subjects = subjects
```

The default list is created once when the function definition is evaluated, not once per call.

This can lead to unexpected sharing.

A safer pattern is:

```python
class Student:
    def __init__(self, subjects=None):
        if subjects is None:
            subjects = []

        self.subjects = subjects
```

Now a fresh list is created when no list is supplied.

The broader principle is:

> Be careful when instance attributes reference mutable objects.

---

## 20. Instance Attributes Can Be Updated

Objects often change state over time.

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
```

Usage:

```python
counter = Counter()

counter.increment()
counter.increment()

print(counter.value)
```

Output:

```text
2
```

The object transitions through states:

```text
Initial:
value = 0

After first increment:
value = 1

After second increment:
value = 2
```

This is one of the primary reasons to model a concept as an object.

---

## 21. Instance Attributes and Invariants

A well-designed class may need to maintain certain conditions, called **invariants**.

For example, a bank account may require:

```text
balance >= 0
```

A naive implementation:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
```

allows:

```python
account = BankAccount(-1000)
```

If negative balances are invalid for the application's model, the class should enforce its invariant.

For example:

```python
class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.balance = balance
```

This demonstrates why object state and behavior often belong together.

---

## 22. Direct Attribute Access vs Controlled State Changes

Python permits direct modification:

```python
account.balance = 5000
```

Sometimes this is acceptable.

In other designs, state changes should go through methods:

```python
account.deposit(5000)
```

The second approach can provide a place to enforce business rules.

For example:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
```

The method controls how the state changes.

This becomes particularly relevant when discussing encapsulation.

---

## 23. Instance Attributes Can Be Computed

An instance attribute does not have to be a value directly supplied by the caller.

It can be derived during initialization:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height
```

Now:

```python
rectangle = Rectangle(10, 5)

print(rectangle.area)
```

Output:

```text
50
```

However, whether derived data should be stored or computed dynamically is a design decision.

If the value depends on mutable state:

```python
self.width
self.height
```

storing `area` creates another state value that must remain synchronized.

In such cases, a method or property may be preferable:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

This avoids duplicated state.

---

## 24. Avoiding Redundant State

Consider:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height
```

If:

```python
rectangle.width = 20
```

then `rectangle.area` remains the old value.

The object now contains inconsistent state.

A better design may calculate the area when needed:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

This illustrates an important design principle:

> Do not store derived state unnecessarily when it can be calculated reliably from authoritative state.

---

## 25. Instance Attributes and Object Identity

Two objects can contain identical attribute values while still being different objects.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Ali", 20)
student2 = Student("Ali", 20)
```

The state is equivalent in this example:

```text
student1.name → "Ali"
student2.name → "Ali"

student1.age → 20
student2.age → 20
```

But:

```python
print(student1 is student2)
```

returns:

```text
False
```

Identical state does not imply identical identity.

---

## 26. Inspecting Instance Attributes with `__dict__`

Many ordinary Python objects store instance attributes in a dictionary accessible through `__dict__`.

Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Ali", 20)

print(student.__dict__)
```

A typical result is:

```text
{'name': 'Ali', 'age': 20}
```

This shows the instance's stored attributes.

However, do not assume that every Python object uses `__dict__`. Classes can use mechanisms such as `__slots__`, and built-in or extension types may have different storage models.

Therefore, `__dict__` is useful for understanding ordinary Python objects but is not a universal requirement of objects.

---

## 27. `vars()` and Instance Attributes

For objects that provide a `__dict__`, `vars()` can provide similar information:

```python
print(vars(student))
```

Typical output:

```text
{'name': 'Ali', 'age': 20}
```

Conceptually:

```python
vars(student)
```

is closely related to:

```python
student.__dict__
```

for ordinary objects.

Use such inspection tools mainly for debugging and learning rather than designing application logic around their exact representation.

---

## 28. Instance Attributes vs Class Attributes

Consider:

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name
```

Here:

```text
school
```

is a class attribute.

While:

```text
self.name
```

is an instance attribute.

Conceptually:

```text
Class: Student
└── school → "ABC School"

Instance: student
└── name → "Ali"
```

The distinction is critical because class attributes and instance attributes have different ownership and lookup behavior.

Class attributes are covered in detail later.

---

## 29. Attribute Lookup

When Python evaluates:

```python
student.name
```

it performs attribute lookup according to Python's object model.

For a normal instance, Python first considers attributes associated with the instance and then follows class and inheritance lookup rules as necessary.

This means that:

```python
student.name
```

does not necessarily imply that `name` must physically be stored in `student.__dict__`.

The attribute may be supplied by:

* The instance
* The class
* A parent class
* A descriptor
* Other mechanisms in Python's attribute model

This is why the concept of an **attribute** is broader than simply "a key in `__dict__`."

---

## 30. Naming Instance Attributes

Instance attributes normally follow `snake_case`.

Preferred:

```python
class Student:
    def __init__(self, first_name, student_id):
        self.first_name = first_name
        self.student_id = student_id
```

Avoid:

```python
self.FirstName
self.studentID
self.studentName
```

unless a particular external API or established convention requires a different naming style.

Consistent naming improves readability.

---

## 31. Instance Attributes in AI/ML Systems

Instance attributes are heavily used in AI and machine-learning software.

A simplified model class might look like:

```python
class Model:
    def __init__(self, name, learning_rate):
        self.name = name
        self.learning_rate = learning_rate
```

Create two models:

```python
model1 = Model("Classifier", 0.01)
model2 = Model("Regressor", 0.001)
```

Each model has its own state:

```text
model1
├── name → "Classifier"
└── learning_rate → 0.01

model2
├── name → "Regressor"
└── learning_rate → 0.001
```

A more realistic ML object might contain:

* Model configuration
* Learned parameters
* Hyperparameters
* Training state
* Preprocessing configuration
* Evaluation metadata

Frameworks such as PyTorch and scikit-learn use sophisticated class-based designs to represent these concepts.

---

## 32. Instance Attributes and Encapsulation

Instance attributes are related to encapsulation because a class can control how its internal state is exposed and modified.

For example:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
```

The leading underscore is a convention indicating that `_balance` is intended for non-public use.

Python does not make a single leading underscore a strict access-control mechanism.

Later, encapsulation will cover:

* Public attributes
* Non-public conventions
* Name mangling
* Properties
* Controlled state changes
* Interface design

---

## 33. Common Errors

### Error 1: Forgetting `self`

Incorrect:

```python
class Student:
    def __init__(self, name):
        name = name
```

This does not store the name on the object.

Correct:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

---

### Error 2: Using an attribute before creating it

Incorrect:

```python
class Student:
    def display(self):
        print(self.name)
```

If no `name` attribute has been established through initialization or elsewhere, calling `display()` can raise:

```text
AttributeError
```

A predictable class should establish the state its methods require.

---

### Error 3: Accidentally sharing mutable state

Be careful with:

```python
class Student:
    def __init__(self, subjects=[]):
        self.subjects = subjects
```

Use a `None` default and create a new list when necessary:

```python
class Student:
    def __init__(self, subjects=None):
        if subjects is None:
            subjects = []

        self.subjects = subjects
```

---

### Error 4: Storing unnecessary derived state

Avoid storing values that can become inconsistent with authoritative state.

Instead of:

```python
self.width = width
self.height = height
self.area = width * height
```

consider calculating:

```python
def area(self):
    return self.width * self.height
```

when appropriate.

---

### Error 5: Assuming `__dict__` exists on every object

Not every Python object necessarily exposes instance state through `__dict__`.

Use `__dict__` for inspection when appropriate, not as a universal assumption about Python objects.

---

## 34. Complete Example

Consider a simple `MachineLearningModel` class:

```python
class MachineLearningModel:
    def __init__(self, name, learning_rate, trained=False):
        self.name = name
        self.learning_rate = learning_rate
        self.trained = trained

    def train(self):
        self.trained = True

    def display_status(self):
        status = "trained" if self.trained else "not trained"
        print(f"{self.name}: {status}")
```

Create an instance:

```python
model = MachineLearningModel(
    "Classifier",
    0.01
)
```

Initial state:

```text
name           → "Classifier"
learning_rate  → 0.01
trained        → False
```

Check the status:

```python
model.display_status()
```

Output:

```text
Classifier: not trained
```

Change the object's state:

```python
model.train()
```

Now:

```text
trained → True
```

Check again:

```python
model.display_status()
```

Output:

```text
Classifier: trained
```

The example demonstrates the central relationship:

```text
Instance attributes
        +
Methods that operate on them
        ↓
Object state + behavior
```

---

## 35. Instance Attributes Mental Model

A useful mental model is:

```text
Class
│
├── defines expected structure
├── defines methods
└── defines shared class-level behavior
          │
          ↓
      Instance
          │
          ├── identity
          ├── instance attributes
          └── access to class-defined behavior
```

For example:

```text
Student
│
├── name
├── age
└── introduce()
       │
       ├── student1 → name="Ali", age=20
       │
       └── student2 → name="Sara", age=22
```

The method is defined once by the class, while each instance can maintain different state.

---

## Summary

Instance attributes represent the state of individual objects.

Key points:

* Instance attributes belong to particular instances.
* They are commonly initialized with `self.attribute = value`.
* `self` identifies the current instance inside instance methods.
* Parameters and instance attributes are different concepts.
* Different instances can have different attribute values.
* Attributes can be read with dot notation.
* Attributes can generally be modified through assignment.
* Python allows attributes to be added dynamically, but predictable class design is usually preferable.
* Missing attributes can result in `AttributeError`.
* Instance attributes can reference mutable or immutable objects.
* Multiple attributes can accidentally reference the same mutable object.
* Avoid mutable default arguments when independent state is intended.
* Methods can read and modify instance state.
* Classes can enforce invariants through controlled state changes.
* Derived state should not be stored unnecessarily when doing so can create inconsistency.
* `__dict__` can expose stored instance attributes for many ordinary Python objects, but it is not universal.
* Instance attributes differ from class attributes.
* Attribute lookup involves more than simply checking an instance dictionary.
* Instance state is fundamental to modeling real-world and software concepts.
* AI/ML classes frequently use instance attributes for configuration, parameters, state, and metadata.

The central idea is:

```text
Class
  ↓
defines a type and behavior

Instance
  ↓
owns its own state

Instance attribute
  ↓
stores part of that individual state
```

Understanding instance attributes is essential before studying instance methods, because methods provide the behavior that operates on this state.
