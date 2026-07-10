# Logical Operators Syntax

## Introduction

Logical operators are used to combine or modify Boolean expressions. They are commonly used with comparison operators to create conditions that evaluate to either `True` or `False`.

Python provides three logical operators:

- `and`
- `or`
- `not`

---

# Basic Syntax

## `and` Operator

Returns `True` only if all conditions are `True`.

### Syntax

```python
condition1 and condition2
```

### Example

```python
age = 25

print(age >= 18 and age <= 60)
```

---

## `or` Operator

Returns `True` if at least one condition is `True`.

### Syntax

```python
condition1 or condition2
```

### Example

```python
marks = 45

print(marks >= 50 or marks >= 40)
```

---

## `not` Operator

Reverses the Boolean value of a condition.

### Syntax

```python
not condition
```

### Example

```python
is_logged_in = False

print(not is_logged_in)
```

---

# Combining Multiple Conditions

Multiple logical operators can be used in a single expression.

### Syntax

```python
condition1 and condition2 or condition3
```

### Example

```python
age = 20
marks = 85

print(age >= 18 and marks >= 80)
```

---

# Using Parentheses

Parentheses improve readability and make the intended order of evaluation clear.

### Syntax

```python
(condition1 and condition2)
```

### Example

```python
temperature = 25

print((temperature >= 20) and (temperature <= 30))
```

---

# Syntax Summary

| Operator | Syntax |
|----------|--------|
| `and` | `condition1 and condition2` |
| `or` | `condition1 or condition2` |
| `not` | `not condition` |

---

# Notes

- Logical operators work with Boolean expressions.
- Comparison operators are commonly used to create these expressions.
- Parentheses are recommended when combining multiple conditions.
- Logical expressions always evaluate to `True` or `False`.

---

# Best Practices

- Write clear and readable conditions.
- Use meaningful variable names.
- Keep logical expressions simple.
- Use parentheses to improve readability.
- Follow PEP 8 formatting guidelines.

---

# Summary

- Python provides three logical operators: `and`, `or`, and `not`.
- The `and` operator requires all conditions to be `True`.
- The `or` operator requires at least one condition to be `True`.
- The `not` operator reverses a Boolean value.
- Using proper syntax and parentheses makes logical expressions easier to read and understand.