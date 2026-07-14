# Conditional Statements — Revision Notes

## Learning Objectives

After completing this module, you should be able to:

- Understand the purpose of conditional statements.
- Write `if`, `if-else`, `if-elif-else`, and nested `if` statements.
- Use comparison operators to evaluate conditions.
- Combine conditions using logical operators.
- Read and trace the execution of conditional code.
- Avoid common mistakes when writing decision-making logic.

---

# Quick Overview

Conditional statements allow a program to make decisions by executing different blocks of code based on whether a condition is `True` or `False`.

Python supports four main conditional structures:

- `if`
- `if-else`
- `if-elif-else`
- Nested `if`

---

# Syntax Reference

## if Statement

```python
if condition:
    statement
```

---

## if-else Statement

```python
if condition:
    statement1
else:
    statement2
```

---

## if-elif-else Statement

```python
if condition1:
    statement1
elif condition2:
    statement2
else:
    statement3
```

---

## Nested if Statement

```python
if condition1:
    if condition2:
        statement
```

---

# Comparison Operators

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

All comparison operators return either `True` or `False`.

---

# Logical Operators

| Operator | Description |
|----------|-------------|
| `and` | Returns `True` if both conditions are `True` |
| `or` | Returns `True` if at least one condition is `True` |
| `not` | Reverses a Boolean value |

---

# Execution Flow

Python evaluates conditions from top to bottom.

- If the `if` condition is `True`, its block executes.
- Otherwise, each `elif` condition is checked in order.
- If no condition is `True`, the `else` block executes (if present).
- In an `if-elif-else` chain, only the first matching branch is executed.

---

# Best Practices

- Write clear and meaningful conditions.
- Keep conditional logic simple whenever possible.
- Use `elif` instead of multiple independent `if` statements when only one outcome should occur.
- Maintain consistent indentation (4 spaces per level).
- Test boundary values when comparing numbers.
- Arrange conditions from the most specific to the most general when appropriate.

---

# Common Mistakes

- Using `=` instead of `==`
- Forgetting the colon (`:`)
- Incorrect indentation
- Writing `elif` without a preceding `if`
- Comparing incompatible data types
- Placing conditions in an order that makes later conditions unreachable

---

# Key Differences

| Structure | Purpose |
|-----------|---------|
| `if` | Execute code when a condition is `True` |
| `if-else` | Choose between two possible outcomes |
| `if-elif-else` | Choose among multiple possible outcomes |
| Nested `if` | Make a decision inside another decision |

---

# Frequently Asked Questions

### Can an `if` statement exist without an `else`?

Yes. The `else` block is optional.

---

### Can there be multiple `elif` statements?

Yes. You can use as many `elif` statements as needed.

---

### Can there be more than one `else`?

No. An `if` statement can have only one `else` block.

---

### What happens if every condition is `False` and there is no `else`?

No conditional block is executed, and the program continues with the next statement.

---

# Revision Checklist

Before moving to the next module, ensure that you can:

- Explain what conditional statements are.
- Write valid `if`, `if-else`, `if-elif-else`, and nested `if` statements.
- Use comparison operators correctly.
- Use logical operators (`and`, `or`, `not`) correctly.
- Trace the execution of conditional code.
- Identify and correct common syntax and logic errors.
- Choose the appropriate conditional structure for a given problem.

---

# Summary

- Conditional statements control the flow of a program based on conditions.
- Conditions evaluate to either `True` or `False`.
- Python provides `if`, `if-else`, `if-elif-else`, and nested `if` statements.
- Comparison operators create conditions.
- Logical operators combine or modify conditions.
- Proper indentation is required because it defines code blocks.
- Well-structured conditional statements make programs easier to read, maintain, and debug.