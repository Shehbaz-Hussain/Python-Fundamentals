# Module Syntax

## Overview

A **module** is a Python file containing reusable code such as functions, classes, constants, and executable statements.

A Python module normally uses the `.py` extension.

Example:

```text
calculator.py
```

The module can then be imported into another Python file.

---

## Basic Module

```python
# calculator.py

def add(first: int, second: int) -> int:
    return first + second
```

Import it:

```python
import calculator

result = calculator.add(10, 5)
print(result)
```

Output:

```text
15
```

---

## Module Constants

Constants can be defined at module level:

```python
# settings.py

APP_NAME = "Python Application"
MAX_USERS = 100
```

Import them:

```python
import settings

print(settings.APP_NAME)
print(settings.MAX_USERS)
```

---

## Module Functions

A module can contain multiple related functions:

```python
# math_utils.py

def add(first: int, second: int) -> int:
    return first + second


def subtract(first: int, second: int) -> int:
    return first - second


def multiply(first: int, second: int) -> int:
    return first * second
```

Use:

```python
import math_utils

print(math_utils.add(10, 5))
print(math_utils.multiply(4, 3))
```

---

## Module Classes

Modules can also contain classes:

```python
# student.py

class Student:
    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> None:
        print(f"My name is {self.name}.")
```

Import and use:

```python
from student import Student

student = Student("Aisha")
student.introduce()
```

---

## Importing a Module

Use:

```python
import module_name
```

Example:

```python
import math

print(math.sqrt(25))
```

The module name is used as a namespace:

```python
math.sqrt(25)
```

---

## Importing Specific Names

Use:

```python
from module_name import name
```

Example:

```python
from math import sqrt

print(sqrt(25))
```

Multiple names can be imported:

```python
from math import sqrt, pi

print(sqrt(25))
print(pi)
```

---

## Module Alias

Use `as` to create an alias:

```python
import statistics as stats

print(stats.mean([10, 20, 30]))
```

A specific imported name can also have an alias:

```python
from math import sqrt as square_root

print(square_root(49))
```

---

## Module Documentation

A module can begin with a module-level docstring:

```python
"""Utilities for basic numerical calculations."""


def add(first: int, second: int) -> int:
    return first + second
```

The docstring documents the purpose of the module.

---

## Main Guard

A module that can also be executed directly may use:

```python
def main() -> None:
    print("Application started")


if __name__ == "__main__":
    main()
```

This prevents the application entry point from running automatically when the module is imported.

---

## Complete Module Example

```python
"""Basic temperature conversion utilities."""

FREEZING_CELSIUS = 0.0


def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def main() -> None:
    temperature = 25.0
    result = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C = {result}°F")


if __name__ == "__main__":
    main()
```

Another file can reuse the functions:

```python
from temperature import celsius_to_fahrenheit

print(celsius_to_fahrenheit(30))
```

---

## Module Namespace

When using:

```python
import temperature
```

access module members through the module namespace:

```python
temperature.celsius_to_fahrenheit(30)
```

This makes the source of the imported name explicit.

---

## Module File Structure

A simple module can follow this structure:

```text
project/
├── main.py
└── utilities.py
```

`utilities.py`:

```python
def greet(name: str) -> str:
    return f"Hello, {name}."
```

`main.py`:

```python
import utilities


def main() -> None:
    print(utilities.greet("Aisha"))


if __name__ == "__main__":
    main()
```

---

## Importing Custom Modules

If a custom module is available on Python's import search path:

```python
import utilities
```

Python can locate and load it.

The module should have an importable filename:

```text
utilities.py
```

Avoid names that conflict with important standard-library modules or commonly installed packages.

---

## Module Execution

A module can be executed directly:

```bash
python utilities.py
```

Or, when it belongs to a package, it can often be executed using:

```bash
python -m package.utilities
```

The `-m` form is especially useful when package context is required.

---

## Import Execution

Importing a module may execute its top-level statements during the first import.

For example:

```python
# example.py

print("Module loaded")
```

Then:

```python
import example
```

prints:

```text
Module loaded
```

For this reason, modules should avoid unnecessary top-level side effects.

---

## Recommended Module Pattern

```python
"""Short description of the module."""

CONSTANT = "value"


def reusable_function() -> None:
    print("Reusable functionality")


def main() -> None:
    reusable_function()


if __name__ == "__main__":
    main()
```

This pattern separates:

1. Module documentation
2. Constants
3. Reusable functionality
4. Program entry point

---

## Common Mistakes

### Incorrect Module Name

Avoid filenames such as:

```text
math.py
random.py
json.py
```

when creating unrelated custom modules, because they can conflict with standard-library modules.

### Wildcard Imports

Avoid:

```python
from module import *
```

Prefer explicit imports:

```python
from module import function_a, function_b
```

### Unnecessary Global State

Avoid using module-level mutable state unless there is a clear reason.

### Heavy Import-Time Work

Avoid expensive operations that execute automatically whenever the module is imported.

---

## Quick Reference

### Create a module

```text
utilities.py
```

### Import the module

```python
import utilities
```

### Use a module member

```python
utilities.function()
```

### Import a specific member

```python
from utilities import function
```

### Import with an alias

```python
import utilities as utils
```

### Main guard

```python
if __name__ == "__main__":
    main()
```

### Execute a package module

```bash
python -m package.module
```

## Core Principle

Keep a module focused on a clear responsibility and expose reusable functions, classes, constants, or other well-defined interfaces through explicit imports.
