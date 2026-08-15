# Abstraction

Abstraction is the process of exposing the essential interface of a component while hiding implementation details that users of that component do not need to know.

In object-oriented programming, abstraction helps separate **what an object does** from **how it does it**.

For example, when you call:

```python
model.predict(data)
```

you may care that the model produces a prediction, but you do not necessarily need to know every internal calculation used to produce that prediction.

Abstraction is therefore primarily about **interfaces, responsibilities, and separation of concerns**.

---

## 1. What Is Abstraction?

Consider a coffee machine.

A user may interact with:

```text
Start
Select coffee
Select size
```

The user does not need to understand:

* Heating circuitry
* Pump operation
* Water pressure
* Temperature control
* Internal timing

The interface exposes what the machine can do while hiding how the operations are implemented.

Software abstraction follows a similar principle.

```text
User / Consumer
       ↓
Public interface
       ↓
Hidden implementation
```

---

## 2. Abstraction in Python

Python supports abstraction through several mechanisms, including:

* Functions
* Classes
* Encapsulation
* Abstract base classes
* Protocols
* Public interfaces
* Module and package boundaries

In this module, the main focus is object-oriented abstraction and **abstract base classes (ABCs)**.

---

## 3. Abstraction vs Encapsulation

These concepts are related but not identical.

### Abstraction

Focuses on:

> **What should the object expose?**

### Encapsulation

Focuses on:

> **How should state and implementation details be organized and protected?**

For example:

```text
Abstraction
    ↓
Defines useful interface

Encapsulation
    ↓
Controls access to implementation/state
```

They often work together, but they solve different design problems.

---

## 4. Simple Example

Suppose we have:

```python
class EmailService:
    def send(self, message):
        print("Sending email")
```

A caller can simply use:

```python
service = EmailService()
service.send("Hello")
```

The caller does not need to know the internal implementation of sending an email.

The public operation:

```python
send()
```

acts as an interface.

---

## 5. Why Abstraction Matters

Abstraction helps developers:

* Reduce unnecessary complexity.
* Separate interfaces from implementations.
* Hide implementation details.
* Reduce coupling.
* Define clear responsibilities.
* Build replaceable components.
* Make large systems easier to understand.
* Create consistent APIs.

It becomes increasingly valuable as software grows.

---

## 6. Abstraction and Complexity

Imagine an AI application containing:

```text
Data loading
Data validation
Preprocessing
Feature transformation
Model training
Model evaluation
Prediction
Logging
Storage
```

A high-level application should not need to understand every internal detail of every component.

Instead, it might use interfaces such as:

```python
processor.process(data)
model.fit(data)
model.predict(data)
```

Each operation hides lower-level complexity.

---

## 7. Abstract Interfaces

An abstract interface describes operations that an implementation must provide.

For example:

```text
Model
 ├── fit()
 ├── predict()
 └── evaluate()
```

Different model implementations may behave differently internally, but the consumer can interact with them through the same interface.

This is one of the most important uses of abstraction in software engineering.

---

## 8. Abstract Base Classes

Python provides the `abc` module for defining abstract base classes.

Basic example:

```python
from abc import ABC, abstractmethod
```

We can define:

```python
class Model(ABC):
    @abstractmethod
    def predict(self, data):
        pass
```

Here:

* `ABC` provides the abstract-base-class mechanism.
* `@abstractmethod` marks a method that subclasses are expected to implement.

---

## 9. Creating a Concrete Subclass

A subclass can implement the abstract method:

```python
class LinearModel(Model):
    def predict(self, data):
        return "Prediction"
```

Now:

```python
model = LinearModel()

print(model.predict([1, 2, 3]))
```

Output:

```text
Prediction
```

`LinearModel` is concrete because it implements the required abstract method.

---

## 10. Instantiating an Abstract Class

Consider:

```python
from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def predict(self, data):
        pass
```

Attempting:

```python
model = Model()
```

raises a `TypeError`.

The class is abstract because it contains an abstract method.

The abstract class defines an interface rather than a complete concrete implementation.

---

## 11. Why Prevent Instantiation?

Suppose:

```python
class Model(ABC):
    @abstractmethod
    def predict(self, data):
        pass
```

What does it mean to create:

```python
Model()
```

if there is no meaningful implementation of `predict()`?

The abstract base class represents a general concept.

Concrete subclasses provide the actual behavior.

```text
Model
  ↓
Abstract concept

LinearModel
  ↓
Concrete implementation

TreeModel
  ↓
Concrete implementation

NeuralNetwork
  ↓
Concrete implementation
```

---

## 12. Abstract Methods

An abstract method defines an operation that concrete subclasses are expected to implement.

Example:

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

The class says:

> Every concrete shape must provide an `area()` operation.

The base class does not necessarily need to know how the area is calculated.

---

## 13. Concrete Implementations

A circle:

```python
class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5
```

A square:

```python
class Square(Shape):
    def area(self):
        return 5 * 5
```

Both implement:

```python
area()
```

but use different calculations.

The abstraction defines the operation.

The subclasses define the implementation.

---

## 14. Abstract Method Syntax

The standard pattern is:

```python
from abc import ABC, abstractmethod


class Parent(ABC):

    @abstractmethod
    def operation(self):
        pass
```

A subclass implements it:

```python
class Child(Parent):

    def operation(self):
        print("Implementation")
```

This creates a contract between the abstraction and concrete implementations.

---

## 15. The `ABC` Base Class

`ABC` is provided by Python's `abc` module.

Example:

```python
from abc import ABC


class Vehicle(ABC):
    pass
```

A class inheriting from `ABC` can participate in the abstract base class system.

However, simply inheriting from `ABC` does not automatically make a class abstract.

You normally also define one or more abstract methods.

---

## 16. The `@abstractmethod` Decorator

The `abstractmethod` decorator marks a method as abstract.

Example:

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
```

A concrete subclass should implement:

```python
class Car(Vehicle):

    def start(self):
        print("Car started")
```

Now:

```python
car = Car()
car.start()
```

Output:

```text
Car started
```

---

## 17. Abstract Classes Can Have Concrete Methods

An abstract class does not need every method to be abstract.

For example:

```python
from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def predict(self, data):
        pass

    def describe(self):
        print("Machine-learning model")
```

A subclass:

```python
class LinearModel(Model):

    def predict(self, data):
        return "Prediction"
```

inherits the concrete `describe()` method.

Therefore, abstract classes can provide:

* Abstract operations
* Shared implementations
* Shared state
* Common utility behavior

---

## 18. Abstract Classes Can Have `__init__()`

An abstract class can also define an initializer:

```python
from abc import ABC, abstractmethod


class Model(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def predict(self, data):
        pass
```

A subclass can reuse it:

```python
class LinearModel(Model):

    def __init__(self, name):
        super().__init__(name)

    def predict(self, data):
        return "Prediction"
```

Then:

```python
model = LinearModel("Linear Regression")

print(model.name)
```

Output:

```text
Linear Regression
```

---

## 19. Abstract Methods Can Have Implementations

An abstract method can contain implementation code.

For example:

```python
from abc import ABC, abstractmethod


class BaseProcessor(ABC):

    @abstractmethod
    def process(self, data):
        print("Common processing")
```

A subclass may call the abstract implementation:

```python
class Processor(BaseProcessor):

    def process(self, data):
        super().process(data)
        print("Specific processing")
```

The important point is that `@abstractmethod` marks the method as abstract even if it contains code.

Abstract does not necessarily mean "has no implementation."

---

## 20. Abstract Properties

The `abc` module can also be used with properties.

Example:

```python
from abc import ABC, abstractmethod


class Model(ABC):

    @property
    @abstractmethod
    def name(self):
        pass
```

A subclass can implement the property:

```python
class LinearModel(Model):

    @property
    def name(self):
        return "Linear Model"
```

Now:

```python
model = LinearModel()

print(model.name)
```

Output:

```text
Linear Model
```

This allows an abstract interface to specify required attributes exposed through properties.

---

## 21. Multiple Abstract Methods

An abstract class can define several requirements:

```python
from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def fit(self, data):
        pass

    @abstractmethod
    def predict(self, data):
        pass

    @abstractmethod
    def evaluate(self, data):
        pass
```

A concrete model must implement all abstract methods before it can be instantiated.

---

## 22. Incomplete Subclasses Remain Abstract

Suppose:

```python
class Model(ABC):

    @abstractmethod
    def fit(self, data):
        pass

    @abstractmethod
    def predict(self, data):
        pass
```

Then:

```python
class LinearModel(Model):

    def fit(self, data):
        print("Training")
```

`LinearModel` still has an unimplemented abstract method:

```python
predict()
```

Therefore it remains abstract.

Trying:

```python
model = LinearModel()
```

raises a `TypeError`.

---

## 23. Completing the Implementation

Implement both methods:

```python
class LinearModel(Model):

    def fit(self, data):
        print("Training")

    def predict(self, data):
        return "Prediction"
```

Now:

```python
model = LinearModel()

model.fit([])
print(model.predict([]))
```

Output:

```text
Training
Prediction
```

The class is now concrete.

---

## 24. Abstraction and Polymorphism

Abstraction and polymorphism frequently work together.

Consider:

```python
from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def predict(self, data):
        pass
```

Different implementations:

```python
class LinearModel(Model):
    def predict(self, data):
        return "Linear prediction"


class TreeModel(Model):
    def predict(self, data):
        return "Tree prediction"
```

A consumer can use:

```python
def run_prediction(model, data):
    return model.predict(data)
```

The abstraction defines the required interface.

Polymorphism allows different implementations to be used through that interface.

---

## 25. Abstraction and Encapsulation

Consider:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
```

The user interacts with:

```python
account.deposit(100)
```

rather than directly managing the internal balance update.

Here:

* Encapsulation organizes and controls access to internal state.
* Abstraction exposes the useful operation.
* The caller does not need to know the internal update logic.

These concepts complement one another.

---

## 26. Abstraction Through Functions

Abstraction is not limited to classes.

Consider:

```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
```

A caller can use:

```python
average = calculate_average([10, 20, 30])
```

without needing to know how the function performs the calculation.

The function itself provides an abstraction over the implementation.

Therefore, abstraction is a broader software-engineering concept, not exclusively an OOP feature.

---

## 27. Abstraction Through Modules

Modules also provide abstraction.

Suppose a module provides:

```python
load_data()
```

The consumer can call:

```python
data = load_data()
```

without needing to understand every internal implementation detail.

A module can hide:

* Helper functions
* Internal variables
* Parsing logic
* Validation logic
* Internal algorithms

while exposing a small public API.

---

## 28. Abstraction and APIs

An API is an interface through which software components communicate.

For example:

```python
model.fit(data)
model.predict(data)
```

can form part of a model API.

The implementation may involve:

```text
Data transformation
Parameter calculations
Numerical operations
Optimization
Internal state
```

The API hides those details from the caller.

This is abstraction in practical software development.

---

## 29. Abstraction and AI Engineering

Abstraction is particularly important in AI systems because AI applications often combine many components.

For example:

```text
DataLoader
    ↓
Preprocessor
    ↓
FeatureExtractor
    ↓
Model
    ↓
Evaluator
    ↓
PredictionService
```

Each component can expose a focused interface.

For example:

```python
data = loader.load()
data = processor.transform(data)
model.fit(data)
result = model.predict(data)
```

The high-level workflow becomes easier to understand because internal implementation details are hidden behind well-defined interfaces.

---

## 30. Example: Abstract Data Processor

```python
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data):
        pass
```

Concrete implementations:

```python
class TextProcessor(DataProcessor):

    def process(self, data):
        return data.lower()
```

and:

```python
class ImageProcessor(DataProcessor):

    def process(self, data):
        return "Processed image"
```

The application can depend on:

```python
processor.process(data)
```

without needing to know the internal processing algorithm.

---

## 31. Example: Abstract Model Interface

A simplified model abstraction might be:

```python
from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def fit(self, data):
        pass

    @abstractmethod
    def predict(self, data):
        pass
```

A concrete implementation:

```python
class SimpleModel(Model):

    def fit(self, data):
        print("Model trained")

    def predict(self, data):
        return "Prediction"
```

Now higher-level code can work with the interface:

```python
def train_and_predict(model, data):
    model.fit(data)
    return model.predict(data)
```

The function does not need to know the model's internal implementation.

---

## 32. Abstraction Reduces Coupling

Suppose code directly depends on a concrete class:

```python
def run():
    model = NeuralNetworkModel()
    model.predict(data)
```

This creates a strong dependency on that implementation.

A more abstract design might be:

```python
def run(model):
    return model.predict(data)
```

Now the caller supplies the implementation.

This can reduce coupling and make the component easier to replace.

---

## 33. Abstraction and Separation of Concerns

Suppose a machine-learning application contains:

```text
Training
Evaluation
Prediction
Logging
Storage
```

If one class handles all of these responsibilities, the design can become difficult to maintain.

Instead, abstraction can separate them:

```text
Trainer
Evaluator
Predictor
Logger
Storage
```

Each component exposes only the operations relevant to its responsibility.

This improves conceptual organization.

---

## 34. Abstraction and Interfaces

Python does not have a separate `interface` keyword like some languages.

Instead, interfaces can be expressed through:

* Abstract base classes
* Protocols
* Duck typing
* Documented APIs
* Conventions

For example:

```python
class Model(ABC):
    @abstractmethod
    def predict(self, data):
        pass
```

acts as an explicit interface contract.

---

## 35. Abstract Base Classes vs Protocols

Python provides two important approaches.

### Abstract Base Class

```python
from abc import ABC, abstractmethod

class Model(ABC):

    @abstractmethod
    def predict(self, data):
        pass
```

This creates an explicit inheritance-based abstraction.

### Protocol

```python
from typing import Protocol

class Predictable(Protocol):

    def predict(self, data):
        ...
```

A class can satisfy the protocol structurally without explicitly inheriting from it.

Conceptually:

```text
ABC
→ nominal / inheritance-oriented abstraction

Protocol
→ structural typing abstraction
```

Both are useful, but they serve somewhat different purposes.

---

## 36. When to Use an Abstract Base Class

An ABC can be appropriate when:

* A strong conceptual hierarchy exists.
* Shared implementation belongs in a base class.
* You want explicit inheritance.
* You want runtime enforcement of abstract methods.
* The base class represents a meaningful abstraction.

Example:

```text
Model
 ├── LinearModel
 ├── TreeModel
 └── NeuralNetwork
```

If these classes genuinely belong to the same conceptual hierarchy, an ABC may be appropriate.

---

## 37. When to Use a Protocol

A protocol can be useful when:

* You care primarily about behavior.
* Unrelated classes should be compatible.
* You want structural typing.
* You do not control the implementation classes.
* Inheritance would create unnecessary coupling.

For example, several unrelated classes might provide:

```python
predict(data)
```

without sharing a parent class.

A protocol can express that common requirement for static type checking.

---

## 38. Abstraction Does Not Mean Hiding Everything

A common misconception is:

> Abstraction means hiding all implementation details.

That is too broad.

A good abstraction hides **unnecessary complexity** while exposing the information required to use the component correctly.

For example:

```python
model.predict(data)
```

may expose:

* Method name
* Expected input
* Return value
* Relevant exceptions

while hiding:

* Internal calculations
* Internal data structures
* Implementation-specific details

Good abstraction is about choosing the right boundary.

---

## 39. Abstraction Boundaries

An abstraction boundary separates:

```text
Public interface
----------------
Implementation details
```

For example:

```python
class EmailService:
    def send(self, message):
        self._connect()
        self._authenticate()
        self._send_message(message)
```

The caller uses:

```python
service.send("Hello")
```

The internal steps are not necessary for normal use.

The `send()` method is the abstraction boundary.

---

## 40. Good Abstractions

A good abstraction usually has:

* A clear purpose
* A small, understandable interface
* Well-defined behavior
* Appropriate responsibility
* Minimal unnecessary dependencies
* Predictable semantics

For example:

```python
model.predict(data)
```

is a relatively focused operation.

A method such as:

```python
model.train_save_log_email_predict_evaluate()
```

would combine too many responsibilities.

---

## 41. Abstraction and Cohesion

**Cohesion** refers to how closely related the responsibilities of a component are.

High cohesion is generally desirable.

For example:

```text
DataProcessor
    → data-processing responsibilities
```

is more cohesive than:

```text
ApplicationManager
    → database
    → email
    → model training
    → UI
    → logging
```

Good abstractions generally have focused responsibilities.

---

## 42. Abstraction and Coupling

**Coupling** refers to the degree of dependency between components.

Suppose:

```python
def predict(model, data):
    return model.predict(data)
```

The function depends on a behavior:

```python
predict()
```

rather than a specific concrete implementation.

This can reduce coupling.

Lower coupling often makes systems easier to change and test.

---

## 43. Common Mistake: Thinking `ABC` Automatically Makes Methods Abstract

This is incorrect:

```python
from abc import ABC


class Model(ABC):
    def predict(self, data):
        pass
```

The class inherits from `ABC`, but `predict()` is not automatically abstract.

To make the method abstract:

```python
from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def predict(self, data):
        pass
```

The `@abstractmethod` decorator is what marks the method as abstract.

---

## 44. Common Mistake: Assuming Abstract Methods Must Be Empty

An abstract method can contain implementation:

```python
from abc import ABC, abstractmethod


class Base(ABC):

    @abstractmethod
    def process(self):
        print("Common behavior")
```

The method is still abstract.

A subclass may use:

```python
super().process()
```

if that shared implementation is appropriate.

---

## 45. Common Mistake: Assuming Python Has a Dedicated `interface` Keyword

Python does not define a Java-style:

```text
interface
```

keyword.

Instead, Python uses mechanisms such as:

* ABCs
* Protocols
* Duck typing
* Conventions
* Documentation

Therefore, it is more accurate to say Python supports interfaces conceptually and through language/library mechanisms rather than through a dedicated `interface` syntax.

---

## 46. Common Mistake: Overusing Abstract Classes

Not every class hierarchy needs an ABC.

If you have:

```python
class Model:
    def predict(self, data):
        ...
```

and there is no need to enforce an interface or establish a formal hierarchy, an ABC may add unnecessary complexity.

Use abstraction mechanisms when they solve an actual design problem.

---

## 47. Common Mistake: Creating Abstract Classes Too Early

Do not create:

```text
BaseEntity
AbstractEntity
AbstractBaseEntity
GenericEntity
```

before you understand the actual relationships in the application.

Premature abstraction can make simple code harder to understand.

A useful principle is:

> **Prefer simple concrete designs until a stable abstraction is justified.**

---

## 48. Common Mistake: Confusing Abstraction With Encapsulation

These concepts overlap but are not identical.

### Abstraction

Focus:

```text
What does the object provide?
```

### Encapsulation

Focus:

```text
How is state and implementation organized and accessed?
```

A class can use encapsulation without an abstract base class.

Likewise, a function can provide abstraction without encapsulation in the OOP sense.

---

## 49. Common Mistake: Hiding Too Much

If an abstraction hides information that callers legitimately need, the API becomes difficult to use.

For example, an ML model interface should document:

```text
Input format
Output format
Required parameters
Possible errors
```

Hiding implementation details should not mean hiding necessary usage information.

---

## 50. Practical Design Process

When designing a class hierarchy, ask:

### Step 1: What behavior is common?

For example:

```python
predict(data)
```

### Step 2: What implementations differ?

For example:

```text
Linear model
Tree model
Neural network
```

### Step 3: Is there a meaningful abstraction?

If yes:

```text
Model
```

### Step 4: Should the interface be enforced?

If yes, consider:

```text
ABC
```

or:

```text
Protocol
```

### Step 5: Is inheritance actually appropriate?

If not, use:

```text
Duck typing
Protocol
Composition
```

depending on the requirements.

---

## 51. Abstraction in Real Software

Professional software rarely consists of one enormous class.

Instead, systems are usually divided into components with focused interfaces.

For example:

```text
Application
    ↓
Service Layer
    ↓
Domain Objects
    ↓
Repositories
    ↓
External Systems
```

Each layer exposes an interface to the layer above it.

This is abstraction applied at the architectural level.

---

## 52. Abstraction in AI Systems

An AI application may have:

```text
DataSource
    ↓
DataProcessor
    ↓
FeaturePipeline
    ↓
Model
    ↓
Evaluator
    ↓
InferenceService
```

Each component can expose a small API.

For example:

```python
data = source.load()
data = processor.process(data)
model.fit(data)
result = model.predict(data)
```

The application can use these interfaces without knowing every internal detail.

This is how abstraction scales from individual classes to complete software architectures.

---

## 53. Abstraction and Machine-Learning Libraries

Machine-learning libraries often expose high-level interfaces.

For example, a model may conceptually provide:

```python
model.fit(X, y)
model.predict(X)
```

The user does not need to manually implement every internal mathematical operation each time.

The library abstracts away implementation details while exposing a consistent interface.

This is one reason understanding OOP and abstraction is valuable before working extensively with professional AI/ML libraries.

---

## 54. Abstraction Is a Design Decision

Abstraction should not be treated as an automatic rule.

A useful question is:

> **What details should this component's users need to know?**

If a detail is necessary for correct usage, expose it.

If it is purely an implementation concern, consider hiding it.

The goal is not maximum abstraction.

The goal is an appropriate abstraction boundary.

---

## 55. Key Takeaways

Remember:

* Abstraction focuses on essential behavior and interfaces.
* It separates **what** a component does from **how** it does it.
* Abstraction can be implemented with functions, classes, modules, ABCs, and protocols.
* Python's `abc` module provides abstract base classes.
* `ABC` supports the abstract class mechanism.
* `@abstractmethod` marks methods as abstract.
* Abstract classes cannot normally be instantiated while required abstract methods remain unimplemented.
* Abstract classes can contain concrete methods and initialization logic.
* Abstract methods can contain implementations.
* Python does not have a dedicated `interface` keyword.
* `Protocol` supports structural typing.
* Abstraction and encapsulation are related but distinct concepts.
* Abstraction often reduces coupling.
* Good abstractions expose necessary behavior while hiding unnecessary complexity.
* Abstraction is highly useful in AI and machine-learning software architecture.
* Not every class hierarchy requires an abstract base class.
* Premature abstraction can increase complexity.

A simplified abstract interface:

```python
from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def predict(self, data):
        pass
```

Concrete implementations:

```python
class LinearModel(Model):

    def predict(self, data):
        return "Linear prediction"


class TreeModel(Model):

    def predict(self, data):
        return "Tree prediction"
```

The abstraction specifies:

```python
predict(data)
```

while each implementation determines how prediction occurs.

The central principle is:

> **Expose the behavior that consumers need and hide implementation details that do not belong to the consumer's responsibilities.**
