# Object-Oriented Programming Quiz — Answer Key

> **Module:** 15 — Object-Oriented Programming
> **Python Version:** Python 3.13+
> **Difficulty:** Beginner → Intermediate
> **Total Questions:** 60

## Overview

This answer key provides the correct answers and technical explanations for
the Object-Oriented Programming assessment.

Use this file only after completing `oop-quiz.md`.

---

# Part 1 — Multiple Choice

## 1. What is a class in Python?

**Answer:** B

**Explanation:**
A class is a definition that describes a type. It can define attributes and
methods that determine the state and behavior of its instances.

---

## 2. What is an object?

**Answer:** A

**Explanation:**
An object is an instance of a class. A class can be used to create multiple
independent instances.

---

## 3. Which statement best describes instantiation?

**Answer:** B

**Explanation:**
Instantiation is the process of creating an instance of a class. For example,
`Student()` creates an instance of `Student`.

---

## 4. Which syntax creates an instance of `Student`?

**Answer:** C

**Explanation:**
Calling a class creates an instance of that class:

```python
student = Student()
```

The other choices either assign the class itself or use syntax that is not
valid Python.

---

## 5. Which statement best describes an instance attribute?

**Answer:** A

**Explanation:**
An instance attribute represents state associated with a particular object.
For example:

```python
student.name = "Aisha"
```

The value belongs to that specific `student` instance.

---

## 6. Which statement correctly describes a class attribute?

**Answer:** B

**Explanation:**
A class attribute is defined in the class namespace and is associated with the
class. Instances can access it through normal attribute lookup when they do
not provide an attribute with the same name.

---

## 7. Which statement is correct?

**Answer:** C

**Explanation:**
`company` is defined directly in the class body, so it is a class attribute.
`self.name` is created on individual instances, so `name` is an instance
attribute.

---

## 8. Why can two instances of the same class have different values for an instance attribute?

**Answer:** A

**Explanation:**
Each instance maintains its own instance state. For example:

```python
student1.name = "Aisha"
student2.name = "Bilal"
```

Both objects belong to the same class but contain different values.

---

## 9. What happens when an instance does not contain an attribute being accessed?

**Answer:** B

**Explanation:**
Python performs attribute lookup according to its object and class lookup
rules. If the attribute is not found on the instance, Python can find it on
the class or through other parts of the lookup process.

---

## 10. What happens when an instance defines an attribute with the same name as a class attribute?

**Answer:** B

**Explanation:**
The instance attribute normally takes precedence when accessed through that
instance.

For example:

```python
class Device:
    category = "Electronic"

phone = Device()
phone.category = "Mobile"
```

`phone.category` is `"Mobile"`, while `Device.category` remains
`"Electronic"`.

---

## 11. What does `self` conventionally refer to inside an instance method?

**Answer:** B

**Explanation:**
`self` is the conventional name for the parameter that refers to the current
instance.

For example:

```python
class Student:
    def show_name(self):
        print(self.name)
```

When `student.show_name()` is called, `self` refers to `student`.

---

## 12. Which statement about `self` is technically correct?

**Answer:** C

**Explanation:**
`self` is not a Python keyword. It is the established convention for naming
the instance parameter of an instance method.

Although another name can technically be used, `self` should normally be used
for readability and consistency.

---

## 13. Why is `self.name` different from `name` inside an instance method?

**Answer:** A

**Explanation:**
`self.name` performs attribute access on the current instance.

A bare `name` is resolved according to Python's variable scope rules and may
refer to a local variable, enclosing variable, global variable, or built-in,
depending on the context.

---

## 14. What is the primary purpose of `__init__()`?

**Answer:** A

**Explanation:**
`__init__()` initializes an instance after the instance has been created.

It is commonly used to establish initial instance state:

```python
def __init__(self, name):
    self.name = name
```

Object creation and initialization are separate stages in Python's object
model.

---

## 15. Which statement about `__init__()` is correct?

**Answer:** B

**Explanation:**
`__init__()` initializes the state of an already-created instance.

It is not required for every class, and it should not return the instance.
The object creation protocol involves `__new__()` followed by `__init__()` when
appropriate.

---

## 16. Which decorator defines a class method?

**Answer:** B

**Explanation:**
`@classmethod` transforms a method so that it receives the class as its first
implicit argument.

Example:

```python
class Person:
    @classmethod
    def create(cls):
        return cls()
```

---

## 17. What does a class method conventionally receive as its first parameter?

**Answer:** C

**Explanation:**
The conventional name is `cls`.

It refers to the class on which the class method was invoked.

---

## 18. What does a static method automatically receive?

**Answer:** D

**Explanation:**
A static method does not receive an implicit instance or class argument.

Arguments required by the method must be supplied explicitly.

---

## 19. Which situation is generally appropriate for a static method?

**Answer:** C

**Explanation:**
A static method is useful when behavior logically belongs to a class but does
not need access to instance state or class state.

For example:

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
```

---

## 20. Which situation is commonly appropriate for a class method?

**Answer:** A

**Explanation:**
Class methods are commonly used for alternative constructors or operations
that need access to the class itself.

For example:

```python
class User:
    @classmethod
    def from_name(cls, name):
        return cls(name)
```

Using `cls` allows subclasses to participate correctly in many such designs.

---

## 21. Which relationship is generally represented by inheritance?

**Answer:** B

**Explanation:**
Inheritance generally represents an **is-a** relationship.

For example:

```text
Dog is an Animal.
```

Inheritance should represent a genuine subtype relationship rather than being
used merely to reuse implementation.

---

## 22. What is method overriding?

**Answer:** A

**Explanation:**
Method overriding occurs when a subclass provides its own implementation of a
method inherited from a superclass.

Example:

```python
class Animal:
    def speak(self):
        print("Animal")


class Dog(Animal):
    def speak(self):
        print("Dog")
```

---

## 23. What is the primary purpose of `super()`?

**Answer:** B

**Explanation:**
`super()` returns a proxy that performs attribute lookup according to the
method resolution order (MRO).

It is commonly used to extend inherited behavior:

```python
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog")
```

---

## 24. What does polymorphism allow?

**Answer:** B

**Explanation:**
Polymorphism allows different objects to be used through compatible behavior
or interfaces.

The objects do not necessarily need to belong to the same inheritance
hierarchy.

---

## 25. What is duck typing?

**Answer:** B

**Explanation:**
Duck typing focuses on whether an object supports the operations required by
the code rather than requiring a specific class or inheritance relationship.

The principle is commonly summarized as:

> If an object supports the required behavior, it can be used.

---

# Part 2 — True or False

## 26. A class and an object are the same thing.

**Answer:** False

**Explanation:**
A class is a definition of a type, while an object is an instance of that
class.

---

## 27. Multiple instances can be created from the same class.

**Answer:** True

**Explanation:**
A class can be instantiated multiple times.

Each resulting instance can maintain independent state.

---

## 28. Two instances of the same class can maintain different instance attribute values.

**Answer:** True

**Explanation:**
Instance attributes belong to individual instances.

For example:

```python
student1.name = "Aisha"
student2.name = "Bilal"
```

The two objects can have different values.

---

## 29. `self` is a Python keyword.

**Answer:** False

**Explanation:**
`self` is a convention, not a keyword.

Python does not reserve the name `self`, although using another name is
strongly discouraged in normal code because it violates established Python
conventions.

---

## 30. `__init__()` initializes an instance after the instance has been created.

**Answer:** True

**Explanation:**
`__init__()` is an initializer. It receives the newly created instance and
usually establishes its initial state.

---

## 31. A class attribute can be accessed through an instance if the instance does not provide an attribute with the same name.

**Answer:** True

**Explanation:**
Python's attribute lookup can continue from the instance to its class.

Example:

```python
class Device:
    category = "Electronic"

device = Device()

print(device.category)
```

This prints:

```text
Electronic
```

---

## 32. A static method automatically receives `self`.

**Answer:** False

**Explanation:**
A static method receives neither an implicit instance argument nor an implicit
class argument.

---

## 33. A class method conventionally receives `cls` as its first parameter.

**Answer:** True

**Explanation:**
`cls` is the conventional parameter name for the class passed to a class
method.

---

## 34. Duck typing requires classes to share the same superclass.

**Answer:** False

**Explanation:**
Duck typing is based on supported behavior, not a required inheritance
relationship.

---

## 35. Composition commonly represents a has-a relationship.

**Answer:** True

**Explanation:**
Composition represents objects that contain or collaborate with other objects.

For example:

```text
Car has an Engine.
```

---

# Part 3 — Code Output

## 36. What is the output?

**Answer:** C

```text
Aisha
```

**Explanation:**
The `Student` initializer assigns `"Aisha"` to the instance attribute
`self.name`.

Therefore:

```python
student.name
```

returns `"Aisha"`.

---

## 37. What is the output?

**Answer:** B

```text
5
```

**Explanation:**
The instance begins with:

```python
self.value = 4
```

Calling `increment()` executes:

```python
self.value += 1
```

The resulting value is `5`.

---

## 38. What is the output?

**Answer:** B

```text
Electronic
Electronic
```

**Explanation:**
`category` is a class attribute.

Neither `phone` nor `laptop` defines its own `category`, so attribute lookup
finds the value on `Device`.

---

## 39. What is the output?

**Answer:** C

```text
Mobile
Electronic
```

**Explanation:**
This assignment:

```python
phone.category = "Mobile"
```

creates an instance attribute on `phone`.

It does not modify the class attribute:

```python
Device.category
```

Therefore the two accesses produce different values.

---

## 40. What is the output?

**Answer:** C

```text
2
```

**Explanation:**
The class attribute starts at `0`.

Each call to `Employee()` executes:

```python
Employee.count += 1
```

Two instances are created, so the final value is `2`.

---

## 41. What is the output?

**Answer:** C

```text
7
```

**Explanation:**
`add()` is a static method, so it receives `3` and `4` as explicit arguments.

The expression:

```python
3 + 4
```

produces `7`.

---

## 42. What is the output?

**Answer:** B

```text
Human
```

**Explanation:**
`Person.get_species()` invokes the class method with `Person` as `cls`.

Therefore:

```python
cls.species
```

resolves to:

```text
Human
```

---

## 43. What is the output?

**Answer:** B

```text
Dog
```

**Explanation:**
`Dog` overrides the `speak()` method inherited from `Animal`.

When:

```python
dog.speak()
```

is called, Python dispatches to the implementation defined in `Dog`.

---

## 44. What is the output?

**Answer:** C

```text
Animal
Dog
```

**Explanation:**
The subclass method first calls:

```python
super().speak()
```

which invokes the inherited `Animal.speak()` implementation.

After that, the subclass prints `"Dog"`.

---

## 45. What is the output?

**Answer:** C

```text
Printing
Scanning
```

**Explanation:**
`process()` does not require a particular class.

It only requires an object that provides:

```python
print_document()
```

`Printer` and `Scanner` both provide that behavior, demonstrating duck
typing.

---

## 46. What is the output?

**Answer:** B

```text
Child
```

**Explanation:**
`Child` defines its own `value` class attribute.

Therefore, when `child.value` is accessed, the value defined in `Child`
takes precedence over the inherited `Parent.value`.

---

## 47. What is the output?

**Answer:** C

```text
Parent Child
```

**Explanation:**
`Child.message()` first calls:

```python
super().message()
```

which returns `"Parent"`.

The subclass then concatenates:

```python
" Child"
```

resulting in:

```text
Parent Child
```

---

## 48. What is the output?

**Answer:** B

```text
500
```

**Explanation:**
The attribute:

```python
self.__balance
```

is name-mangled by Python.

However, the `get_balance()` method is defined inside the class and can access
the mangled attribute normally.

Therefore the method returns `500`.

---

## 49. What is the output?

**Answer:** B

```text
Engine started
```

**Explanation:**
`Car` contains an `Engine` instance:

```python
self.engine = Engine()
```

The `Car.start()` method delegates to:

```python
self.engine.start()
```

This demonstrates composition.

---

## 50. What is the output?

**Answer:** A

```text
Parent
```

**Explanation:**
`Child` does not override `show()`.

Python therefore finds the inherited implementation defined in `Parent`.

---

# Part 4 — Conceptual Reasoning

## 51. Why is the distinction between instance attributes and class attributes important?

**Answer:** B

**Explanation:**
Instance attributes represent state associated with individual objects, while
class attributes are associated with the class and can be shared through
attribute lookup.

Understanding this distinction is essential for correctly modeling object
state.

---

## 52. Why can an instance attribute hide a class attribute with the same name?

**Answer:** B

**Explanation:**
When an attribute is accessed through an instance, Python's attribute lookup
rules can find an attribute on the instance before finding the corresponding
attribute on the class.

For example:

```python
class Device:
    category = "Electronic"

device = Device()
device.category = "Mobile"
```

The instance-level value is returned for `device.category`.

---

## 53. A `Car` object contains an `Engine` object and delegates engine-related operations to it. Which relationship is most appropriate?

**Answer:** B

**Explanation:**
A `Car` has an `Engine`, so this is a **has-a** relationship.

Composition is therefore more appropriate than inheritance.

---

## 54. Which situation generally favors composition over inheritance?

**Answer:** B

**Explanation:**
Composition is appropriate when an object needs to collaborate with another
object without representing a subtype of that object's type.

Inheritance should generally be reserved for genuine **is-a** relationships.

---

## 55. Which statement best describes method overriding?

**Answer:** A

**Explanation:**
A subclass can provide its own implementation of an inherited method.

This allows the subclass to specialize or replace inherited behavior.

---

## 56. Which statement best describes duck typing?

**Answer:** B

**Explanation:**
Duck typing focuses on behavior.

If an object provides the operations required by a piece of code, that object
can often be used regardless of its specific class hierarchy.

---

## 57. What is the purpose of name mangling for names beginning with two leading underscores?

**Answer:** B

**Explanation:**
Python transforms names such as:

```python
__balance
```

into a class-specific mangled form.

This helps reduce accidental name collisions, especially in inheritance
hierarchies.

Name mangling does **not** provide absolute privacy or security.

---

## 58. Which statement best describes encapsulation?

**Answer:** A

**Explanation:**
Encapsulation involves organizing related state and behavior and providing
appropriate interfaces through which that state and behavior can be used.

Python does not enforce strict private access in the same way as some
languages. It relies substantially on conventions, interfaces, properties,
and mechanisms such as name mangling.

---

## 59. Which statement best distinguishes abstraction from encapsulation?

**Answer:** A

**Explanation:**
Abstraction focuses on exposing essential behavior while hiding unnecessary
implementation details.

Encapsulation focuses on organizing state and behavior together and controlling
how they are accessed or modified through appropriate interfaces.

The concepts are related but not identical.

---

## 60. Which design best demonstrates polymorphism?

**Answer:** A

**Explanation:**
The function accepts different objects because each object provides the
required operation.

For example:

```python
def process(device):
    device.print_document()
```

Both `Printer` and `Scanner` can be passed to the function because they provide
the expected `print_document()` behavior.

This demonstrates behavioral polymorphism through duck typing.

---

# Scoring Guide

| Score | Performance Level            | Interpretation                                |
| ----: | ---------------------------- | --------------------------------------------- |
| 54–60 | Excellent                    | Strong understanding of Module 15 concepts    |
| 48–53 | Very Good                    | Good understanding with minor gaps            |
| 42–47 | Good                         | Core concepts understood; review weaker areas |
| 36–41 | Developing                   | Several concepts require additional practice  |
| 30–35 | Needs Review                 | Significant gaps in OOP fundamentals          |
|  0–29 | Foundational Review Required | Revisit the module before progressing         |

## Recommended Review Areas

If you missed questions about:

* **Classes and objects:** Review class definitions, instances, and instantiation.
* **Attributes:** Review instance attributes, class attributes, and attribute lookup.
* **Methods:** Review `self`, instance methods, class methods, and static methods.
* **Initialization:** Review `__new__()` versus `__init__()`.
* **Inheritance:** Review inheritance, overriding, and `super()`.
* **Composition:** Review has-a versus is-a relationships.
* **Polymorphism:** Review behavioral polymorphism and duck typing.
* **Encapsulation:** Review interfaces, name mangling, and object state.
* **Abstraction:** Review interfaces and implementation hiding.

---

# End of Answer Key
