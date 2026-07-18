# Global Variable Syntax

## Introduction

A global variable is declared outside all functions.

It can be accessed from different parts of the program.

---

## Syntax

```python
variable_name = value

def function_name():
    print(variable_name)
```

---

## Example

```python
language = "Python"

def show_language():
    print(language)

show_language()
```

### Output

```
Python
```

---

## Characteristics

- Declared outside functions.
- Available throughout the program.
- Remains in memory while the program runs.

---

## Best Practices

- Use global variables only when necessary.
- Prefer passing values through function parameters.
- Avoid modifying global variables frequently.

---

## Summary

Global variables provide shared data across different parts of a Python program, but they should be used carefully to maintain clean and predictable code.