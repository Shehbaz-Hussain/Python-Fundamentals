# Package Syntax

## Overview

A **package** organizes related Python modules into a hierarchical structure.

A basic package can be represented as:

```text
project/
├── main.py
└── utilities/
    ├── __init__.py
    └── numbers.py
```

Here:

* `utilities` is the package.
* `numbers.py` is a module inside the package.
* `__init__.py` defines the package initializer for a regular package.

Modern Python also supports **namespace packages**, which can exist without an `__init__.py` file.

---

## Basic Package Structure

```text
myproject/
├── main.py
└── tools/
    ├── __init__.py
    └── calculator.py
```

`calculator.py`:

```python
def add(first: int, second: int) -> int:
    return first + second
```

---

## Import a Module from a Package

Use:

```python
import tools.calculator
```

Then access the function through the package and module namespace:

```python
result = tools.calculator.add(10, 5)
print(result)
```

---

## Import with `from`

A module inside a package can be imported with:

```python
from tools import calculator

print(calculator.add(10, 5))
```

A specific member can also be imported:

```python
from tools.calculator import add

print(add(10, 5))
```

---

## Package Initializer

A regular package can contain:

```text
tools/
├── __init__.py
└── calculator.py
```

The initializer may be empty:

```python
# tools/__init__.py
```

Or it can expose selected package-level names:

```python
from .calculator import add
```

Then:

```python
from tools import add

print(add(10, 5))
```

Keep package initialization lightweight.

---

## Package with Multiple Modules

```text
project/
├── main.py
└── utilities/
    ├── __init__.py
    ├── numbers.py
    └── strings.py
```

`numbers.py`:

```python
def add(first: int, second: int) -> int:
    return first + second
```

`strings.py`:

```python
def capitalize_text(text: str) -> str:
    return text.capitalize()
```

Import them:

```python
from utilities.numbers import add
from utilities.strings import capitalize_text

print(add(10, 5))
print(capitalize_text("python"))
```

---

## Nested Packages

Packages can contain subpackages:

```text
project/
└── application/
    ├── __init__.py
    ├── core/
    │   ├── __init__.py
    │   └── processing.py
    └── utils/
        ├── __init__.py
        └── formatting.py
```

Import a module using its full package path:

```python
from application.core import processing
```

Or:

```python
from application.utils.formatting import format_name
```

---

## Absolute Package Import

An absolute import specifies the package path from the top-level package:

```python
from application.utils.formatting import format_name
```

This is useful when the package structure is clear and stable.

---

## Relative Package Import

Inside a package module, relative imports can reference nearby modules:

```python
from .formatting import format_name
```

The single dot represents the current package.

For a parent package:

```python
from ..utils import formatting
```

Relative imports require the module to be executed within an appropriate package context.

---

## Executing a Package Module

Suppose the structure is:

```text
project/
└── application/
    ├── __init__.py
    └── main.py
```

Run the module using:

```bash
python -m application.main
```

This allows Python to execute the module while maintaining its package context.

---

## Package-Level API

A package can expose selected functionality through `__init__.py`.

Example:

```text
tools/
├── __init__.py
└── calculator.py
```

`calculator.py`:

```python
def add(first: int, second: int) -> int:
    return first + second
```

`__init__.py`:

```python
from .calculator import add
```

Users can then write:

```python
from tools import add

print(add(2, 3))
```

Instead of:

```python
from tools.calculator import add
```

Only expose names at package level when doing so creates a useful and stable interface.

---

## Package Namespace

A package provides a namespace for its modules.

For example:

```python
import tools.calculator
```

The module is accessed through:

```python
tools.calculator
```

This helps organize related functionality and reduce naming conflicts.

---

## Package with a Main Entry Point

A package may provide an executable module:

```text
application/
├── __init__.py
├── __main__.py
└── utilities.py
```

The `__main__.py` file can contain:

```python
def main() -> None:
    print("Application started")


if __name__ == "__main__":
    main()
```

The package can then be executed with:

```bash
python -m application
```

---

## Common Mistakes

### 1. Incorrect Package Path

If the structure is:

```text
application/
└── utils/
    └── formatting.py
```

the import should reflect the actual hierarchy:

```python
from application.utils.formatting import format_name
```

### 2. Confusing Modules and Packages

A module is normally a Python file:

```text
calculator.py
```

A package is a directory that organizes modules and possibly subpackages:

```text
utilities/
├── __init__.py
└── calculator.py
```

### 3. Assuming `__init__.py` Is Always Required

Modern Python supports namespace packages without `__init__.py`.

Do not state that every package must contain an `__init__.py` file.

### 4. Running a Package Module Incorrectly

Relative imports may fail when a package module is executed directly:

```bash
python application/main.py
```

When package context is required, prefer:

```bash
python -m application.main
```

### 5. Heavy Package Initialization

Avoid expensive or unnecessary work inside:

```text
__init__.py
```

Package initialization should generally remain lightweight.

---

## Quick Reference

### Package structure

```text
package/
├── __init__.py
└── module.py
```

### Import a module

```python
import package.module
```

### Import a module with `from`

```python
from package import module
```

### Import a specific member

```python
from package.module import function
```

### Absolute import

```python
from package.utils import helper
```

### Relative import

```python
from .utils import helper
```

### Parent-package relative import

```python
from ..utils import helper
```

### Execute a package module

```bash
python -m package.module
```

### Execute a package

```bash
python -m package
```

The last form requires an appropriate package entry point, commonly `__main__.py`.

## Core Principle

Use packages to organize related modules into clear, maintainable namespaces and use explicit imports to make dependencies understandable.
