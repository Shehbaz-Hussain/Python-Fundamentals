# Module 15 - Object-Oriented Programming Solutions

## Intermediate Level Solutions

**Python Programming Foundation**

**Module:** 15 - Object-Oriented Programming

**Difficulty:** Intermediate

**Python Version:** 3.13+

---

# Solution 01: Student Class

```python
class Student:
    def __init__(self, name, age, program):
        self.name = name
        self.age = age
        self.program = program


student1 = Student("Ali", 20, "BS Artificial Intelligence")
student2 = Student("Sara", 21, "BS Computer Science")
student3 = Student("Ahmed", 22, "BS Data Science")

print("Student 1:")
print("Name:", student1.name)
print("Age:", student1.age)
print("Program:", student1.program)

print()

print("Student 2:")
print("Name:", student2.name)
print("Age:", student2.age)
print("Program:", student2.program)

print()

print("Student 3:")
print("Name:", student3.name)
print("Age:", student3.age)
print("Program:", student3.program)
```

---

# Solution 02: Student Information Method

```python
class Student:
    def __init__(self, name, age, program):
        self.name = name
        self.age = age
        self.program = program

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Program: {self.program}")


student1 = Student("Ali", 20, "BS Artificial Intelligence")
student2 = Student("Sara", 21, "BS Computer Science")

student1.display_info()

print()

student2.display_info()
```

---

# Solution 03: Rectangle Calculator

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rectangle = Rectangle(10, 5)

print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())
```

---

# Solution 04: Bank Account

```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


account = BankAccount("Ali", 50000)

account.deposit(10000)
account.withdraw(15000)
account.display_balance()
```

---

# Solution 05: Employee Salary Manager

```python
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")


employee = Employee("Sara", "Developer", 80000)

employee.give_raise(10000)
employee.display_info()
```

---

# Solution 06: Product Inventory

```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def increase_quantity(self, amount):
        if amount > 0:
            self.quantity += amount

    def decrease_quantity(self, amount):
        if amount <= 0:
            print("Quantity must be greater than zero.")
        elif amount > self.quantity:
            print("Insufficient product quantity.")
        else:
            self.quantity -= amount

    def display_product(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")


product = Product("Laptop", 120000, 10)

product.increase_quantity(5)
product.decrease_quantity(2)
product.display_product()
```

---

# Solution 07: Class Attribute

```python
class Student:
    school_name = "Karakoram International University"

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Ali", 20)
student2 = Student("Sara", 21)
student3 = Student("Ahmed", 22)

students = [student1, student2, student3]

for student in students:
    print(f"Name: {student.name}")
    print(f"School: {student.school_name}")
    print()
```

The `school_name` attribute belongs to the class, while `name` and `age` belong to individual objects.

---

# Solution 08: Employee Object Counter

```python
class Employee:
    employee_count = 0

    def __init__(self, name, position):
        self.name = name
        self.position = position
        Employee.employee_count += 1


employee1 = Employee("Ali", "Developer")
employee2 = Employee("Sara", "Designer")
employee3 = Employee("Ahmed", "Manager")
employee4 = Employee("Ayesha", "Data Analyst")
employee5 = Employee("Hamza", "AI Engineer")

print("Total Employees:", Employee.employee_count)
```

---

# Solution 09: Encapsulated Bank Account

```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")

    def check_balance(self):
        return self.__balance


account = BankAccount("Ali", 50000)

account.deposit(10000)
account.withdraw(15000)

print("Balance:", account.check_balance())
```

The double underscore creates a name-mangled attribute, making direct external access inappropriate.

---

# Solution 10: Animal Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def make_sound(self):
        print(f"{self.name}: Bark")


class Cat(Animal):
    def make_sound(self):
        print(f"{self.name}: Meow")


dog = Dog("Buddy")
cat = Cat("Milo")

dog.make_sound()
cat.make_sound()
```

---

# Solution 11: Vehicle Inheritance

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")


class Car(Vehicle):
    def drive(self):
        print("The car is driving.")


class Motorcycle(Vehicle):
    def ride(self):
        print("The motorcycle is riding.")


class Truck(Vehicle):
    def load(self):
        print("The truck is loading cargo.")


car = Car("Toyota", "Corolla")
motorcycle = Motorcycle("Honda", "CB 150F")
truck = Truck("Volvo", "FH")

car.display_info()
car.drive()

print()

motorcycle.display_info()
motorcycle.ride()

print()

truck.display_info()
truck.load()
```

---

# Solution 12: Method Overriding

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working.")


class Developer(Employee):
    def work(self):
        print(f"{self.name} is writing code.")


class Manager(Employee):
    def work(self):
        print(f"{self.name} is managing the team.")


developer = Developer("Ali")
manager = Manager("Sara")

developer.work()
manager.work()
```

The child classes override the `work()` method inherited from `Employee`.

---

# Solution 13: Polymorphism

```python
class Dog:
    def make_sound(self):
        print("Dog: Bark")


class Cat:
    def make_sound(self):
        print("Cat: Meow")


class Bird:
    def make_sound(self):
        print("Bird: Chirp")


animals = [
    Dog(),
    Cat(),
    Bird()
]

for animal in animals:
    animal.make_sound()
```

The same `make_sound()` operation produces different behavior depending on the object's type.

---

# Solution 14: Shape System

```python
import math


class Shape:
    def area(self):
        raise NotImplementedError("Child classes must implement area().")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(5),
    Rectangle(10, 4),
    Triangle(8, 6)
]

for shape in shapes:
    print(f"Area: {shape.area():.2f}")
```

---

# Solution 15: Payment System

```python
class CashPayment:
    def pay(self, amount):
        print(f"Paid {amount} using cash.")


class CardPayment:
    def pay(self, amount):
        print(f"Paid {amount} using card.")


class OnlinePayment:
    def pay(self, amount):
        print(f"Paid {amount} using online payment.")


payments = [
    CashPayment(),
    CardPayment(),
    OnlinePayment()
]

for payment in payments:
    payment.pay(5000)
```

Each class provides its own implementation of the same `pay()` interface.

---

# Solution 16: Library Management System

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"{self.title} by {self.author} - {status}")


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print("Book is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print("This member does not have this book.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def display_available_books(self):
        print("Available Books:")

        for book in self.books:
            if not book.is_borrowed:
                book.display_info()


book1 = Book("Python Programming", "John Smith")
book2 = Book("Artificial Intelligence", "David Brown")

member1 = Member("Ali")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.register_member(member1)

library.display_available_books()

print()

member1.borrow_book(book1)

print()

library.display_available_books()

print()

member1.return_book(book1)

print()

library.display_available_books()
```

---

# Solution 17: Shopping Cart

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name}: {self.price}")


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"{product_name} removed from cart.")
                return

        print("Product not found.")

    def display_products(self):
        if not self.products:
            print("Cart is empty.")
            return

        print("Shopping Cart:")

        for product in self.products:
            product.display()

    def calculate_total(self):
        return sum(product.price for product in self.products)


product1 = Product("Laptop", 120000)
product2 = Product("Mouse", 3000)
product3 = Product("Keyboard", 5000)

cart = ShoppingCart()

cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

cart.display_products()

print("Total:", cart.calculate_total())

cart.remove_product("Mouse")

print()

cart.display_products()
print("Total:", cart.calculate_total())
```

---

# Solution 18: Composition

```python
class Engine:
    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()

    def start(self):
        print(f"{self.brand} is starting.")
        self.engine.start()

    def stop(self):
        print(f"{self.brand} is stopping.")
        self.engine.stop()


car = Car("Toyota")

car.start()
car.stop()
```

The `Car` has an `Engine` object. This is **composition**: the `Car` is composed of an `Engine`.

---

# Solution 19: Abstract Shape

```python
from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


circle = Circle(5)
rectangle = Rectangle(10, 4)

print(f"Circle Area: {circle.area():.2f}")
print(f"Rectangle Area: {rectangle.area():.2f}")
```

`Shape` defines the required interface, while concrete subclasses provide the implementation.

---

# Solution 20: AI Model Class

```python
class AIModel:
    def __init__(self, name, model_type, version, accuracy):
        self.name = name
        self.model_type = model_type
        self.version = version
        self.accuracy = accuracy
        self.status = "Unloaded"

    def load(self):
        self.status = "Loaded"
        print(f"{self.name} has been loaded.")

    def unload(self):
        self.status = "Unloaded"
        print(f"{self.name} has been unloaded.")

    def display_info(self):
        print(f"Model Name: {self.name}")
        print(f"Model Type: {self.model_type}")
        print(f"Version: {self.version}")
        print(f"Accuracy: {self.accuracy}%")
        print(f"Status: {self.status}")


model = AIModel(
    "ImageClassifier",
    "Computer Vision",
    "1.0",
    94.5
)

model.display_info()

print()

model.load()

print()

model.display_info()
```

---

# Final Project: AI Model Management System

## Solution

```python
class AIModel:
    def __init__(self, name, model_type, version, accuracy):
        self.name = name
        self.model_type = model_type
        self.version = version
        self.accuracy = accuracy
        self.status = "Inactive"

    def activate(self):
        self.status = "Active"

    def deactivate(self):
        self.status = "Inactive"

    def update_info(self, model_type, version, accuracy):
        self.model_type = model_type
        self.version = version
        self.accuracy = accuracy

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Type: {self.model_type}")
        print(f"Version: {self.version}")
        print(f"Accuracy: {self.accuracy}%")
        print(f"Status: {self.status}")


class ModelRegistry:
    def __init__(self):
        self.models = []

    def add_model(self, model):
        self.models.append(model)
        print(f"Model '{model.name}' added successfully.")

    def display_models(self):
        if not self.models:
            print("No models available.")
            return

        for index, model in enumerate(self.models, start=1):
            print(f"\nModel {index}")
            print("-" * 30)
            model.display_info()

    def search_model(self, name):
        for model in self.models:
            if model.name.lower() == name.lower():
                return model

        return None

    def remove_model(self, name):
        model = self.search_model(name)

        if model is None:
            print("Model not found.")
            return

        self.models.remove(model)
        print(f"Model '{name}' removed successfully.")

    def display_statistics(self):
        total_models = len(self.models)
        active_models = sum(
            model.status == "Active"
            for model in self.models
        )

        inactive_models = total_models - active_models

        print("\nModel Statistics")
        print("-" * 30)
        print(f"Total Models: {total_models}")
        print(f"Active Models: {active_models}")
        print(f"Inactive Models: {inactive_models}")


def display_menu():
    print("\nAI Model Management System")
    print("-" * 30)
    print("1. Add Model")
    print("2. Display Models")
    print("3. Search Model")
    print("4. Update Model")
    print("5. Activate Model")
    print("6. Deactivate Model")
    print("7. Remove Model")
    print("8. Display Statistics")
    print("9. Exit")


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def add_model(registry):
    name = input("Enter model name: ")
    model_type = input("Enter model type: ")
    version = input("Enter version: ")
    accuracy = get_float_input("Enter accuracy: ")

    model = AIModel(
        name,
        model_type,
        version,
        accuracy
    )

    registry.add_model(model)


def search_model(registry):
    name = input("Enter model name: ")

    model = registry.search_model(name)

    if model is None:
        print("Model not found.")
    else:
        model.display_info()


def update_model(registry):
    name = input("Enter model name: ")

    model = registry.search_model(name)

    if model is None:
        print("Model not found.")
        return

    model_type = input("Enter new model type: ")
    version = input("Enter new version: ")
    accuracy = get_float_input("Enter new accuracy: ")

    model.update_info(
        model_type,
        version,
        accuracy
    )

    print("Model updated successfully.")


def activate_model(registry):
    name = input("Enter model name: ")

    model = registry.search_model(name)

    if model is None:
        print("Model not found.")
    else:
        model.activate()
        print("Model activated successfully.")


def deactivate_model(registry):
    name = input("Enter model name: ")

    model = registry.search_model(name)

    if model is None:
        print("Model not found.")
    else:
        model.deactivate()
        print("Model deactivated successfully.")


def remove_model(registry):
    name = input("Enter model name: ")
    registry.remove_model(name)


def main():
    registry = ModelRegistry()

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_model(registry)

        elif choice == "2":
            registry.display_models()

        elif choice == "3":
            search_model(registry)

        elif choice == "4":
            update_model(registry)

        elif choice == "5":
            activate_model(registry)

        elif choice == "6":
            deactivate_model(registry)

        elif choice == "7":
            remove_model(registry)

        elif choice == "8":
            registry.display_statistics()

        elif choice == "9":
            print("Program exited.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```

---

# Final Project Structure

The final project separates responsibilities between two main classes:

```text
AIModel
    |
    ├── Stores model information
    ├── Activates model
    ├── Deactivates model
    └── Updates model information

ModelRegistry
    |
    ├── Stores models
    ├── Adds models
    ├── Searches models
    ├── Removes models
    ├── Displays models
    └── Calculates statistics
```

The procedural functions handle user interaction, while the classes manage application data and behavior.

---

# OOP Concepts Demonstrated

## 1. Classes

Classes define the structure and behavior of objects.

```python
class AIModel:
    pass
```

## 2. Objects

Objects are instances of classes.

```python
model = AIModel(...)
```

## 3. Encapsulation

Data and behavior are grouped together inside classes.

## 4. Inheritance

A child class can reuse and extend functionality from a parent class.

```python
class Dog(Animal):
    pass
```

## 5. Polymorphism

Different objects can respond to the same method interface differently.

```python
for animal in animals:
    animal.make_sound()
```

## 6. Abstraction

Abstract classes define required interfaces without providing all implementation details.

```python
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

## 7. Composition

An object can contain another object.

```python
class Car:
    def __init__(self):
        self.engine = Engine()
```

---

# Important Notes

These solutions demonstrate one valid implementation for each problem. OOP problems generally have multiple correct designs.

The important objective is not to reproduce the exact code. You should understand:

* Why a class is needed.
* What responsibility each class has.
* Which data belongs to an object.
* Which behavior belongs to a method.
* When inheritance is appropriate.
* When composition is more appropriate than inheritance.
* How polymorphism allows common interfaces.
* How encapsulation controls object state.
* How abstraction defines required behavior.

For the final project, the design can be extended later with file storage, authentication, model version management, prediction logging, and other AI engineering features.
