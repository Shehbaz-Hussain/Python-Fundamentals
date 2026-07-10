# Logical Operators Cheat Sheet

## Overview

Logical operators are used to combine or modify Boolean expressions. They are commonly used with comparison operators to make decisions in Python programs.

---

# Logical Operators

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `and` | Returns `True` if all conditions are `True` | `5 > 2 and 8 > 4` | `True` |
| `or` | Returns `True` if at least one condition is `True` | `5 > 8 or 8 > 4` | `True` |
| `not` | Reverses a Boolean value | `not True` | `False` |

---

# Basic Syntax

## `and`

```python
condition1 and condition2
```

Example:

```python
age >= 18 and age <= 60
```

---

## `or`

```python
condition1 or condition2
```

Example:

```python
marks >= 50 or attendance >= 75
```

---

## `not`

```python
not condition
```

Example:

```python
not is_logged_in
```

---

# Truth Tables

## `and`

| A | B | A and B |
|---|---|-----------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

## `or`

| A | B | A or B |
|---|---|----------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

## `not`

| A | not A |
|---|-------|
| True | False |
| False | True |

---

# Operator Precedence

From highest to lowest:

1. `()`
2. `not`
3. `and`
4. `or`

Example:

```python
True or False and False
```

Evaluation:

```text
False and False
↓

True or False
↓

True
```

---

# Short-Circuit Evaluation

## `and`

Stops when the first `False` condition is found.

Example:

```python
False and True
```

Result:

```text
False
```

---

## `or`

Stops when the first `True` condition is found.

Example:

```python
True or False
```

Result:

```text
True
```

---

# Common Examples

## Age Validation

```python
age >= 18 and age <= 60
```

---

## Login Validation

```python
username == "admin" and password == "python123"
```

---

## Voting Eligibility

```python
age >= 18
```

---

## Temperature Check

```python
temperature < 0 or temperature > 35
```

---

## Positive Even Number

```python
number > 0 and number % 2 == 0
```

---

# Best Practices

- Use meaningful variable names.
- Keep conditions short and readable.
- Use parentheses to improve clarity.
- Understand operator precedence.
- Test logical expressions with different values.
- Follow PEP 8 formatting guidelines.

---

# Common Mistakes

- Using `=` instead of `==`
- Confusing `and` and `or`
- Forgetting that `not` reverses a Boolean value
- Ignoring operator precedence
- Writing overly complex conditions

---

# Quick Revision

| Operator | Returns `True` When |
|----------|---------------------|
| `and` | All conditions are `True` |
| `or` | At least one condition is `True` |
| `not` | The original condition is `False` |

---

# Remember

- Python has **three** logical operators.
- Logical operators always return `True` or `False`.
- Precedence order: `()` → `not` → `and` → `or`.
- Use parentheses whenever they improve readability.
- Logical operators are widely used in decision-making programs.