# Class Attributes

A **class attribute** is an attribute defined on a class rather than created separately for each instance.

Class attributes represent data that is logically associated with the class itself or is intended to be shared by instances.

Example:

```python
class Student:
    school = "ABC School"
```

Here, `school` is a class attribute.

Objects created from `Student` can access it:

```python
student1 = Student()
student2 = Student()

print(student1.school)
print(student2.school)
```

Both objects can access the same class-level value.

---

## 1. Class Attributes vs Instance Attributes

The most important distinction is where the attribute belongs.

### Class attribute

```python
class Student:
    school = "ABC School"
```

The attribute is defined on the class.

### Instance attribute

```python
class Student:
    def __init__(self, name):
        self.name = name
```

The attribute belongs to an individual instance.

Conceptually:

```text
Student class
│
└── school → "ABC School"

student1
└── name → "Ali"

student2
└── name → "Sara"
```

The class attribute is associated with the class, while `name` is stored independently for each object.

---

## 2. Defining a Class Attribute

A class attribute is normally defined directly inside the class body:

```python
class Student:
    school = "ABC School"
    country = "Pakistan"
```

These attributes belong to the class namespace.

They can be accessed through the class:

```python
print(Student.school)
print(Student.country)
```

Output:

```text
ABC School
Pakistan
```

---

## 3. Accessing Class Attributes Through Instances

Instances can also access class attributes:

```python
class Student:
    school = "ABC School"


student = Student()

print(student.school)
```

Output:

```text
ABC School
```

Python's attribute lookup mechanism searches the instance and then the class when appropriate.

Therefore:

```python
student.school
```

can resolve to:

```python
Student.school
```

when no instance attribute named `school` exists.

---

## 4. Attribute Lookup

Understanding lookup order is important.

Consider:

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name
```

For:

```python
student = Student("Ali")
```

the expression:

```python
student.name
```

finds `name` in the instance.

The expression:

```python
student.school
```

does not find `school` in the instance, so Python can find it on the class.

A simplified model is:

```text
student.school
     ↓
instance namespace
     ↓
not found
     ↓
class namespace
     ↓
"ABC School"
```

Actual Python attribute lookup can involve inheritance and descriptors, so this is a simplified model.

---

## 5. Class Attributes Are Not Automatically Copied Into Instances

Suppose:

```python
class Student:
    school = "ABC School"
```

and:

```python
student = Student()
```

It is tempting to think Python creates:

```python
student.school = "ABC School"
```

automatically.

That is not what happens.

The value remains associated with the class unless an instance attribute with the same name is explicitly created.

This distinction becomes important when modifying class attributes.

---

## 6. Class Attribute Access Through the Class

The clearest way to access class-level data is often:

```python
Student.school
```

rather than:

```python
student.school
```

Using the class makes the intended ownership clearer.

Example:

```python
class Student:
    school = "ABC School"

print(Student.school)
```

This communicates that `school` belongs to the class-level definition.

---

## 7. Class Attributes Can Represent Shared Information

Class attributes are useful when the same conceptual value applies to all instances.

For example:

```python
class Employee:
    company = "TechCorp"
```

Every employee belongs to the same company:

```python
employee1 = Employee()
employee2 = Employee()
```

Both can access:

```python
print(employee1.company)
print(employee2.company)
```

Both resolve to:

```text
TechCorp
```

---

## 8. Class Attributes as Constants

Class attributes can also represent values intended to remain constant during normal program execution.

Example:

```python
class Circle:
    PI = 3.141592653589793
```

Then:

```python
print(Circle.PI)
```

The uppercase naming convention communicates that `PI` is intended to be treated as a constant.

Python does not enforce immutability merely because the name is uppercase.

This:

```python
Circle.PI = 4
```

is technically possible.

Therefore, uppercase names represent a convention rather than a language-level restriction.

---

## 9. Class Attributes and Configuration

A class attribute can provide shared configuration.

```python
class Model:
    framework = "Python"
    default_learning_rate = 0.01
```

Then:

```python
print(Model.framework)
print(Model.default_learning_rate)
```

This can be useful when the values logically belong to the class rather than to one particular object.

---

## 10. Class Attributes vs Instance Attributes

Consider:

```python
class Student:
    school = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Here:

```text
school
    ↓
class attribute

name
    ↓
instance attribute

age
    ↓
instance attribute
```

Create two objects:

```python
student1 = Student("Ali", 20)
student2 = Student("Sara", 21)
```

The state can be viewed as:

```text
Student
└── school → "ABC School"

student1
├── name → "Ali"
└── age → 20

student2
├── name → "Sara"
└── age → 21
```

---

## 11. Instance Attributes Can Shadow Class Attributes

Consider:

```python
class Student:
    school = "ABC School"
```

Create:

```python
student = Student()
```

Initially:

```python
print(student.school)
```

produces:

```text
ABC School
```

Now assign:

```python
student.school = "XYZ School"
```

This creates an instance attribute named `school`.

Now:

```python
print(student.school)
```

produces:

```text
XYZ School
```

But:

```python
print(Student.school)
```

still produces:

```text
ABC School
```

The instance attribute **shadows** the class attribute for that particular object.

---

## 12. Shadowing Diagram

After:

```python
student.school = "XYZ School"
```

the structure is conceptually:

```text
Student class
└── school → "ABC School"

student instance
└── school → "XYZ School"
```

When Python evaluates:

```python
student.school
```

the instance attribute takes precedence.

When Python evaluates:

```python
Student.school
```

it accesses the class attribute.

---

## 13. Assigning Through an Instance Does Not Usually Modify the Class Attribute

This is a common beginner mistake.

Consider:

```python
class Student:
    school = "ABC School"
```

Then:

```python
student = Student()

student.school = "XYZ School"
```

This does **not** generally change:

```python
Student.school
```

Instead, it creates an instance attribute.

Therefore:

```python
print(student.school)
print(Student.school)
```

produces:

```text
XYZ School
ABC School
```

---

## 14. Modifying the Class Attribute

To modify the shared class attribute, assign through the class:

```python
class Student:
    school = "ABC School"
```

Then:

```python
Student.school = "XYZ School"
```

Now:

```python
student1 = Student()
student2 = Student()

print(student1.school)
print(student2.school)
```

both resolve to:

```text
XYZ School
```

provided neither instance has its own `school` attribute.

---

## 15. Existing Instance Attributes Can Hide Class Changes

Consider:

```python
class Student:
    school = "ABC School"
```

Create:

```python
student1 = Student()
student2 = Student()
```

Then:

```python
student1.school = "Private School"
```

Now:

```text
student1.school → "Private School"
student2.school → "ABC School"
```

If the class changes:

```python
Student.school = "XYZ School"
```

then:

```text
student1.school → "Private School"
student2.school → "XYZ School"
```

The class-level value changed, but `student1` continues using its own instance attribute.

---

## 16. Reading vs Writing Class Attributes Through Instances

These operations behave differently:

### Reading

```python
student.school
```

can find the value on the class if it is absent from the instance.

### Writing

```python
student.school = "XYZ School"
```

normally creates or updates an instance attribute.

This distinction is critical:

```text
Read through instance
    ↓
may use class attribute

Write through instance
    ↓
normally affects instance namespace
```

---

## 17. Inspecting Instance Attributes with `__dict__`

For ordinary Python objects, you can inspect the instance namespace using `__dict__`.

Example:

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name


student = Student("Ali")

print(student.__dict__)
```

You will see something similar to:

```text
{'name': 'Ali'}
```

Notice that `school` is not stored in the instance dictionary.

It is stored in the class namespace.

You can inspect:

```python
print(Student.__dict__)
```

which contains the class's attributes and methods.

The exact representation contains additional entries generated by Python.

---

## 18. `__dict__` Is an Implementation-Level View

`__dict__` is useful for learning and debugging, but code should not generally depend on every detail of an object's internal dictionary.

Some Python objects can use alternative storage mechanisms such as `__slots__`.

Therefore:

```python
object.__dict__
```

should not be assumed to exist for every possible Python object.

---

## 19. Class Attributes with Mutable Objects

Class attributes can contain mutable objects:

```python
class Student:
    subjects = []
```

This is dangerous if the intention is for every student to have an independent list.

Consider:

```python
student1 = Student()
student2 = Student()

student1.subjects.append("Python")
```

Now:

```python
print(student2.subjects)
```

may produce:

```text
['Python']
```

because both instances resolve `subjects` to the same class-level list.

This is usually not the desired behavior for per-instance state.

---

## 20. Correct Use of Instance Mutable State

If each object should have its own list, initialize it in `__init__()`:

```python
class Student:
    def __init__(self):
        self.subjects = []
```

Now:

```python
student1 = Student()
student2 = Student()

student1.subjects.append("Python")
```

produces:

```python
print(student1.subjects)
print(student2.subjects)
```

Output:

```text
['Python']
[]
```

Each instance has a separate list.

---

## 21. Shared Mutable Class State

A shared mutable class attribute can be intentional.

For example:

```python
class Event:
    all_events = []
```

If the design explicitly requires every instance to contribute to one shared collection, this may be appropriate.

However, this design should be deliberate because all instances access the same mutable object.

---

## 22. Class Attributes for Counting Instances

A class attribute can maintain a shared counter.

Example:

```python
class User:
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1
```

Create objects:

```python
user1 = User("Ali")
user2 = User("Sara")
user3 = User("Ahmed")
```

Then:

```python
print(User.count)
```

produces:

```text
3
```

The counter belongs to the class because it represents a property of the class as a whole.

---

## 23. Why `User.count` Is Used

Inside:

```python
User.count += 1
```

the code explicitly modifies the class attribute.

If you wrote:

```python
self.count += 1
```

the behavior would be different.

Python would first look up `count`, potentially find the class attribute, calculate the new value, and then assignment through `self` would create an instance attribute.

Therefore, when intentionally modifying shared class-level state, accessing the class explicitly is usually clearer.

---

## 24. A Better Class-Level Counter Pattern

For a simple educational example:

```python
class User:
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1
```

This clearly communicates:

```text
self.name
    ↓
instance state

User.count
    ↓
class state
```

This distinction is valuable when learning object-oriented design.

---

## 25. Class Attributes and Inheritance

Class attributes participate in inheritance.

Consider:

```python
class Animal:
    kingdom = "Animalia"


class Dog(Animal):
    pass
```

Then:

```python
print(Dog.kingdom)
```

produces:

```text
Animalia
```

The subclass can access the inherited class attribute.

Conceptually:

```text
Dog
 ↓
Animal
 ↓
kingdom
```

Python's class attribute lookup follows the inheritance hierarchy when the attribute is not found directly on the subclass.

---

## 26. Overriding an Inherited Class Attribute

A subclass can define an attribute with the same name:

```python
class Animal:
    kingdom = "Animalia"


class Dog(Animal):
    kingdom = "Animalia - Dog"
```

Now:

```python
print(Animal.kingdom)
print(Dog.kingdom)
```

produces:

```text
Animalia
Animalia - Dog
```

The subclass's attribute takes precedence for lookup through `Dog`.

---

## 27. Instance Attributes Can Also Override Inherited Attributes

Consider:

```python
class Animal:
    category = "Animal"


class Dog(Animal):
    pass
```

Then:

```python
dog = Dog()
dog.category = "Domestic Animal"
```

Now:

```python
print(dog.category)
```

produces:

```text
Domestic Animal
```

while:

```python
print(Dog.category)
```

produces:

```text
Animal
```

Again, the instance attribute shadows the class attribute.

---

## 28. Class Attributes and `self`

A class attribute can be accessed through `self`:

```python
class Student:
    school = "ABC School"

    def display_school(self):
        print(self.school)
```

This works because attribute lookup can reach the class when the instance does not have its own `school`.

However, if the method specifically intends to access the class-level attribute, using:

```python
Student.school
```

can make the intent clearer.

---

## 29. `self.attribute` vs `ClassName.attribute`

Compare:

```python
class Student:
    school = "ABC School"

    def show(self):
        print(self.school)
        print(Student.school)
```

Both may produce the same value initially.

But they do not express exactly the same intent.

```python
self.school
```

means:

> Find `school` relative to this instance.

```python
Student.school
```

means:

> Access `school` directly from this class.

This distinction matters when instance-level shadowing exists.

---

## 30. Class Attributes and `type(self)`

In reusable class designs, hard-coding the class name can sometimes be less flexible.

For example:

```python
class Model:
    version = 1

    def display_version(self):
        print(type(self).version)
```

`type(self)` refers to the actual class of the current object.

This can matter when subclasses are involved.

For example:

```python
class AdvancedModel(Model):
    version = 2
```

An `AdvancedModel` instance can resolve:

```python
type(self).version
```

to:

```text
2
```

This is an advanced technique and should be used only when the design requires it.

---

## 31. Class Attributes and Class Methods

Class attributes often work together with class methods.

Example:

```python
class User:
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1

    @classmethod
    def total_users(cls):
        return cls.count
```

Then:

```python
print(User.total_users())
```

returns the number of created users.

The relationship is:

```text
class attribute
      ↓
shared class state
      ↓
class method
      ↓
operates on class state
```

Class methods are covered separately.

---

## 32. Class Attributes in AI and Machine Learning

Class attributes can represent metadata or configuration shared across instances.

For example:

```python
class Model:
    framework = "Python"
    model_type = "Machine Learning"
```

Every instance can access:

```python
model.framework
model.model_type
```

However, model-specific state should normally be instance-level:

```python
class Model:
    framework = "Python"

    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
        self.weights = None
```

Here:

```text
framework
    ↓
shared class-level information

learning_rate
weights
    ↓
instance-specific state
```

---

## 33. Example: Shared Model Registry

A more realistic conceptual example is:

```python
class Model:
    registry = []

    def __init__(self, name):
        self.name = name
        Model.registry.append(self)
```

Create:

```python
model1 = Model("Classifier")
model2 = Model("Regressor")
```

Now:

```python
print(Model.registry)
```

contains references to both model objects.

This represents shared class-level state.

However, global/shared registries introduce coupling and lifecycle concerns, so production systems should use them deliberately.

---

## 34. Class Attributes Should Represent Class-Level Concepts

A useful design question is:

> Does this value describe the class or this specific object?

If it describes every object collectively:

```python
class Company:
    industry = "Software"
```

may be appropriate.

If it differs for each object:

```python
class Employee:
    def __init__(self, name):
        self.name = name
```

should use an instance attribute.

The distinction is about **ownership and semantics**, not merely syntax.

---

## 35. Class Attributes Are Not Automatically Constants

This:

```python
class Config:
    MAX_RETRIES = 3
```

looks like a constant.

But Python does not prevent:

```python
Config.MAX_RETRIES = 10
```

The uppercase name communicates intent.

Python's naming conventions do not enforce immutability.

---

## 36. Class Attributes and Immutable Values

Immutable values such as:

```python
int
float
str
tuple
frozenset
```

are often safer as shared class attributes when they represent class-level constants.

For example:

```python
class NeuralNetwork:
    DEFAULT_LEARNING_RATE = 0.001
```

An instance can read:

```python
model.DEFAULT_LEARNING_RATE
```

but class-level access is often clearer:

```python
NeuralNetwork.DEFAULT_LEARNING_RATE
```

---

## 37. Class Attributes and Mutable Values Require Care

Consider:

```python
class Model:
    layers = []
```

This means every instance resolving `layers` can access the same list.

If each model should have its own layers, use:

```python
class Model:
    def __init__(self):
        self.layers = []
```

The distinction is:

```text
Model.layers
    ↓
one shared list

self.layers
    ↓
one list per instance
```

This is one of the most important practical differences between class and instance attributes.

---

## 38. Example: Class Attribute Used Correctly

A class-wide default can be appropriate:

```python
class Model:
    DEFAULT_BATCH_SIZE = 32

    def __init__(self, batch_size=None):
        if batch_size is None:
            batch_size = self.DEFAULT_BATCH_SIZE

        self.batch_size = batch_size
```

Then:

```python
model1 = Model()
model2 = Model(64)
```

produces:

```text
model1.batch_size → 32
model2.batch_size → 64
```

The default belongs conceptually to the class, while the selected batch size belongs to each model instance.

---

## 39. Class Attribute as a Default Is Not the Same as an Instance Attribute

Consider:

```python
class Model:
    DEFAULT_BATCH_SIZE = 32

    def __init__(self, batch_size=None):
        self.batch_size = (
            self.DEFAULT_BATCH_SIZE
            if batch_size is None
            else batch_size
        )
```

There are two different concepts:

```text
DEFAULT_BATCH_SIZE
    ↓
class-level default

batch_size
    ↓
instance-specific configuration
```

This is often a clean design.

---

## 40. Common Mistake: Expecting Instance Assignment to Update the Class

Incorrect assumption:

```python
student.school = "XYZ School"
```

will change:

```python
Student.school
```

It normally will not.

Instead:

```python
student.school = "XYZ School"
```

creates or updates:

```text
student.school
```

while:

```python
Student.school
```

remains unchanged.

To change the class attribute:

```python
Student.school = "XYZ School"
```

---

## 41. Common Mistake: Using Class Attributes for Per-Object Mutable State

Avoid:

```python
class Student:
    subjects = []
```

when each student should have independent subjects.

Use:

```python
class Student:
    def __init__(self):
        self.subjects = []
```

This ensures each instance receives a separate list.

---

## 42. Common Mistake: Assuming All Instance Attributes Must Be Defined in `__init__()`

This is not a strict Python requirement.

For example:

```python
class Student:
    def add_email(self, email):
        self.email = email
```

An `email` attribute can be created later.

However, if an attribute is a fundamental part of the object's expected state, defining it during initialization usually makes the class easier to reason about.

For example:

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.email = None
```

This establishes a predictable object state.

---

## 43. Class Attribute Lookup with Inheritance

Consider:

```python
class A:
    value = 10


class B(A):
    pass


class C(B):
    pass
```

Then:

```python
print(C.value)
```

finds `value` through the inheritance hierarchy.

Conceptually:

```text
C
↓
B
↓
A
↓
value = 10
```

Python's method resolution order, or **MRO**, determines the lookup sequence in inheritance hierarchies.

MRO becomes especially important with multiple inheritance.

---

## 44. A Practical Example

Consider a simple AI experiment class:

```python
class Experiment:
    framework = "Python"
    version = 1

    def __init__(self, name, learning_rate):
        self.name = name
        self.learning_rate = learning_rate
        self.results = []
```

Create:

```python
experiment1 = Experiment("Classification", 0.01)
experiment2 = Experiment("Regression", 0.001)
```

The state can be viewed as:

```text
Experiment
├── framework → "Python"
└── version → 1

experiment1
├── name → "Classification"
├── learning_rate → 0.01
└── results → []

experiment2
├── name → "Regression"
├── learning_rate → 0.001
└── results → []
```

This demonstrates a sensible distinction between shared metadata and per-experiment state.

---

## 45. Design Rule

When deciding between a class attribute and an instance attribute, ask:

### Is the value shared conceptually?

Use a class attribute.

```python
class Model:
    FRAMEWORK = "Python"
```

### Is the value specific to each object?

Use an instance attribute.

```python
class Model:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
```

### Is it mutable and should each instance have its own copy?

Initialize it per instance.

```python
class Model:
    def __init__(self):
        self.layers = []
```

This simple decision rule prevents many common OOP design errors.

---

## Summary

Class attributes belong to the class rather than being independently stored on each instance.

Key points:

* Class attributes are defined in the class body.
* They can be accessed through the class.
* Instances can also read class attributes through normal attribute lookup.
* Instance attributes normally belong to individual objects.
* Instance attributes can shadow class attributes.
* Assigning through an instance normally creates or updates an instance attribute.
* Assigning through the class modifies the class attribute.
* Mutable class attributes are shared and therefore require careful design.
* Per-instance mutable state should generally be initialized in `__init__()`.
* Class attributes can represent shared configuration, metadata, defaults, or constants by convention.
* Class attributes participate in inheritance.
* Subclasses can override inherited class attributes.
* `__dict__` can help demonstrate the difference between instance and class namespaces.
* Class-level counters and registries are possible but should be used deliberately.
* In AI/ML software, class attributes can represent shared defaults or metadata, while model-specific state normally belongs to instances.

The essential distinction is:

```text
Class Attribute
    ↓
shared class-level concept

Instance Attribute
    ↓
individual object's state
```

For example:

```python
class Model:
    DEFAULT_BATCH_SIZE = 32

    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
        self.weights = None
```

Here:

```text
DEFAULT_BATCH_SIZE
    → class-level default

learning_rate
    → instance-specific configuration

weights
    → instance-specific model state
```

Understanding this distinction is necessary before moving to **class methods**, where methods intentionally operate in relation to the class rather than a particular instance.
