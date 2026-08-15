# Polymorphism

Polymorphism is an object-oriented programming concept in which a common interface can be used with objects that provide different implementations or behaviors.

The word **polymorphism** comes from Greek roots meaning **"many forms."**

In Python, polymorphism commonly appears through:

* Method overriding
* Duck typing
* Common protocols
* Abstract interfaces
* Operator overloading

The central idea is:

> **Different objects can respond to the same operation in different ways.**

Polymorphism allows software to work with objects based on what they can do rather than requiring every object to have exactly the same implementation.

---

## 1. What Is Polymorphism?

Consider several classes:

```python
class Dog:
    def speak(self):
        print("Woof")


class Cat:
    def speak(self):
        print("Meow")


class Cow:
    def speak(self):
        print("Moo")
```

Each class provides a method named:

```python
speak()
```

But each implementation behaves differently.

We can write:

```python
dog = Dog()
cat = Cat()
cow = Cow()

dog.speak()
cat.speak()
cow.speak()
```

Output:

```text
Woof
Meow
Moo
```

The same operation:

```python
speak()
```

has different behavior depending on the object.

That is polymorphic behavior.

---

## 2. The Core Idea

Polymorphism can be represented conceptually as:

```text
Common operation
      |
      +---- Object A → behavior A
      |
      +---- Object B → behavior B
      |
      +---- Object C → behavior C
```

For example:

```text
speak()
  ├── Dog → Woof
  ├── Cat → Meow
  └── Cow → Moo
```

The calling code can use the common operation without needing to know every implementation detail.

---

## 3. Why Polymorphism Matters

Polymorphism helps software become:

* More extensible
* More reusable
* Easier to maintain
* Less dependent on concrete implementations
* Easier to test
* Easier to extend with new object types

Suppose an application supports three payment methods:

```text
CreditCard
PayPal
BankTransfer
```

If each provides:

```python
pay()
```

then higher-level code can work with the common operation.

Adding another payment type becomes easier because the new class only needs to satisfy the expected interface.

---

## 4. Polymorphism Through Inheritance

One common form of polymorphism uses inheritance.

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

Now:

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

The loop uses the same operation:

```python
animal.speak()
```

but the actual implementation depends on the object.

---

## 5. Method Overriding Enables Polymorphism

Method overriding is closely related to polymorphism.

The parent defines a common operation:

```python
class Animal:
    def speak(self):
        print("Animal sound")
```

The subclasses specialize it:

```python
class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("Meow")
```

The subclasses provide different implementations of the same method.

This gives the program a common interface with multiple behaviors.

---

## 6. Polymorphic Function

A function can accept an object and call a method without knowing its concrete class.

```python
def make_speak(animal):
    animal.speak()
```

Now:

```python
make_speak(Dog())
make_speak(Cat())
```

Output:

```text
Woof
Meow
```

The function does not need:

```python
if type(animal) == Dog:
    ...
elif type(animal) == Cat:
    ...
```

Instead, it simply relies on the required behavior.

This is a major advantage of polymorphism.

---

## 7. Avoiding Type-Based Conditional Logic

A less flexible approach is:

```python
def make_speak(animal):
    if isinstance(animal, Dog):
        print("Woof")
    elif isinstance(animal, Cat):
        print("Meow")
```

This function must be modified whenever a new animal type is introduced.

A polymorphic approach is:

```python
def make_speak(animal):
    animal.speak()
```

Now a new class can participate by implementing `speak()`.

```python
class Cow:
    def speak(self):
        print("Moo")
```

No modification to `make_speak()` is required.

This is one reason polymorphism can improve extensibility.

---

## 8. Duck Typing

Python strongly supports **duck typing**.

The informal principle is:

> If an object behaves like the required type, it can be used accordingly.

Consider:

```python
class Dog:
    def speak(self):
        print("Woof")


class Robot:
    def speak(self):
        print("Beep")
```

There is no inheritance relationship.

Yet:

```python
def make_speak(obj):
    obj.speak()
```

works with both:

```python
make_speak(Dog())
make_speak(Robot())
```

Output:

```text
Woof
Beep
```

This is polymorphism through compatible behavior rather than inheritance.

---

## 9. Duck Typing Does Not Mean "Anything Goes"

Duck typing does not mean Python ignores interfaces or requirements.

If a function does:

```python
def process(obj):
    obj.run()
```

then the object must provide a compatible `run()` operation.

An object without it will fail:

```python
class Person:
    pass

process(Person())
```

This results in an `AttributeError` because `Person` does not provide `run()`.

Duck typing means that compatibility is primarily determined by behavior rather than explicit inheritance.

---

## 10. Polymorphism Without Inheritance

Consider:

```python
class PDFReport:
    def generate(self):
        print("Generating PDF")


class HTMLReport:
    def generate(self):
        print("Generating HTML")


class TextReport:
    def generate(self):
        print("Generating text")
```

There is no common parent class.

Yet:

```python
def generate_report(report):
    report.generate()
```

works with all three.

```python
generate_report(PDFReport())
generate_report(HTMLReport())
generate_report(TextReport())
```

Output:

```text
Generating PDF
Generating HTML
Generating text
```

This is valid polymorphism in Python.

---

## 11. Protocol-Oriented Thinking

A useful way to think about duck typing is through protocols.

A protocol describes expected behavior.

For example:

```text
Iterable
    ↓
Supports iteration
```

or:

```text
File-like object
    ↓
Supports operations such as read()
```

The object does not necessarily need to inherit from a particular class.

It needs to provide the operations expected by the consumer.

Python uses many such protocols.

---

## 12. Common Python Protocols

Python's data model defines many protocols.

Examples include:

| Protocol        | Typical operation    |
| --------------- | -------------------- |
| Iterable        | `iter()` / iteration |
| Sized           | `len()`              |
| Callable        | `()`                 |
| Context manager | `with`               |
| Container       | `in`                 |
| Numeric         | arithmetic operators |
| Mapping         | key-based access     |

These protocols allow different object types to work with common Python operations.

---

## 13. Polymorphism With `len()`

Consider:

```python
numbers = [10, 20, 30]
text = "Python"
```

Both support:

```python
len()
```

Therefore:

```python
print(len(numbers))
print(len(text))
```

Output:

```text
3
6
```

The objects are different:

```text
list
str
```

but both support the `Sized` protocol.

The same operation works with multiple types.

---

## 14. Polymorphism With `+`

Python's `+` operator behaves differently depending on the operands.

```python
print(2 + 3)
```

Output:

```text
5
```

For strings:

```python
print("AI" + " Engineering")
```

Output:

```text
AI Engineering
```

The operation is the same:

```python
+
```

but the behavior depends on the operand types.

This is another example of polymorphism.

---

## 15. Operator Overloading

Python allows classes to define special methods that determine how operators behave.

For example:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )
```

Now:

```python
p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2
```

The expression:

```python
p1 + p2
```

uses the class's `__add__()` implementation.

Different classes can implement `__add__()` differently.

---

## 16. Common Special Methods

Python provides many special methods that support polymorphic behavior.

Examples:

```python
__str__()
__repr__()
__len__()
__eq__()
__lt__()
__add__()
__sub__()
__mul__()
__getitem__()
```

These methods allow objects to participate in Python's built-in operations and protocols.

For example:

```python
len(obj)
```

can invoke:

```python
obj.__len__()
```

when the object's type supports the corresponding protocol.

---

## 17. Polymorphism Through Abstract Interfaces

Polymorphism can also be built around an abstract interface.

Python provides abstract base classes through the `abc` module.

Example:

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

Subclasses can provide their own implementation:

```python
class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5


class Square(Shape):
    def area(self):
        return 5 * 5
```

Now both support:

```python
area()
```

but calculate it differently.

---

## 18. Polymorphic Processing of Shapes

We can write:

```python
def print_area(shape):
    print(shape.area())
```

Then:

```python
print_area(Circle())
print_area(Square())
```

The function depends on the common interface:

```python
area()
```

rather than the concrete implementation.

This is a central object-oriented design technique.

---

## 19. Polymorphism in Machine Learning

Polymorphism is highly relevant to machine-learning software.

Consider a simplified model interface:

```python
class Model:
    def predict(self, data):
        raise NotImplementedError
```

Different models can implement:

```python
class Classifier(Model):
    def predict(self, data):
        return "class prediction"


class Regressor(Model):
    def predict(self, data):
        return "numeric prediction"
```

Both expose:

```python
predict()
```

but perform different operations.

Higher-level code can depend on the common operation.

---

## 20. Example: Model Pipeline

Consider:

```python
def run_prediction(model, data):
    return model.predict(data)
```

Now:

```python
classifier = Classifier()
regressor = Regressor()

print(run_prediction(classifier, data))
print(run_prediction(regressor, data))
```

The function does not need to know the internal algorithm.

It only requires that the object provide:

```python
predict(data)
```

This is a practical example of polymorphic design.

---

## 21. Polymorphism in Data Processing

Consider:

```python
class CSVProcessor:
    def process(self, data):
        return "CSV processed"


class JSONProcessor:
    def process(self, data):
        return "JSON processed"


class ImageProcessor:
    def process(self, data):
        return "Image processed"
```

Then:

```python
def process_data(processor, data):
    return processor.process(data)
```

The processing function is independent of the concrete processor.

This makes the system easier to extend.

---

## 22. Polymorphism and Dependency Inversion

Polymorphism often supports dependency inversion.

Instead of:

```python
def run():
    model = NeuralNetworkModel()
    model.predict(data)
```

higher-level code can depend on an abstraction:

```python
def run(model):
    return model.predict(data)
```

Now the caller can provide:

```text
NeuralNetworkModel
LinearModel
TreeModel
MockModel
```

as long as each provides the expected behavior.

This reduces coupling between components.

---

## 23. Polymorphism and Testing

Polymorphism can simplify testing.

Suppose production code expects:

```python
model.predict(data)
```

A test can provide a simple substitute:

```python
class FakeModel:
    def predict(self, data):
        return "test prediction"
```

Then:

```python
def run_prediction(model, data):
    return model.predict(data)
```

can be tested without using a real machine-learning model.

This is one practical benefit of programming against behavior rather than concrete implementations.

---

## 24. Polymorphism and Extensibility

Suppose an application initially supports:

```text
CSVProcessor
JSONProcessor
```

Later, you need:

```text
XMLProcessor
```

If the application relies on a common operation:

```python
process(data)
```

you can add:

```python
class XMLProcessor:
    def process(self, data):
        return "XML processed"
```

The existing processing code may not require modification.

This follows the general idea of designing software so new implementations can be added without unnecessarily changing existing consumers.

---

## 25. Polymorphism vs Inheritance

These concepts should not be treated as synonyms.

### Inheritance

Inheritance establishes a relationship between classes:

```text
Child → Parent
```

### Polymorphism

Polymorphism means different objects can be used through a common operation or interface.

Inheritance can enable polymorphism, but it is not required.

For example:

```python
class Dog:
    def speak(self):
        print("Woof")


class Robot:
    def speak(self):
        print("Beep")
```

There is no inheritance relationship, but the objects are still usable polymorphically through `speak()`.

---

## 26. Polymorphism vs Method Overriding

These are also different concepts.

### Method overriding

A subclass replaces an inherited method:

```python
class Dog(Animal):
    def speak(self):
        print("Woof")
```

### Polymorphism

Different objects can respond to a common operation:

```python
for animal in animals:
    animal.speak()
```

Overriding is one mechanism that can produce polymorphic behavior.

Polymorphism is the broader concept.

---

## 27. Polymorphism vs Duck Typing

Duck typing is one mechanism through which Python provides polymorphism.

### Duck typing

Focuses on whether an object provides the expected behavior.

```python
obj.run()
```

### Polymorphism

Describes the ability to use different objects through a common operation or interface.

Therefore:

```text
Duck typing → mechanism/style
Polymorphism → broader behavior/design concept
```

---

## 28. Static Typing and Protocols

Python also supports structural typing through `typing.Protocol`.

Example:

```python
from typing import Protocol


class Speakable(Protocol):
    def speak(self) -> None:
        ...
```

A class does not need to inherit from `Speakable`.

If it provides a compatible `speak()` method, static type checkers can recognize that it satisfies the protocol.

For example:

```python
class Dog:
    def speak(self) -> None:
        print("Woof")
```

Conceptually:

```text
Speakable
    ↑
Dog satisfies required structure
```

This provides a more explicit form of structural typing while retaining Python's flexible behavior-based model.

---

## 29. Nominal vs Structural Typing

Two important concepts are:

### Nominal typing

Compatibility is determined primarily by declared relationships such as inheritance.

```text
Child inherits from Parent
```

### Structural typing

Compatibility is determined by the structure or behavior an object provides.

```text
Object provides required methods
```

Python supports both approaches.

Inheritance and abstract base classes can provide nominal relationships, while duck typing and `Protocol` support structural approaches.

---

## 30. A Practical Polymorphism Example

Consider different notification systems:

```python
class EmailNotification:
    def send(self, message):
        print(f"Email: {message}")


class SMSNotification:
    def send(self, message):
        print(f"SMS: {message}")


class PushNotification:
    def send(self, message):
        print(f"Push: {message}")
```

The common behavior is:

```python
send(message)
```

Now:

```python
def notify(notification, message):
    notification.send(message)
```

We can use:

```python
notify(EmailNotification(), "Hello")
notify(SMSNotification(), "Hello")
notify(PushNotification(), "Hello")
```

Output:

```text
Email: Hello
SMS: Hello
Push: Hello
```

The function does not care which concrete notification class it receives.

---

## 31. Why This Design Is Better

Without polymorphism, code might become:

```python
def notify(notification_type, message):
    if notification_type == "email":
        ...
    elif notification_type == "sms":
        ...
    elif notification_type == "push":
        ...
```

This tightly couples the function to every supported notification type.

With polymorphism:

```python
def notify(notification, message):
    notification.send(message)
```

the function depends only on the required operation.

This is generally more extensible.

---

## 32. Polymorphism and the Open/Closed Principle

Polymorphism often supports the **Open/Closed Principle**:

> Software entities should generally be open for extension but closed for modification.

For example:

```python
def notify(notification, message):
    notification.send(message)
```

If a new notification class provides `send()`, the function may continue working without modification.

The system is extended by adding a new implementation rather than modifying the existing consumer.

This principle is not absolute, but polymorphism is a common technique for achieving it.

---

## 33. Polymorphism and Separation of Responsibilities

A good polymorphic design separates responsibilities.

For example:

```text
Notification
    ↓
Defines expected operation

EmailNotification
    ↓
Handles email behavior

SMSNotification
    ↓
Handles SMS behavior

notify()
    ↓
Uses the common operation
```

Each component has a clear responsibility.

The caller does not need to understand the internal implementation of each notification type.

---

## 34. When Polymorphism Is Useful

Polymorphism is particularly useful when:

* Several objects provide a common operation.
* Different implementations are expected.
* New implementations may be added later.
* Higher-level code should not depend on concrete classes.
* You want to reduce type-specific conditional logic.
* Components need to be replaceable.
* Testing requires substitute implementations.

---

## 35. When Polymorphism May Be Unnecessary

Do not introduce a class hierarchy merely to demonstrate polymorphism.

If you have:

```python
def calculate_total(price, tax):
    return price + tax
```

a class hierarchy may be unnecessary.

Likewise, if there is only one implementation and no meaningful abstraction, introducing several classes can increase complexity.

Good design requires identifying actual variation and responsibilities.

---

## 36. Common Mistake: Confusing Polymorphism With Inheritance

Incorrect statement:

> Polymorphism means inheritance.

More accurate:

> Inheritance is one mechanism that can enable polymorphic behavior.

Python also supports polymorphism through duck typing, protocols, built-in protocols, and other mechanisms.

---

## 37. Common Mistake: Checking Every Concrete Type

Avoid unnecessary code such as:

```python
if isinstance(obj, Dog):
    ...
elif isinstance(obj, Cat):
    ...
elif isinstance(obj, Cow):
    ...
```

when all objects already provide:

```python
speak()
```

Prefer:

```python
obj.speak()
```

This lets each object determine its own implementation.

Type checks are not inherently wrong, but excessive type-specific branching can indicate that polymorphism or another abstraction may be more appropriate.

---

## 38. Common Mistake: Assuming Duck Typing Means No Errors

Duck typing does not guarantee that an object supports the expected behavior.

This:

```python
def run(obj):
    obj.execute()
```

will fail if:

```python
class Person:
    pass
```

is passed to it.

The object must satisfy the required behavioral contract.

---

## 39. Common Mistake: Creating Artificial Interfaces

Not every class needs to implement the same methods.

Forcing unrelated classes to share an interface can make the design confusing.

Polymorphism is useful when the common operation represents a meaningful abstraction.

---

## 40. Common Mistake: Overusing Inheritance

You do not need:

```text
BaseClass
    ↓
SubclassA
    ↓
SubclassB
    ↓
SubclassC
```

simply to achieve polymorphism.

Composition and duck typing may be better choices depending on the problem.

---

## 41. A Professional Design Example

Consider an AI application with multiple model implementations:

```python
class LinearModel:
    def predict(self, data):
        return "linear prediction"


class NeuralNetwork:
    def predict(self, data):
        return "neural network prediction"


class DecisionTree:
    def predict(self, data):
        return "tree prediction"
```

The application can define:

```python
def evaluate_model(model, data):
    prediction = model.predict(data)
    return prediction
```

Then:

```python
models = [
    LinearModel(),
    NeuralNetwork(),
    DecisionTree()
]

for model in models:
    print(evaluate_model(model, data))
```

The evaluation logic depends on the common operation:

```python
predict(data)
```

rather than the implementation.

This is a simplified example of a design pattern frequently encountered in real software libraries.

---

## 42. Polymorphism in Machine-Learning Frameworks

Many machine-learning libraries use object-oriented abstractions.

A framework may define common operations such as:

```text
fit()
predict()
transform()
score()
```

Different algorithms provide different implementations.

For example, conceptually:

```text
Estimator
   ├── Linear Model
   ├── Tree Model
   └── Neural Model
```

Higher-level components can interact with these objects through shared interfaces.

Understanding polymorphism therefore helps when reading and designing ML-oriented APIs.

---

## 43. Polymorphism and API Design

When designing an API, ask:

> What behavior does the consumer actually need?

Suppose the consumer only needs:

```python
model.predict(data)
```

Then the consumer does not necessarily need to know:

* How the model was trained.
* Which algorithm it uses.
* How parameters are stored.
* Which internal data structures it uses.

The API can therefore expose the common behavior while hiding implementation details.

This reduces coupling.

---

## 44. Polymorphism and Dependency Injection

Polymorphism also enables dependency injection.

Instead of constructing a dependency inside a function:

```python
def train():
    model = NeuralNetwork()
    ...
```

provide the dependency externally:

```python
def train(model):
    ...
```

Now the caller can provide different implementations.

For example:

```python
train(NeuralNetwork())
train(LinearModel())
train(MockModel())
```

This makes software more modular and testable.

---

## 45. Design Principle

A useful principle is:

> **Program against abstractions or required behavior rather than unnecessary implementation details.**

For example:

```python
def run_prediction(model, data):
    return model.predict(data)
```

is less coupled than:

```python
def run_prediction(neural_network_model, data):
    # neural-network-specific assumptions
    ...
```

The first design can work with a broader set of compatible objects.

---

## 46. Polymorphism Does Not Require Identical Internals

Two classes can implement the same operation in completely different ways.

For example:

```python
class LinearModel:
    def predict(self, data):
        return "Uses linear equation"


class NeuralNetwork:
    def predict(self, data):
        return "Uses learned neural network"
```

Their internals differ substantially.

The consumer only needs:

```python
predict(data)
```

This separation between interface and implementation is one of the most useful aspects of polymorphic design.

---

## 47. Practical Mental Model

Think of polymorphism as:

```text
              Common operation
                     |
        +------------+------------+
        |            |            |
     Object A     Object B     Object C
        |            |            |
    Behavior A   Behavior B   Behavior C
```

The caller knows:

```text
"What operation can I perform?"
```

rather than:

```text
"Which exact class is this?"
```

That distinction is fundamental.

---

## 48. Key Takeaways

Polymorphism means that different objects can be used through a common operation or interface while providing different behavior.

Remember:

* Polymorphism means "many forms."
* Method overriding can provide polymorphism.
* Inheritance can enable polymorphism but is not required.
* Duck typing is an important Python mechanism for polymorphism.
* Python's protocols provide polymorphic behavior for built-in operations.
* Abstract base classes can define polymorphic interfaces.
* `typing.Protocol` supports structural typing for static analysis.
* Operator overloading is another form of polymorphic behavior.
* Polymorphism reduces unnecessary type-specific branching.
* It can reduce coupling between components.
* It can improve extensibility and testability.
* It is highly relevant to machine-learning and AI software design.
* Polymorphism should be introduced when a meaningful common abstraction exists.

The essential pattern is:

```python
def process(obj):
    obj.operation()
```

Different objects can provide different implementations:

```python
class A:
    def operation(self):
        print("A")


class B:
    def operation(self):
        print("B")
```

Then:

```python
process(A())
process(B())
```

produces different behavior through the same interface.

The key principle is:

> **Polymorphism allows code to depend on what an object can do rather than unnecessarily depending on what concrete class the object belongs to.**
