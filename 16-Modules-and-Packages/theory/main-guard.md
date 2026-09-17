# The Main Guard

## Overview

The **main guard** is a standard Python pattern used to control code that should run only when a module is executed as the program's main entry point.

The pattern is:

```python
if __name__ == "__main__":
    main()
```

It allows the same Python file to serve two purposes:

* Provide reusable functions, classes, or other definitions when imported.
* Run application-specific code when executed as the main program.

---

## The Basic Pattern

A common structure is:

```python
def main() -> None:
    print("Application started")


if __name__ == "__main__":
    main()
```

When the file is executed as the main program, Python sets:

```python
__name__ == "__main__"
```

The condition is therefore true, and `main()` is called.

When the file is imported as a module, the condition is normally false, so `main()` is not called automatically.

---

## Why the Main Guard Is Needed

Consider a file without a main guard:

```python
# calculator.py

def add(a: int, b: int) -> int:
    return a + b


print("Calculator started")
print(add(10, 5))
```

Now another file imports it:

```python
import calculator
```

The import can produce:

```text
Calculator started
15
```

This happens because top-level statements in a module can execute during its initialization.

That behavior may be undesirable when the module is intended primarily for reuse.

A main guard separates reusable definitions from direct-execution behavior.

---

## Using a Main Guard

The previous example can be reorganized:

```python
# calculator.py

def add(a: int, b: int) -> int:
    return a + b


def main() -> None:
    print("Calculator started")
    print(add(10, 5))


if __name__ == "__main__":
    main()
```

Now:

```python
import calculator
```

imports the `add()` function without automatically calling `main()`.

But:

```bash
python calculator.py
```

runs the program and calls `main()`.

---

## How the Main Guard Works

The expression:

```python
__name__ == "__main__"
```

checks the value of the module's `__name__` attribute.

When the module is the main entry point:

```python
__name__ == "__main__"
```

When it is imported normally:

```python
__name__ == "calculator"
```

for a module imported as `calculator`.

Therefore:

```python
if __name__ == "__main__":
    main()
```

means approximately:

> Run `main()` only when this module is being used as the main entry point.

---

## The Main Guard Does Not Prevent All Module Code from Running

The main guard only controls the code placed inside it.

For example:

```python
print("Module initialized")


def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(add(10, 5))
```

When another module imports this file, the first `print()` can still execute:

```text
Module initialized
```

The code inside the main guard does not execute.

This distinction is important.

A main guard is not a mechanism that prevents the entire module from executing during import. It specifically controls the guarded block.

---

## Defining `main()`

A common best practice is to put direct-execution logic inside a `main()` function:

```python
def main() -> None:
    name = input("Enter your name: ")
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
```

This provides a clear application entry point.

It also keeps the top-level module namespace relatively clean and makes the program's execution flow easier to identify.

---

## Main Guard with Reusable Functions

Consider:

```python
def calculate_area(length: float, width: float) -> float:
    return length * width


def main() -> None:
    area = calculate_area(10.0, 5.0)
    print(f"Area: {area}")


if __name__ == "__main__":
    main()
```

The `calculate_area()` function remains reusable.

Another module can import it:

```python
from geometry import calculate_area

area = calculate_area(8.0, 4.0)

print(area)
```

The calculation is available without automatically executing the example in `main()`.

---

## Main Guard and Command-Line Programs

The main guard is commonly used in command-line programs.

For example:

```python
def main() -> None:
    print("Python Utility")
    print("Processing started...")


if __name__ == "__main__":
    main()
```

Running:

```bash
python utility.py
```

starts the application.

Importing:

```python
import utility
```

makes its definitions available without starting the application.

For more advanced command-line interfaces, argument-parsing tools such as Python's `argparse` module can be used inside `main()`.

---

## Main Guard and Input

Interactive code should generally be protected when it is intended only for direct execution.

For example:

```python
def main() -> None:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print(f"{name} is {age} years old.")


if __name__ == "__main__":
    main()
```

If another module imports this file, it does not unexpectedly prompt the user for input.

This is particularly important for reusable libraries and modules.

---

## Main Guard and File Operations

File operations can also be placed inside `main()`:

```python
from pathlib import Path


def main() -> None:
    path = Path("data.txt")
    path.write_text("Python modules", encoding="utf-8")


if __name__ == "__main__":
    main()
```

Importing the module does not automatically create or overwrite `data.txt`.

The file operation occurs only when the module is used as the main entry point.

---

## Main Guard and Tests

A main guard can be useful for simple manual tests:

```python
def multiply(a: int, b: int) -> int:
    return a * b


if __name__ == "__main__":
    print(multiply(6, 7))
```

Executing the module directly runs the test:

```text
42
```

Importing it elsewhere provides the function without running the test.

For professional projects, dedicated test files and testing frameworks should normally be used for comprehensive automated testing.

---

## Main Guard in a Custom Module

Consider this project:

```text
project/
├── main.py
└── calculations.py
```

`calculations.py`:

```python
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

`main.py`:

```python
import calculations


def main() -> None:
    result = calculations.add(20, 10)
    print(result)


if __name__ == "__main__":
    main()
```

When `main.py` is executed, `calculations` is imported, but its own `main()` function is not called.

Only the `main()` function in `main.py` serves as the program entry point.

---

## Main Guard and Import Safety

A reusable module should avoid unexpected actions when imported.

Without a main guard:

```python
start_database()
delete_old_files()
send_report()
```

could potentially execute as a side effect of importing the module.

With appropriate organization:

```python
def start_database() -> None:
    ...


def delete_old_files() -> None:
    ...


def send_report() -> None:
    ...


def main() -> None:
    start_database()
    delete_old_files()
    send_report()


if __name__ == "__main__":
    main()
```

the application workflow is explicitly controlled.

The example above uses `...` only to illustrate structure; actual implementations should provide complete function bodies.

---

## Main Guard and `__name__`

The main guard depends directly on `__name__`.

The relationship can be summarized as:

```text
Direct execution
    ↓
__name__ == "__main__"
    ↓
main guard is True
    ↓
main() runs
```

When imported:

```text
Import
    ↓
__name__ is the module's import name
    ↓
__name__ == "__main__" is normally False
    ↓
main() does not run automatically
```

This is the central purpose of the pattern.

---

## Main Guard and Packages

The main guard also works with modules that are part of packages.

For example:

```text
application/
├── __init__.py
├── main.py
└── utilities/
    └── text.py
```

A package module can contain:

```python
def main() -> None:
    print("Utility application")


if __name__ == "__main__":
    main()
```

However, package modules should be executed in an appropriate package context when they rely on package-relative imports.

Python also supports executing modules using:

```bash
python -m package.module
```

This is often useful for package-based applications because Python establishes the module's package context appropriately.

---

## Common Mistakes

### 1. Writing the Condition Incorrectly

Incorrect:

```python
if __name__ = "__main__":
```

Correct:

```python
if __name__ == "__main__":
```

The comparison operator is `==`.

---

### 2. Forgetting the Quotes

Incorrect:

```python
if __name__ == __main__:
```

Correct:

```python
if __name__ == "__main__":
```

`"__main__"` is a string literal.

---

### 3. Calling `main()` Before the Guard

This defeats the purpose:

```python
def main() -> None:
    print("Started")


main()

if __name__ == "__main__":
    main()
```

The first `main()` call executes regardless of whether the module was imported.

Prefer:

```python
def main() -> None:
    print("Started")


if __name__ == "__main__":
    main()
```

---

### 4. Putting Reusable Definitions Inside the Guard

Avoid:

```python
if __name__ == "__main__":
    def add(a: int, b: int) -> int:
        return a + b
```

When imported, `add()` will not be defined.

Reusable functions and classes should generally be defined outside the main guard.

---

### 5. Assuming the Main Guard Prevents All Import-Time Execution

This is incorrect:

```python
print("This runs during import")


if __name__ == "__main__":
    print("This runs only for the main entry point")
```

The first statement can still execute during import.

Keep reusable modules free from unnecessary top-level side effects.

---

## Best Practices

* Use the standard form:

  ```python
  if __name__ == "__main__":
      main()
  ```
* Put application entry-point logic inside `main()`.
* Keep reusable functions and classes outside the guard.
* Avoid unnecessary side effects at module level.
* Use the main guard for scripts that should also be importable.
* Use `python -m package.module` when appropriate for package-based execution.
* Keep automated tests in dedicated test modules rather than relying only on code inside a main guard.

---

## Key Takeaways

* The main guard controls code intended for direct execution.
* Its standard form is:

  ```python
  if __name__ == "__main__":
      main()
  ```
* The main module receives `__name__ == "__main__"`.
* An imported module normally has its module name as `__name__`.
* Code inside the main guard does not run automatically when the module is imported.
* Reusable definitions should generally remain outside the guard.
* The main guard helps a file function both as a reusable module and as an executable program.
