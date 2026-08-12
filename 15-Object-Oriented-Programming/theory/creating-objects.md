# Creating Objects

An object is an instance of a class. After defining a class, you create objects by calling the class.

Object creation is fundamental to OOP because the class defines the type and behavior, while each object represents a particular instance with its own state.

---

## 1. Basic Object Creation

Suppose a class has already been defined:

```python
class Student:
    pass
```

An object can be created by calling the class:

```python
student = Student()
```

Here:

* `Student` is the class.
* `Student()` invokes the class.
* `student` refers to the resulting object.

Conceptually:

```text
Student
   │
   │ call
   ↓
Student()
   │
   ↓
student → Student instance
```

---

## 2. A Class Is Callable

For ordinary Python classes, the class object can be called like a function:

```python
student = Student()
```

This does not mean that a class is a function.

Rather, classes are callable objects. Calling a class initiates the process of creating an instance.

You can verify that a class is callable:

```python
class Student:
    pass

print(callable(Student))
```

Output:

```text
True
```

The distinction is:

```text
Function call
    ↓
returns a value

Class call
    ↓
creates/returns an instance
```

The actual class-instantiation process involves Python's object model and methods such as `__new__()` and `__init__()`, which will be introduced later where appropriate.

---

## 3. Creating an Object from a Class

Consider:

```python
class Car:
    pass

car = Car()
```

The class defines the type:

```text
Car
```

The object is:

```text
car → Car instance
```

You can inspect its type:

```python
print(type(car))
```

The result identifies `car` as an instance of `Car`.

---

## 4. Creating Multiple Objects

One class can create many independent objects.

```python
class Student:
    pass

student1 = Student()
student2 = Student()
student3 = Student()
```

Conceptually:

```text
             Student
                │
       ┌────────┼────────┐
       ↓        ↓        ↓
   student1  student2  student3
```

Each variable refers to a separate instance.

You can verify this:

```python
print(student1 is student2)
print(student2 is student3)
```

Output:

```text
False
False
```

---

## 5. Objects Have Different Identities

Each object has its own identity.

```python
class Student:
    pass

student1 = Student()
student2 = Student()

print(id(student1))
print(id(student2))
```

The values are normally different because the objects are distinct.

Remember that `id()` is primarily useful for discussing object identity during the object's lifetime. It should not generally be used as a business identifier for application data.

---

## 6. Creating Objects with Initialization Data

Most useful classes need some initial state.

For example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Objects can now be created with arguments:

```python
student1 = Student("Ali", 20)
student2 = Student("Sara", 22)
```

The objects have different state:

```text
student1
├── name → "Ali"
└── age  → 20

student2
├── name → "Sara"
└── age  → 22
```

The class defines the structure, while the arguments determine the state of each instance.

---

## 7. Arguments Passed During Object Creation

When you write:

```python
student = Student("Ali", 20)
```

the values:

```text
"Ali"
20
```

are supplied to the initialization process.

For the class:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

the arguments correspond to:

```text
name → "Ali"
age  → 20
```

The resulting object retains those values through its instance attributes.

---

## 8. The Role of `__init__()`

`__init__()` is commonly used to initialize a newly created object's state.

Example:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

Create an object:

```python
product = Product("Keyboard", 50)
```

After initialization:

```text
product
├── name  → "Keyboard"
└── price → 50
```

`__init__()` will be covered in detail in a later section.

For now, remember:

> `__init__()` is commonly used to initialize instance state after an instance has been created.

---

## 9. Creating an Object Without `__init__()`

A class does not have to define its own `__init__()`.

```python
class Student:
    pass

student = Student()
```

This is valid.

Python's object model provides inherited behavior that allows the instance to be created even though the class contains no explicit initializer.

---

## 10. Creating Objects with Default Arguments

A class can define default values for initialization parameters:

```python
class Student:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
```

Now both are valid:

```python
student1 = Student("Ali")
student2 = Student("Sara", 21)
```

Their states differ:

```text
student1
├── name → "Ali"
└── age  → 18

student2
├── name → "Sara"
└── age  → 21
```

This follows the same default-argument rules learned with functions.

---

## 11. Creating Objects with Keyword Arguments

Initialization arguments can be supplied by keyword:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Then:

```python
student = Student(name="Ali", age=20)
```

Keyword arguments make the relationship between values and parameters explicit.

They can also be supplied in a different order:

```python
student = Student(age=20, name="Ali")
```

The parameter names determine where the values go.

---

## 12. Creating Objects with Positional Arguments

Arguments can also be supplied positionally:

```python
student = Student("Ali", 20)
```

Here:

```text
"Ali" → name
20    → age
```

The order matters.

If the class defines:

```python
def __init__(self, name, age):
```

then:

```python
Student("Ali", 20)
```

is different from:

```python
Student(20, "Ali")
```

The second version assigns the values to the wrong parameters and may produce incorrect application behavior or later errors.

---

## 13. Positional and Keyword Arguments Together

Python allows positional and keyword arguments to be combined when the ordering rules are respected.

```python
student = Student("Ali", age=20)
```

This means:

```text
name → "Ali"
age  → 20
```

A positional argument must not appear after a keyword argument in the same call.

Invalid:

```python
Student(name="Ali", 20)
```

Python raises a `SyntaxError`.

---

## 14. Creating Objects from Variables

Arguments can come from existing variables:

```python
name = "Ali"
age = 20

student = Student(name, age)
```

The resulting object receives those values.

This is common when object state comes from:

* User input
* Configuration
* Data structures
* API responses
* Database records
* Other objects

---

## 15. Creating Objects from Expressions

Arguments do not have to be literal values.

Expressions can be used:

```python
age = 18

student = Student("Ali", age + 2)
```

The resulting age is:

```text
20
```

Likewise:

```python
student = Student("Ali", 10 + 10)
```

is valid.

Object construction follows normal Python expression evaluation before the class call receives the resulting values.

---

## 16. Creating Objects from Function Results

A function can provide values for object construction:

```python
def get_age():
    return 20
```

Then:

```python
student = Student("Ali", get_age())
```

The function is evaluated first, and its returned value is passed to the class.

This demonstrates that object creation integrates naturally with Python's normal expression and function-call mechanisms.

---

## 17. Assigning the Same Object to Multiple Variables

Consider:

```python
student1 = Student("Ali", 20)
student2 = student1
```

No second object is created.

Instead:

```text
student1 ──┐
           ↓
      Student object
           ↑
student2 ──┘
```

Therefore:

```python
print(student1 is student2)
```

returns:

```text
True
```

Both names refer to the same instance.

---

## 18. Creating Separate Objects

To create separate instances, call the class separately:

```python
student1 = Student("Ali", 20)
student2 = Student("Ali", 20)
```

Even though the values are identical, the instances are separate.

```python
print(student1 is student2)
```

returns:

```text
False
```

Conceptually:

```text
student1 → Student instance A

student2 → Student instance B
```

The two objects may contain equivalent state while still having different identities.

---

## 19. Identity and Equality

Consider:

```python
class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Ali")
student2 = Student("Ali")
```

The objects are different instances:

```python
print(student1 is student2)
```

Output:

```text
False
```

However, equality is a separate concept:

```python
print(student1 == student2)
```

For an ordinary user-defined class that has not customized equality, this will normally also be `False`.

A class can later define custom equality semantics using methods such as `__eq__()`.

The important principle is:

```text
is  → identity
==  → equality
```

---

## 20. Creating Objects in a Loop

Objects can be created repeatedly using loops.

For example:

```python
class Student:
    def __init__(self, name):
        self.name = name

students = []

for name in ["Ali", "Sara", "Hamza"]:
    students.append(Student(name))
```

The list now contains three separate `Student` instances.

Conceptually:

```text
students
│
├── Student("Ali")
├── Student("Sara")
└── Student("Hamza")
```

This illustrates how OOP integrates with Python's data structures and control flow.

---

## 21. Creating Objects from Data

Objects are often created from structured data.

For example:

```python
students_data = [
    ("Ali", 20),
    ("Sara", 22),
    ("Hamza", 19)
]
```

A class can represent each student:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Objects can then be created from the data:

```python
students = []

for name, age in students_data:
    students.append(Student(name, age))
```

Now each record has been transformed into a `Student` object.

This pattern is common in application development.

---

## 22. Creating Objects Inside Functions

Objects can be created inside functions:

```python
class Student:
    def __init__(self, name):
        self.name = name


def create_student():
    return Student("Ali")
```

Calling:

```python
student = create_student()
```

creates a `Student` instance and returns a reference to it.

The object continues to exist as long as it remains reachable.

This demonstrates that objects are not restricted to global or top-level code.

---

## 23. Creating Objects Inside Methods

One object can create or use another object.

```python
class Engine:
    pass


class Car:
    def __init__(self):
        self.engine = Engine()
```

Now:

```python
car = Car()
```

creates a `Car` object and an `Engine` object associated with it.

Conceptually:

```text
Car instance
    │
    └── engine → Engine instance
```

This is an example of composition.

---

## 24. Objects Can Be Passed to Functions

Objects can be passed to ordinary functions.

```python
class Student:
    def __init__(self, name):
        self.name = name


def display_student(student):
    print(student.name)
```

Create an object:

```python
student = Student("Ali")
```

Pass it to the function:

```python
display_student(student)
```

This demonstrates that OOP does not replace functions.

Functions and objects can be combined naturally.

---

## 25. Objects Can Be Returned from Functions

A function can return an object:

```python
def create_student(name):
    return Student(name)
```

Then:

```python
student = create_student("Ali")
```

The caller receives the resulting object.

This pattern is useful for factory functions and other object-creation mechanisms.

---

## 26. Objects Can Be Stored in Collections

Objects can be stored in lists, tuples, sets, dictionaries, and other data structures.

For example:

```python
class Student:
    def __init__(self, name):
        self.name = name


students = [
    Student("Ali"),
    Student("Sara"),
    Student("Hamza")
]
```

Now:

```python
for student in students:
    print(student.name)
```

The loop operates on objects.

This is an important practical pattern because real applications rarely contain only one object.

---

## 27. Creating Objects with Different State

Consider:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
```

Create multiple accounts:

```python
account1 = BankAccount("Ali", 1000)
account2 = BankAccount("Sara", 5000)
account3 = BankAccount("Hamza", 2500)
```

The objects share the same type but maintain different state:

```text
account1
├── owner   → "Ali"
└── balance → 1000

account2
├── owner   → "Sara"
└── balance → 5000

account3
├── owner   → "Hamza"
└── balance → 2500
```

This is the core benefit of instance-based modeling.

---

## 28. Modifying One Object Does Not Normally Modify Another

Given:

```python
account1 = BankAccount("Ali", 1000)
account2 = BankAccount("Sara", 5000)
```

If:

```python
account1.balance = 2000
```

then:

```text
account1.balance → 2000
account2.balance → 5000
```

The instances have independent instance attributes.

This independence is an important property of object state.

However, shared mutable class attributes can create different behavior, which is why understanding class attributes later is important.

---

## 29. Object Creation and References

Python variables hold references to objects.

For example:

```python
student = Student("Ali")
```

Conceptually:

```text
student
   │
   ↓
Student instance
```

When another variable is assigned:

```python
other = student
```

the reference is copied:

```text
student ──┐
          ↓
     Student object
          ↑
other ────┘
```

No new object is created.

---

## 30. Object Creation and Mutability

If an object is mutable, changing it through one reference can be observed through another reference to the same object.

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name


student1 = Student("Ali")
student2 = student1

student2.name = "Sara"

print(student1.name)
```

Output:

```text
Sara
```

Why?

Because:

```text
student1
    │
    └────┐
         ↓
     same object
         ↑
    ┌────┘
student2
```

Both variables refer to the same mutable object.

---

## 31. Object Creation and Garbage Collection

Objects are managed by Python's memory-management system.

Consider:

```python
student = Student("Ali")
```

The variable references the object.

If the reference is removed:

```python
student = None
```

and no other references exist, the object becomes unreachable.

Python can then reclaim its memory.

The exact implementation details depend on the Python implementation. CPython uses reference counting together with cyclic garbage collection.

You generally do not manually free ordinary Python objects.

---

## 32. Object Creation Does Not Mean Permanent Storage

Creating an object in memory does not automatically save it to disk or a database.

For example:

```python
student = Student("Ali")
```

creates an in-memory object.

If an application needs persistent storage, it must explicitly use mechanisms such as:

* Files
* Databases
* Serialization
* External services

Object creation and persistence are separate concepts.

---

## 33. Object Creation in AI/ML

AI and machine-learning software frequently creates objects representing:

* Models
* Datasets
* Training configurations
* Optimizers
* Tokenizers
* Pipelines
* Preprocessors
* Evaluation components

A simplified example:

```python
class Model:
    def __init__(self, name):
        self.name = name

    def predict(self, data):
        print(f"{self.name} is making predictions.")
```

Create an instance:

```python
model = Model("Classifier")
```

Then:

```python
model.predict(data)
```

The object represents a model component with state and behavior.

Real ML frameworks use significantly more sophisticated object systems, but the basic principle remains the same.

---

## 34. Common Errors

### Error 1: Forgetting to call the class

Incorrect:

```python
student = Student
```

This stores the class object itself.

It does not create a `Student` instance.

Correct:

```python
student = Student()
```

---

### Error 2: Missing required initialization arguments

Given:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

This is invalid:

```python
student = Student("Ali")
```

because `age` is required.

Correct:

```python
student = Student("Ali", 20)
```

---

### Error 3: Confusing two references with two objects

This:

```python
student1 = Student("Ali")
student2 = student1
```

creates one object.

This:

```python
student1 = Student("Ali")
student2 = Student("Ali")
```

creates two objects.

---

### Error 4: Using `is` to compare object values

Avoid:

```python
if student1 is student2:
    ...
```

when your intention is to compare logical values.

Use equality semantics:

```python
if student1 == student2:
    ...
```

when appropriate.

---

### Error 5: Assuming object creation automatically persists data

This:

```python
student = Student("Ali")
```

does not save the student to a database or file.

It only creates an in-memory object.

---

## 35. Complete Example

Consider a simple `BankAccount` class:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def display(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")
```

Create two objects:

```python
account1 = BankAccount("Ali", 1000)
account2 = BankAccount("Sara", 5000)
```

Each object has independent state.

```python
account1.deposit(500)
```

Now:

```text
account1.balance → 1500
account2.balance → 5000
```

Display the accounts:

```python
account1.display()
account2.display()
```

The class provides one reusable definition, while the objects represent individual accounts.

---

## 36. Object Creation Mental Model

A useful model is:

```text
Class Definition
       │
       ↓
   Class Object
       │
       │ call
       ↓
   ClassName(...)
       │
       ↓
   Instance Object
       │
       ├── identity
       ├── type
       ├── instance state
       └── access to class-defined behavior
```

For example:

```text
Student
   │
   ├── Student("Ali", 20)
   │       ↓
   │    student1
   │
   └── Student("Sara", 22)
           ↓
        student2
```

Both objects have type `Student`, but they are separate instances.

---

## Summary

Object creation is the process of obtaining instances from a class.

Key points:

* A class is called to create an instance.
* `ClassName()` is the basic object-creation syntax.
* Classes are callable objects.
* `__init__()` commonly initializes instance state.
* Arguments can be passed positionally or by keyword.
* One class can create many objects.
* Separate class calls normally produce separate instances.
* Assigning one object reference to another does not create a new object.
* `is` checks object identity.
* `==` checks equality according to the object's equality semantics.
* Objects can be stored in collections.
* Objects can be passed to and returned from functions.
* Objects can contain references to other objects.
* Object creation produces an in-memory object; it does not automatically provide persistent storage.
* OOP and functions can be used together.
* AI and machine-learning systems frequently use objects to represent models, datasets, pipelines, and other components.

The essential distinction is:

```text
Student("Ali", 20)
        │
        ↓
Creates an instance

student2 = student1
        │
        ↓
Creates another reference
—not another instance
```

Understanding this distinction is essential before moving on to instance attributes and object state.
