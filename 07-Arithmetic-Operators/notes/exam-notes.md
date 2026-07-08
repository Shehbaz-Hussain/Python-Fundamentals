# `notes/exam-notes.md`

````markdown
# 📝 Arithmetic Operators Quick Revision

Arithmetic operators are used to perform mathematical calculations on numeric values in Python. They are one of the most commonly used operator categories and form the foundation for programming, data analysis, artificial intelligence, and software development.

---

# 📖 Definition

An **arithmetic operator** is a symbol that performs a mathematical operation on one or more operands (values or variables).

Example:

```python
a = 10
b = 3

print(a + b)
```

**Output**

```text
13
```

---

# 📋 Complete Operator Table

| Operator | Meaning | Example | Output |
|----------|---------|---------|--------|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 5` | `2.0` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus (Remainder) | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

---

# ⭐ Important Exam Points

- Arithmetic operators work with numeric data types.
- Python supports:
  - `int`
  - `float`
  - `complex` (limited arithmetic)
- Division (`/`) always returns a float.
- Floor division (`//`) rounds down toward negative infinity.
- Modulus (`%`) returns the remainder.
- Exponentiation (`**`) calculates powers.
- Operator precedence determines evaluation order.
- Parentheses can override precedence.

> **Exam Tip**
>
> Questions involving `/`, `//`, `%`, and `**` appear frequently in examinations.

---

# ❓ Frequently Asked Theory Questions

## 1. What are arithmetic operators?

Arithmetic operators perform mathematical calculations on numbers.

---

## 2. How many arithmetic operators are available in Python?

Seven:

- `+`
- `-`
- `*`
- `/`
- `//`
- `%`
- `**`

---

## 3. What is the difference between `/` and `//`?

| `/` | `//` |
|------|-------|
| Returns exact division | Returns floor value |
| Result is float | Result may be int or float |
| Does not discard decimal | Removes fractional part after flooring |

Example:

```python
print(7 / 2)
print(7 // 2)
```

Output:

```text
3.5
3
```

---

## 4. What does `%` do?

Returns the remainder after division.

```python
print(15 % 4)
```

Output

```text
3
```

---

## 5. What is exponentiation?

Exponentiation raises one number to the power of another.

```python
print(3 ** 4)
```

Output

```text
81
```

---

# 💻 Important Output-Based Questions

## Question 1

```python
print(8 + 2 * 5)
```

Answer

```text
18
```

---

## Question 2

```python
print((8 + 2) * 5)
```

Answer

```text
50
```

---

## Question 3

```python
print(10 // 3)
```

Answer

```text
3
```

---

## Question 4

```python
print(10 / 3)
```

Answer

```text
3.3333333333333335
```

---

## Question 5

```python
print(10 % 3)
```

Answer

```text
1
```

---

## Question 6

```python
print(2 ** 5)
```

Answer

```text
32
```

---

## Question 7

```python
print(5 + 4 * 3 ** 2)
```

Answer

```text
41
```

Explanation:

```text
3² = 9
4 × 9 = 36
36 + 5 = 41
```

---

## Question 8

```python
print(9 // 2)
```

Answer

```text
4
```

---

## Question 9

```python
print(9 % 2)
```

Answer

```text
1
```

---

## Question 10

```python
print(18 / 6 + 2)
```

Answer

```text
5.0
```

---

# 📐 Common Formula Examples

## Average

Formula

```text
Average = Sum / Count
```

Example

```python
total = 250
count = 5

average = total / count

print(average)
```

Output

```text
50.0
```

---

## Area of Rectangle

Formula

```text
Area = Length × Width
```

```python
length = 8
width = 4

area = length * width

print(area)
```

Output

```text
32
```

---

## Perimeter of Rectangle

Formula

```text
Perimeter = 2 × (Length + Width)
```

```python
length = 8
width = 4

perimeter = 2 * (length + width)

print(perimeter)
```

Output

```text
24
```

---

## Celsius to Fahrenheit

Formula

```text
F = (C × 9 / 5) + 32
```

```python
celsius = 30

fahrenheit = (celsius * 9 / 5) + 32

print(fahrenheit)
```

Output

```text
86.0
```

---

## Fahrenheit to Celsius

Formula

```text
C = (F - 32) × 5 / 9
```

```python
fahrenheit = 86

celsius = (fahrenheit - 32) * 5 / 9

print(celsius)
```

Output

```text
30.0
```

---

## Simple Interest

Formula

```text
SI = (P × R × T) / 100
```

```python
principal = 5000
rate = 8
time = 2

si = principal * rate * time / 100

print(si)
```

Output

```text
800.0
```

---

## Square

```python
number = 7

print(number ** 2)
```

Output

```text
49
```

---

## Cube

```python
number = 4

print(number ** 3)
```

Output

```text
64
```

---

## Power

```python
print(5 ** 4)
```

Output

```text
625
```

---

# ⚖️ Operator Precedence Summary

| Priority | Operators |
|-----------|-----------|
| Highest | `()` |
| | `**` |
| | Unary `+`, Unary `-` |
| | `*`, `/`, `//`, `%` |
| Lowest | `+`, `-` |

Example

```python
print(4 + 6 * 2)
```

Output

```text
16
```

---

# 🔢 Integer vs Float Results

| Expression | Result |
|------------|--------|
| `5 + 3` | `8` |
| `5 - 3` | `2` |
| `5 * 3` | `15` |
| `5 / 2` | `2.5` |
| `5 // 2` | `2` |
| `5 % 2` | `1` |
| `5 ** 2` | `25` |

---

# 📉 Floor Division Rules

- Uses `//`
- Returns the mathematical floor of the quotient.
- Floors toward negative infinity.
- Can return `int` or `float`, depending on operand types.

Examples

```python
print(17 // 5)
```

```text
3
```

```python
print(-17 // 5)
```

```text
-4
```

> **Note**
>
> Floor division with negative numbers often appears in exams.

---

# 🔄 Modulus Rules

- Returns the remainder.
- The result has the same sign as the divisor.

Examples

```python
print(10 % 3)
```

Output

```text
1
```

```python
print(-10 % 3)
```

Output

```text
2
```

---

# ⚡ Exponentiation Rules

- Uses `**`
- Right-associative

Example

```python
print(2 ** 3 ** 2)
```

Equivalent to

```python
2 ** (3 ** 2)
```

Output

```text
512
```

---

# ⚠️ Common Exam Mistakes

❌ Assuming `/` returns an integer.

```python
print(8 / 2)
```

Returns

```text
4.0
```

---

❌ Confusing `//` with `/`.

---

❌ Forgetting operator precedence.

---

❌ Ignoring parentheses.

---

❌ Misunderstanding floor division with negative numbers.

---

❌ Using `%` as percentage instead of remainder.

---

❌ Thinking `^` means exponent.

Python uses:

```python
**
```

not

```python
^
```

---

# 📄 One-Page Exam Revision

## Operators

| Operator | Meaning |
|----------|---------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `//` | Floor Division |
| `%` | Remainder |
| `**` | Power |

---

## Key Facts

- `/` always returns a float.
- `//` performs floor division.
- `%` returns the remainder.
- `**` calculates powers.
- Parentheses have the highest precedence.
- Exponentiation is right-associative.
- Mixed `int` and `float` arithmetic usually produces a `float`.
- Floor division with negative numbers rounds down, not toward zero.

> **Best Practice**
>
> Use parentheses to make expressions easier to read and avoid precedence-related mistakes.

---

## Last-Minute Memory Box

- `+` → Add
- `-` → Subtract
- `*` → Multiply
- `/` → Exact division (float)
- `//` → Floor division
- `%` → Remainder
- `**` → Power
- `()` → Highest precedence
- `^` is **not** the exponent operator in Python.
````
