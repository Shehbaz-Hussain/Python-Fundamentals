# Static Methods

A **static method** is a method defined inside a class that does not receive an instance or class reference automatically.

Python defines static methods using the `@staticmethod` decorator.

The basic syntax is:

```python
class ClassName:
    @staticmethod
    def method_name(parameters):
        ...
```

Unlike instance methods and class methods, a static method does not automatically receive:

* `self` — the instance
* `cls` — the class

Static methods are useful when an operation is logically related to a class but does not depend on instance or class state.

---

## 1. Basic Example

```python
class MathTools:
    @staticmethod
    def add(a, b):
        return a + b
```

The method can be called through the class:

```python
result = MathTools.add(10, 20)

print(result)
```

Output:

```text
30
```

No `MathTools` object is required.

---

## 2. Why Use `@staticmethod`?

Consider a class containing several operations related to data validation:

```python
class User:
    @staticmethod
    def is_valid_age(age):
        return age >= 18
```

The method does not need:

```python
self
```

because the result does not depend on a particular `User` object.

It also does not need:

```python
cls
```

because it does not depend on class-level state.

The method is simply grouped inside `User` because the operation is conceptually relevant to users.

---

## 3. Static Methods vs Instance Methods

An instance method receives an object automatically:

```python
class User:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        return self.name
```

The method needs `self` because it accesses:

```python
self.name
```

A static method does not:

```python
class User:
    @staticmethod
    def is_valid_name(name):
        return len(name) > 0
```

The distinction is:

```text
Instance method
    ↓
self
    ↓
depends on instance state

Static method
    ↓
no automatic instance
    ↓
does not depend on instance state
```

---

## 4. Static Methods vs Class Methods

A class method receives the class:

```python
class User:
    @classmethod
    def get_count(cls):
        return cls.count
```

A static method does not:

```python
class User:
    @staticmethod
    def normalize_name(name):
        return name.strip().lower()
```

The difference is:

```text
Instance method
    → self

Class method
    → cls

Static method
    → no automatic self or cls
```

This distinction should be based on what the method actually needs.

---

## 5. Calling a Static Method Through the Class

The clearest usage is:

```python
class Calculator:
    @staticmethod
    def multiply(a, b):
        return a * b


result = Calculator.multiply(5, 4)

print(result)
```

Output:

```text
20
```

No object is created.

---

## 6. Calling a Static Method Through an Instance

A static method can also be accessed through an instance:

```python
calculator = Calculator()

print(calculator.multiply(5, 4))
```

Output:

```text
20
```

Unlike an ordinary instance method, Python does not insert the instance as the first argument.

Conceptually:

```text
calculator.multiply(5, 4)
        ↓
multiply(5, 4)
```

not:

```text
multiply(calculator, 5, 4)
```

For methods that do not depend on object state, calling them through the class is generally clearer.

---

## 7. Static Methods Do Not Receive `self`

Consider:

```python
class Converter:
    @staticmethod
    def kilometers_to_miles(kilometers):
        return kilometers * 0.621371
```

The method signature is:

```python
def kilometers_to_miles(kilometers):
```

There is no:

```python
self
```

because no instance is automatically passed.

Usage:

```python
miles = Converter.kilometers_to_miles(10)

print(miles)
```

---

## 8. Static Methods Do Not Receive `cls`

Similarly, a static method does not automatically receive the class:

```python
class Validator:
    @staticmethod
    def is_positive(number):
        return number > 0
```

There is no:

```python
cls
```

The method receives only the explicitly supplied argument.

---

## 9. Static Methods Can Still Access Global Names

A static method can access names available in its surrounding scope.

For example:

```python
TAX_RATE = 0.10


class Invoice:
    @staticmethod
    def calculate_tax(amount):
        return amount * TAX_RATE
```

The method does not receive the class or instance, but it can access the module-level name `TAX_RATE`.

However, relying heavily on global state can increase coupling.

The important point is:

> `@staticmethod` controls automatic method binding; it does not isolate a function from Python's normal name-resolution rules.

---

## 10. Static Methods Can Use Parameters

Static methods can accept any parameters required by their operation.

```python
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32
```

Usage:

```python
temperature = Temperature.celsius_to_fahrenheit(25)

print(temperature)
```

Output:

```text
77.0
```

The method is independent of any particular `Temperature` object.

---

## 11. Static Methods Can Perform Validation

A common use case is validation.

```python
class User:
    @staticmethod
    def is_valid_email(email):
        return "@" in email
```

Usage:

```python
print(User.is_valid_email("alice@example.com"))
```

Output:

```text
True
```

The validation logic does not require a `User` instance.

For real applications, email validation is more complex than checking for `@`; this example only demonstrates the structure.

---

## 12. Static Methods Can Normalize Data

Example:

```python
class TextProcessor:
    @staticmethod
    def normalize(text):
        return text.strip().lower()
```

Usage:

```python
result = TextProcessor.normalize("  Hello World  ")

print(result)
```

Output:

```text
hello world
```

The method performs a transformation without depending on class or instance state.

---

## 13. Static Methods as Utility Operations

A static method can encapsulate a small operation related to the class's domain.

```python
class Geometry:
    @staticmethod
    def rectangle_area(width, height):
        return width * height

    @staticmethod
    def rectangle_perimeter(width, height):
        return 2 * (width + height)
```

Usage:

```python
print(Geometry.rectangle_area(5, 4))
print(Geometry.rectangle_perimeter(5, 4))
```

Output:

```text
20
18
```

No `Geometry` object is necessary.

---

## 14. Why Not Just Use a Function?

This is an important design question.

The following is perfectly valid:

```python
def rectangle_area(width, height):
    return width * height
```

There is no automatic reason to turn it into a static method.

A static method may make sense when the operation is strongly associated with the class's conceptual responsibility:

```python
class Geometry:
    @staticmethod
    def rectangle_area(width, height):
        return width * height
```

But if the operation has no meaningful relationship to the class, a module-level function may be clearer.

This is an important OOP design principle:

> Do not use a class merely to group unrelated utility functions.

---

## 15. Static Method vs Module-Level Function

Consider:

```python
def normalize_name(name):
    return name.strip().lower()
```

This is appropriate if the operation is generally useful throughout a module or package.

Compare:

```python
class User:
    @staticmethod
    def normalize_name(name):
        return name.strip().lower()
```

This may be appropriate if the operation is specifically part of the conceptual API surrounding `User`.

The decision should be based on cohesion and organization, not on a preference for classes.

---

## 16. Static Methods and Encapsulation

Static methods can keep related implementation logic inside a class.

For example:

```python
class PasswordPolicy:
    @staticmethod
    def is_valid(password):
        if len(password) < 8:
            return False

        return True
```

The validation operation is conceptually associated with password policy.

The method does not need an instance because the validation is purely based on its input.

---

## 17. Static Methods and Class Attributes

A static method does not automatically receive `cls`, but it can explicitly access the class if the class name is appropriate.

For example:

```python
class Circle:
    PI = 3.141592653589793

    @staticmethod
    def area(radius):
        return Circle.PI * radius ** 2
```

This works, but there is an important design consideration.

The method is now explicitly coupled to the class name `Circle`.

If subclasses should customize the behavior using their own class-level values, a class method may be more appropriate:

```python
class Circle:
    PI = 3.141592653589793

    @classmethod
    def area(cls, radius):
        return cls.PI * radius ** 2
```

The correct decorator depends on the intended design.

---

## 18. Static Methods and Instance State

A static method cannot directly use `self` unless an instance is explicitly passed as an argument.

For example:

```python
class Student:
    @staticmethod
    def display(student):
        print(student.name)
```

Usage:

```python
student = Student()
student.name = "Ali"

Student.display(student)
```

This is technically possible.

However, if the operation naturally belongs to an instance, an instance method is usually clearer:

```python
class Student:
    def display(self):
        print(self.name)
```

Therefore, explicitly passing an object to a static method is not normally a reason to use `@staticmethod`.

---

## 19. Static Methods Are Not Automatically Private

A static method can be public:

```python
class Validator:
    @staticmethod
    def validate(value):
        ...
```

or intended as non-public:

```python
class Validator:
    @staticmethod
    def _normalize(value):
        ...
```

The underscore is a naming convention indicating non-public intent.

Python does not enforce private methods through the static method mechanism.

---

## 20. Static Methods and Type Conversion

Static methods can encapsulate conversion logic.

```python
class DataConverter:
    @staticmethod
    def to_float(value):
        return float(value)
```

Usage:

```python
result = DataConverter.to_float("3.14")

print(result)
```

Output:

```text
3.14
```

This can be useful when conversion belongs to a larger domain-specific abstraction.

However, simple conversions such as `float(value)` generally do not need a class wrapper.

---

## 21. Static Methods in Data Processing

Static methods can be used for stateless preprocessing operations.

```python
class DataProcessor:
    @staticmethod
    def normalize(value, minimum, maximum):
        return (value - minimum) / (maximum - minimum)
```

Usage:

```python
result = DataProcessor.normalize(
    75,
    0,
    100
)

print(result)
```

Output:

```text
0.75
```

The operation depends only on its arguments.

---

## 22. Static Methods in Machine Learning

Stateless helper operations sometimes appear around ML components.

For example:

```python
class Metrics:
    @staticmethod
    def accuracy(correct, total):
        if total == 0:
            raise ValueError("Total cannot be zero")

        return correct / total
```

Usage:

```python
score = Metrics.accuracy(95, 100)

print(score)
```

Output:

```text
0.95
```

No metric object is required because the calculation does not depend on stored state.

---

## 23. Another ML Example: Normalization

A simplified preprocessing operation could be:

```python
class Preprocessor:
    @staticmethod
    def min_max(value, minimum, maximum):
        if maximum == minimum:
            raise ValueError("Range cannot be zero")

        return (value - minimum) / (maximum - minimum)
```

Usage:

```python
normalized = Preprocessor.min_max(50, 0, 100)

print(normalized)
```

Output:

```text
0.5
```

This method is stateless.

A real preprocessing pipeline may require stored parameters learned from training data, in which case an instance method would often be more appropriate.

---

## 24. Stateless vs Stateful Operations

This distinction is particularly important in AI and machine learning.

### Stateless operation

The result depends only on explicit inputs:

```python
class Metrics:
    @staticmethod
    def accuracy(correct, total):
        return correct / total
```

### Stateful operation

The result depends on data stored inside an object:

```python
class Model:
    def __init__(self, weights):
        self.weights = weights

    def predict(self, inputs):
        ...
```

The second operation needs `self`.

Therefore:

```text
Stateless
    → static method may be appropriate

Stateful
    → instance method is usually appropriate
```

---

## 25. Static Methods and Pure Functions

A static method can often resemble a pure function.

For example:

```python
class MathTools:
    @staticmethod
    def square(value):
        return value * value
```

Given the same input:

```text
square(5)
```

the method produces the same result, assuming no external mutable state affects it.

However, being a static method does **not** automatically make a function mathematically pure.

A static method can still access:

* Global variables
* Files
* Databases
* Environment variables
* Network resources
* External mutable state

Purity depends on behavior, not on the decorator.

---

## 26. Static Methods and Side Effects

For example:

```python
class Logger:
    @staticmethod
    def log(message):
        print(message)
```

This is stateless but has a side effect: it writes to standard output.

Therefore:

```text
static method
    ≠
automatically pure function
```

The decorator only determines method binding.

---

## 27. Static Methods and Inheritance

Static methods can be inherited.

```python
class Parent:
    @staticmethod
    def greet():
        print("Hello")


class Child(Parent):
    pass
```

Then:

```python
Child.greet()
```

produces:

```text
Hello
```

The method does not receive `Child` automatically.

This differs from a class method, where `cls` would refer to the class involved in the call.

---

## 28. Static Method Inheritance Example

Consider:

```python
class MathTools:
    @staticmethod
    def square(value):
        return value * value


class AdvancedMathTools(MathTools):
    pass
```

Then:

```python
print(AdvancedMathTools.square(5))
```

produces:

```text
25
```

The inherited static method works normally.

But because it receives no automatic class reference, it does not naturally adapt its behavior based on the subclass.

---

## 29. Static Method vs Class Method in Inheritance

Compare:

```python
class Parent:
    value = 10

    @classmethod
    def get_value(cls):
        return cls.value
```

A subclass can override:

```python
class Child(Parent):
    value = 20
```

Then:

```python
print(Child.get_value())
```

returns:

```text
20
```

Now compare:

```python
class Parent:
    value = 10

    @staticmethod
    def get_value():
        return Parent.value
```

The static method explicitly references `Parent`.

Calling:

```python
Child.get_value()
```

would still use the implementation's reference to `Parent.value`.

Therefore, if subclass-specific behavior matters, a class method may be the better abstraction.

---

## 30. Static Methods and Alternative Constructors

Static methods can technically create objects:

```python
class Person:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def create(name):
        return Person(name)
```

But this is usually less flexible than:

```python
class Person:
    @classmethod
    def create(cls, name):
        return cls(name)
```

The class method supports inheritance more naturally.

Therefore, **alternative constructors are usually better implemented with `@classmethod` rather than `@staticmethod`.**

---

## 31. Static Methods and Utility Classes

Some languages commonly use classes containing only static utility methods.

Python does not require this pattern.

For example:

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b
```

This works.

But Python's module system often provides a simpler alternative:

```python
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b
```

The choice should depend on the architecture and conceptual relationship of the operations.

---

## 32. Cohesion Matters

A class should ideally contain functionality that belongs together conceptually.

Good:

```python
class PasswordValidator:
    @staticmethod
    def is_valid_length(password):
        return len(password) >= 8

    @staticmethod
    def contains_number(password):
        return any(char.isdigit() for char in password)
```

The methods share a coherent responsibility.

Less appropriate:

```python
class Miscellaneous:
    @staticmethod
    def calculate_tax(...):
        ...

    @staticmethod
    def resize_image(...):
        ...

    @staticmethod
    def validate_email(...):
        ...

    @staticmethod
    def convert_temperature(...):
        ...
```

The class has poor cohesion.

A module or separate domain-specific classes may be more appropriate.

---

## 33. Static Methods and Separation of Responsibilities

Static methods should not be used to hide unrelated functionality inside classes.

Suppose:

```python
class Model:
    @staticmethod
    def send_email(...):
        ...

    @staticmethod
    def resize_image(...):
        ...

    @staticmethod
    def calculate_accuracy(...):
        ...
```

These operations belong to different responsibilities.

A better design might separate:

```text
Model
EmailService
ImageProcessor
Metrics
```

This improves cohesion and maintainability.

---

## 34. Static Methods and Dependency Injection

A stateless operation may be implemented as a static method:

```python
class Metrics:
    @staticmethod
    def accuracy(correct, total):
        return correct / total
```

However, if the operation later needs configurable behavior or injected dependencies, an instance-based design may become more appropriate.

For example:

```python
class Metrics:
    def __init__(self, rounding):
        self.rounding = rounding
```

The important lesson is that decorators should follow design requirements.

Do not choose `@staticmethod` simply because it is shorter.

---

## 35. Static Methods and Testing

Stateless static methods can be straightforward to test.

Example:

```python
class Converter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32
```

A test can directly evaluate:

```python
assert Converter.celsius_to_fahrenheit(0) == 32
assert Converter.celsius_to_fahrenheit(100) == 212
```

No object setup is required.

However, a module-level function would be equally testable.

The testing benefit is primarily the lack of required object state, not the static method decorator itself.

---

## 36. Static Methods and `staticmethod()` Built-in

The decorator syntax:

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
```

is the normal form.

Conceptually, `staticmethod()` is also a built-in descriptor:

```python
class Calculator:
    def add(a, b):
        return a + b

    add = staticmethod(add)
```

The decorator syntax is preferred because it is more readable.

---

## 37. Static Methods and Method Binding

A normal function defined in a class becomes a descriptor that binds to instances when accessed through an instance.

For example:

```python
class Example:
    def method(self):
        ...
```

Accessing:

```python
example.method
```

produces a bound method.

With:

```python
class Example:
    @staticmethod
    def method():
        ...
```

the function is not bound to an instance.

Therefore:

```text
Normal method
    → function becomes bound to instance

Static method
    → function remains unbound
```

This is the technical reason no `self` is automatically supplied.

---

## 38. A Complete Example

Consider:

```python
class DataProcessor:
    @staticmethod
    def normalize_text(text):
        return text.strip().lower()

    @staticmethod
    def is_valid_score(score):
        return 0 <= score <= 100

    @staticmethod
    def percentage(score, total):
        if total == 0:
            raise ValueError("Total cannot be zero")

        return (score / total) * 100
```

Usage:

```python
text = DataProcessor.normalize_text("  Hello  ")
valid = DataProcessor.is_valid_score(85)
percentage = DataProcessor.percentage(85, 100)

print(text)
print(valid)
print(percentage)
```

Output:

```text
hello
True
85.0
```

None of these operations requires instance or class state.

---

## 39. AI/ML Example: Stateless Metrics

```python
class Metrics:
    @staticmethod
    def accuracy(correct, total):
        if total == 0:
            raise ValueError("Total cannot be zero")

        return correct / total

    @staticmethod
    def error_rate(errors, total):
        if total == 0:
            raise ValueError("Total cannot be zero")

        return errors / total
```

Usage:

```python
accuracy = Metrics.accuracy(92, 100)
error_rate = Metrics.error_rate(8, 100)
```

These operations are stateless.

They depend entirely on their explicit arguments.

---

## 40. AI/ML Example: Stateful vs Stateless

A model's prediction generally depends on learned parameters:

```python
class Model:
    def __init__(self, weights):
        self.weights = weights

    def predict(self, inputs):
        # Uses self.weights
        ...
```

This should be an instance method because the model's state matters.

A metric calculation may not require stored state:

```python
class Metrics:
    @staticmethod
    def accuracy(correct, total):
        return correct / total
```

This can be static because it depends only on explicit inputs.

This distinction appears frequently in AI and machine-learning software.

---

## 41. Common Mistake: Adding `self` Unnecessarily

Incorrect:

```python
class Calculator:
    @staticmethod
    def add(self, a, b):
        return a + b
```

Calling:

```python
Calculator.add(5, 10)
```

would interpret:

```text
self = 5
a = 10
```

and leave `b` missing.

Correct:

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
```

A static method should normally define only the parameters it actually needs.

---

## 42. Common Mistake: Adding `cls` Unnecessarily

Incorrect:

```python
class Calculator:
    @staticmethod
    def add(cls, a, b):
        return a + b
```

`@staticmethod` does not automatically provide `cls`.

Correct:

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
```

If the method genuinely needs the class, use `@classmethod` instead.

---

## 43. Common Mistake: Using `@staticmethod` for Instance Behavior

Consider:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    @staticmethod
    def deposit(account, amount):
        account.balance += amount
```

This can work, but it is unnecessarily awkward.

A normal instance method is clearer:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

The behavior naturally belongs to a specific account.

---

## 44. Common Mistake: Using Static Methods for Class State

If the method needs class-level data:

```python
class Model:
    version = 1
```

then:

```python
@staticmethod
def get_version():
    return Model.version
```

may work, but:

```python
@classmethod
def get_version(cls):
    return cls.version
```

is generally more appropriate when subclass-aware behavior is desired.

---

## 45. Common Mistake: Assuming Static Means Private

This:

```python
@staticmethod
def helper():
    ...
```

does not make `helper()` private.

It only controls binding.

A non-public convention would be:

```python
@staticmethod
def _helper():
    ...
```

Even then, Python generally relies on convention rather than strict access control.

---

## 46. When Should You Use a Static Method?

A static method is appropriate when:

* The operation logically belongs to a class.
* It does not need instance state.
* It does not need class state.
* It does not require automatic `self`.
* It does not require automatic `cls`.
* Keeping the operation with the class improves organization and cohesion.

Examples:

```text
Validation
Normalization
Stateless calculations
Formatting
Domain-specific conversions
Stateless preprocessing
Simple metric calculations
```

---

## 47. When Should You Use a Regular Function Instead?

Prefer a module-level function when:

* The operation has no meaningful relationship to a class.
* The function is broadly reusable.
* A class would only be acting as a namespace.
* Grouping it inside a class does not improve conceptual organization.

For example:

```python
def calculate_accuracy(correct, total):
    return correct / total
```

may be preferable to:

```python
class Metrics:
    @staticmethod
    def calculate_accuracy(correct, total):
        return correct / total
```

There is no universal requirement to place stateless functions inside classes.

---

## 48. Decision Guide

A useful decision process is:

```text
Does the operation need instance state?
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
        │
        ↓
Is the operation conceptually
part of this class?
        │
       Yes
        ↓
   Static method

        No
        ↓
 Module-level function
```

This is a design heuristic, not a rigid language rule.

---

## 49. Comparison Table

| Feature                  | Instance Method           | Class Method                              | Static Method                      |
| ------------------------ | ------------------------- | ----------------------------------------- | ---------------------------------- |
| Decorator                | None                      | `@classmethod`                            | `@staticmethod`                    |
| Automatic first argument | `self`                    | `cls`                                     | None                               |
| Access to instance state | Yes                       | No direct instance                        | No automatic access                |
| Access to class state    | Yes, through class lookup | Yes                                       | No automatic access                |
| Requires instance        | Usually                   | No                                        | No                                 |
| Common use               | Object behavior           | Class behavior / alternative constructors | Stateless class-related operations |

---

## 50. Practical Design Example

Consider an ML model:

```python
class Model:
    framework = "Python"

    def __init__(self, weights):
        self.weights = weights

    def predict(self, inputs):
        # Uses self.weights
        ...

    @classmethod
    def default(cls):
        return cls(weights=[])

    @staticmethod
    def validate_input(inputs):
        return inputs is not None
```

Each method has a distinct responsibility:

```text
predict()
    ↓
needs model-specific state
    ↓
instance method

default()
    ↓
creates a model using the class
    ↓
class method

validate_input()
    ↓
needs no instance or class state
    ↓
static method
```

This is the conceptual distinction you should carry into larger software systems.

---

## Summary

A static method is a class-defined function that does not receive an instance or class reference automatically.

Key points:

* Use `@staticmethod`.
* It receives no automatic `self`.
* It receives no automatic `cls`.
* It can be called without creating an instance.
* It can be accessed through the class or an instance.
* It is useful for stateless operations conceptually related to a class.
* It is often useful for validation, normalization, conversion, and simple calculations.
* It can be inherited by subclasses.
* It does not automatically adapt to subclass-specific class state.
* A class method is generally better when class-aware behavior or alternative construction is required.
* An instance method is generally better when behavior depends on object state.
* A module-level function may be better when the operation is not meaningfully associated with a class.
* `@staticmethod` does not make a method private or automatically pure.
* The decorator controls method binding, not the method's overall behavior.

The essential distinction is:

```text
Instance Method
    → self
    → object-specific state

Class Method
    → cls
    → class-level state or class-aware construction

Static Method
    → no automatic self/cls
    → stateless class-related operation
```

A practical example:

```python
class Model:
    def __init__(self, weights):
        self.weights = weights

    @classmethod
    def default(cls):
        return cls(weights=[])

    @staticmethod
    def validate_input(inputs):
        return inputs is not None
```

Here:

```text
__init__()
    → initializes instance state

default()
    → class-aware construction

validate_input()
    → independent stateless operation
```

The next topic is **encapsulation**, where the module moves from class-level behavior toward controlling and protecting object state.
