# The `__name__` Variable

## Overview

Every Python module has a special attribute called `__name__`.

Its value identifies how Python is treating the module in the current execution context. This makes `__name__` especially important when a Python file can be used both as:

* A reusable module imported by other code
* A program executed directly

The `__name__` variable is also the foundation of Python's **main guard**:

```python
if __name__ == "__main__":
    ...
```

---

## What Is `__name__`?

`__name__` is a special module-level variable automatically provided by Python.

For a module imported normally, its value generally corresponds to the module's import name.

For example, consider:

```text
project/
├── main.py
└── calculator.py
```

`calculator.py`:

```python
print(__name__)
```

If `main.py` contains:

```python
import calculator
```

the output is normally:

```text
calculator
```

Python therefore knows the imported module by its module name.

---

## `__name__` When a File Is Executed Directly

When a Python file is executed as the main program, Python assigns:

```python
__name__ = "__main__"
```

For example:

```python
# app.py

print(__name__)
```

Running:

```bash
python app.py
```

produces:

```text
__main__
```

This is different from importing the same file as a module.

---

## Direct Execution vs Importing

Consider:

```python
# calculator.py

print(__name__)
```

If the file is executed directly:

```bash
python calculator.py
```

the output is:

```text
__main__
```

If another file imports it:

```python
import calculator
```

the value is normally:

```text
calculator
```

The same source file therefore receives different `__name__` values depending on how it is being used.

---

## Why Python Uses `__name__`

The distinction allows a module to determine whether it is being executed directly or imported.

For example:

```python
def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(add(10, 5))
```

When the file is executed directly, the condition is true and the test code runs.

When the file is imported, the condition is false and the test code does not run.

This allows the same file to provide reusable functionality without automatically executing its program-specific entry-point code during import.

---

## The Main Guard

The following pattern is called the **main guard**:

```python
if __name__ == "__main__":
    main()
```

A common complete structure is:

```python
def main() -> None:
    print("Application started")


if __name__ == "__main__":
    main()
```

When the file is executed directly:

```text
__name__ == "__main__"
```

is true, so `main()` runs.

When the file is imported, the condition is false, so `main()` is not called automatically.

---

## A Reusable Module with a Main Guard

Consider:

```python
# calculator.py

def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def main() -> None:
    print(add(10, 5))
    print(multiply(4, 3))


if __name__ == "__main__":
    main()
```

The file has two roles:

1. It provides reusable functions.
2. It can be executed directly as a small program.

Another module can import it:

```python
import calculator

result = calculator.add(20, 10)

print(result)
```

Importing `calculator` does not execute the `main()` call because the main guard condition is false in the imported module.

---

## Inspecting `__name__`

You can inspect the value directly:

```python
print(__name__)
```

When the file is executed directly:

```text
__main__
```

When the file is imported as a normal module:

```text
module_name
```

This makes `__name__` useful for understanding Python's execution context.

---

## `__name__` Is a Module Attribute

It is useful to understand that `__name__` is not a special global variable unrelated to modules.

It is a module attribute.

For example:

```python
import math

print(math.__name__)
```

produces:

```text
math
```

The current module also has its own `__name__`:

```python
print(__name__)
```

Both are attributes associated with module objects.

---

## `__name__` and Imported Custom Modules

Consider:

```text
project/
├── main.py
└── utilities.py
```

`utilities.py`:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"


print(f"utilities.__name__ = {__name__}")
```

`main.py`:

```python
import utilities

print(utilities.greet("Shehbaz"))
```

When `main.py` is executed, the imported module normally reports:

```text
utilities.__name__ = utilities
```

The main module reports:

```python
print(__name__)
```

as:

```text
__main__
```

Thus, different modules in the same process can have different `__name__` values.

---

## Why the Main Guard Matters

Without a main guard, code intended only for direct execution can run unexpectedly during import.

For example:

```python
# calculator.py

def add(a: int, b: int) -> int:
    return a + b


print("Running calculator")
print(add(10, 5))
```

If another file executes:

```python
import calculator
```

the top-level `print()` statements execute as part of importing the module.

If the intended behavior is to run those statements only when the file is used as a program, use:

```python
def add(a: int, b: int) -> int:
    return a + b


def main() -> None:
    print("Running calculator")
    print(add(10, 5))


if __name__ == "__main__":
    main()
```

Now importing the module provides the reusable function without starting the direct-execution behavior.

---

## `__name__` and Testing

The main guard can also be useful for lightweight manual testing.

For example:

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


if __name__ == "__main__":
    print(calculate_total(19.99, 3))
```

The test code runs when the file is executed directly.

When the module is imported by a test suite or another application, the guarded code does not execute automatically.

For larger projects, dedicated test modules and testing frameworks are preferable to relying entirely on manual tests inside the implementation module.

---

## `__name__` in Packages

When modules are organized into packages, their names can contain package components.

For example:

```text
application/
├── __init__.py
├── main.py
└── utilities/
    ├── __init__.py
    └── text.py
```

When `text.py` is imported as part of the package, its `__name__` can be:

```text
application.utilities.text
```

The exact execution context matters, particularly when modules are run using Python's module execution mechanisms.

This is one reason package modules should generally be designed to work within their intended package structure rather than assuming they will always be executed as standalone files.

---

## Important Limitation

It is tempting to think that:

```python
__name__ == "__main__"
```

always means "this file was launched directly from a terminal."

That is a useful basic model, but Python supports several execution mechanisms, and the exact value and package context can depend on how code is launched.

For introductory development, the important rule is:

> The module used as the program's main entry point receives the special `__name__` value `"__main__"`.

---

## Common Mistakes

### 1. Comparing Without Quotes

Incorrect:

```python
if __name__ == __main__:
    main()
```

Correct:

```python
if __name__ == "__main__":
    main()
```

`"__main__"` is a string.

### 2. Calling `main()` Outside the Guard

This:

```python
def main() -> None:
    print("Application started")


main()
```

runs whenever the module executes, including when it is imported.

If the behavior should happen only during direct execution, use:

```python
if __name__ == "__main__":
    main()
```

### 3. Putting Everything Inside `main()`

Reusable functions should normally remain independently accessible.

Prefer:

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


def main() -> None:
    print(calculate_total(10.0, 3))


if __name__ == "__main__":
    main()
```

rather than placing all functionality inside `main()`.

### 4. Assuming `__name__` Is Always the Filename

The value is based on the module's execution/import context, not simply the filename string in every situation.

---

## Best Practices

* Use `__name__` to distinguish module execution contexts.
* Use the main guard for direct-execution behavior.
* Keep reusable functions and classes outside the main guard.
* Put application entry-point logic in a `main()` function when appropriate.
* Avoid unnecessary side effects at module level.
* Remember that package execution can affect module names and import context.

---

## Key Takeaways

* `__name__` is a special module attribute.
* A normally imported module has a name corresponding to its import name.
* The main entry-point module receives:

  ```python
  __name__ == "__main__"
  ```
* The main guard is:

  ```python
  if __name__ == "__main__":
      main()
  ```
* The main guard prevents direct-execution code from running automatically when the module is imported.
* `__name__` allows a Python file to support both reusable-module and direct-program use.
