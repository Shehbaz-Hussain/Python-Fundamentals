# Python Arithmetic Operators – Interview Questions

## Module

**07 – Arithmetic Operators**

---

# Introduction

This document contains commonly asked interview questions related to Python arithmetic operators. The questions range from beginner to intermediate level and are designed to strengthen conceptual understanding and prepare you for technical interviews.

---

# Beginner Level Questions

## 1. What are arithmetic operators in Python?

**Answer**

Arithmetic operators are symbols used to perform mathematical operations on numeric values such as integers and floating-point numbers.

Python provides seven arithmetic operators:

| Operator | Name |
|----------|------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `//` | Floor Division |
| `%` | Modulus |
| `**` | Exponentiation |

---

## 2. Which arithmetic operator is used for addition?

**Answer**

The `+` operator is used to add two numbers.

```python
print(10 + 5)
```

**Output**

```text
15
```

---

## 3. What is the difference between `/` and `//`?

**Answer**

The `/` operator performs **true division** and always returns a floating-point (`float`) result.

The `//` operator performs **floor division**, returning the quotient rounded down toward negative infinity.

Example:

```python
print(9 / 2)
print(9 // 2)
```

**Output**

```text
4.5
4
```

---

## 4. What does the modulus operator (`%`) do?

**Answer**

The modulus operator returns the remainder after division.

```python
print(10 % 3)
```

**Output**

```text
1
```

---

## 5. Which operator is used for exponentiation?

**Answer**

Python uses the `**` operator.

```python
print(2 ** 4)
```

**Output**

```text
16
```

---

## 6. Does `/` always return a float?

**Answer**

Yes.

Even if the division produces a whole number, `/` returns a `float`.

```python
print(8 / 2)
```

**Output**

```text
4.0
```

---

## 7. What data types can arithmetic operators work with?

**Answer**

Arithmetic operators commonly work with:

- `int`
- `float`

Some operators can also work with other numeric types such as `complex`, depending on the operation.

---

## 8. What is an arithmetic expression?

**Answer**

An arithmetic expression is a combination of operands and arithmetic operators that evaluates to a value.

Example:

```python
(10 + 5) * 2
```

---

## 9. What is operator precedence?

**Answer**

Operator precedence determines the order in which Python evaluates operators in an expression.

General precedence:

1. Parentheses `()`
2. Exponentiation `**`
3. `*`, `/`, `//`, `%`
4. `+`, `-`

---

## 10. Why should parentheses be used?

**Answer**

Parentheses improve readability and allow you to control the order of evaluation.

Example:

```python
(10 + 5) * 2
```

---

# Intermediate Level Questions

## 11. What is the difference between modulus and floor division?

**Answer**

- `//` returns the integer quotient (rounded down).
- `%` returns the remainder.

Example:

```python
print(17 // 5)
print(17 % 5)
```

**Output**

```text
3
2
```

---

## 12. What happens when you divide by zero?

**Answer**

Python raises a `ZeroDivisionError`.

Example:

```python
10 / 0
```

---

## 13. Why is `2 ^ 3` not equal to 8?

**Answer**

Because `^` is the **bitwise XOR** operator, not the exponentiation operator.

Correct exponentiation:

```python
2 ** 3
```

---

## 14. What is the output?

```python
print(2 + 3 * 4)
```

**Answer**

```
14
```

Explanation:

```text
3 × 4 = 12

2 + 12 = 14
```

---

## 15. What is the output?

```python
print((2 + 3) * 4)
```

**Answer**

```
20
```

---

## 16. Explain floor division with a negative number.

**Answer**

Floor division rounds the result down toward negative infinity.

Example:

```python
print(-7 // 2)
```

**Output**

```text
-4
```

---

## 17. Explain the difference between operands and operators.

**Answer**

In the expression:

```python
10 + 5
```

- `10` and `5` are **operands**.
- `+` is the **operator**.

---

## 18. What is the output?

```python
print(5 + 2 ** 3)
```

**Answer**

```
13
```

Explanation:

```text
2 ** 3 = 8

5 + 8 = 13
```

---

## 19. What is the output?

```python
print((8 + 2) // 3)
```

**Answer**

```
3
```

---

## 20. Why is operator precedence important?

**Answer**

Without understanding operator precedence, programs may produce unexpected results.

Using parentheses makes expressions more predictable and easier to understand.

---

# Practical Coding Questions

### 21. Write a program to calculate the area of a rectangle.

---

### 22. Write a program to calculate the average of five numbers.

---

### 23. Write a simple calculator using arithmetic operators.

---

### 24. Convert Celsius to Fahrenheit.

---

### 25. Calculate the simple interest for given values of principal, rate, and time.

---

### 26. Write a program that uses floor division and modulus to convert seconds into hours, minutes, and seconds.

---

### 27. Find whether a number is even or odd using the modulus operator.

---

### 28. Calculate the area and circumference of a circle.

---

### 29. Write a billing program that calculates discount and final price.

---

### 30. Accept two numbers from the user and display the results of all arithmetic operators.

---

# Rapid-Fire Interview Questions

- How many arithmetic operators does Python provide?
- Which operator returns the remainder?
- Which operator performs exponentiation?
- What is the difference between `/` and `//`?
- Does `/` return an `int` or a `float`?
- What is operator precedence?
- Which operator has the highest precedence among arithmetic operators?
- Why are parentheses useful?
- What error occurs when dividing by zero?
- What is the difference between an operator and an operand?
- Is `^` the exponentiation operator in Python?
- Which operator is commonly used to determine if a number is even or odd?
- Can arithmetic operators be used with variables?
- What is an arithmetic expression?
- What is the result of `10 // 3`?
- What is the result of `10 % 3`?
- What is the result of `2 ** 5`?
- What data type does `/` return?
- What does `%` return?
- Why should meaningful variable names be used in arithmetic expressions?

---

# Tips for Interviews

- Understand the purpose of each arithmetic operator.
- Be able to explain operator precedence.
- Know the difference between `/`, `//`, and `%`.
- Remember that `/` always returns a `float`.
- Do not confuse `^` with `**`.
- Practice writing small arithmetic programs without referring to notes.
- Explain your reasoning clearly when solving coding problems.

---

# Summary

Arithmetic operators are among the first concepts evaluated in Python interviews because they form the foundation of programming logic. A strong understanding of operator behavior, precedence, mathematical expressions, and practical applications will prepare you for beginner and intermediate Python technical interviews.