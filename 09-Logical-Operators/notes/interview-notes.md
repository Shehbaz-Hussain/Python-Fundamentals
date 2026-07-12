# Interview Notes — Logical Operators

## Introduction

These interview notes cover the most common beginner-level interview questions related to Python logical operators. They are intended for university students, fresh graduates, and beginners preparing for technical interviews, coding assessments, and programming quizzes.

---

# What Are Logical Operators?

Logical operators are used to combine or modify Boolean expressions. They always produce a Boolean result (`True` or `False`).

Python provides three logical operators:

- `and`
- `or`
- `not`

---

# Beginner Interview Questions and Expected Answers

## 1. What are logical operators in Python?

### Expected Answer

Logical operators are operators used to combine or modify Boolean expressions. They return either `True` or `False`.

---

## 2. Name the logical operators available in Python.

### Expected Answer

Python has three logical operators:

- `and`
- `or`
- `not`

---

## 3. What does the `and` operator do?

### Expected Answer

The `and` operator returns `True` only when **both** conditions are `True`.

### Example

```python
age = 20

print(age >= 18 and age <= 30)
```

Output

```text
True
```

---

## 4. What does the `or` operator do?

### Expected Answer

The `or` operator returns `True` if **at least one** condition is `True`.

### Example

```python
marks = 45

print(marks >= 50 or marks == 45)
```

Output

```text
True
```

---

## 5. What does the `not` operator do?

### Expected Answer

The `not` operator reverses a Boolean value.

### Example

```python
print(not True)
```

Output

```text
False
```

---

## 6. What is a Boolean value?

### Expected Answer

A Boolean value is either:

- `True`
- `False`

---

## 7. What is a logical expression?

### Expected Answer

A logical expression is an expression that combines one or more conditions using logical operators and evaluates to either `True` or `False`.

---

## 8. Which comparison operators are commonly used with logical operators?

### Expected Answer

- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`

---

## 9. What is the difference between `and` and `or`?

### Expected Answer

| `and` | `or` |
|-------|------|
| Requires all conditions to be `True`. | Requires at least one condition to be `True`. |

---

## 10. What does the following code print?

```python
print(True and False)
```

### Expected Answer

```text
False
```

---

## 11. What does the following code print?

```python
print(True or False)
```

### Expected Answer

```text
True
```

---

## 12. What does the following code print?

```python
print(not False)
```

### Expected Answer

```text
True
```

---

## 13. Can logical operators be used inside an `if` statement?

### Expected Answer

Yes. Logical operators are commonly used in `if` statements to combine multiple conditions.

### Example

```python
age = 22

if age >= 18 and age <= 60:
    print("Eligible")
```

---

## 14. What is operator precedence for logical operators?

### Expected Answer

The order of precedence is:

1. `not`
2. `and`
3. `or`

---

## 15. What is short-circuit evaluation?

### Expected Answer

Short-circuit evaluation means Python may stop evaluating a logical expression as soon as the final result is already known.

---

# Practical Interview Examples

## Example 1 — Age Verification

```python
age = 19

print(age >= 18 and age <= 60)
```

Expected Output

```text
True
```

---

## Example 2 — Scholarship Eligibility

```python
marks = 90
attendance = 95

print(marks >= 85 and attendance >= 90)
```

Expected Output

```text
True
```

---

## Example 3 — Login Check

```python
username = "admin"
password = "python123"

print(username == "admin" and password == "python123")
```

Expected Output

```text
True
```

---

## Example 4 — Discount Eligibility

```python
amount = 6000
coupon = "no"

print(amount >= 5000 or coupon == "yes")
```

Expected Output

```text
True
```

---

## Example 5 — Boolean Negation

```python
print(not (5 > 10))
```

Expected Output

```text
True
```

---

# Common Interview Mistakes

## Using Uppercase Keywords

Incorrect

```python
AND
OR
NOT
```

Correct

```python
and
or
not
```

---

## Confusing Comparison Operators with Logical Operators

Comparison operators compare values.

Logical operators combine or modify Boolean expressions.

---

## Ignoring Operator Precedence

Remember the order:

```text
not
↓

and
↓

or
```

Use parentheses whenever an expression becomes difficult to read.

---

## Forgetting That `not` Reverses a Boolean Value

Example

```python
not True
```

Result

```text
False
```

---

## Writing Unnecessarily Complex Conditions

Prefer clear and readable expressions over long, difficult-to-understand conditions.

---

# Interview Tips

- Learn the purpose of each logical operator.
- Memorize the truth tables.
- Practice predicting program output without executing the code.
- Understand the difference between comparison operators and logical operators.
- Remember the operator precedence.
- Use parentheses to improve readability.
- Be prepared to explain your reasoning, not just the final answer.

---

# Quick Revision

Remember these key facts:

- Python has **three logical operators**.
- Logical expressions return `True` or `False`.
- `and` requires all conditions to be `True`.
- `or` requires at least one condition to be `True`.
- `not` reverses a Boolean value.
- Operator precedence:
  1. `not`
  2. `and`
  3. `or`
- Python performs short-circuit evaluation.
- Logical operators are frequently combined with comparison operators and `if` statements.

---

# Summary

Logical operators are one of the first topics discussed in Python technical interviews because they form the basis of decision-making in programs. A solid understanding of `and`, `or`, `not`, truth tables, operator precedence, and short-circuit evaluation will help you answer beginner interview questions confidently and prepare you for more advanced Python concepts in later modules.