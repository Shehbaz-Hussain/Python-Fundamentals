# Logical Operators Cheat Sheet

## Introduction

This cheat sheet is a quick reference for **Module 09: Logical Operators**. It summarizes the most important concepts, syntax, truth tables, operator precedence, common patterns, best practices, and common mistakes. It is intended for fast revision before quizzes, exams, coding exercises, and interviews.

---

# Logical Operators

| Operator | Description | Returns `True` When |
|----------|-------------|---------------------|
| `and` | Logical AND | Both conditions are `True` |
| `or` | Logical OR | At least one condition is `True` |
| `not` | Logical NOT | Reverses a Boolean value |

---

# Syntax

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
marks >= 50 or marks == 45
```

---

## `not`

```python
not condition
```

Example:

```python
not(age < 18)
```

---

# Truth Tables

## `and`

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

## `or`

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

## `not`

| Condition | Result |
|-----------|--------|
| True | False |
| False | True |

---

# Operator Precedence

When parentheses are not used, Python evaluates logical operators in this order:

| Priority | Operator |
|----------|----------|
| 1 (Highest) | `not` |
| 2 | `and` |
| 3 (Lowest) | `or` |

**Memory Order:**

```text
not
↓

and
↓

or
```

---

# Short-Circuit Evaluation

Python may stop evaluating an expression as soon as the final result is already known.

### Example 1

```python
True or False
```

Result:

```text
True
```

The second condition is not evaluated.

---

### Example 2

```python
False and True
```

Result:

```text
False
```

The second condition is not evaluated.

---

# Common Patterns

## Check Whether a Value Is in a Range

```python
age >= 18 and age <= 60
```

---

## Check Multiple Valid Values

```python
grade == "A" or grade == "B"
```

---

## Reverse a Condition

```python
not(age < 18)
```

---

## Check Pass Status

```python
marks >= 50
```

---

## Check Eligibility

```python
age >= 18 and citizen == "yes"
```

---

# Quick Examples

### Example 1

```python
print(True and True)
```

Output:

```text
True
```

---

### Example 2

```python
print(True and False)
```

Output:

```text
False
```

---

### Example 3

```python
print(False or True)
```

Output:

```text
True
```

---

### Example 4

```python
print(not False)
```

Output:

```text
True
```

---

### Example 5

```python
age = 20

print(age >= 18 and age <= 30)
```

Output:

```text
True
```

---

# Best Practices

- Use meaningful variable names.
- Keep logical expressions short and readable.
- Use parentheses to improve readability.
- Test logical expressions with different input values.
- Combine logical operators with comparison operators carefully.
- Follow proper indentation in `if` statements.

---

# Common Mistakes

## Using Uppercase Keywords

❌ Incorrect

```python
AND
OR
NOT
```

✅ Correct

```python
and
or
not
```

---

## Confusing Comparison and Logical Operators

Comparison operators compare values.

Logical operators combine or modify Boolean expressions.

---

## Ignoring Operator Precedence

Remember:

```text
not
↓

and
↓

or
```

---

## Forgetting Parentheses

Use parentheses when expressions become difficult to read.

Example:

```python
(age >= 18 and age <= 60)
```

---

## Writing Long, Complex Expressions

Prefer simple and readable conditions over complicated expressions.

---

# Memory Tricks

## `and`

**Think:** All conditions must be true.

---

## `or`

**Think:** At least one condition must be true.

---

## `not`

**Think:** Reverse the answer.

---

## Operator Precedence

Remember the phrase:

> **Not And Or**

This represents the evaluation order:

```text
not
↓

and
↓

or
```

---

# Quick Revision Checklist

Before moving to the next module, make sure you can:

- Explain logical operators.
- Use `and`, `or`, and `not`.
- Read and create truth tables.
- Predict the result of logical expressions.
- Apply operator precedence correctly.
- Explain short-circuit evaluation.
- Combine comparison and logical operators.
- Use logical operators inside `if` statements.
- Identify common mistakes.
- Write simple and readable logical expressions.

---

# Summary

Logical operators are fundamental tools for making decisions in Python programs. By mastering `and`, `or`, and `not`, along with truth tables, operator precedence, and short-circuit evaluation, you can build accurate and readable conditional logic. Keep this cheat sheet as a quick reference while practicing and revising Python fundamentals.