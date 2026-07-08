# ⚡ Arithmetic Operators Revision Notes

This document is designed for **ultra-fast revision** before exams, interviews, coding assessments, and practical programming sessions. It summarizes the most important concepts about Python arithmetic operators in a concise and easy-to-review format.

---

# 📖 Definition

Arithmetic operators are symbols used to perform mathematical operations on numeric values.

They are commonly used for:

- Calculations
- Data processing
- Algorithms
- Artificial Intelligence
- Machine Learning
- Scientific computing
- Financial applications
- Game development

Example

```python
a = 12
b = 5

print(a + b)
```

Output

```text
17
```

---

# 📋 Operator Summary Table

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | True Division | `10 / 4` | `2.5` |
| `//` | Floor Division | `10 // 4` | `2` |
| `%` | Modulus | `10 % 4` | `2` |
| `**` | Exponentiation | `2 ** 5` | `32` |

---

# 📌 Key Rules

- Arithmetic operators work with numeric data types.
- `/` always returns a `float`.
- `//` performs floor division.
- `%` returns the remainder after division.
- `**` performs exponentiation.
- Parentheses have the highest precedence.
- Mixed `int` and `float` arithmetic usually produces a `float`.
- Floor division with negative numbers rounds toward negative infinity.
- Exponentiation is right-associative.

> **Note**
>
> Understanding operator precedence helps you predict expression results correctly.

---

# 💻 Important Syntax

## Addition

```python
result = a + b
```

---

## Subtraction

```python
result = a - b
```

---

## Multiplication

```python
result = a * b
```

---

## Division

```python
result = a / b
```

---

## Floor Division

```python
result = a // b
```

---

## Modulus

```python
result = a % b
```

---

## Exponentiation

```python
result = a ** b
```

---

# ⭐ Most Important Facts

- Python has **7 arithmetic operators**.
- `/` always performs true division.
- `//` returns the mathematical floor of the quotient.
- `%` computes the remainder.
- `**` raises a number to a power.
- `^` is **not** the exponent operator.
- Parentheses improve readability and control evaluation order.
- Division or modulus by zero raises a `ZeroDivisionError`.
- Invalid arithmetic between incompatible types raises a `TypeError`.

Example

```python
print(8 / 2)
print(8 // 2)
```

Output

```text
4.0
4
```

---

# 🧠 Things to Remember

- `+` adds values.
- `-` subtracts values.
- `*` multiplies values.
- `/` always returns a floating-point result.
- `//` rounds down to the floor value.
- `%` finds the remainder.
- `**` calculates powers.
- Use parentheses to avoid ambiguity.
- Always validate user input before performing arithmetic.
- Check for division by zero before using `/`, `//`, or `%`.

> **Best Practice**
>
> Write arithmetic expressions that are easy to read by using descriptive variable names and parentheses where appropriate.

---

# ⚠️ Common Errors

## Confusing `/` and `//`

Incorrect expectation

```python
print(7 / 2)
```

Output

```text
3.5
```

Correct floor division

```python
print(7 // 2)
```

Output

```text
3
```

---

## Using `^` Instead of `**`

Incorrect

```python
print(2 ^ 3)
```

Output

```text
1
```

Correct

```python
print(2 ** 3)
```

Output

```text
8
```

---

## Forgetting Operator Precedence

```python
print(2 + 3 * 4)
```

Output

```text
14
```

Using parentheses

```python
print((2 + 3) * 4)
```

Output

```text
20
```

---

## Dividing by Zero

```python
print(10 / 0)
```

Output

```text
ZeroDivisionError
```

---

## Mixing Incompatible Data Types

```python
print(5 + "5")
```

Output

```text
TypeError
```

Correct

```python
print(5 + int("5"))
```

Output

```text
10
```

---

# 🔢 Operator Precedence Order

Python evaluates arithmetic expressions according to operator precedence.

| Priority | Operators | Description |
|----------|-----------|-------------|
| 1 (Highest) | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | Unary `+`, Unary `-` | Positive/Negative |
| 4 | `*`, `/`, `//`, `%` | Multiplication, Division, Floor Division, Modulus |
| 5 (Lowest) | `+`, `-` | Addition, Subtraction |

Example

```python
print(4 + 2 * 3)
```

Output

```text
10
```

Using parentheses

```python
print((4 + 2) * 3)
```

Output

```text
18
```

> **Tip**
>
> When in doubt, use parentheses to make expressions easier to read and avoid precedence-related mistakes.

---

# 🎯 Output Prediction Tips

Follow these steps when predicting the output of an arithmetic expression:

1. Evaluate expressions inside parentheses.
2. Evaluate exponentiation (`**`).
3. Evaluate unary `+` and `-`.
4. Evaluate `*`, `/`, `//`, and `%` from left to right.
5. Evaluate `+` and `-` from left to right.
6. Check the resulting data type (`int` or `float`).

### Example 1

```python
print(3 + 2 * 5)
```

Output

```text
13
```

### Example 2

```python
print((3 + 2) * 5)
```

Output

```text
25
```

### Example 3

```python
print(2 ** 3 ** 2)
```

Output

```text
512
```

---

# 💼 Interview Quick Facts

- Python has **7 arithmetic operators**.
- `/` performs true division.
- `//` performs floor division.
- `%` returns the remainder.
- `**` performs exponentiation.
- `^` is the bitwise XOR operator, **not** exponentiation.
- Exponentiation (`**`) is **right-associative**.
- `/` always returns a `float`.
- Mixing `int` and `float` typically produces a `float`.
- `bool` values participate in arithmetic (`True == 1`, `False == 0`).
- Division or modulus by zero raises a `ZeroDivisionError`.
- Invalid arithmetic between incompatible types raises a `TypeError`.

Example

```python
print(True + 5)
```

Output

```text
6
```

---

# 📝 Exam Quick Facts

Questions commonly asked in exams include:

- Define arithmetic operators.
- List all arithmetic operators.
- Differentiate `/` and `//`.
- Explain the modulus operator.
- Explain exponentiation.
- Predict the output of arithmetic expressions.
- Explain operator precedence.
- Explain floor division with negative numbers.
- Write programs to calculate:
  - Average
  - Area
  - Perimeter
  - Simple Interest
  - Temperature conversion
  - Square and cube
- Identify common arithmetic mistakes.

> **Exam Tip**
>
> Practice output-based questions regularly. They test both conceptual understanding and knowledge of operator precedence.

---

# 🧠 Memory Tricks

| Remember | Trick |
|----------|-------|
| `+` | Add values |
| `-` | Subtract values |
| `*` | Multiply values |
| `/` | True division → always returns a `float` |
| `//` | Floor division → rounds down |
| `%` | Modulus → remainder |
| `**` | Power |
| `()` | Highest precedence |
| `^` | XOR, **not** exponentiation |

### Easy Sequence

```text
Add
Subtract
Multiply
Divide
Floor Divide
Modulus
Power
```

Or simply remember:

```text
+  -  *  /  //  %  **
```

---

# ⏱️ 5-Minute Revision Sheet

## Arithmetic Operators

| Operator | Meaning |
|----------|---------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | True Division |
| `//` | Floor Division |
| `%` | Modulus |
| `**` | Exponentiation |

---

## Important Rules

- `/` → always returns a `float`
- `//` → rounds toward negative infinity
- `%` → returns the remainder
- `**` → calculates powers
- `^` → bitwise XOR
- Parentheses have the highest precedence
- Mixed `int` and `float` arithmetic usually returns a `float`

---

## Common Exceptions

| Exception | Cause |
|-----------|-------|
| `ZeroDivisionError` | Division, floor division, or modulus by zero |
| `TypeError` | Arithmetic between incompatible data types |

---

## Frequently Used Expressions

```python
average = total / count
```

```python
area = length * width
```

```python
perimeter = 2 * (length + width)
```

```python
square = number ** 2
```

```python
cube = number ** 3
```

```python
remainder = number % 2
```

```python
is_even = number % 2 == 0
```

---

# ✅ Last-Minute Checklist

Before your exam or interview, verify that you can:

- [ ] Name all seven arithmetic operators.
- [ ] Explain the difference between `/` and `//`.
- [ ] Explain how `%` works.
- [ ] Explain the purpose of `**`.
- [ ] State that `^` is the bitwise XOR operator.
- [ ] Predict outputs using operator precedence.
- [ ] Explain floor division with negative numbers.
- [ ] Recognize when Python returns `int` versus `float`.
- [ ] Handle `ZeroDivisionError`.
- [ ] Recognize `TypeError` caused by incompatible operand types.
- [ ] Solve basic arithmetic programming problems.
- [ ] Write clear, readable arithmetic expressions using parentheses where appropriate.

---

# 📌 Final Revision Summary

Remember these core facts:

- Arithmetic operators are fundamental to Python programming.
- There are **seven** arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, and `**`.
- `/` always performs true division and returns a `float`.
- `//` performs floor division, rounding toward negative infinity.
- `%` computes the remainder after division.
- `**` performs exponentiation and is right-associative.
- Parentheses take the highest precedence and improve readability.
- Use descriptive variable names and validate user input in practical programs.
- Understanding operator precedence is essential for predicting program output accurately.

> **Revision Tip**
>
> If you can explain each operator, predict expression outputs correctly, and write simple arithmetic programs without assistance, you are well prepared for most beginner-level Python exams and technical interviews.