# Encapsulation

**Encapsulation** is an object-oriented design principle concerned with organizing state and behavior together and controlling how an object's internal representation is accessed or modified.

In Python, encapsulation is implemented primarily through:

* Classes and objects
* Instance attributes
* Methods that operate on object state
* Naming conventions for non-public members
* Name mangling for double-underscore attributes
* Properties when controlled attribute access is required

A critical point is that Python does **not** provide strict private fields in the same way as languages such as Java or C++.

Instead, Python generally emphasizes **conventions, interfaces, and developer responsibility**.

---

## 1. What Does Encapsulation Mean?

Suppose a bank account contains:

```text
Account
├── account number
├── owner
├── balance
├── deposit()
└── withdraw()
```

The account's state and operations are related.

Instead of allowing unrelated code to manipulate the balance arbitrarily, the class can provide methods that define valid operations.

Conceptually:

```text
Object
│
├── Internal state
│
└── Public behavior
       │
       ├── deposit()
       └── withdraw()
```

The object becomes responsible for maintaining its own state.

---

## 2. Encapsulation Is More Than "Hiding Data"

A common oversimplification is:

> Encapsulation means making variables private.

That is incomplete.

Encapsulation is more fundamentally about:

* Bundling state and behavior.
* Defining clear interfaces.
* Controlling how state changes.
* Protecting invariants.
* Reducing unnecessary dependencies on implementation details.

For example, a bank account should not merely expose a balance. It should define rules governing how the balance changes.

---

## 3. A Basic Example

Without encapsulation:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
```

External code can directly perform:

```python
account.balance = -100000
```

The class has no control over whether that value is valid.

A better design can centralize the operation:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount
```

Now the class defines how deposits are performed.

---

## 4. Internal State

Internal state refers to information maintained by an object.

Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

The object contains:

```text
name
age
```

These attributes represent the object's state.

Encapsulation becomes important when the class needs to control how that state is used or modified.

---

## 5. Public Members

A public attribute or method is intended to be directly accessible.

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        return self.name
```

External code can use:

```python
student = Student("Ali")

print(student.name)
print(student.display_name())
```

There is no underscore convention indicating that these members are non-public.

---

## 6. Single Underscore Convention

Python uses a single leading underscore to communicate that a name is intended for internal or non-public use.

Example:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
```

The `_balance` name means:

> This attribute is intended for internal use and should generally not be treated as part of the public API.

However:

```python
account._balance
```

is still technically accessible.

Python does not prevent it.

---

## 7. The Single Underscore Is a Convention

This is valid:

```python
account._balance = 500
```

Python does not raise an access-control error merely because the attribute starts with `_`.

Therefore:

```text
_balance
    ↓
non-public convention
    ↓
not strict private access
```

This distinction is essential for understanding Python's approach to encapsulation.

---

## 8. Why Use `_name`?

The underscore communicates intent to other developers.

Consider:

```python
class NeuralNetwork:
    def __init__(self):
        self._weights = []
```

The underscore suggests:

> `_weights` is implementation state and should not normally be manipulated directly by users of the class.

A public API might instead expose:

```python
def predict(self, inputs):
    ...
```

The caller interacts with the model through meaningful operations rather than depending on its internal representation.

---

## 9. Public Interface vs Internal Implementation

A well-designed class can expose a small public interface while keeping implementation details internal.

For example:

```python
class BankAccount:
    def deposit(self, amount):
        ...

    def withdraw(self, amount):
        ...
```

The user does not need to know exactly how the account stores its balance.

This creates a boundary:

```text
External code
      │
      ▼
Public interface
      │
      ▼
Internal implementation
      │
      ▼
Object state
```

This separation reduces coupling between components.

---

## 10. Double Underscore Attributes

Python supports another mechanism using two leading underscores:

```python
class User:
    def __init__(self):
        self.__password = "secret"
```

The `__password` attribute is subject to **name mangling**.

Name mangling changes the internal attribute name to include the class name.

Conceptually:

```text
__password
     ↓
_User__password
```

For a class named `User`, Python internally stores the attribute under a mangled name similar to:

```python
_User__password
```

---

## 11. Name Mangling Is Not True Privacy

This is a critical distinction.

A double underscore does **not** make the attribute absolutely inaccessible.

For example:

```python
class User:
    def __init__(self):
        self.__password = "secret"
```

Python transforms the name internally.

It is possible, although generally inappropriate, to access the mangled attribute:

```python
user._User__password
```

Therefore:

```text
__password
    ↓
name mangling
    ↓
not absolute privacy
```

Name mangling primarily helps avoid accidental name collisions and discourages direct access.

---

## 12. Why Does Python Use Name Mangling?

One important purpose is preventing accidental attribute collisions in inheritance hierarchies.

Consider:

```python
class Parent:
    def __init__(self):
        self.__value = "parent"
```

Python mangles this approximately as:

```text
_Parent__value
```

If a subclass defines:

```python
class Child(Parent):
    def __init__(self):
        self.__value = "child"
```

that becomes approximately:

```text
_Child__value
```

The two attributes have different names internally.

This helps prevent accidental collisions.

---

## 13. Single vs Double Underscore

Compare:

```python
self._value
```

and:

```python
self.__value
```

### Single underscore

```text
_value
    ↓
non-public convention
```

### Double leading underscore

```text
__value
    ↓
name mangling
```

Neither should be interpreted as a traditional language-enforced private field.

---

## 14. Encapsulation Through Methods

One way to control state is to expose operations rather than raw attributes.

Example:

```python
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount

    def get_balance(self):
        return self._balance
```

Usage:

```python
account = BankAccount(100)

account.deposit(50)

print(account.get_balance())
```

Output:

```text
150
```

The class controls the rules for changing the balance.

---

## 15. Protecting Invariants

An **invariant** is a condition that should remain true for an object to be valid.

For a bank account:

```text
balance >= 0
```

may be an invariant.

A class can enforce it:

```python
class BankAccount:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount
```

The class becomes responsible for preserving the account's valid state.

---

## 16. Why Invariants Matter

Suppose external code can freely manipulate:

```python
account.balance
```

It could potentially create an invalid state:

```python
account.balance = -500
```

If all modifications pass through validated methods, the class has more control over maintaining its invariants.

This is one of the strongest practical reasons for encapsulation.

---

## 17. Encapsulation and APIs

A class's **public API** consists of the operations that users of the class are expected to depend upon.

For example:

```python
class Model:
    def train(self, data):
        ...

    def predict(self, inputs):
        ...
```

Users should generally interact with:

```python
model.train(...)
model.predict(...)
```

rather than depending on internal implementation details such as:

```python
model._internal_cache
model._training_state
```

The public API provides a stable conceptual interface.

---

## 18. Encapsulation and Implementation Changes

Suppose a model initially stores parameters as:

```python
self._weights = []
```

Later, the implementation changes to:

```python
self._parameters = {}
```

If external code directly depends on `_weights`, the change can break that code.

If external code uses:

```python
model.predict(...)
```

the internal representation can change without necessarily affecting callers.

This is one reason encapsulation reduces coupling.

---

## 19. Encapsulation and Coupling

**Coupling** describes the degree to which components depend on one another.

Directly accessing internal implementation details increases coupling.

For example:

```python
model._weights
model._cache
model._optimizer_state
```

creates dependencies on internal representation.

Using public behavior:

```python
model.predict(data)
```

creates a dependency on the public interface instead.

Generally:

```text
Less dependence on implementation details
                ↓
Lower coupling
                ↓
Easier maintenance
```

---

## 20. Encapsulation and Abstraction

Encapsulation and abstraction are related but not identical.

### Encapsulation

Focuses on:

* Bundling state and behavior.
* Controlling access.
* Protecting invariants.
* Separating public interfaces from internal implementation.

### Abstraction

Focuses on:

* Representing essential behavior.
* Hiding unnecessary complexity.
* Defining what an object does rather than exactly how it does it.

A useful distinction is:

```text
Encapsulation
    → How is internal state controlled?

Abstraction
    → What essential interface should users interact with?
```

Both concepts become important in larger software systems.

---

## 21. Properties

Python provides `property()` and the `@property` decorator for controlled attribute-style access.

Example:

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
```

Usage:

```python
person = Person(20)

print(person.age)
```

The caller uses:

```python
person.age
```

rather than:

```python
person.get_age()
```

The property provides a controlled interface while preserving attribute-style syntax.

---

## 22. Property Getters

A property getter defines how an attribute is read.

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
```

When:

```python
person.age
```

is evaluated, Python invokes the getter method.

Conceptually:

```text
person.age
    ↓
@property getter
    ↓
self._age
```

---

## 23. Property Setters

A property can also define controlled assignment.

```python
class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value
```

Now:

```python
person = Person(20)

person.age = 25
```

is allowed.

But:

```python
person.age = -5
```

raises:

```text
ValueError
```

The property setter enforces the class invariant.

---

## 24. Why Use Properties?

Properties are useful when an attribute needs controlled access without changing the interface from attribute syntax.

For example:

```python
person.age
```

is often cleaner than:

```python
person.get_age()
```

and:

```python
person.age = 30
```

can remain natural while still invoking validation logic.

Properties are particularly useful when a value:

* Needs validation.
* Is computed.
* Requires transformation.
* Should be read-only.
* May need implementation changes later.

---

## 25. Read-Only Properties

A property with no setter is effectively read-only through the property interface.

Example:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def diameter(self):
        return self._radius * 2
```

Usage:

```python
circle = Circle(5)

print(circle.diameter)
```

Output:

```text
10
```

Attempting:

```python
circle.diameter = 20
```

raises an error because no setter has been defined.

---

## 26. Computed Properties

A property does not necessarily correspond to stored state.

Example:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
```

Usage:

```python
rectangle = Rectangle(5, 4)

print(rectangle.area)
```

Output:

```text
20
```

`area` is calculated dynamically.

There is no need to store a separate `self.area` value.

---

## 27. Properties and Encapsulation

Properties allow a class to expose a clean interface while controlling internal representation.

Example:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance
```

The caller can read:

```python
account.balance
```

while the internal storage remains:

```python
_account._balance
```

The leading underscore communicates that `_balance` is implementation state.

---

## 28. Read-Only Model Parameters

In machine-learning software, some model information may be exposed as read-only.

For example:

```python
class Model:
    def __init__(self, version):
        self._version = version

    @property
    def version(self):
        return self._version
```

Then:

```python
model = Model("1.0")

print(model.version)
```

But:

```python
model.version = "2.0"
```

is not permitted through the property interface.

This can protect important object invariants.

---

## 29. Encapsulation in AI/ML Objects

Consider a simplified model:

```python
class Model:
    def __init__(self, weights):
        self._weights = weights

    def predict(self, inputs):
        ...
```

The model's weights are internal state.

Users typically care about:

```python
model.predict(inputs)
```

rather than the exact representation of:

```python
model._weights
```

The model class can therefore encapsulate implementation details.

In real ML frameworks, model objects often contain substantially more internal state, such as:

* Parameters
* Buffers
* Optimizer state
* Training state
* Configuration
* Caches
* Device information

Encapsulation helps keep these implementation details separate from the public API.

---

## 30. Encapsulation in a Training Component

Consider:

```python
class Trainer:
    def __init__(self, model, learning_rate):
        self._model = model
        self._learning_rate = learning_rate

    def train(self, data):
        ...
```

The trainer owns internal state:

```text
_model
_learning_rate
```

and exposes a high-level operation:

```python
trainer.train(data)
```

The caller does not need to manually manipulate every internal training variable.

---

## 31. Encapsulation and Separation of Responsibilities

A class should control the state for which it is responsible.

For example:

```python
class BankAccount:
    def deposit(self, amount):
        ...

    def withdraw(self, amount):
        ...
```

The account should be responsible for validating account-related state.

Likewise:

```python
class Model:
    def predict(self, inputs):
        ...
```

The model should be responsible for prediction behavior.

This leads to a broader design principle:

> Objects should manage the state and behavior that logically belong to their responsibilities.

---

## 32. Encapsulation Does Not Mean Every Attribute Must Be Hidden

Do not automatically make every attribute non-public.

This is perfectly reasonable:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

If `x` and `y` are intentionally part of the object's public conceptual interface, direct access may be appropriate.

Encapsulation is about appropriate boundaries, not hiding everything.

---

## 33. Over-Encapsulation Can Be Harmful

Consider:

```python
class Person:
    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value
```

If no validation or behavior is needed, these methods may provide little value.

Python commonly allows:

```python
class Person:
    def __init__(self, name):
        self.name = name
```

The design should match the actual requirements.

Do not create getters and setters mechanically just because another language commonly uses them.

---

## 34. Python's Philosophy

Python generally follows the principle often summarized as:

> We are all consenting adults here.

The language tends to favor conventions and clear interfaces over strict access restrictions.

Therefore:

```text
_public
    ↓
intended public API

_internal
    ↓
intended non-public implementation

__internal
    ↓
name mangling to reduce collisions
```

These mechanisms communicate intent rather than providing absolute security boundaries.

---

## 35. Encapsulation Is Not Security

This distinction is important.

A non-public attribute such as:

```python
self._password
```

does not provide secure storage.

A name-mangled attribute such as:

```python
self.__password
```

does not provide cryptographic protection.

Python's encapsulation mechanisms are primarily software-design mechanisms.

Do not use them as a substitute for:

* Encryption
* Authentication
* Authorization
* Secure secret management
* Access-control systems

---

## 36. Name Mangling Example

```python
class Account:
    def __init__(self):
        self.__balance = 100
```

Python internally transforms the attribute name approximately to:

```text
_Account__balance
```

Therefore:

```python
account.__balance
```

does not directly find the attribute under that exact name.

But:

```python
account._Account__balance
```

can access the mangled attribute.

Again, this demonstrates that name mangling is not a security feature.

---

## 37. Name Mangling and Subclasses

Consider:

```python
class Parent:
    def __init__(self):
        self.__value = "parent"


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = "child"
```

The two attributes are approximately:

```text
_Parent__value
_Child__value
```

They do not collide because their names are mangled using different class names.

This is one of the practical purposes of double-leading-underscore attributes.

---

## 38. Encapsulation Through a Property Setter

A useful example is a model's learning rate.

```python
class ModelConfig:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    @property
    def learning_rate(self):
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, value):
        if value <= 0:
            raise ValueError("Learning rate must be positive")

        self._learning_rate = value
```

Now:

```python
config = ModelConfig(0.01)
```

is valid.

But:

```python
config.learning_rate = -0.1
```

raises an exception.

The property protects the invariant:

```text
learning_rate > 0
```

---

## 39. Encapsulation Through a Read-Only Property

Consider a model's number of parameters.

```python
class Model:
    def __init__(self, weights):
        self._weights = weights

    @property
    def parameter_count(self):
        return len(self._weights)
```

The parameter count is computed from internal state.

Users can write:

```python
print(model.parameter_count)
```

but should not directly assign:

```python
model.parameter_count = 1000
```

because the value should be derived from the actual parameters.

---

## 40. Encapsulation and Invariants in ML

Machine-learning objects frequently have state that must remain consistent.

For example:

```text
Model
├── input dimension
├── output dimension
├── weights
└── bias
```

An invariant might be:

```text
number of weight rows == expected input dimension
```

If arbitrary external code can replace the weights without validation, the model may become internally inconsistent.

Encapsulating updates allows the class to validate changes before accepting them.

---

## 41. Encapsulation and Mutable Objects

Encapsulation becomes more difficult when internal mutable objects are exposed directly.

Consider:

```python
class Model:
    def __init__(self, weights):
        self._weights = weights

    @property
    def weights(self):
        return self._weights
```

If `weights` is a mutable list, callers may modify it:

```python
model.weights.append(10)
```

The property does not automatically prevent mutation.

This is an important limitation.

Encapsulation requires thinking about **references and mutability**, not merely attribute visibility.

---

## 42. Returning Copies

If necessary, a class can return a copy rather than its internal mutable object.

```python
class Model:
    def __init__(self, weights):
        self._weights = weights

    @property
    def weights(self):
        return self._weights.copy()
```

Now:

```python
weights = model.weights
weights.append(10)
```

does not directly modify the internal list.

This approach can help preserve internal state.

The appropriate solution depends on the object's data structures and performance requirements.

---

## 43. Encapsulation and Immutable Interfaces

Another approach is to expose immutable representations where appropriate.

For example:

```python
class Point:
    def __init__(self, x, y):
        self._coordinates = (x, y)

    @property
    def coordinates(self):
        return self._coordinates
```

The tuple itself cannot be modified in place.

This can simplify reasoning about object state.

However, immutability and encapsulation are related but distinct concepts.

---

## 44. Encapsulation vs Data Hiding

These terms are often used interchangeably, but they are not identical.

### Encapsulation

Organizes and controls state and behavior.

### Data hiding

Restricts or discourages direct access to implementation details.

Python supports both conceptually, but its mechanisms are primarily based on conventions and interfaces rather than strict access restrictions.

---

## 45. Encapsulation vs Abstraction

A practical comparison:

| Concept       | Main concern                                                    |
| ------------- | --------------------------------------------------------------- |
| Encapsulation | Control and organization of state and behavior                  |
| Data hiding   | Limiting exposure of implementation details                     |
| Abstraction   | Exposing essential behavior while hiding unnecessary complexity |

For example:

```python
model.predict(data)
```

is an abstraction.

Keeping:

```python
model._internal_cache
```

outside the public interface is related to encapsulation and data hiding.

---

## 46. Common Mistake: Calling `_name` Private

Incorrect assumption:

```python
self._balance
```

means:

> Python prevents external code from accessing this attribute.

That is false.

Correct interpretation:

```text
_balance
    ↓
Python convention for non-public use
```

It remains accessible.

---

## 47. Common Mistake: Treating `__name` as Secure

Incorrect assumption:

```python
self.__password
```

means:

> The value is inaccessible from outside the class.

That is false.

Python performs name mangling, but the attribute can still be accessed using its mangled name.

Name mangling is primarily useful for avoiding accidental name collisions.

---

## 48. Common Mistake: Using Getters and Setters for Everything

This pattern:

```python
class Person:
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
```

is not automatically better than:

```python
class Person:
    def __init__(self, name):
        self.name = name
```

If no control or transformation is needed, direct public attributes can be perfectly reasonable.

Use properties or methods when they provide meaningful behavior.

---

## 49. Common Mistake: Returning Internal Mutable State

Consider:

```python
class Model:
    @property
    def weights(self):
        return self._weights
```

If `_weights` is mutable, callers may mutate the internal state indirectly.

The property itself does not guarantee encapsulation.

Possible alternatives include:

* Returning a copy.
* Returning an immutable representation.
* Providing controlled mutation methods.
* Designing the object so the state cannot be changed after initialization.

The correct choice depends on the requirements.

---

## 50. Common Mistake: Confusing Encapsulation With Abstraction

Encapsulation is not simply:

> Hiding complexity.

That is more closely associated with abstraction.

Encapsulation concerns the organization and control of state and behavior.

For example:

```python
account.withdraw(100)
```

encapsulates the account's state-changing operation.

The fact that the caller does not need to know the internal withdrawal algorithm is also an abstraction benefit.

The two concepts often work together.

---

## 51. Best Practices for Encapsulation

### 1. Define a clear public interface

Expose operations that users actually need.

### 2. Keep implementation details non-public when appropriate

Use `_name` to communicate internal intent.

### 3. Protect important invariants

Validate state transitions.

### 4. Use properties when controlled attribute access is useful

Do not create getters and setters unnecessarily.

### 5. Avoid exposing mutable internal state carelessly

Consider copies or immutable representations.

### 6. Keep responsibilities within the appropriate class

The class should manage state that belongs to it.

### 7. Do not treat name mangling as security

`__name` is not encryption or access control.

### 8. Avoid excessive encapsulation

Public attributes are acceptable when they are genuinely part of the public interface.

---

## 52. Practical Example: Bank Account

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount
```

Usage:

```python
account = BankAccount("Ali", 1000)

account.deposit(500)
account.withdraw(200)

print(account.balance)
```

Output:

```text
1300
```

The object controls the valid state transitions.

---

## 53. Practical Example: ML Configuration

```python
class ModelConfig:
    def __init__(self, learning_rate, epochs):
        self.learning_rate = learning_rate
        self.epochs = epochs

    @property
    def learning_rate(self):
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, value):
        if value <= 0:
            raise ValueError("Learning rate must be positive")

        self._learning_rate = value

    @property
    def epochs(self):
        return self._epochs

    @epochs.setter
    def epochs(self, value):
        if value <= 0:
            raise ValueError("Epoch count must be positive")

        self._epochs = value
```

The configuration object guarantees:

```text
learning_rate > 0
epochs > 0
```

The validation logic is encapsulated within the class.

---

## 54. Practical Example: Model State

```python
class Model:
    def __init__(self, weights):
        self._weights = weights

    @property
    def parameter_count(self):
        return len(self._weights)

    def predict(self, inputs):
        # Model prediction logic
        ...
```

The public interface exposes:

```text
parameter_count
predict()
```

while `_weights` remains an implementation detail.

This design becomes particularly useful as models become more complex.

---

## 55. Encapsulation and Maintainability

Good encapsulation can make software easier to maintain because internal implementation can change without requiring every caller to change.

For example, a model might initially use:

```text
_list of weights
```

and later use:

```text
_numpy array
```

or:

```text
dictionary of named parameters
```

If callers depend only on the public model interface, the internal representation can change with less disruption.

This is one of the major benefits of encapsulation in large systems.

---

## 56. Encapsulation and API Stability

A public API should represent behavior that users can reasonably depend upon.

Internal implementation details should not become accidental APIs.

For example:

```python
model.predict(inputs)
```

is a meaningful public operation.

But:

```python
model._internal_tensor_cache
```

is typically an implementation detail.

When designing libraries, keeping this distinction clear helps preserve API stability.

---

## Summary

Encapsulation is an OOP design principle for organizing state and behavior and controlling how internal state is accessed and modified.

Key points:

* Encapsulation groups related state and behavior.
* It helps classes maintain valid internal state.
* It supports clear public interfaces.
* A single leading underscore indicates intended non-public use.
* `_name` is a convention, not strict access control.
* A double leading underscore triggers name mangling.
* Name mangling helps avoid accidental name collisions.
* `__name` is not a security mechanism.
* Properties provide controlled attribute-style access.
* Property setters can enforce invariants.
* Read-only properties can expose derived or protected information.
* Returning mutable internal objects can weaken encapsulation.
* Copies or immutable representations may sometimes be appropriate.
* Encapsulation reduces unnecessary coupling to implementation details.
* Encapsulation and abstraction are related but distinct concepts.
* Python favors conventions and explicit interfaces rather than strict private fields.
* Good encapsulation does not mean hiding every attribute.
* Functions and classes should expose only boundaries that provide meaningful design value.

The core idea can be summarized as:

```text
Object
│
├── Internal state
│      ↓
│   controlled by the class
│
└── Public interface
       ↓
    meaningful operations
```

A well-designed object should protect important invariants while exposing a clear and useful interface.

For Python, remember the three important mechanisms:

```text
_name
    → non-public convention

__name
    → name mangling

@property
    → controlled attribute-style access
```

These mechanisms form an important part of Python's practical approach to encapsulation.
