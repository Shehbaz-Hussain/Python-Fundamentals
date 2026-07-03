# notes.md

# Python Variables - Quick Revision Notes

This document provides a concise review of the most important ideas about Python variables.

---

## 1. Definition
A variable is a named container that stores a value.

```python
name = "Alice"
```

---

## 2. Assignment Syntax
Use the assignment operator `=` to store a value.

```python
age = 25
```

---

## 3. Reassignment
You can change the value of a variable later.

```python
score = 10
score = 15
```

---

## 4. Dynamic Typing
Python allows a variable to hold different types at different times.

```python
x = 10
x = "ten"
```

---

## 5. Naming Rules
A variable name must:

- start with a letter or underscore
- contain letters, digits, or underscores
- not use spaces
- not start with a digit

### Valid
```python
name = "Sam"
user_name = "Sam"
age2 = 20
```

### Invalid
```python
2name = "Sam"
user-name = "Sam"
```

---

## 6. PEP 8 Naming Convention
Use `snake_case` for variable names.

```python
student_name = "Liam"
account_balance = 100.50
```

---

## 7. Keywords to Avoid
Do not use Python reserved keywords as variable names.

Examples:
```python
class = 5
if = 10
```

---

## 8. Case Sensitivity
Python treats uppercase and lowercase as different.

```python
name = "Ava"
Name = "Ben"
```

---

## 9. Multiple Assignment
Assign several values in one line.

```python
x, y, z = 10, 20, 30
```

---

## 10. Swapping Variables
```python
a = 5
b = 8
a, b = b, a
```

---

## 11. Deleting Variables
```python
del name
```

---

## 12. Type Checking
Use `type()` to check the data type.

```python
age = 21
print(type(age))
```

---

## 13. Memory Address
Use `id()` to view the object identity.

```python
x = 10
print(id(x))
```

---

## 14. Basic Scope
Variables have a scope, or region of use.

```python
x = 10

def show():
    print(x)
```

---

## 15. Constants by Convention
Use uppercase names for values that should not change.

```python
PI = 3.14
MAX_SCORE = 100
```

---

## 16. Mutable vs Immutable
- Mutable: `list`, `dict`, `set`
- Immutable: `int`, `float`, `str`, `tuple`

---

## 17. Common Mistakes
- Using invalid names
- Using keywords as names
- Confusing `=` with `==`
- Forgetting to initialize variables

---

## 18. Interview Facts
- Variables store values.
- Python uses dynamic typing.
- Variable names are case-sensitive.
- `type()` checks the data type.
- `id()` checks memory identity.

---

## 19. Quick Revision Table

| Topic | Rule / Idea |
|---|---|
| Assignment | `name = value` |
| Reassignment | Change a variable later |
| Naming | Use descriptive names |
| Case sensitivity | `name` and `Name` are different |
| Keywords | Avoid reserved words |
| PEP 8 | Prefer `snake_case` |
| Type check | Use `type()` |
| Memory identity | Use `id()` |

---

## 20. Memory Tricks
- Think of a variable as a labeled box.
- Think of the value as the item inside the box.
- Think of `=` as placing an item into the box.

---

## 21. Key Takeaways
- Variables store data.
- Good names improve readability.
- Python variables can be reassigned.
- Follow Python naming rules carefully.
