# Module Summary

## Overview

In this module, you learned how Python uses logical operators to combine and modify conditions. Logical operators are fundamental for writing programs that make decisions based on one or more conditions.

Logical operators always evaluate expressions that result in Boolean values (`True` or `False`).

---

# What You Learned

You studied the following topics:

- Introduction to logical operators
- The `and` operator
- The `or` operator
- The `not` operator
- Operator precedence
- Truth tables
- Short-circuit evaluation
- Common real-world use cases

---

# Logical Operators

| Operator | Purpose | Returns `True` When |
|----------|---------|---------------------|
| `and` | Combines conditions | All conditions are `True` |
| `or` | Combines alternative conditions | At least one condition is `True` |
| `not` | Reverses a condition | The original condition is `False` |

---

# Operator Precedence

Python evaluates the logical operators in the following order:

| Order | Operator |
|------:|----------|
| 1 | `not` |
| 2 | `and` |
| 3 | `or` |

Using parentheses `()` makes expressions easier to read and removes ambiguity.

---

# Truth Tables

## `and`

| A | B | A and B |
|---|---|----------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### `or`

| A | B | A or B |
|---|---|---------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### `not`

| A | not A |
|---|-------|
| True | False |
| False | True |

---

# Short-Circuit Evaluation

Python can stop evaluating a logical expression as soon as the final result is known.

### With `and`

- Evaluation stops when a condition becomes `False`.

### With `or`

- Evaluation stops when a condition becomes `True`.

This behavior improves program efficiency.

---

# Best Practices

- Use meaningful variable names.
- Keep logical expressions simple.
- Use parentheses to improve readability.
- Test logical expressions with different values.
- Write conditions that are easy to understand.

---

# Common Mistakes

- Confusing `=` with `==`.
- Mixing `and` and `or` without understanding precedence.
- Forgetting that `not` reverses a Boolean value.
- Writing overly complex logical expressions.
- Ignoring parentheses in long conditions.

---

# Real-World Applications

Logical operators are commonly used in:

- Login systems
- Password validation
- Voting eligibility
- Admission checking
- Employee bonus calculation
- Security systems
- Temperature monitoring
- Input validation
- Business rule enforcement
- Decision-making programs

---

# Key Points to Remember

- Python has **three** logical operators:
  - `and`
  - `or`
  - `not`
- Logical operators always produce a Boolean result.
- `and` requires every condition to be `True`.
- `or` requires at least one condition to be `True`.
- `not` reverses a Boolean value.
- Parentheses improve readability and make the intended order of evaluation clear.
- Short-circuit evaluation helps Python evaluate logical expressions efficiently.

---

# Next Module

The next module introduces **Conditional Statements (`if`, `elif`, and `else`)**.

You will learn how to use logical expressions to control the flow of a Python program and execute different blocks of code based on conditions.