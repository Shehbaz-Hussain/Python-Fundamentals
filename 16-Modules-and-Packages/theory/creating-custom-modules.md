# Creating Custom Modules

## Overview

A **custom module** is a Python file created by a developer to organize reusable code.

Any Python file containing reusable definitions such as functions, classes, constants, or other module-level code can serve as a custom module.

For example:

```text
project/
├── main.py
└── calculator.py
```

Here, `calculator.py` can provide functionality that `main.py` imports and uses.

Custom modules are one of the simplest ways to divide a Python application into focused, reusable components.

---

## Why Create Custom Modules?

As applications grow, putting all code into one file becomes difficult to maintain.

A custom module can help you:

* Organize related functionality.
* Reuse code across multiple files.
* Separate responsibilities.
* Improve readability.
* Reduce duplication.
* Make testing easier.
* Establish a foundation for larger package structures.

For example, instead of placing all mathematical operations in `main.py`, they can be moved into a dedicated `calculator.py` module.

---

## Basic Custom Module

Create a file named:

```text
calculator.py
```

with:

```python
def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b
```

This file is now a custom module named `calculator`.

Another Python file can import it:

```python
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
```

Output:

```text
15
5
```

The importing module accesses the functions through the `calculator` namespace.

---

## Module Names

The filename determines the module's import name in a basic local project.

For:

```text
calculator.py
```

the module is normally imported as:

```python
import calculator
```

The `.py` extension is not included in the import statement.

For:

```text
text_utils.py
```

use:

```python
import text_utils
```

Python module names should generally be simple, descriptive, and compatible with normal Python identifier conventions.

A common convention is lowercase names with underscores when needed:

```text
file_utils.py
data_processing.py
string_helpers.py
```

---

## Creating a Reusable Utility Module

Suppose an application needs several text operations.

Instead of putting everything into one file, create:

```text
text_utils.py
```

```python
def normalize_text(text: str) -> str:
    return " ".join(text.strip().split())


def count_words(text: str) -> int:
    normalized = normalize_text(text)

    if not normalized:
        return 0

    return len(normalized.split())
```

Another file can use the module:

```python
import text_utils

text = "  Python   modules are useful.  "

clean_text = text_utils.normalize_text(text)
word_count = text_utils.count_words(text)

print(clean_text)
print(word_count)
```

Output:

```text
Python modules are useful.
4
```

The text-processing responsibility is isolated from the application code.

---

## Importing a Custom Module

A custom module can be imported with the standard `import` statement:

```python
import calculator
```

Then access its members:

```python
calculator.add(2, 3)
calculator.subtract(8, 3)
```

This approach makes the source of each function explicit.

For example:

```python
result = calculator.add(10, 20)
```

clearly shows that `add()` belongs to the `calculator` module.

---

## Importing Specific Members

A custom module can also be imported with `from ... import ...`.

For example:

```python
from calculator import add

result = add(10, 20)

print(result)
```

Multiple members can be imported:

```python
from calculator import add, subtract

print(add(10, 5))
print(subtract(10, 5))
```

This creates direct local bindings for the imported names.

---

## Using an Import Alias

A custom module can have a local alias:

```python
import text_utils as text

print(text.normalize_text("  Python   "))
```

Aliases should improve readability rather than make code unnecessarily difficult to understand.

For most custom modules, the original descriptive module name is usually preferable unless there is a clear reason for an alias.

---

## Custom Modules with Constants

A module can contain constants alongside functions.

Example:

```python
# conversion.py

KM_TO_MILES = 0.621371


def kilometers_to_miles(kilometers: float) -> float:
    return kilometers * KM_TO_MILES
```

Another file can import the module:

```python
import conversion

distance = conversion.kilometers_to_miles(10)

print(distance)
```

The module groups related data and behavior together.

---

## Custom Modules with Classes

Custom modules can also contain classes.

Example:

```python
# student.py

class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def describe(self) -> str:
        return f"{self.name} is {self.age} years old."
```

Another file can import the class:

```python
from student import Student

student = Student("Aisha", 20)

print(student.describe())
```

This allows classes to be maintained separately from the code that uses them.

---

## Custom Modules with a Main Guard

A custom module may also be directly executable.

Example:

```python
# calculator.py

def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def main() -> None:
    print(add(10, 5))
    print(subtract(10, 5))


if __name__ == "__main__":
    main()
```

The functions can be imported without automatically executing the demonstration code.

When the file is run directly:

```bash
python calculator.py
```

the `main()` function executes.

Not every custom module needs a main guard. It is useful when a module also has a meaningful direct-execution behavior.

---

## A Small Multi-File Application

A simple project can be organized as:

```text
calculator_app/
├── main.py
└── calculator.py
```

`calculator.py`:

```python
def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b
```

`main.py`:

```python
import calculator


def main() -> None:
    print(calculator.add(10, 5))
    print(calculator.subtract(10, 5))
    print(calculator.multiply(10, 5))
    print(calculator.divide(10, 5))


if __name__ == "__main__":
    main()
```

This structure separates calculation logic from application execution.

---

## Module Documentation

A custom module can contain a module-level docstring:

```python
"""Utility functions for working with numbers."""


def square(number: int) -> int:
    return number * number
```

The docstring documents the purpose of the module.

It can be inspected with:

```python
import numbers

print(numbers.__doc__)
```

Clear module documentation becomes increasingly useful as projects grow.

---

## Keeping Modules Focused

A good module should generally have a clear responsibility.

For example:

```text
file_utils.py
```

can contain file-related operations:

```python
from pathlib import Path


def read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text_file(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")
```

It would be less appropriate to place unrelated database operations, network clients, mathematical algorithms, and user-interface code into the same module simply because they are all used by one application.

Focused modules are easier to understand and maintain.

---

## Custom Modules and Reuse

Suppose two programs need the same validation function.

Without a module, the function might be duplicated:

```text
application_a.py
application_b.py
```

With a custom module:

```text
validation.py
application_a.py
application_b.py
```

`validation.py`:

```python
def is_valid_age(age: int) -> bool:
    return 0 <= age <= 120
```

`application_a.py`:

```python
from validation import is_valid_age

print(is_valid_age(25))
```

`application_b.py`:

```python
from validation import is_valid_age

print(is_valid_age(150))
```

Both applications reuse the same implementation.

---

## How Python Finds a Custom Module

For an import such as:

```python
import calculator
```

Python searches locations available through its module search path.

The exact locations depend on how Python was launched and how the environment is configured.

For a simple project:

```text
project/
├── main.py
└── calculator.py
```

running `main.py` from the appropriate project context normally allows `main.py` to import `calculator`.

This is one reason project structure and execution context matter.

---

## Common Mistakes

### 1. Including `.py` in the Import

Incorrect:

```python
import calculator.py
```

Correct:

```python
import calculator
```

---

### 2. Using the Wrong Filename

If the file is:

```text
math_utils.py
```

the import should normally be:

```python
import math_utils
```

not:

```python
import mathutils
```

---

### 3. Creating a Naming Conflict

Avoid naming custom modules after important standard-library modules.

For example, creating:

```text
json.py
```

in a project can interfere with:

```python
import json
```

because Python's import resolution depends on its search path.

Use descriptive names that do not unintentionally shadow standard-library or third-party modules.

---

### 4. Running from the Wrong Context

A custom module may fail to import if the project is executed from an unexpected location or package context.

For example:

```python
import calculator
```

does not guarantee that Python will search every directory on the computer for `calculator.py`.

Python uses its configured module search path.

---

### 5. Putting Too Much into One Module

A file containing hundreds or thousands of unrelated lines can become difficult to maintain.

As responsibilities grow, related functionality can be separated into multiple modules and eventually packages.

---

### 6. Unnecessary Top-Level Side Effects

Avoid modules that perform significant actions merely because they are imported:

```python
delete_database()
send_email()
remove_files()
```

Imports should generally make reusable functionality available without unexpectedly performing application-level operations.

Place direct-execution workflows behind an appropriate main guard.

---

## Best Practices

* Give each module a clear responsibility.
* Use descriptive lowercase module names.
* Keep reusable functions and classes organized by purpose.
* Prefer explicit imports.
* Avoid unnecessary wildcard imports.
* Avoid naming conflicts with standard-library and third-party modules.
* Keep import-time side effects minimal.
* Add a module docstring when it improves documentation.
* Use type hints where they make interfaces clearer.
* Use a main guard when a module is also intended to be directly executable.
* Move related modules into packages as the project grows.

---

## Key Takeaways

* A custom module is a Python file created to organize reusable code.
* Functions, classes, constants, and other definitions can be placed inside custom modules.
* A file such as `calculator.py` can normally be imported with:

  ```python
  import calculator
  ```
* Specific members can be imported with:

  ```python
  from calculator import add
  ```
* Custom modules promote code reuse and separation of responsibilities.
* A module should generally have a focused purpose.
* Python finds modules using its configured module search path.
* Good module organization provides the foundation for larger package-based applications.
