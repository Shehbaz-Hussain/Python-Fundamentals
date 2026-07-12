# Exam Notes — Logical Operators

## Introduction

These exam notes provide a concise review of the most important concepts from **Module 09: Logical Operators**. They are designed for quick revision before quizzes, laboratory exams, midterm examinations, and final examinations.

---

# What Are Logical Operators?

Logical operators are used to **combine**, **modify**, or **evaluate** Boolean expressions.

A logical expression always produces one of two values:

- `True`
- `False`

Python provides three logical operators:

| Operator | Purpose |
|----------|---------|
| `and` | Returns `True` if both conditions are `True`. |
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
print(5 > 3)
```

Output:

```text
True
```

---

# The `and` Operator

The `and` operator requires **both conditions** to be `True`.

### Syntax

```python
condition1 and condition2
```

### Example

```python
age = 20

print(age >= 18 and age <= 30)
```

Output:

```text
True
```

---

# Truth Table — `and`

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

# The `or` Operator

The `or` operator returns `True` if **at least one** condition is `True`.

### Syntax

```python
condition1 or condition2
```

### Example

```python
marks = 45

print(marks >= 50 or marks == 45)
```

Output:

```text
True
```

---

# Truth Table — `or`

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

# The `not` Operator

The `not` operator reverses a Boolean value.

### Syntax

```python
not condition
```

### Example

```python
print(not True)
```

Output:

```text
False
```

---

# Truth Table — `not`

| Condition | Result |
|-----------|--------|
| True | False |
| False | True |

---

# Combining Comparison and Logical Operators

Logical operators are commonly used with comparison operators.

Example:

```python
age = 22

print(age >= 18 and age <= 60)
```

---

# Using Logical Operators in `if` Statements

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
| Highest | `not` |
| Medium | `and` |
| Lowest | `or` |

Example:

```python
True or False and False
```

Python evaluates:

```python
False and False
```

first.

Final result:

```text
True
```

---

# Using Parentheses

Parentheses make expressions easier to read and remove ambiguity.

Example:

```python
(age >= 18 and age <= 60)
```

Using parentheses is considered a good programming practice.

---

# Short-Circuit Evaluation

Python sometimes stops evaluating an expression as soon as the final result is known.

Example:

```python
True or False
```

Since the first value is already `True`, Python does not need to evaluate the second condition.

Similarly,

```python
False and True
```

Since the first value is already `False`, the entire expression must be `False`.

---

# Frequently Tested Concepts

Make sure you understand the following topics:

- Boolean values
- Logical expressions
- `and`
- `or`
- `not`
- Truth tables
- Operator precedence
- Parentheses
- Short-circuit evaluation
- Using logical operators with comparison operators
- Using logical operators in `if` statements

---

# Common Exam Questions

You should be able to answer questions such as:

- What are logical operators?
- Name the three logical operators.
- Explain the difference between `and` and `or`.
- What does `not` do?
- Draw the truth tables.
- Explain operator precedence.
- What is short-circuit evaluation?
- Predict the output of logical expressions.
- Identify syntax errors involving logical operators.

---

# Common Mistakes

Avoid these common mistakes during exams:

### Using uppercase keywords

Incorrect:

```python
AND
OR
NOT
```

Correct:

```python
and
or
not
```

---

### Confusing comparison and logical operators

Comparison operators compare values.

Logical operators combine or modify comparisons.

---

### Ignoring Operator Precedence

Incorrect understanding of precedence can produce unexpected results.

Remember:

```text
not
↓

and
↓

or
```

---

### Forgetting Parentheses

Although not always required, parentheses improve readability and help avoid mistakes.

---

### Writing Complex Expressions

Keep logical expressions simple whenever possible.

---

# Quick Revision

Remember these key points:

- Python has **three logical operators**.
- Logical operators always produce **Boolean values**.
- `and` requires both conditions to be `True`.
- `or` requires at least one condition to be `True`.
- `not` reverses a Boolean value.
- Parentheses improve readability.
- Operator precedence:
  1. `not`
  2. `and`
  3. `or`
- Python performs short-circuit evaluation.
- Logical operators are frequently combined with comparison operators and `if` statements.

---

# Exam Tips

- Read each condition carefully before evaluating it.
- Solve comparison expressions first.
- Apply logical operators according to precedence.
- Use truth tables if you are unsure.
- Predict outputs before running code.
- Practice writing and evaluating logical expressions by hand.

---

# Summary

Logical operators are fundamental to decision-making in Python. Mastering `and`, `or`, and `not`, along with truth tables, operator precedence, and short-circuit evaluation, is essential for writing correct conditional logic. These topics are frequently tested in university examinations, coding assessments, and technical interviews, making them an important part of your Python foundation.