# Conditional Statements — Exam Notes

## Overview

Conditional statements allow a program to make decisions by executing different blocks of code based on whether a condition evaluates to `True` or `False`.

They are one of the fundamental control flow mechanisms in Python.

---

# Types of Conditional Statements

## 1. if Statement

Executes a block of code only when the condition is `True`.

### Syntax

```python
if condition:
    statement
```

### Example

```python
age = 18

if age >= 18:
    print("Eligible to vote")
```

---

## 2. if-else Statement

Chooses between two possible execution paths.

### Syntax

```python
if condition:
    statement1
else:
    statement2
```

### Example

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## 3. if-elif-else Statement

Used when multiple conditions need to be checked.

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
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Below Grade B")
```

---

## 4. Nested if Statement

An `if` statement placed inside another `if` or `else` block.

### Example

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
```

---

# Comparison Operators

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

---

# Logical Operators

| Operator | Purpose |
|----------|---------|
| `and` | Both conditions must be True |
| `or` | At least one condition must be True |
| `not` | Reverses a Boolean value |

---

# Flow of Execution

Python evaluates conditions from top to bottom.

- The first condition that evaluates to `True` is executed.
- Remaining `elif` and `else` blocks are skipped.
- Only one branch executes in an `if-elif-else` chain.

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

# Important Rules

- Every condition must produce either `True` or `False`.
- `elif` cannot appear without a preceding `if`.
- `else` is optional.
- There can be multiple `elif` blocks.
- Only one `else` block is allowed.
- Maintain consistent indentation.

---

# Common Exam Questions

- What is a conditional statement?
- Explain the difference between `if` and `if-else`.
- When should `elif` be used?
- What is a nested `if` statement?
- Why is indentation important in Python?
- What happens if multiple conditions are `True` in an `if-elif-else` chain?
- Explain the purpose of logical operators in conditional statements.

---

# Frequently Tested Mistakes

- Using `=` instead of `==`
- Incorrect indentation
- Missing colon (`:`)
- Writing `elif` without an `if`
- Comparing incompatible values
- Forgetting that only the first matching condition executes

---

# Quick Revision

- `if` → Executes when the condition is `True`
- `if-else` → Chooses between two outcomes
- `if-elif-else` → Handles multiple conditions
- Nested `if` → Places one conditional inside another
- Comparison operators compare values
- Logical operators combine conditions
- Indentation defines code blocks
- Only one branch executes in an `if-elif-else` structure