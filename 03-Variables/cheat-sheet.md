# cheat-sheet.md

# Python Variables Cheat Sheet

A quick reference guide for variables in Python.

---

## 1. Basic Assignment

```python
name = "Alice"
age = 25
```

- `=` assigns a value to a variable.
- The variable name is on the left.
- The value is on the right.

---

## 2. Reassignment

```python
score = 10
score = 15
```

A variable can be assigned a new value later.

---

## 3. Naming Rules

### Valid names
```python
name = "Sam"
user_name = "Sam"
age2 = 20
```

### Invalid names
```python
2name = "Sam"
user-name = "Sam"
```

### Rules
- Start with a letter or underscore.
- Use letters, digits, and underscores.
- Do not use spaces.
- Do not start with a digit.

---

## 4. PEP 8 Style

Use `snake_case`.

```python
student_name = "Liam"
account_balance = 100.50
```

### Good practice
- Use descriptive names.
- Keep names lowercase.
- Avoid overly short names.

---

## 5. Reserved Keywords

Do not use Python keywords as variable names.

Examples:
```python
class = 5
if = 10
```

---

## 6. Data Types

```python
age = 20          # int
price = 19.99     # float
name = "Ava"     # str
is_student = True # bool
```

---

## 7. Multiple Assignment

```python
x, y, z = 10, 20, 30
```

---

## 8. One Value to Many Variables

```python
a = b = c = 5
```

---

## 9. Swapping Variables

```python
a = 5
b = 8
a, b = b, a
```

---

## 10. Type Checking

```python
age = 21
print(type(age))
```

Output:
```python
<class 'int'>
```

---

## 11. Memory Address

```python
x = 10
print(id(x))
```

---

## 12. Delete a Variable

```python
del name
```

---

## 13. Variables in Expressions

```python
base = 10
height = 5
area = base * height
print(area)
```

Output:
```python
50
```

---

## 14. Constants by Convention

```python
PI = 3.14
MAX_SCORE = 100
```

Use uppercase names for values that should remain constant.

---

## 15. Best Practices

- Use meaningful names.
- Follow PEP 8.
- Initialize variables before use.
- Avoid keywords.
- Keep code readable.

---

## 16. Things to Avoid

```python
2name = "A"
class = 5
```

```python
if age = 20:
    print("adult")
```

- Do not use invalid names.
- Do not use keywords.
- Do not use `=` for comparison.

---

## 17. Quick Examples

### Example 1
```python
name = "Nora"
print(name)
```

### Example 2
```python
a = 3
b = 4
c = a + b
print(c)
```

### Example 3
```python
user_name = "Alex"
print(user_name)
```
