# Or Operator (`or`)

## Definition

The `or` operator is a logical operator in Python that combines two or more conditions. It returns `True` if **at least one** condition is `True`.

It returns `False` only when **all** conditions are `False`.

---

# Purpose

The `or` operator is used when a program should continue if **any one** of multiple conditions is satisfied.

---

# Syntax

```python
condition1 or condition2
```

Multiple conditions can also be combined.

```python
condition1 or condition2 or condition3
```

---

# How It Works

The `or` operator evaluates each condition.

- If at least one condition is `True`, the result is `True`.
- If every condition is `False`, the result is `False`.

---

# Simple Examples

## Example 1

```python
marks = 45

print(marks >= 50 or marks >= 40)
```

**Output**

```text
True
```

The second condition is `True`, so the overall result is `True`.

---

## Example 2

```python
age = 16

print(age >= 18 or age >= 21)
```

**Output**

```text
False
```

Both conditions are `False`.

---

## Example 3

```python
temperature = 35

print(temperature < 0 or temperature > 30)
```

**Output**

```text
True
```

The second condition is `True`.

---

## Example 4

```python
number = -5

print(number > 0 or number % 2 == 0)
```

**Output**

```text
False
```

The number is neither positive nor even.

---

# Truth Table

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

# Common Use Cases

The `or` operator is commonly used for:

- Login using username or email
- Checking multiple acceptable values
- Age or permission validation
- Temperature alerts
- Security systems
- Input validation
- Exam eligibility with alternative conditions
- Decision-making based on multiple possibilities

---

# Notes

- Only one condition needs to be `True`.
- The result is `False` only if every condition is `False`.
- The `or` operator is frequently combined with comparison operators.

---

# Best Practices

- Write clear and readable conditions.
- Use meaningful variable names.
- Avoid unnecessary conditions.
- Use parentheses when combining multiple logical operators.

---

# Summary

- The `or` operator combines two or more conditions.
- It returns `True` if at least one condition is `True`.
- It returns `False` only when all conditions are `False`.
- It is useful when there are multiple acceptable conditions for a decision.