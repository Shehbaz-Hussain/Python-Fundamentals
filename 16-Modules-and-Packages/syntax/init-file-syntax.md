# `__init__.py` Syntax

## Overview

`__init__.py` is the conventional initializer file for a **regular Python package**.

A basic package structure is:

```text
utilities/
├── __init__.py
└── calculator.py
```

The file may be empty or may contain package-level code, metadata, or selected exports.

Modern Python also supports **namespace packages**, so `__init__.py` is not required for every package.

---

## Empty `__init__.py`

The simplest form is an empty file:

```python
# utilities/__init__.py
```

This can be useful when creating a regular package with an explicit package initializer.

---

## Package Metadata

Package-level metadata can be defined in `__init__.py`:

```python
__version__ = "1.0.0"
```

Access it with:

```python
import utilities

print(utilities.__version__)
```

Keep package metadata simple and lightweight.

---

## Re-Exporting a Function

Suppose:

```text
utilities/
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

The function can then be imported directly from the package:

```python
from utilities import add

print(add(10, 5))
```

---

## Re-Exporting Multiple Names

```python
from .calculator import add, subtract
```

Then:

```python
from utilities import add, subtract

print(add(10, 5))
print(subtract(10, 5))
```

Only expose names at package level when this improves the package interface.

---

## Relative Import in `__init__.py`

Package-internal imports commonly use relative syntax:

```python
from .calculator import add
```

The `.` refers to the current package.

For a subpackage:

```python
from .core import Processor
```

The exact import path must match the package structure.

---

## Package-Level API

A package can use `__init__.py` to provide a simpler public interface.

Structure:

```text
tools/
├── __init__.py
├── calculator.py
└── formatting.py
```

`__init__.py`:

```python
from .calculator import add
from .formatting import format_name
```

Users can write:

```python
from tools import add, format_name
```

instead of importing from individual implementation modules.

---

## Using `__all__`

A package can define `__all__`:

```python
from .calculator import add, subtract

__all__ = ["add", "subtract"]
```

`__all__` can document names intended for wildcard-import semantics and can communicate part of the public interface.

Explicit imports are generally preferred over:

```python
from tools import *
```

---

## Package Initialization

Code in `__init__.py` can run when the regular package is imported.

For example:

```python
print("Utilities package initialized")
```

Then:

```python
import utilities
```

may produce:

```text
Utilities package initialized
```

Avoid unnecessary output or expensive operations during package import.

---

## `__init__.py` with a Subpackage

Example:

```text
application/
├── __init__.py
└── core/
    ├── __init__.py
    └── processor.py
```

`core/__init__.py` can expose selected functionality:

```python
from .processor import Processor
```

Then:

```python
from application.core import Processor
```

---

## Empty vs Configured `__init__.py`

### Empty

```python
# application/__init__.py
```

Useful when no package-level interface or initialization is required.

### Configured

```python
from .calculator import add

__version__ = "1.0.0"
```

Useful when the package needs selected exports or lightweight metadata.

---

## Common Mistakes

### 1. Heavy Initialization

Avoid:

```python
# __init__.py
load_large_dataset()
connect_to_database()
start_application()
```

Importing the package would trigger these operations.

Prefer explicit functions for operations that should happen on demand.

---

### 2. Circular Imports

Be careful when package-level re-exports create circular dependencies.

For example:

```text
package/
├── __init__.py
├── module_a.py
└── module_b.py
```

If `module_a` imports `module_b` while `module_b` imports `module_a`, the package can develop an import cycle.

Keep dependencies clear and minimize unnecessary package-level imports.

---

### 3. Exposing Everything

Do not automatically re-export every internal function:

```python
from .module_a import *
from .module_b import *
```

Prefer a small, intentional public interface.

---

### 4. Assuming `__init__.py` Is Mandatory

Modern Python supports namespace packages without this file.

Therefore, avoid the rule:

```text
Every Python package must contain __init__.py
```

A more accurate statement is:

```text
__init__.py is used to define a regular package and can provide package initialization and package-level exports.
```

---

## Quick Reference

### Empty initializer

```python
# package/__init__.py
```

### Package metadata

```python
__version__ = "1.0.0"
```

### Re-export a function

```python
from .module import function
```

### Re-export multiple names

```python
from .module import function_a, function_b
```

### Define public names

```python
__all__ = ["function_a", "function_b"]
```

### Import from package

```python
from package import function
```

### Basic structure

```text
package/
├── __init__.py
└── module.py
```

## Core Principle

Use `__init__.py` intentionally: keep package initialization lightweight and expose only the package-level functionality that forms a useful, stable interface.
