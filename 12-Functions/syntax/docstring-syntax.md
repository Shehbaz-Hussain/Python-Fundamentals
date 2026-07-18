# Docstring Syntax

## Introduction

A docstring is a string placed immediately after a function definition.

It describes what the function does, making the code easier to understand and maintain.

Python stores the docstring as part of the function.

---

## Syntax

```python
def function_name():
    """
    Description of the function.
    """
```

---

## Example

```python
def greet():
    """
    Displays a welcome message.
    """
    print("Welcome!")

greet()
```

---

## Multi-line Docstring

```python
def add(a, b):
    """
    Adds two numbers.

    Parameters:
        a: First number
        b: Second number

    Returns:
        Sum of both numbers
    """
    return a + b
```

---

## Benefits

- Improves code readability.
- Helps other developers understand the function.
- Useful for generating documentation automatically.
- Encourages better code documentation.

---

## Best Practices

- Write clear and concise descriptions.
- Explain parameters and return values when appropriate.
- Keep docstrings updated as the function changes.

---

## Summary

Docstrings are an important documentation feature in Python that makes functions easier to understand, maintain, and reuse.