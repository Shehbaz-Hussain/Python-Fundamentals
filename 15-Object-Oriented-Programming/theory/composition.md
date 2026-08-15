# Composition

Composition is an object-oriented design technique in which one object contains or uses another object to accomplish part of its responsibility.

Instead of establishing an **is-a** relationship through inheritance, composition commonly represents a **has-a** or **uses-a** relationship.

For example:

```text
Car
 ├── has an Engine
 └── has a Battery
```

A `Car` is not an `Engine`. It **has an `Engine`**.

Composition is one of the most important alternatives to inheritance in object-oriented design.

---

## 1. What Is Composition?

Consider:

```python
class Engine:
    def start(self):
        print("Engine started")
```

A `Car` can contain an `Engine`:

```python
class Car:
    def __init__(self):
        self.engine = Engine()
```

Now:

```python
car = Car()
car.engine.start()
```

Output:

```text
Engine started
```

The `Car` object delegates engine-related behavior to its `Engine` object.

This is composition.

---

## 2. The Core Idea

Composition can be represented as:

```text
Car
 │
 └── Engine
       │
       └── start()
```

The `Car` does not inherit from `Engine`.

Instead:

```python
self.engine = Engine()
```

creates an object relationship.

The important distinction is:

```text
Inheritance:
Car is an Engine       ❌

Composition:
Car has an Engine      ✓
```

---

## 3. Why Composition Matters

Composition helps developers:

* Build complex objects from smaller objects.
* Separate responsibilities.
* Reduce unnecessary inheritance.
* Reuse behavior without creating rigid class hierarchies.
* Replace components more easily.
* Improve testability.
* Reduce coupling.
* Create modular systems.

Large software systems are often built by composing smaller components.

---

## 4. Simple Example

```python
class CPU:
    def process(self):
        print("CPU processing")


class Computer:
    def __init__(self):
        self.cpu = CPU()

    def run(self):
        self.cpu.process()
        print("Computer running")
```

Usage:

```python
computer = Computer()
computer.run()
```

Output:

```text
CPU processing
Computer running
```

`Computer` delegates CPU-specific work to its `CPU` object.

---

## 5. Composition vs Inheritance

Consider:

```python
class Dog(Animal):
    ...
```

This represents:

```text
Dog is an Animal
```

That is inheritance.

Now:

```python
class Car:
    def __init__(self):
        self.engine = Engine()
```

represents:

```text
Car has an Engine
```

That is composition.

The relationship is fundamentally different.

---

## 6. "Is-A" vs "Has-A"

A useful initial test is:

### Inheritance

```text
is-a
```

Examples:

```text
Dog is an Animal
Circle is a Shape
Student is a Person
```

### Composition

```text
has-a
```

Examples:

```text
Car has an Engine
Computer has a CPU
Order has a Customer
Model has a Preprocessor
```

This is a useful design heuristic, but it is not the only factor that determines the correct architecture.

---

## 7. Basic Composition Syntax

The general pattern is:

```python
class Component:
    def operation(self):
        print("Component operation")


class Container:
    def __init__(self):
        self.component = Component()

    def run(self):
        self.component.operation()
```

The container object owns or uses another object.

---

## 8. Passing Dependencies Into a Class

The contained object does not always need to be created inside the containing class.

Instead:

```python
class Car:
    def __init__(self, engine):
        self.engine = engine
```

Then:

```python
engine = Engine()
car = Car(engine)
```

Now the `Car` receives its dependency from outside.

This technique is called **dependency injection**.

It is often preferable when the component should be replaceable or independently configured.

---

## 9. Why Dependency Injection Is Useful

Suppose:

```python
class Car:
    def __init__(self):
        self.engine = Engine()
```

The `Car` is tightly coupled to the concrete `Engine` implementation.

Instead:

```python
class Car:
    def __init__(self, engine):
        self.engine = engine
```

allows:

```python
car = Car(Engine())
```

or another compatible implementation.

This makes the design more flexible.

---

## 10. Composition Through Delegation

Composition often works together with **delegation**.

Consider:

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()
```

The `Car` delegates engine startup to its contained object.

The caller can simply use:

```python
car.start()
```

The caller does not need to directly access:

```python
car.engine.start()
```

This creates a cleaner interface.

---

## 11. Composition and Encapsulation

Composition can also support encapsulation.

Instead of exposing internal components:

```python
car.engine.start()
```

the class can provide:

```python
car.start()
```

Example:

```python
class Car:
    def __init__(self, engine):
        self._engine = engine

    def start(self):
        self._engine.start()
```

Now the `Car` controls how its engine is used.

This can hide internal implementation details from callers.

---

## 12. Multiple Components

A class can be composed from several objects.

For example:

```python
class Engine:
    def start(self):
        print("Engine started")


class Battery:
    def charge(self):
        print("Battery charged")


class Car:
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def start(self):
        self.battery.charge()
        self.engine.start()
```

The `Car` coordinates multiple components.

```text
Car
 ├── Engine
 └── Battery
```

Each component has a focused responsibility.

---

## 13. Composition and Separation of Responsibilities

Suppose one class handles:

```text
Engine logic
Battery logic
Navigation logic
Payment logic
Logging logic
```

That class can become difficult to maintain.

Composition allows these responsibilities to be separated:

```text
Engine
Battery
Navigator
PaymentProcessor
Logger
```

Then another object can coordinate them.

```text
Application
 ├── Navigator
 ├── PaymentProcessor
 └── Logger
```

This often results in more cohesive components.

---

## 14. Composition in a Banking System

Consider:

```python
class Account:
    def deposit(self, amount):
        print(f"Deposited {amount}")


class Customer:
    def __init__(self, account):
        self.account = account
```

A `Customer` has an `Account`.

The relationship is:

```text
Customer
   │
   └── Account
```

It would usually make little sense to write:

```python
class Customer(Account):
    ...
```

because a customer is not an account.

Composition models the relationship more accurately.

---

## 15. Composition in an Order System

Consider:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self, products):
        self.products = products
```

An order contains products.

Conceptually:

```text
Order
 ├── Product
 ├── Product
 └── Product
```

This is composition.

The `Order` does not inherit from `Product`.

---

## 16. Composition With Collections

Composition can involve multiple objects of the same type.

For example:

```python
class Team:
    def __init__(self, players):
        self.players = players
```

Now:

```python
players = [
    Player("Ali"),
    Player("Sara"),
    Player("John")
]

team = Team(players)
```

The `Team` is composed of `Player` objects.

This pattern is extremely common in software systems.

---

## 17. Composition and Object Graphs

When objects contain references to other objects, they form an object graph.

For example:

```text
Application
    |
    +-- Model
    |     |
    |     +-- Optimizer
    |
    +-- DataProcessor
    |
    +-- Logger
```

Each object collaborates with other objects.

This is how many real-world applications are structured internally.

---

## 18. Composition in AI Systems

Composition is especially useful in AI and machine-learning applications.

A model pipeline might contain:

```text
Pipeline
 ├── DataCleaner
 ├── FeatureTransformer
 ├── Model
 └── Evaluator
```

Each component has a focused responsibility.

A high-level object can coordinate them.

```python
class Pipeline:
    def __init__(self, cleaner, transformer, model):
        self.cleaner = cleaner
        self.transformer = transformer
        self.model = model
```

This allows the pipeline to be assembled from independent components.

---

## 19. AI Example: Preprocessor and Model

Consider:

```python
class Preprocessor:
    def transform(self, data):
        return data


class Model:
    def predict(self, data):
        return "Prediction"
```

Now compose them:

```python
class PredictionPipeline:
    def __init__(self, preprocessor, model):
        self.preprocessor = preprocessor
        self.model = model

    def predict(self, data):
        processed = self.preprocessor.transform(data)
        return self.model.predict(processed)
```

Usage:

```python
pipeline = PredictionPipeline(
    Preprocessor(),
    Model()
)

result = pipeline.predict(data)
```

The pipeline coordinates multiple responsibilities without implementing all of them itself.

---

## 20. Composition and Machine-Learning Pipelines

Machine-learning workflows often naturally form compositions:

```text
Raw Data
   ↓
Preprocessor
   ↓
Feature Transformer
   ↓
Model
   ↓
Postprocessor
   ↓
Prediction
```

Each component can be represented as an object.

The overall pipeline composes these components into a larger system.

This is a practical example of object-oriented composition in AI engineering.

---

## 21. Replacing Components

One major benefit of composition is that components can often be replaced.

Suppose:

```python
class StandardScaler:
    def transform(self, data):
        return data
```

and:

```python
class Normalizer:
    def transform(self, data):
        return data
```

A pipeline could accept either:

```python
pipeline = PredictionPipeline(
    StandardScaler(),
    Model()
)
```

or:

```python
pipeline = PredictionPipeline(
    Normalizer(),
    Model()
)
```

The pipeline only needs a compatible `transform()` operation.

This combines composition with polymorphism.

---

## 22. Composition and Polymorphism

Composition and polymorphism are often used together.

Suppose:

```python
class Model:
    def predict(self, data):
        raise NotImplementedError
```

Then:

```python
class LinearModel(Model):
    def predict(self, data):
        return "Linear prediction"


class TreeModel(Model):
    def predict(self, data):
        return "Tree prediction"
```

A pipeline can compose a model:

```python
class Pipeline:
    def __init__(self, model):
        self.model = model

    def predict(self, data):
        return self.model.predict(data)
```

Now:

```python
Pipeline(LinearModel())
Pipeline(TreeModel())
```

can use the same pipeline interface.

This is a powerful design combination:

```text
Composition
    +
Polymorphism
    =
Replaceable components
```

---

## 23. Composition and Dependency Injection

Consider:

```python
class Pipeline:
    def __init__(self, model):
        self.model = model
```

The model is injected into the pipeline.

This means the pipeline does not need to know how the model is constructed.

It only needs a compatible object.

For example:

```python
pipeline = Pipeline(LinearModel())
```

or:

```python
pipeline = Pipeline(TreeModel())
```

This is dependency injection through composition.

---

## 24. Composition Over Inheritance

A widely used design guideline is:

> **Prefer composition over inheritance when composition better represents the relationship or provides more flexibility.**

This does not mean:

> Never use inheritance.

Inheritance is appropriate when there is a genuine subtype relationship and the subclass satisfies the behavioral expectations of the base abstraction.

Composition is often preferable when the goal is to assemble capabilities or delegate responsibilities.

---

## 25. Example: Inheritance for Code Reuse

Suppose:

```python
class Logger:
    def log(self, message):
        print(message)
```

Then:

```python
class Model(Logger):
    pass
```

This gives `Model` a `log()` method.

But conceptually:

```text
Model is a Logger
```

may not be true.

The inheritance relationship exists primarily for code reuse.

That can create an inappropriate abstraction.

---

## 26. Composition as an Alternative

Instead:

```python
class Model:
    def __init__(self, logger):
        self.logger = logger
```

Now:

```text
Model has a Logger
```

The relationship is clearer.

The model can use:

```python
self.logger.log("Training started")
```

without claiming that the model itself is a logger.

---

## 27. Composition Provides More Flexibility

With inheritance:

```text
Model
  ↓
Logger behavior permanently attached through hierarchy
```

With composition:

```text
Model
  ↓
Logger object
```

the logger can potentially be replaced:

```python
model = Model(ConsoleLogger())
```

or:

```python
model = Model(FileLogger())
```

The model does not need to change its class hierarchy.

---

## 28. Composition and Multiple Capabilities

Suppose a model needs:

* Logging
* Metrics
* Storage

Inheritance could lead to an awkward hierarchy:

```text
Model
 ├── LoggerModel
 ├── MetricsModel
 └── StorageModel
```

What happens when one model needs all three?

The hierarchy can become complicated.

Composition is often cleaner:

```python
class Model:
    def __init__(self, logger, metrics, storage):
        self.logger = logger
        self.metrics = metrics
        self.storage = storage
```

Now the model can collaborate with several independent components.

---

## 29. Composition and Dynamic Behavior

Composition can allow behavior to change by replacing a component.

For example:

```python
class Application:
    def __init__(self, storage):
        self.storage = storage
```

The application could use:

```text
MemoryStorage
FileStorage
DatabaseStorage
CloudStorage
```

depending on the environment.

The application's class hierarchy does not need to change.

This is a major advantage in configurable systems.

---

## 30. Composition and Testing

Composition can make testing easier because dependencies can be replaced with test doubles.

Consider:

```python
class Service:
    def __init__(self, model):
        self.model = model
```

A production system might use:

```python
service = Service(RealModel())
```

A test can use:

```python
service = Service(FakeModel())
```

The service can be tested without running the full model implementation.

This technique is widely used in professional software engineering.

---

## 31. Example: Fake AI Model

```python
class FakeModel:
    def predict(self, data):
        return "test prediction"


class PredictionService:
    def __init__(self, model):
        self.model = model

    def predict(self, data):
        return self.model.predict(data)
```

Test:

```python
service = PredictionService(FakeModel())

result = service.predict([])

print(result)
```

Output:

```text
test prediction
```

The service does not need to know that the model is fake.

It only requires compatible behavior.

---

## 32. Composition and Loose Coupling

A component is loosely coupled when it has limited knowledge of the internal details of its dependencies.

For example:

```python
class Service:
    def __init__(self, model):
        self.model = model

    def run(self, data):
        return self.model.predict(data)
```

The service knows:

```text
model supports predict()
```

It does not need to know:

```text
How prediction is implemented
How model parameters are stored
Which algorithm is used
```

This is a strong separation of concerns.

---

## 33. Composition and Cohesion

Composition can also improve cohesion.

For example:

```text
Logger
    → logging responsibilities

Model
    → model responsibilities

Storage
    → persistence responsibilities
```

Instead of placing all logic in:

```text
MegaApplication
```

the application coordinates focused components.

Each component has a narrower responsibility.

---

## 34. Composition vs Aggregation

Composition and aggregation are related forms of object relationships.

### Composition

Often represents stronger ownership.

Example:

```text
House
 └── Room
```

Conceptually, the room may be considered part of the house's internal structure.

### Aggregation

Represents a weaker relationship where objects can exist independently.

Example:

```text
Team
 └── Player
```

A player can exist independently of a particular team.

In Python, these distinctions are usually expressed through ordinary object references rather than special syntax.

---

## 35. Composition vs Aggregation in Python

Python does not enforce a formal language-level distinction between composition and aggregation.

Both may look like:

```python
class Container:
    def __init__(self, component):
        self.component = component
```

The difference is primarily about **ownership and lifecycle semantics**.

Therefore, the distinction is conceptual rather than syntactic.

---

## 36. Object Lifetime and Composition

Consider:

```python
class Engine:
    pass


class Car:
    def __init__(self):
        self.engine = Engine()
```

The `Car` creates its own `Engine`.

This can represent stronger ownership.

Compare:

```python
engine = Engine()

car = Car(engine)
```

Here, the engine is supplied externally and may be shared or managed independently.

The object relationship depends on the design and lifecycle requirements.

---

## 37. Composition and Interface-Based Design

Suppose:

```python
class Storage:
    def save(self, data):
        raise NotImplementedError
```

Different implementations:

```python
class FileStorage(Storage):
    def save(self, data):
        print("Saved to file")


class DatabaseStorage(Storage):
    def save(self, data):
        print("Saved to database")
```

Now:

```python
class Application:
    def __init__(self, storage):
        self.storage = storage

    def save(self, data):
        self.storage.save(data)
```

The application composes a storage dependency.

Polymorphism allows the storage implementation to vary.

---

## 38. Composition in Web and Backend Systems

A backend service might be composed from:

```text
UserService
AuthenticationService
Database
Cache
Logger
EmailService
```

A higher-level application object can coordinate these components.

For example:

```python
class Application:
    def __init__(
        self,
        user_service,
        auth_service,
        database,
        logger
    ):
        self.user_service = user_service
        self.auth_service = auth_service
        self.database = database
        self.logger = logger
```

The application itself does not implement every responsibility.

It composes specialized objects.

---

## 39. Composition in AI Engineering

An AI service might be structured as:

```text
AIService
 ├── Retriever
 ├── Embedder
 ├── VectorStore
 ├── Model
 └── Logger
```

For example:

```python
class AIService:
    def __init__(self, retriever, embedder, model):
        self.retriever = retriever
        self.embedder = embedder
        self.model = model
```

The service coordinates these components.

Each component can evolve independently as long as the required interfaces remain compatible.

This architecture is common in modern AI applications.

---

## 40. Composition and Retrieval-Augmented Generation

A simplified RAG system might contain:

```text
RAGSystem
 ├── Embedder
 ├── VectorStore
 ├── Retriever
 └── Generator
```

Each object performs a focused responsibility.

Conceptually:

```python
class RAGSystem:
    def __init__(self, embedder, retriever, generator):
        self.embedder = embedder
        self.retriever = retriever
        self.generator = generator
```

The system composes these components into a larger workflow.

This is composition at an AI application level.

---

## 41. Composition and Machine-Learning Pipelines

A training pipeline might contain:

```text
TrainingPipeline
 ├── DataLoader
 ├── Preprocessor
 ├── Trainer
 ├── Evaluator
 └── ModelSaver
```

Instead of implementing all responsibilities inside one massive class, each component can expose a focused operation.

For example:

```python
class TrainingPipeline:
    def __init__(
        self,
        loader,
        preprocessor,
        trainer,
        evaluator
    ):
        self.loader = loader
        self.preprocessor = preprocessor
        self.trainer = trainer
        self.evaluator = evaluator
```

This makes the architecture modular.

---

## 42. Composition and Framework Design

Many Python frameworks use composition extensively.

A framework may construct an object from:

```text
Configuration
Database
Cache
Logger
Middleware
Services
```

Each component is configured separately.

The overall application is assembled from smaller objects.

Understanding composition therefore helps when reading framework code.

---

## 43. Composition vs a Giant Class

Poor design:

```python
class AIApplication:
    def load_data(self):
        ...

    def clean_data(self):
        ...

    def train_model(self):
        ...

    def evaluate_model(self):
        ...

    def save_model(self):
        ...

    def send_email(self):
        ...

    def log(self):
        ...
```

This class has many unrelated responsibilities.

Composition can separate them:

```text
DataLoader
DataProcessor
Trainer
Evaluator
ModelStorage
EmailService
Logger
```

Then:

```text
AIApplication
 ├── DataLoader
 ├── DataProcessor
 ├── Trainer
 ├── Evaluator
 ├── ModelStorage
 ├── EmailService
 └── Logger
```

The application coordinates specialized objects instead of implementing everything itself.

---

## 44. Common Mistake: Using Inheritance for Every Relationship

Incorrect reasoning:

> `Car` uses `Engine`, so `Car` should inherit from `Engine`.

This is conceptually wrong.

A car is not an engine.

The correct relationship is:

```text
Car has an Engine
```

Therefore composition is more appropriate.

---

## 45. Common Mistake: Confusing Composition With Simple Variable Storage

Composition is not merely:

```python
self.name = "Ali"
```

An ordinary value attribute is not necessarily what we mean by object composition.

Composition specifically refers to building an object from or around other objects and delegating or coordinating responsibilities between them.

For example:

```python
self.engine = Engine()
```

is a clear example.

---

## 46. Common Mistake: Creating Dependencies Internally When They Should Be Replaceable

Consider:

```python
class Service:
    def __init__(self):
        self.model = NeuralNetwork()
```

This makes the service tightly coupled to `NeuralNetwork`.

If replacement or testing is important, dependency injection is often better:

```python
class Service:
    def __init__(self, model):
        self.model = model
```

Now the dependency is configurable.

---

## 47. Common Mistake: Excessive Delegation

Composition does not mean every method should simply forward to another object.

For example:

```python
class Service:
    def run(self):
        return self.component.run()
```

may be appropriate when `Service` intentionally exposes a higher-level interface.

But if a class merely forwards dozens of methods without adding meaningful abstraction, the design may indicate unnecessary indirection.

Use delegation where it clarifies responsibilities.

---

## 48. Common Mistake: Over-Engineering

Do not create:

```text
ServiceFactory
ComponentFactory
AbstractComponentFactory
ComponentManager
```

for a problem that could be solved with:

```python
component = Component()
```

Composition should reduce complexity, not introduce unnecessary layers.

---

## 49. When Composition Is a Strong Choice

Composition is particularly useful when:

* An object has another object as a component.
* Responsibilities need to be separated.
* Dependencies should be replaceable.
* Multiple capabilities need to be combined.
* You want to avoid rigid inheritance hierarchies.
* Components may vary independently.
* Testing requires substitute dependencies.
* The system needs configurable architecture.

---

## 50. When Inheritance May Be Better

Composition is not universally superior.

Inheritance may be appropriate when:

* A true subtype relationship exists.
* A common abstraction is meaningful.
* Subclasses satisfy the base class contract.
* Shared behavior belongs naturally in a base class.
* Polymorphism through the hierarchy is useful.

For example:

```text
Circle is a Shape
Dog is an Animal
```

may justify inheritance.

---

## 51. Composition vs Inheritance Decision Guide

Ask these questions:

### Question 1

Is the relationship genuinely:

```text
is-a
```

If yes, inheritance may be appropriate.

### Question 2

Is the relationship:

```text
has-a
```

If yes, composition is usually more natural.

### Question 3

Do you mainly want code reuse?

Do not automatically choose inheritance.

Consider composition.

### Question 4

Does the component need to be replaceable?

Composition with dependency injection may be preferable.

### Question 5

Does the subclass satisfy the parent abstraction?

If not, inheritance is probably inappropriate.

---

## 52. Composition Over Inheritance Is a Guideline

The phrase:

> Prefer composition over inheritance.

should not be interpreted as:

> Never use inheritance.

A more technically accurate interpretation is:

> When both approaches can model the problem, composition often provides greater flexibility and lower coupling, but inheritance remains appropriate for genuine subtype relationships.

The correct choice depends on the domain and design requirements.

---

## 53. Composition and the Open/Closed Principle

Composition can help systems remain extensible.

For example:

```python
class Service:
    def __init__(self, storage):
        self.storage = storage
```

New storage implementations can be introduced without modifying the `Service` class, assuming they satisfy the required interface.

This allows the system to be extended through new components.

---

## 54. Composition and the Single Responsibility Principle

The **Single Responsibility Principle (SRP)** suggests that a component should have a focused responsibility.

Composition makes this easier.

Instead of:

```text
AIApplication
 → data loading
 → preprocessing
 → training
 → evaluation
 → logging
```

use:

```text
DataLoader
Preprocessor
Trainer
Evaluator
Logger
```

Then compose them:

```text
AIApplication
 ├── DataLoader
 ├── Preprocessor
 ├── Trainer
 ├── Evaluator
 └── Logger
```

Each component has a focused responsibility.

---

## 55. Composition and Dependency Inversion

Dependency inversion encourages high-level components to avoid depending directly on low-level concrete implementations.

Composition makes dependency injection natural:

```python
class PredictionService:
    def __init__(self, model):
        self.model = model
```

The service depends on the required behavior of `model`, rather than constructing a specific implementation internally.

This can make architecture more modular.

---

## 56. Composition and Testing

A composed system can be tested component by component.

For example:

```text
PredictionService
      ↓
FakeModel
```

instead of:

```text
PredictionService
      ↓
RealModel
      ↓
Database
      ↓
Network
      ↓
External API
```

The first setup is often easier to test because dependencies can be substituted.

This is a major reason composition is common in professional software engineering.

---

## 57. Practical Example: AI Prediction Service

```python
class Model:
    def predict(self, data):
        return "Prediction"


class Logger:
    def log(self, message):
        print(message)


class PredictionService:
    def __init__(self, model, logger):
        self.model = model
        self.logger = logger

    def predict(self, data):
        self.logger.log("Prediction started")
        result = self.model.predict(data)
        self.logger.log("Prediction completed")
        return result
```

Now:

```python
model = Model()
logger = Logger()

service = PredictionService(model, logger)

print(service.predict([]))
```

The service composes:

```text
Model
Logger
```

and coordinates their responsibilities.

---

## 58. Practical Example: Replaceable Model

Suppose:

```python
class LinearModel:
    def predict(self, data):
        return "Linear prediction"


class NeuralNetwork:
    def predict(self, data):
        return "Neural prediction"
```

The service does not need to change:

```python
class PredictionService:
    def __init__(self, model):
        self.model = model

    def predict(self, data):
        return self.model.predict(data)
```

Use:

```python
service = PredictionService(LinearModel())
```

or:

```python
service = PredictionService(NeuralNetwork())
```

The same service works with either implementation.

This combines:

```text
Composition
+
Dependency Injection
+
Polymorphism
```

---

## 59. Composition and Architecture

Composition is not limited to small classes.

It can describe an entire application architecture.

For example:

```text
AI Application
│
├── Data Layer
│   ├── DataLoader
│   └── DataRepository
│
├── Processing Layer
│   ├── Cleaner
│   └── Transformer
│
├── ML Layer
│   ├── Model
│   └── Evaluator
│
└── Infrastructure
    ├── Logger
    └── Storage
```

Higher-level components coordinate lower-level components.

This creates a system composed of smaller subsystems.

---

## 60. Key Takeaways

Composition means building objects from other objects and using those objects to perform responsibilities.

Remember:

* Composition commonly represents a **has-a** relationship.
* Inheritance commonly represents an **is-a** relationship.
* Composition allows complex systems to be assembled from smaller components.
* Delegation is often used with composition.
* Dependency injection is a common way to provide composed dependencies.
* Composition can reduce coupling.
* Composition can improve cohesion and testability.
* Composition works naturally with polymorphism.
* Components can often be replaced without changing the containing class.
* Composition is useful in AI and machine-learning pipelines.
* Aggregation and composition describe different ownership semantics, although Python does not enforce the distinction syntactically.
* Composition over inheritance is a guideline, not an absolute rule.
* Inheritance remains appropriate for genuine subtype relationships.
* Avoid using inheritance merely for code reuse.
* Avoid excessive delegation and unnecessary abstraction.
* Good composition creates focused, replaceable, and understandable components.

The fundamental pattern is:

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()
```

Here:

```text
Car
 └── has an Engine
```

The `Car` does not need to implement the engine's internal behavior. It composes an `Engine` object and delegates the appropriate responsibility to it.

A practical design principle is:

> **Build complex behavior by composing focused objects when that produces clearer relationships, lower coupling, and greater flexibility than inheritance.**
