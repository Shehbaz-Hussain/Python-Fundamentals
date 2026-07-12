# Revision Notes — Logical Operators

## Introduction

This revision guide provides a concise review of **Module 09: Logical Operators**. It is designed to help you revise the complete module in **15–20 minutes** before quizzes, laboratory exams, midterm examinations, final examinations, or technical interviews.

---

# Learning Objectives

After reviewing these notes, you should be able to:

- Explain logical operators.
- Use `and`, `or`, and `not` correctly.
- Combine comparison operators with logical operators.
- Understand truth tables.
- Apply operator precedence.
- Explain short-circuit evaluation.
- Write simple logical expressions using `if` statements.

---

# Logical Operators

Logical operators combine or modify Boolean expressions.

Python has **three logical operators**:

| Operator | Purpose |
|----------|---------|
| `and` | Returns `True` only if both conditions are `True`. |
| `or` | Returns `True` if at least one condition is `True`. |
| `not` | Reverses a Boolean value. |

---

# Boolean Values

Python has two Boolean values:

```python
True
False
```

Logical expressions always evaluate to one of these values.

Example:

```python
print(10 > 5)
```

Output:

```text
True
```

---

# The `and` Operator

### Syntax

```python
condition1 and condition2
```

### Example

```python
age = 22

print(age >= 18 and age <= 60)
```

Output

```text
True
```

### Truth Table

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

# The `or` Operator

### Syntax

```python
condition1 or condition2
```

### Example

```python
marks = 45

print(marks >= 50 or marks == 45)
```

Output

```text
True
```

### Truth Table

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

# The `not` Operator

### Syntax

```python
not condition
```

### Example

```python
print(not False)
```

Output

```text
True
```

### Truth Table

| Condition | Result |
|-----------|--------|
| True | False |
| False | True |

---

# Combining Comparison and Logical Operators

Logical operators are often used with comparison operators.

Example:

```python
temperature = 28

print(temperature >= 20 and temperature <= 30)
```

Output

```text
True
```

---

# Using Logical Operators with `if`

Example:

```python
marks = 75

if marks >= 50 and marks <= 100:
    print("Pass")
```

---

# Operator Precedence

When parentheses are not used, Python evaluates logical operators in the following order:

| Priority | Operator |
|----------|----------|
| 1 (Highest) | `not` |
| 2 | `and` |
| 3 (Lowest) | `or` |

Example:

```python
True or False and False
```

Python first evaluates:

```python
False and False
```

Final result:

```text
True
```

---

# Short-Circuit Evaluation

Python may stop evaluating an expression as soon as the final result is known.

Examples:

```python
True or False
```

The second condition is not evaluated because the result is already `True`.

```python
False and True
```

The second condition is not evaluated because the result is already `False`.

---

# Common Patterns

## Check Whether a Number Is in a Range

```python
number >= 1 and number <= 10
```

---

## Check Multiple Acceptable Values

```python
grade == "A" or grade == "B"
```

---

## Reverse a Condition

```python
not(age < 18)
```

---

# Common Mistakes

- Writing `AND`, `OR`, or `NOT` instead of lowercase `and`, `or`, and `not`.
- Confusing comparison operators with logical operators.
- Ignoring operator precedence.
- Forgetting to use parentheses when expressions become difficult to read.
- Creating unnecessarily long and complex logical expressions.

---

# Best Practices

- Use meaningful variable names.
- Keep logical expressions simple.
- Add parentheses to improve readability.
- Test expressions with different values.
- Write clean and properly indented code.

---

# Frequently Tested Topics

- Definition of logical operators
- Boolean values
- `and`
- `or`
- `not`
- Truth tables
- Logical expressions
- Operator precedence
- Short-circuit evaluation
- Using logical operators with comparison operators
- Using logical operators in `if` statements

---

# Memory Tricks

## `and`

Think:

> **All conditions must be true.**

---

## `or`

Think:

> **At least one condition must be true.**

---

## `not`

Think:

> **Reverse the answer.**

---

## Operator Precedence

Remember:

```text
not
↓

and
↓

or
```

---

# 5-Minute Final Revision Checklist

Before your exam, make sure you can answer these questions:

- What are logical operators?
- Name all three logical operators.
- What does `and` do?
- What does `or` do?
- What does `not` do?
- What are Boolean values?
- Can logical operators be used with comparison operators?
- What is operator precedence?
- What is short-circuit evaluation?
- Can logical operators be used inside `if` statements?

If you can confidently answer these questions, you are well prepared for Module 09.

---

# Summary

Logical operators are essential for decision-making in Python. Understanding how `and`, `or`, and `not` work, along with truth tables, operator precedence, and short-circuit evaluation, enables you to write clear and correct conditional logic. Mastering these fundamentals provides a strong foundation for future topics such as nested conditions, loops, functions, and more advanced programming concepts.