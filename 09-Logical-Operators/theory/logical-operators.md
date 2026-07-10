# Logical Operators

## Definition

Logical operators are special operators in Python that are used to combine or modify one or more conditions. They work with Boolean values (`True` and `False`) and return a Boolean result.

Logical operators are commonly used when a program needs to make decisions based on multiple conditions.

---

# Purpose

The purpose of logical operators is to:

- Combine multiple conditions into a single expression.
- Evaluate whether one or more conditions are true or false.
- Reverse the result of a condition.
- Build more flexible and powerful decision-making expressions.

---

# Logical Operators in Python

Python provides three logical operators.

| Operator | Description |
|----------|-------------|
| `and` | Returns `True` if both conditions are `True`. |
| `or` | Returns `True` if at least one condition is `True`. |
| `not` | Reverses the Boolean value of a condition. |

---

# Syntax

## Using `and`

```python
condition1 and condition2
```

## Using `or`

```python
condition1 or condition2
```

## Using `not`

```python
not condition
```

---

# Explanation

Logical operators evaluate Boolean expressions.

A Boolean expression always produces one of two values:

- `True`
- `False`

Logical operators use these values to determine the final result.

### Example

```python
age = 20

print(age >= 18 and age <= 60)
```

Output

```text
True
```

Both conditions are true, so the result is `True`.

---

### Example

```python
marks = 45

print(marks >= 50 or marks >= 40)
```

Output

```text
True
```

The second condition is true, so the entire expression becomes `True`.

---

### Example

```python
is_logged_in = False

print(not is_logged_in)
```

Output

```text
True
```

The `not` operator reverses the Boolean value.

---

# When to Use Logical Operators

Logical operators are useful when checking:

- Age limits
- Login information
- Password validation
- Admission requirements
- Voting eligibility
- Employee bonuses
- Temperature ranges
- Security checks
- Multiple input conditions

---

# Advantages

- Combine multiple conditions easily.
- Make programs more flexible.
- Improve decision making.
- Reduce unnecessary code.
- Increase code readability when used correctly.

---

# Notes

- Logical operators work with Boolean values.
- Comparison operators are often used together with logical operators.
- Parentheses can improve readability in complex expressions.
- Keep conditions simple and easy to understand.

---

# Best Practices

- Use meaningful variable names.
- Write readable logical expressions.
- Use parentheses when combining multiple conditions.
- Avoid writing unnecessarily complex expressions.
- Test every condition carefully before using it in a program.

---

# Summary

- Logical operators combine or modify conditions.
- Python has three logical operators:
  - `and`
  - `or`
  - `not`
- They always return a Boolean value (`True` or `False`).
- Logical operators are essential for decision making in Python.
- They are commonly used with comparison operators in real-world programs.