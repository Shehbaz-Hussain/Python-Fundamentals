# Instance Methods

Instance methods are functions defined inside a class that operate on individual objects.

They are one of the central mechanisms of object-oriented programming because they allow an object to combine **state** with **behavior**.

For example, a bank account can store a balance and provide methods that operate on that balance:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

Here:

* `balance` is instance state.
* `deposit()` is an instance method.
* `self` identifies the object whose state the method operates on.

---

## 1. What Is an Instance Method?

An instance method is a function defined inside a class whose first parameter conventionally refers to the instance.

Example:

```python
class Student:
    def introduce(self):
        print("I am a student.")
```

The method:

```python
introduce()
```

is an instance method because it is intended to operate on a particular `Student` object.

Create an instance:

```python
student = Student()
```

Then call the method:

```python
student.introduce()
```

Output:

```text
I am a student.
```

---

## 2. Basic Instance Method Syntax

The general syntax is:

```python
class ClassName:
    def method_name(self):
        # method body
        ...
```

For example:

```python
class Dog:
    def bark(self):
        print("Woof!")
```

Create an object:

```python
dog = Dog()
```

Call the method:

```python
dog.bark()
```

The method is executed in the context of the `dog` instance.

---

## 3. Instance Methods and Instance State

Instance methods become especially useful when they operate on instance attributes.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")
```

Create an object:

```python
student = Student("Ali")
```

Call the method:

```python
student.introduce()
```

Output:

```text
My name is Ali.
```

The method accesses:

```python
self.name
```

which belongs to the current instance.

---

## 4. Why `self` Is Required

The first parameter of a normal instance method is conventionally named `self`.

```python
class Student:
    def introduce(self):
        print(self.name)
```

`self` provides access to the particular instance on which the method is operating.

For example:

```python
student1 = Student()
student2 = Student()
```

When:

```python
student1.introduce()
```

is called, `self` refers to `student1`.

When:

```python
student2.introduce()
```

is called, `self` refers to `student2`.

Therefore, one method definition can operate on many different objects.

The detailed mechanics of `self` are covered in the dedicated `self-parameter.md` section.

---

## 5. Calling an Instance Method

The normal syntax is:

```python
object.method()
```

For example:

```python
class Car:
    def start(self):
        print("Car started.")


car = Car()
car.start()
```

Output:

```text
Car started.
```

The dot operator accesses the method through the object.

---

## 6. Instance Methods with Parameters

An instance method can accept additional parameters.

```python
class Calculator:
    def add(self, a, b):
        return a + b
```

Create an object:

```python
calculator = Calculator()
```

Call the method:

```python
result = calculator.add(10, 5)

print(result)
```

Output:

```text
15
```

The parameters are:

```text
self → the current object
a    → 10
b    → 5
```

When calling through the object, you normally provide only the arguments after `self`.

---

## 7. Instance Methods Can Return Values

Instance methods can use `return` just like ordinary functions.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

Create an object:

```python
rectangle = Rectangle(10, 5)
```

Call the method:

```python
result = rectangle.area()

print(result)
```

Output:

```text
50
```

The method returns a value rather than printing it.

This allows the calling code to decide what to do with the result.

---

## 8. Methods That Modify Object State

An instance method can change the object's attributes.

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

The method changes the state of the particular object.

---

## 9. Methods That Read Object State

Methods do not have to modify state.

They can simply inspect it.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age
```

Usage:

```python
student = Student("Ali", 20)

print(student.get_age())
```

Output:

```text
20
```

The method reads state and returns information about the object.

---

## 10. Methods That Read and Modify State

A method can both read and modify state.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True

        return False
```

Usage:

```python
account = BankAccount(1000)

success = account.withdraw(300)

print(success)
print(account.balance)
```

Output:

```text
True
700
```

The method:

1. Reads `self.balance`.
2. Checks a condition.
3. Modifies `self.balance`.
4. Returns a result.

---

## 11. Methods Can Use Multiple Instance Attributes

A method can operate on several attributes.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height
```

The methods operate on the same object's state.

```python
rectangle = Rectangle(10, 5)

print(rectangle.area())
print(rectangle.perimeter())
```

Output:

```text
50
30
```

---

## 12. One Instance Method Can Call Another

An instance method can call another instance method using `self`.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def introduce(self):
        print(f"My name is {self.get_name()}.")
```

Calling:

```python
student = Student("Ali")
student.introduce()
```

produces:

```text
My name is Ali.
```

The expression:

```python
self.get_name()
```

calls another method on the same object.

This can help separate responsibilities within a class.

---

## 13. Methods Can Accept Objects as Arguments

An instance method can receive another object.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def compare_name(self, other):
        return self.name == other.name
```

Create objects:

```python
student1 = Student("Ali")
student2 = Student("Sara")
```

Compare them:

```python
print(student1.compare_name(student2))
```

Output:

```text
False
```

This demonstrates that objects can interact with other objects.

---

## 14. Methods Can Return Objects

An instance method can return another object.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def copy(self):
        return Point(self.x, self.y)
```

Usage:

```python
point1 = Point(10, 20)
point2 = point1.copy()
```

Now:

```python
print(point1 is point2)
```

Output:

```text
False
```

The method creates a separate object.

---

## 15. Instance Methods Can Use Local Variables

Instance methods can have local variables just like ordinary functions.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def description(self):
        area = self.width * self.height
        return f"Area: {area}"
```

Here:

```python
area
```

is a local variable.

It is different from:

```python
self.area
```

which would be an instance attribute.

This distinction is important:

```text
area       → local variable
self.area  → instance attribute
```

---

## 16. Parameters vs Instance Attributes vs Local Variables

Consider:

```python
class Product:
    def calculate_total(self, price, quantity):
        total = price * quantity
        return total
```

There are three different categories:

```text
price
quantity
    ↓
parameters

total
    ↓
local variable

self.name
self.price
    ↓
instance attributes
```

They have different scopes and purposes.

Understanding this distinction prevents many OOP mistakes.

---

## 17. Instance Methods Can Have Default Parameters

Instance methods follow normal Python function parameter rules.

```python
class Greeter:
    def greet(self, name="Guest"):
        print(f"Hello, {name}.")
```

Calling:

```python
greeter = Greeter()

greeter.greet()
greeter.greet("Ali")
```

Output:

```text
Hello, Guest.
Hello, Ali.
```

The presence of `self` does not change the ordinary rules for the remaining parameters.

---

## 18. Instance Methods Can Accept Keyword Arguments

For example:

```python
class Student:
    def introduce(self, greeting, punctuation="."):
        print(f"{greeting}, {self.name}{punctuation}")

    def __init__(self, name):
        self.name = name
```

Call:

```python
student = Student("Ali")

student.introduce(
    greeting="Hello",
    punctuation="!"
)
```

Output:

```text
Hello, Ali!
```

Instance methods support positional and keyword arguments according to normal Python calling rules.

---

## 19. Instance Methods Can Use Conditional Logic

Methods can contain normal control flow.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def is_positive(self):
        if self.balance > 0:
            return True

        return False
```

Usage:

```python
account = BankAccount(100)

print(account.is_positive())
```

Output:

```text
True
```

OOP does not introduce a separate control-flow system. Classes and methods use ordinary Python language features.

---

## 20. Instance Methods Can Use Loops

Methods can contain loops when iteration is appropriate.

```python
class GradeBook:
    def __init__(self, grades):
        self.grades = grades

    def calculate_total(self):
        total = 0

        for grade in self.grades:
            total += grade

        return total
```

Usage:

```python
grade_book = GradeBook([80, 90, 70])

print(grade_book.calculate_total())
```

Output:

```text
240
```

The method operates on data stored by the object.

---

## 21. Methods and Data Structures

Instance attributes frequently contain data structures.

```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def item_count(self):
        return len(self.items)
```

Usage:

```python
cart = ShoppingCart()

cart.add_item("Keyboard")
cart.add_item("Mouse")

print(cart.item_count())
```

Output:

```text
2
```

This demonstrates how OOP can organize behavior around existing Python data structures.

---

## 22. Instance Methods and Object State

A useful way to understand instance methods is:

```text
Object
│
├── State
│   ├── name
│   ├── age
│   └── balance
│
└── Behavior
    ├── update()
    ├── display()
    └── calculate()
```

The attributes represent **what the object knows**.

The methods represent **what the object can do**.

This is a conceptual model rather than a strict rule. Not every class must expose methods for every piece of state.

---

## 23. Instance Methods and Encapsulation

Instance methods can provide controlled operations over object state.

For example:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount

    def get_balance(self):
        return self._balance
```

The class provides operations for changing and retrieving state.

The leading underscore indicates that `_balance` is intended as non-public by convention.

This is one aspect of encapsulation and will be examined more fully later.

---

## 24. Direct Method Invocation

Suppose:

```python
class Student:
    def introduce(self):
        print("Hello")
```

Then:

```python
student = Student()
student.introduce()
```

is the normal method-call syntax.

Python effectively binds the instance to the method.

Conceptually:

```text
student.introduce()
        │
        ↓
bound method
        │
        ↓
introduce(student)
```

The exact implementation is based on Python's descriptor and method-binding mechanisms, but the conceptual transformation is useful for understanding why `self` receives the instance.

---

## 25. Calling an Instance Method Through the Class

The same method can be accessed through the class:

```python
class Student:
    def introduce(self):
        print("Hello")
```

Create an object:

```python
student = Student()
```

Normal:

```python
student.introduce()
```

Explicit form:

```python
Student.introduce(student)
```

These are conceptually equivalent for this ordinary method.

The second form makes the instance argument explicit.

Normally, the first form is preferred because it communicates the intent more clearly.

---

## 26. What Happens When `self` Is Not Supplied?

Consider:

```python
class Student:
    def introduce(self):
        print("Hello")
```

Calling:

```python
Student.introduce()
```

does not provide the required `self` argument.

Python raises a `TypeError` indicating that the required positional argument is missing.

The normal call:

```python
student.introduce()
```

automatically supplies `student` as the first argument.

---

## 27. `self` Is a Convention

Python does not require the literal parameter name `self`.

Technically, this works:

```python
class Student:
    def introduce(current_student):
        print("Hello")
```

However, this is strongly discouraged.

The standard convention is:

```python
def introduce(self):
```

Using `self` makes the code immediately recognizable to Python developers and follows PEP 8 conventions.

The important concept is the role of the first parameter, not the spelling itself.

---

## 28. Instance Methods and Multiple Objects

One method definition can operate on many objects.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")
```

Create objects:

```python
dog1 = Dog("Max")
dog2 = Dog("Buddy")
```

Call the same method:

```python
dog1.bark()
dog2.bark()
```

Output:

```text
Max says woof!
Buddy says woof!
```

The method is shared by the class, but it operates on different instance state.

---

## 29. Instance Methods and Return Values

Methods can return any appropriate Python value.

For example:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def is_square(self):
        return self.width == self.height
```

Usage:

```python
rectangle = Rectangle(10, 5)

area = rectangle.area()
square = rectangle.is_square()
```

The methods return:

```text
area   → 50
square → False
```

Methods should generally return information when the caller needs to use it, rather than printing it unnecessarily.

---

## 30. Printing vs Returning

Compare:

```python
class Calculator:
    def add_and_print(self, a, b):
        print(a + b)
```

with:

```python
class Calculator:
    def add(self, a, b):
        return a + b
```

The second method is usually more reusable:

```python
calculator = Calculator()

result = calculator.add(10, 5)

print(result)
```

The returned value can be:

* Printed
* Stored
* Compared
* Passed to another function
* Used in another calculation

A method that only prints a result limits how the result can be used.

---

## 31. Instance Methods and Exceptions

Methods can raise exceptions when invalid operations occur.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
```

The method protects the object's state by rejecting invalid operations.

Exception handling itself should be performed by the caller or an appropriate application layer when necessary.

---

## 32. Instance Methods and State Validation

Methods can validate inputs before changing state.

```python
class Temperature:
    def __init__(self, value):
        self.value = value

    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")

        self.value = value
```

This allows the class to maintain a meaningful state.

The method becomes a controlled boundary for modifying the attribute.

---

## 33. Instance Methods Should Have Clear Responsibilities

A method should ideally have a focused responsibility.

Good:

```python
class Report:
    def calculate_total(self):
        ...

    def format_report(self):
        ...

    def save_report(self):
        ...
```

Each method has a distinct responsibility.

A method that performs unrelated operations can become difficult to understand and test.

This connects OOP to the broader software-engineering principle of **separation of responsibilities**.

---

## 34. Avoid Overloading Classes with Unrelated Methods

A class such as:

```python
class Student:
    def calculate_grade(self):
        ...

    def send_email(self):
        ...

    def connect_to_database(self):
        ...

    def generate_invoice(self):
        ...
```

may indicate poor separation of responsibilities unless these operations genuinely belong to the same abstraction.

The goal of OOP is not to put every related-looking function into a class.

The class should represent a coherent abstraction.

---

## 35. Instance Methods and Cohesion

**Cohesion** describes how closely related the responsibilities of a component are.

A class with highly related methods generally has higher cohesion.

For example:

```python
class BankAccount:
    def deposit(self, amount):
        ...

    def withdraw(self, amount):
        ...

    def get_balance(self):
        ...
```

These operations are strongly related to the concept of a bank account.

By contrast, adding unrelated functionality can reduce cohesion.

High cohesion generally improves maintainability and comprehension.

---

## 36. Instance Methods and Coupling

**Coupling** describes the degree to which one component depends on other components.

A method that requires extensive knowledge of unrelated classes can increase coupling.

For example, if a simple `Student` class directly manages:

* Database connections
* Email servers
* File formats
* User interfaces
* External APIs

the design may become tightly coupled.

Good object-oriented design generally aims for:

```text
High cohesion
+
Reasonably low coupling
```

These are design goals rather than absolute rules.

---

## 37. Instance Methods in AI/ML Software

Instance methods are common in machine-learning systems.

A simplified model might expose methods such as:

```python
class Model:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    def train(self, data):
        print("Training model...")

    def predict(self, data):
        print("Generating predictions...")

    def evaluate(self, data):
        print("Evaluating model...")
```

Usage:

```python
model = Model(0.001)

model.train(training_data)
model.predict(test_data)
model.evaluate(test_data)
```

Real machine-learning libraries use much more complex implementations, but the conceptual relationship remains:

```text
Model object
│
├── State
│   └── configuration / learned parameters
│
└── Behavior
    ├── train()
    ├── predict()
    └── evaluate()
```

Understanding instance methods is therefore directly relevant to reading AI and ML libraries.

---

## 38. Instance Methods and Scikit-Learn-Style APIs

Many machine-learning APIs use methods that operate on model instances.

A simplified example is:

```python
class SimpleModel:
    def fit(self, X, y):
        print("Model fitted.")

    def predict(self, X):
        return []
```

Usage:

```python
model = SimpleModel()

model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

This style is common because the model object can retain learned state between method calls.

Conceptually:

```text
fit()
 ↓
model state changes
 ↓
predict()
 ↓
uses learned state
```

The actual behavior of production ML frameworks is considerably more sophisticated.

---

## 39. Common Errors

### Error 1: Forgetting `self`

Incorrect:

```python
class Student:
    def introduce():
        print("Hello")
```

Calling:

```python
student.introduce()
```

causes a `TypeError` because Python supplies the instance as the first argument.

Correct:

```python
class Student:
    def introduce(self):
        print("Hello")
```

---

### Error 2: Forgetting `self` when accessing instance state

Incorrect:

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(name)
```

`name` is not a local variable in `introduce()`.

Correct:

```python
def introduce(self):
    print(self.name)
```

---

### Error 3: Calling an instance method without an instance

Incorrect:

```python
Student.introduce()
```

when `introduce()` requires `self`.

Normal usage:

```python
student = Student()
student.introduce()
```

---

### Error 4: Using `self` for local data unnecessarily

Not every value should become an instance attribute.

Avoid:

```python
class Calculator:
    def add(self, a, b):
        self.result = a + b
        return self.result
```

if the result does not need to persist as object state.

Prefer:

```python
class Calculator:
    def add(self, a, b):
        result = a + b
        return result
```

or simply:

```python
class Calculator:
    def add(self, a, b):
        return a + b
```

The distinction between temporary local data and persistent object state is important.

---

### Error 5: Putting unrelated behavior into one class

A class should not become a container for arbitrary functions merely because those functions can technically be defined as methods.

Design classes around coherent responsibilities.

---

## 40. Complete Example

Consider a simplified `BankAccount` class:

```python
class BankAccount:
    def __init__(self, owner, balance=0):
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

    def display(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")
```

Create an object:

```python
account = BankAccount("Ali", 1000)
```

Deposit:

```python
account.deposit(500)
```

Withdraw:

```python
account.withdraw(200)
```

Retrieve the balance:

```python
print(account.get_balance())
```

Output:

```text
1300
```

Display the account:

```python
account.display()
```

Output:

```text
Owner: Ali
Balance: 1300
```

This class demonstrates:

* Instance attributes
* Instance methods
* Reading state
* Modifying state
* Input validation
* Returning values
* Object-specific behavior

---

## 41. Instance Method Mental Model

A useful conceptual model is:

```text
Class
│
├── Instance attributes
│       ↓
│     State
│
└── Instance methods
        ↓
      Behavior
        │
        ↓
   operates on
        │
        ↓
   current instance
```

For:

```python
account.deposit(500)
```

think:

```text
account
   │
   └── deposit(500)
            │
            ↓
     modify account state
```

The method is defined once, but the state it operates on belongs to the particular object.

---

## Summary

Instance methods provide behavior for individual objects.

Key points:

* Instance methods are functions defined inside classes.
* Their first parameter is conventionally named `self`.
* `self` refers to the current instance.
* Instance methods can read instance attributes.
* They can modify instance attributes.
* They can return values.
* They can accept additional parameters.
* They can call other methods using `self`.
* They can interact with other objects.
* They can contain normal Python control flow.
* They can raise exceptions and validate state.
* A method should generally have a clear and coherent responsibility.
* High cohesion and reasonable low coupling are important design goals.
* Not every function needs to become a method.
* Instance methods are especially useful when behavior depends on object-specific state.
* AI and ML libraries frequently use instance methods for operations such as training, prediction, evaluation, transformation, and configuration.

The central relationship is:

```text
Instance attributes
       ↓
     State
       +
Instance methods
       ↓
    Behavior
       ↓
operates on the object's state
```

For example:

```python
account.deposit(500)
```

means that the `deposit()` behavior is being performed on the particular `account` instance.

The next concept is `self`, which explains precisely how Python connects an instance method call to the object on which it operates.
