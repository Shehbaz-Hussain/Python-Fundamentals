# Python Conditional Statements Cheat Sheet

> **Module:** 10 - Conditional Statements  
> **Repository:** Python-Programming-Foundation

---

# What Are Conditional Statements?

Conditional statements allow a program to make decisions by executing different blocks of code based on whether a condition is `True` or `False`.

---

# Conditional Statement Types

## 1. if Statement

Executes a block of code only when the condition is `True`.

### Syntax

```python
if condition:
    statement
```

### Example

```python
age = 20

if age >= 18:
    print("Adult")
```

---

## 2. if-else Statement

Executes one block when the condition is `True` and another when it is `False`.

### Syntax

```python
if condition:
    statement1
else:
    statement2
```

### Example

```python
number = 5

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## 3. if-elif-else Statement

Checks multiple conditions in sequence.

### Syntax

```python
if condition1:
    statement1
elif condition2:
    statement2
else:
    statement3
```

### Example

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade F")
```

---

## 4. Nested if Statement

Places one conditional statement inside another.

### Syntax

```python
if condition1:
    if condition2:
        statement
```

### Example

```python
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Access granted")
```

---

# Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `x == y` |
| `!=` | Not equal to | `x != y` |
| `>` | Greater than | `x > y` |
| `<` | Less than | `x < y` |
| `>=` | Greater than or equal to | `x >= y` |
| `<=` | Less than or equal to | `x <= y` |

All comparison operators return either `True` or `False`.

---

# Logical Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | Both conditions must be `True` | `age >= 18 and has_id` |
| `or` | At least one condition must be `True` | `age >= 18 or has_permission` |
| `not` | Reverses a Boolean value | `not is_logged_in` |

---

# Execution Flow

Python evaluates conditions from top to bottom.

```text
Start
  │
  ▼
Evaluate if
  │
  ├── True ──► Execute if block
  │
  └── False
         │
         ▼
    Evaluate elif
         │
         ├── True ──► Execute elif block
         │
         └── False
                │
                ▼
         Execute else block
```

Only **one branch** executes in an `if-elif-else` chain.

---

# Indentation

Python uses indentation to define code blocks.

Correct:

```python
if True:
    print("Hello")
```

Incorrect:

```python
if True:
print("Hello")
```

---

# Common Mistakes

❌ Using `=` instead of `==`

```python
if age = 18:
```

✔ Correct

```python
if age == 18:
```

---

❌ Forgetting the colon

```python
if age >= 18
```

✔ Correct

```python
if age >= 18:
```

---

❌ Incorrect indentation

```python
if age >= 18:
print("Adult")
```

✔ Correct

```python
if age >= 18:
    print("Adult")
```

---

# Best Practices

- Write clear and readable conditions.
- Use meaningful variable names.
- Keep nesting as shallow as possible.
- Use `elif` when only one condition should match.
- Test boundary values (for example, `0`, `18`, `100`).
- Maintain consistent indentation (4 spaces).

---

# Quick Examples

### Positive or Negative

```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

---

### Voting Eligibility

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

---

### Largest of Two Numbers

```python
a = 15
b = 20

if a > b:
    print(a)
else:
    print(b)
```

---

# Exam Tips

- Remember the syntax of each conditional statement.
- Do not confuse `=` with `==`.
- Always end `if`, `elif`, and `else` with a colon (`:`).
- Indent every statement inside a conditional block.
- In an `if-elif-else` chain, only the first matching condition executes.
- Use logical operators to combine multiple conditions.

---

# One-Minute Revision

- `if` → Execute code when a condition is `True`.
- `if-else` → Choose between two outcomes.
- `if-elif-else` → Handle multiple conditions.
- Nested `if` → Make a decision within another decision.
- Comparison operators return `True` or `False`.
- Logical operators combine or modify conditions.
- Indentation defines code blocks in Python.
- Only one branch executes in an `if-elif-else` structure.