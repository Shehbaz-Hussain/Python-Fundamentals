# Not Operator (`not`)

## Definition

The `not` operator is a logical operator in Python that reverses the Boolean value of a condition.

- If the condition is `True`, `not` returns `False`.
- If the condition is `False`, `not` returns `True`.

Unlike `and` and `or`, which combine conditions, `not` modifies a single condition.

---

# Purpose

The `not` operator is used to:

- Reverse the result of a condition.
- Check whether a condition is **not** true.
- Simplify certain logical expressions.
- Improve readability in some decision-making scenarios.

---

# Syntax

```python
not condition
```

---

# How It Works

The `not` operator evaluates a condition and returns the opposite Boolean value.

- `True` becomes `False`.
- `False` becomes `True`.

---

# Simple Examples

## Example 1

```python
is_logged_in = False

print(not is_logged_in)
```

**Output**

```text
True
```

The original value is `False`, so `not` changes it to `True`.

---

## Example 2

```python
age = 15

print(not (age >= 18))
```

**Output**

```text
True
```

The expression `age >= 18` is `False`, so `not` changes it to `True`.

---

## Example 3

```python
number = 8

print(not (number < 0))
```

**Output**

```text
True
```

The condition `number < 0` is `False`, so the result becomes `True`.

---

## Example 4

```python
temperature = 35

print(not (temperature <= 30))
```

**Output**

```text
True
```

Since `temperature <= 30` is `False`, the `not` operator returns `True`.

---

# Truth Table

| Condition | Result of `not` |
|-----------|-----------------|
| True | False |
| False | True |

---

# Common Use Cases

The `not` operator is commonly used for:

- Login status checks
- Security validation
- Permission checking
- Age restrictions
- Input validation
- Reversing conditions
- Access control
- Decision-making programs

---

# Notes

- The `not` operator works with only one condition.
- It always returns the opposite Boolean value.
- Parentheses improve readability when `not` is used with comparison operators.

---

# Best Practices

- Use parentheses to make expressions easier to read.
- Avoid using multiple `not` operators in the same expression.
- Use meaningful variable names.
- Keep conditions simple and understandable.

---

# Summary

- The `not` operator reverses a Boolean value.
- It changes `True` to `False` and `False` to `True`.
- It operates on a single condition.
- It is useful when checking whether a condition is not satisfied.
- Parentheses improve readability when using `not` with comparison operators.