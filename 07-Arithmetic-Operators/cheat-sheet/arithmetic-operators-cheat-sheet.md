# Python Arithmetic Operators Cheat Sheet

## Module

**07 – Arithmetic Operators**

---

# Quick Overview

Arithmetic operators are used to perform mathematical operations on numeric values such as integers and floating-point numbers.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 5` | `2.0` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

---

# Addition (`+`)

Adds two values.

```python
a = 10
b = 5

print(a + b)
```

**Output**

```text
15
```

---

# Subtraction (`-`)

Subtracts one value from another.

```python
a = 20
b = 8

print(a - b)
```

**Output**

```text
12
```

---

# Multiplication (`*`)

Multiplies two values.

```python
length = 8
width = 5

area = length * width

print(area)
```

**Output**

```text
40
```

---

# Division (`/`)

Always returns a floating-point number.

```python
print(9 / 2)
```

**Output**

```text
4.5
```

---

# Floor Division (`//`)

Returns the quotient without the fractional part.

```python
print(9 // 2)
```

**Output**

```text
4
```

---

# Modulus (`%`)

Returns the remainder after division.

```python
print(9 % 2)
```

**Output**

```text
1
```

---

# Exponentiation (`**`)

Raises a number to the power of another number.

```python
print(2 ** 5)
```

**Output**

```text
32
```

---

# Operator Precedence

Python evaluates arithmetic expressions according to the following order.

| Priority | Operator | Description |
|----------|----------|-------------|
| 1 | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `*` `/` `//` `%` | Multiplication, Division, Floor Division, Modulus |
| 4 | `+` `-` | Addition, Subtraction |

Example

```python
result = 10 + 4 * 3
print(result)
```

Output

```text
22
```

Explanation

```text
4 × 3 = 12

10 + 12 = 22
```

---

# Using Parentheses

Parentheses override the default precedence.

```python
result = (10 + 4) * 3

print(result)
```

Output

```text
42
```

---

# Arithmetic with Variables

```python
price = 250
quantity = 4

total = price * quantity

print(total)
```

Output

```text
1000
```

---

# Arithmetic with User Input

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(num1 + num2)
```

---

# Common Mathematical Formulas

## Rectangle Area

```python
area = length * width
```

---

## Rectangle Perimeter

```python
perimeter = 2 * (length + width)
```

---

## Circle Area

```python
pi = 3.14159

area = pi * radius ** 2
```

---

## Average

```python
average = total / count
```

---

## Percentage

```python
percentage = (obtained / total) * 100
```

---

## Temperature Conversion

```python
fahrenheit = (celsius * 9 / 5) + 32
```

---

## Simple Interest

```python
interest = (principal * rate * time) / 100
```

---

# Real-World Uses

Arithmetic operators are commonly used for:

- Financial calculations
- Billing systems
- Shopping carts
- Payroll software
- Scientific calculations
- Engineering applications
- Data analysis
- Artificial Intelligence
- Machine Learning
- Game development
- Inventory management
- Unit conversion programs

---

# Quick Comparison

| Expression | Result |
|------------|--------|
| `10 / 3` | `3.3333333333333335` |
| `10 // 3` | `3` |
| `10 % 3` | `1` |

---

# Important Notes

- `/` always returns a `float`.
- `//` removes the fractional part by rounding down toward negative infinity.
- `%` returns the remainder.
- `**` is used for powers instead of `^`.
- Parentheses improve readability and avoid precedence mistakes.
- Use meaningful variable names in arithmetic expressions.

---

# Common Mistakes

❌ Using `^` for exponentiation.

```python
2 ^ 3
```

✅ Correct

```python
2 ** 3
```

---

❌ Expecting integer output from `/`.

```python
10 / 2
```

Output

```text
5.0
```

---

❌ Forgetting parentheses.

```python
10 + 5 * 2
```

Result

```text
20
```

Not

```text
30
```

---

# Memory Tips

- `+` → Add
- `-` → Subtract
- `*` → Multiply
- `/` → Divide (returns float)
- `//` → Whole-number quotient
- `%` → Remainder
- `**` → Power

---

# Summary

- Python provides **seven arithmetic operators**.
- Arithmetic operators work with integers and floating-point numbers.
- Python follows a defined order of operations (operator precedence).
- Parentheses should be used to make expressions clear and predictable.
- Arithmetic operators are essential for solving mathematical and real-world programming problems.