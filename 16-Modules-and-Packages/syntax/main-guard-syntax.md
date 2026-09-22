# Main Guard Syntax

## Overview

The **main guard** is a Python pattern used to control code that should execute only when a module is run directly.

The standard syntax is:

```python
if __name__ == "__main__":
    ...
```

It is commonly used with a `main()` function:

```python
def main() -> None:
    print("Application started")


if __name__ == "__main__":
    main()
```

This allows the same module to be both:

* Executed directly as a program
* Imported and reused by another module

---

## Basic Main Guard

```python
if __name__ == "__main__":
    print("Program started")
```

When the file is executed directly, the condition is normally true.

When the file is imported, the condition is normally false.

---

## Using a `main()` Function

A common professional structure is:

```python
def main() -> None:
    print("Program started")


if __name__ == "__main__":
    main()
```

The main guard controls when `main()` is called.

This keeps executable behavior separate from reusable definitions.

---

## Direct Execution

Suppose `app.py` contains:

```python
def greet(name: str) -> None:
    print(f"Hello, {name}")


def main() -> None:
    greet("Aisha")


if __name__ == "__main__":
    main()
```

Running:

```bash
python app.py
```

executes:

```python
main()
```

because the file is being run directly.

---

## Importing the Module

Another module can import `app`:

```python
import app

app.greet("Shehbaz")
```

The function definition is available, but:

```python
main()
```

is not automatically called by the main guard.

This prevents importing a reusable module from unexpectedly starting the entire application.

---

## The `__name__` Variable

The main guard depends on the special variable:

```python
__name__
```

When a module is executed directly, Python normally sets:

```python
__name__ == "__main__"
```

Therefore:

```python
if __name__ == "__main__":
```

evaluates to true.

When the module is imported, `__name__` normally contains the module's import name instead.

---

## Standard Pattern

```python
def main() -> None:
    # Program entry point
    ...


if __name__ == "__main__":
    main()
```

This is the recommended basic pattern for modules that provide a direct program entry point.

---

## Main Guard Without `main()`

A main guard can also be used without defining a separate `main()` function:

```python
def calculate_total(values: list[int]) -> int:
    return sum(values)


if __name__ == "__main__":
    numbers = [10, 20, 30]
    print(calculate_total(numbers))
```

This is valid.

For larger programs, however, placing the executable workflow inside `main()` often improves structure and testability.

---

## Main Guard with Command-Line Arguments

A main function can process command-line arguments:

```python
import sys


def main() -> None:
    name = sys.argv[1]
    print(f"Hello, {name}")


if __name__ == "__main__":
    main()
```

Run:

```bash
python app.py Aisha
```

Output:

```text
Hello, Aisha
```

For more sophisticated command-line applications, the `argparse` module is usually preferable.

---

## Main Guard in a Reusable Module

A module can contain reusable functionality:

```python
def add(first: int, second: int) -> int:
    return first + second
```

and an optional demonstration:

```python
if __name__ == "__main__":
    print(add(10, 5))
```

When imported:

```python
from calculator import add

print(add(2, 3))
```

the demonstration code does not run.

---

## Main Guard and Side Effects

Without a main guard:

```python
print("Starting application")
```

runs when the file is imported.

With a main guard:

```python
if __name__ == "__main__":
    print("Starting application")
```

the statement runs only when the module is executed directly.

This helps prevent unwanted import-time side effects.

---

## Main Guard with Functions

A useful structure is:

```python
def load_data() -> list[str]:
    return ["Python", "AI", "ML"]


def display_data(data: list[str]) -> None:
    for item in data:
        print(item)


def main() -> None:
    data = load_data()
    display_data(data)


if __name__ == "__main__":
    main()
```

The reusable functions remain available to other modules.

The application workflow is controlled by the main guard.

---

## Main Guard and Classes

The pattern also works with classes:

```python
class Calculator:
    def add(self, first: int, second: int) -> int:
        return first + second


def main() -> None:
    calculator = Calculator()
    print(calculator.add(10, 5))


if __name__ == "__main__":
    main()
```

The class can be imported without automatically creating an instance or running the application.

---

## Main Guard in Package Modules

When working with packages, direct execution of a module can interact with package context.

For example:

```text
application/
├── __init__.py
├── main.py
└── utilities.py
```

If `main.py` contains package-relative imports, it is often better to execute it through its package:

```bash
python -m application.main
```

rather than:

```bash
python application/main.py
```

The `-m` form gives Python the package context required by relative imports.

---

## Main Guard vs `python -m`

The main guard determines whether direct-entry code runs:

```python
if __name__ == "__main__":
    main()
```

The `-m` option tells Python to execute a module using its importable module name:

```bash
python -m application.main
```

These concepts work together.

A module executed with `python -m application.main` will normally have:

```python
__name__ == "__main__"
```

inside that execution context.

---

## Common Mistakes

### 1. Incorrect Comparison

Use:

```python
if __name__ == "__main__":
```

Do not use:

```python
if __name__ = "__main__":
```

because `=` is assignment, not comparison.

---

### 2. Incorrect String

Use:

```python
"__main__"
```

not:

```python
"main"
```

The standard direct-execution value is `__main__`.

---

### 3. Forgetting the Indentation

Correct:

```python
if __name__ == "__main__":
    main()
```

Incorrect:

```python
if __name__ == "__main__":
main()
```

Python requires the indented block.

---

### 4. Calling `main()` Outside the Guard

This defeats the purpose:

```python
def main() -> None:
    print("Started")


if __name__ == "__main__":
    pass

main()
```

`main()` still runs when the module is imported.

Correct:

```python
if __name__ == "__main__":
    main()
```

---

### 5. Putting All Code at Module Level

Avoid turning a module into a sequence of immediate operations:

```python
data = load_data()
process(data)
save(data)
```

when those operations should occur only during direct execution.

Instead:

```python
def main() -> None:
    data = load_data()
    process(data)
    save(data)


if __name__ == "__main__":
    main()
```

---

## Best Practices

* Use the main guard for modules that have direct executable behavior.
* Prefer a `main()` function for non-trivial application workflows.
* Keep reusable functions and classes outside the main guard.
* Avoid unnecessary import-time side effects.
* Use `python -m package.module` when package context is required.
* Keep the entry-point logic small and easy to understand.
* Do not add a main guard to every module automatically; reusable modules may not need one.

---

## Quick Reference

### Basic

```python
if __name__ == "__main__":
    main()
```

### Recommended Structure

```python
def main() -> None:
    print("Application started")


if __name__ == "__main__":
    main()
```

### With Reusable Functions

```python
def add(first: int, second: int) -> int:
    return first + second


def main() -> None:
    print(add(10, 5))


if __name__ == "__main__":
    main()
```

### Package Execution

```bash
python -m package.module
```

---

## Main Principle

The main guard separates **reusable module functionality** from **direct program execution**.

```python
if __name__ == "__main__":
    main()
```

Use it when a module should behave differently when executed directly versus imported.
