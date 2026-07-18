# Variable Scope

## Introduction

Variable scope determines where a variable can be accessed within a Python program.

A variable is only available inside the region where it is created.

Understanding scope helps avoid errors and improves code organization.

---

## Types of Scope

### Local Scope

A variable created inside a function.

```python
def show():
    number = 10
    print(number)
```

---

### Global Scope

A variable created outside every function.

```python
message = "Hello"

def display():
    print(message)
```

---

## Important Points

- Local variables exist only inside their function.
- Global variables are accessible throughout the program.
- Variables with the same name can exist in different scopes.

---

## Best Practices

- Keep variables as local as possible.
- Avoid unnecessary global variables.
- Use meaningful variable names.

---

## Summary

Variable scope defines where a variable is visible and usable within a program.