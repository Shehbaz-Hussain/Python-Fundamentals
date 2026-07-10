# Short-Circuit Evaluation

## Definition

Short-circuit evaluation is the process in which Python stops evaluating a logical expression as soon as the final result is known.

This makes logical expressions more efficient because Python does not evaluate conditions that cannot change the final result.

---

# Purpose

Short-circuit evaluation is used to:

- Improve program efficiency.
- Avoid unnecessary condition checks.
- Reduce the amount of work performed during evaluation.
- Make logical expressions execute faster.

---

# Short-Circuit with `and`

For the `and` operator:

- If the first condition is `False`, Python immediately returns `False`.
- The remaining conditions are not evaluated because the final result cannot become `True`.

## Example 1

```python
print(False and True)
```

**Output**

```text
False
```

Python does not need to evaluate the second value because the result is already determined.

---

## Example 2

```python
age = 15

print(age >= 18 and age <= 60)
```

**Output**

```text
False
```

The first condition is `False`, so Python already knows the complete expression is `False`.

---

# Short-Circuit with `or`

For the `or` operator:

- If the first condition is `True`, Python immediately returns `True`.
- The remaining conditions are not evaluated because the final result cannot become `False`.

## Example 3

```python
print(True or False)
```

**Output**

```text
True
```

Python does not evaluate the second value because the result is already known.

---

## Example 4

```python
marks = 85

print(marks >= 50 or marks >= 90)
```

**Output**

```text
True
```

The first condition is `True`, so the second condition does not affect the final result.

---

# Why Short-Circuit Evaluation Is Useful

Short-circuit evaluation helps to:

- Save processing time.
- Avoid unnecessary evaluations.
- Make logical expressions more efficient.
- Improve program performance.

---

# Visual Summary

## `and`

```text
First Condition = False
        │
        ▼
Result is False
Stop Evaluation
```

---

## `or`

```text
First Condition = True
        │
        ▼
Result is True
Stop Evaluation
```

---

# Notes

- Short-circuit evaluation happens automatically in Python.
- It applies only to logical operators.
- The behavior is the same whether the expression contains two conditions or more.

---

# Best Practices

- Write the most likely determining condition first when it improves readability.
- Keep logical expressions simple.
- Understand that Python may not evaluate every condition in a logical expression.
- Use parentheses to improve readability when combining multiple conditions.

---

# Summary

- Short-circuit evaluation allows Python to stop evaluating a logical expression as soon as the final result is known.
- With `and`, evaluation stops when a condition is `False`.
- With `or`, evaluation stops when a condition is `True`.
- This behavior improves efficiency by avoiding unnecessary evaluations.
- Short-circuit evaluation is automatic and is a standard feature of Python's logical operators.