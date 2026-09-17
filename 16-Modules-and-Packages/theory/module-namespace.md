# Module Namespace

## Overview

Every Python module has its own **namespace**.

A namespace is a mapping between names and the objects to which those names refer. A module namespace provides a separate scope for the functions, classes, varineables, constants, and other objects defined by that module.

Understanding module namespaces is important because imports do not simply copy source code from one file into another. Instead, Python creates bindings that allow code to access objects through their appropriate namespaces.

---

## What Is a Namespace?

A namespace is a collection of names associated with objects.

For example:

```python
name = "Shehbaz"
age = 21
```

creates names such as:

```text
name → "Shehbaz"
age  → 21
```

A Python module has its own namespace containing the names defined within that module.

---

## A Simple Module Namespace

Consider this module:

```python
# calculator.py

PI = 3.14159


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b
```

The module namespace contains names such as:

```text
PI
add
multiply
```

When another file imports the module:

```python
import calculator
```

the importing code can access those names through the module object:

```python
print(calculator.PI)
print(calculator.add(10, 5))
print(calculator.multiply(4, 3))
```

The `calculator` name in the importing module refers to the imported module object.

---

## Module Namespace and the Importing Namespace

Suppose `calculator.py` contains:

```python
PI = 3.14159


def add(a: int, b: int) -> int:
    return a + b
```

and `main.py` contains:

```python
import calculator

result = calculator.add(10, 5)
```

There are two relevant namespaces:

```text
calculator module namespace
    PI
    add

main module namespace
    calculator
    result
```

The `add` name remains associated with the `calculator` module namespace.

The `main` module does not automatically receive a direct `add` name from:

```python
import calculator
```

Instead, it accesses the function through:

```python
calculator.add
```

---

## Attribute Access

The dot operator is used to access names stored in a module's namespace.

For example:

```python
import math

print(math.pi)
print(math.sqrt(25))
```

Here:

```text
math
```

refers to the module object, while:

```text
math.pi
math.sqrt
```

access names associated with that module.

This is called **attribute access**.

The same concept applies to custom modules:

```python
import calculator

calculator.add(10, 20)
```

---

## `import module` and Namespace Bindings

Consider:

```python
import math
```

This creates a local binding named:

```text
math
```

The imported module can then be accessed through that name:

```python
math.sqrt(16)
```

The names inside `math` remain part of the module's namespace.

This design keeps the module's names grouped together.

---

## `from module import name`

Now consider:

```python
from math import sqrt
```

This creates a direct binding named:

```text
sqrt
```

in the current namespace.

The function can therefore be called as:

```python
sqrt(16)
```

The important difference is:

```text
import math
    current namespace → math

from math import sqrt
    current namespace → sqrt
```

The two statements therefore affect the importing namespace differently.

---

## Example with a Custom Module

Consider:

```python
# greetings.py

message = "Welcome to Python"


def greet(name: str) -> str:
    return f"{message}, {name}!"
```

Another file can import it:

```python
import greetings

print(greetings.message)
print(greetings.greet("Shehbaz"))
```

The names `message` and `greet` belong to the `greetings` module namespace.

The importing module accesses them using:

```python
greetings.message
greetings.greet
```

---

## Directly Importing a Name

The same module can be used with a direct import:

```python
from greetings import greet

print(greet("Shehbaz"))
```

Now the current namespace contains a direct binding for:

```text
greet
```

The `greetings` name itself is not introduced by this statement.

This distinction becomes important when several modules contain names with the same identifier.

---

## Namespace Collisions

A namespace collision occurs when different objects are associated with the same local name.

For example:

```python
from module_a import process
from module_b import process
```

The second import binds `process` to the object imported from `module_b`, replacing the previous local binding.

This can make code difficult to understand.

A module-qualified approach avoids this problem:

```python
import module_a
import module_b

module_a.process()
module_b.process()
```

Now the two names are clearly separated by their module namespaces.

---

## Inspecting a Module Namespace with `dir()`

Python provides the built-in `dir()` function for inspecting names associated with an object.

For example:

```python
import math

print(dir(math))
```

This displays a list of names available through the `math` module.

A custom module can also be inspected:

```python
import calculator

print(dir(calculator))
```

The exact output can include names created by the module and attributes supplied by Python's module machinery.

`dir()` is useful for exploration and debugging, but it should not be treated as a complete description of every implementation detail of a module.

---

## Inspecting a Namespace with `__dict__`

Module objects expose their namespace through the `__dict__` attribute.

For example:

```python
import calculator

print(calculator.__dict__)
```

This provides the module's namespace mapping.

A more readable approach for inspecting specific names is often preferable:

```python
print(calculator.add)
print(calculator.PI)
```

The `__dict__` attribute is mainly useful when learning about namespaces, introspection, and debugging.

---

## Namespaces Are Mappings

A module namespace behaves like a mapping from names to objects.

For example:

```python
# calculator.py

PI = 3.14159
```

conceptually creates a relationship similar to:

```text
"PI" → 3.14159
```

The actual module namespace is represented internally through a dictionary-like mapping and can be observed through:

```python
calculator.__dict__
```

This is one reason Python documentation often describes namespaces in terms of mappings.

---

## Changing Module Attributes

Module attributes can be reassigned through the module object.

For example:

```python
# settings.py

MAX_RETRIES = 3
```

Another module could write:

```python
import settings

settings.MAX_RETRIES = 5

print(settings.MAX_RETRIES)
```

The module object's attribute is now associated with the new value.

However, modifying imported module state from unrelated parts of an application can make software harder to reason about. Shared mutable module-level state should therefore be used carefully.

---

## Module-Level Scope

Names defined directly in a module belong to the module's global scope.

For example:

```python
DEFAULT_PORT = 8000


def show_port() -> None:
    print(DEFAULT_PORT)
```

The function can access `DEFAULT_PORT` because the name exists in the module's global namespace.

The function's local variables, however, belong to the function's own local namespace.

For example:

```python
DEFAULT_PORT = 8000


def show_port() -> None:
    message = f"Port: {DEFAULT_PORT}"
    print(message)
```

Here:

```text
Module namespace:
    DEFAULT_PORT
    show_port

Function local namespace:
    message
```

Different namespaces allow Python to keep names organized according to their scope.

---

## Module Namespace and `__name__`

A module also contains special attributes.

One important attribute is:

```python
__name__
```

For example:

```python
import math

print(math.__name__)
```

This produces:

```text
math
```

A custom module also has a `__name__` attribute corresponding to its module name in the import context.

The special behavior of `__name__` during direct execution and its relationship with the main guard are covered in later sections.

---

## Module Namespace and `__file__`

When available, a module may also expose the `__file__` attribute.

For example:

```python
import json

print(json.__file__)
```

This can show the location of the module's source or compiled implementation, depending on how the module is provided.

Not every module has a `__file__` attribute. For example, some built-in or specially implemented modules may not correspond to a normal source file.

---

## Module Objects

When Python imports a module, the result is a **module object**.

For example:

```python
import calculator
```

binds the name `calculator` to a module object.

That object provides access to the module's namespace:

```python
calculator.add
calculator.PI
```

It also contains module metadata such as:

```python
calculator.__name__
calculator.__dict__
```

This object-based view helps explain why imports behave differently from textual code inclusion.

---

## Module Caching and Namespace Identity

Python maintains imported modules in `sys.modules`.

For example:

```python
import sys
import math

print(sys.modules["math"] is math)
```

This normally produces:

```text
True
```

The module object stored in the import cache is the same object referenced by the local `math` binding.

This caching mechanism is one reason repeated imports within the same Python process generally reuse an existing module object.

---

## Common Mistakes

### Assuming `import` Copies Code

This is incorrect:

```text
import = copy the source code into the current file
```

A better mental model is:

```text
import → locate/load module → create or reuse module object → bind a name
```

### Confusing Module and Local Names

With:

```python
import math
```

the local name is `math`.

With:

```python
from math import sqrt
```

the local name is `sqrt`.

### Ignoring Name Collisions

Direct imports with common names can overwrite existing local bindings.

Use module-qualified access or aliases when necessary.

### Modifying Shared Module State Carelessly

Changing module-level mutable state from many locations can create hidden dependencies and make debugging difficult.

---

## Best Practices

* Understand imports as namespace bindings rather than source-code copying.
* Use module-qualified names when they make object origins clearer.
* Use direct imports when the imported names are clear and unambiguous.
* Avoid unnecessary namespace collisions.
* Keep module-level state limited and purposeful.
* Use `dir()` and `__dict__` for exploration and debugging when appropriate.
* Organize modules around clear responsibilities.

---

## Key Takeaways

* Every Python module has its own namespace.
* A module namespace maps names to objects.
* `import module` binds the module name in the importing namespace.
* `from module import name` binds the selected name directly in the importing namespace.
* The dot operator provides access to names through a module object.
* Module namespaces help prevent unrelated names from being mixed together.
* `dir()` can be used to inspect available names.
* `__dict__` exposes a module's namespace mapping.
* Modules have special attributes such as `__name__`.
* Imported modules are normally cached in `sys.modules`.
* Understanding namespaces makes Python's import system easier to reason about.
