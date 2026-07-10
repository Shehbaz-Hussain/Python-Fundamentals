# Operator Precedence

## Definition

Operator precedence is the order in which Python evaluates operators in an expression.

When an expression contains multiple operators, Python follows a predefined order to determine which operation is performed first.

Understanding operator precedence helps you write correct and predictable logical expressions.

---

# Purpose

Operator precedence is used to:

- Evaluate expressions correctly.
- Remove ambiguity from complex conditions.
- Produce consistent and predictable results.
- Improve code readability when used with parentheses.

---

# Precedence of Operators Learned So Far

The following table shows the precedence of the operators covered up to this module, from **highest** to **lowest**.

| Precedence | Operator | Description |
|------------|----------|-------------|
| 1 (Highest) | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `*`, `/`, `//`, `%` | Multiplication, Division, Floor Division, Modulus |
| 4 | `+`, `-` | Addition, Subtraction |
| 5 | `==`, `!=`, `>`, `<`, `>=`, `<=` | Comparison Operators |
| 6 | `not` | Logical NOT |
| 7 | `and` | Logical AND |
| 8 (Lowest) | `or` | Logical OR |

---

# How Python Evaluates Expressions

Python evaluates operators according to their precedence.

## Example 1

```python
print(5 + 3 * 2)
```

**Output**

```text
11
```

The multiplication is performed before the addition.

---

## Example 2

```python
print((5 + 3) * 2)
```

**Output**

```text
16
```

The parentheses are evaluated first.

---

## Example 3

```python
age = 20

print(age >= 18 and age <= 60)
```

**Output**

```text
True
```

The comparison operators are evaluated first, followed by the `and` operator.

---

## Example 4

```python
print(not True or False)
```

**Output**

```text
False
```

Evaluation order:

1. `not True` → `False`
2. `False or False` → `False`

---

## Example 5

```python
print(True or False and False)
```

**Output**

```text
True
```

Evaluation order:

1. `False and False` → `False`
2. `True or False` → `True`

---

# Using Parentheses

Parentheses have the highest precedence.

They make expressions easier to read and clearly show the intended order of evaluation.

Example:

```python
print((10 > 5) and (8 < 12))
```

**Output**

```text
True
```

---

# Why Parentheses Are Recommended

Even when they are not required, parentheses:

- Improve readability.
- Make complex conditions easier to understand.
- Reduce the chance of logical errors.
- Help others understand your code.

---

# Notes

- Parentheses are evaluated first.
- Arithmetic operators are evaluated before comparison operators.
- Comparison operators are evaluated before logical operators.
- Among logical operators, the order is:
  1. `not`
  2. `and`
  3. `or`

---

# Best Practices

- Use parentheses to make complex expressions clear.
- Do not rely only on operator precedence when readability is important.
- Keep logical expressions short and easy to understand.
- Test complex conditions carefully.

---

# Summary

- Operator precedence determines the order of evaluation.
- Parentheses have the highest precedence.
- Comparison operators are evaluated before logical operators.
- The precedence of logical operators is:
  1. `not`
  2. `and`
  3. `or`
- Using parentheses improves readability and helps prevent logical mistakes.