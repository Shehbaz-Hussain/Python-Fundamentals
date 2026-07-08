# Common Mistakes

## Module

**07 – Arithmetic Operators**

---

# Introduction

Beginners often make similar mistakes when working with arithmetic operators. Understanding these common errors will help you write more accurate Python programs and debug problems more efficiently.

---

# 1. Using `^` Instead of `**` for Exponentiation

One of the most common mistakes is assuming that `^` means "power."

❌ Incorrect

```python
result = 2 ^ 3
print(result)
```

Output

```text
1
```

Why?

In Python, `^` is the **bitwise XOR operator**, **not** the exponentiation operator.

✅ Correct

```python
result = 2 ** 3
print(result)
```

Output

```text
8
```

---

# 2. Expecting Integer Division from `/`

Many beginners expect `/` to return an integer.

❌ Incorrect Expectation

```python
print(10 / 2)
```

Expected

```text
5
```

Actual Output

```text
5.0
```

Explanation

The `/` operator **always returns a `float`**, even when the result is a whole number.

✅ Use floor division if you need an integer quotient.

```python
print(10 // 2)
```

Output

```text
5
```

---

# 3. Confusing `/` and `//`

These operators perform different operations.

```python
print(9 / 2)
```

Output

```text
4.5
```

```python
print(9 // 2)
```

Output

```text
4
```

Remember:

- `/` → Exact division
- `//` → Floor division

---

# 4. Forgetting Operator Precedence

Python evaluates multiplication before addition.

❌ Incorrect Assumption

```python
result = 10 + 5 * 2
print(result)
```

Incorrect Expected Result

```text
30
```

Actual Output

```text
20
```

Explanation

Python evaluates:

```text
5 × 2 = 10

10 + 10 = 20
```

✅ Use parentheses when needed.

```python
result = (10 + 5) * 2
print(result)
```

Output

```text
30
```

---

# 5. Dividing by Zero

Division by zero is not allowed.

❌ Incorrect

```python
print(10 / 0)
```

Output

```text
ZeroDivisionError
```

The same error occurs with:

```python
10 // 0
10 % 0
```

✅ Check the denominator before dividing.

```python
if divisor != 0:
    print(dividend / divisor)
else:
    print("Cannot divide by zero.")
```

---

# 6. Forgetting to Convert User Input

The `input()` function returns a string.

❌ Incorrect

```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print(num1 + num2)
```

Input

```text
10
20
```

Output

```text
1020
```

Explanation

The strings are concatenated instead of added.

✅ Correct

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)
```

Output

```text
30
```

---

# 7. Using the Wrong Data Type

Using integers when decimal values are required can produce incorrect results.

Example

```python
price = 19.99
quantity = 3

total = price * quantity
```

Using `float` preserves decimal precision.

---

# 8. Ignoring Negative Numbers in Floor Division

Some learners think floor division simply removes the decimal part.

❌ Incorrect Assumption

```python
-7 // 2
```

Incorrect Expected Result

```text
-3
```

Actual Output

```text
-4
```

Explanation

The `//` operator rounds **down toward negative infinity**, not toward zero.

---

# 9. Misunderstanding the Modulus Operator

Some beginners think `%` gives the quotient.

❌ Incorrect

```python
10 % 3
```

Incorrect Expected Result

```text
3
```

Actual Output

```text
1
```

Explanation

The modulus operator returns the **remainder**, not the quotient.

---

# 10. Writing Unclear Arithmetic Expressions

Complex expressions without parentheses are difficult to read.

❌ Less Readable

```python
result = a + b * c - d / e + f
```

✅ Better

```python
result = a + (b * c) - (d / e) + f
```

Adding parentheses improves readability, even when they are not strictly required.

---

# 11. Repeating the Same Calculation

Avoid calculating the same expression multiple times.

❌ Inefficient

```python
print(length * width)
print(length * width + 20)
```

✅ Better

```python
area = length * width

print(area)
print(area + 20)
```

Store intermediate results in variables when they are reused.

---

# 12. Using Meaningless Variable Names

Poor variable names reduce code readability.

❌ Poor

```python
a = 250
b = 4
c = a * b
```

✅ Better

```python
price = 250
quantity = 4
total_cost = price * quantity
```

---

# 13. Forgetting Spaces Around Operators

Although Python accepts this syntax:

```python
total=price*quantity
```

PEP 8 recommends adding spaces around operators.

✅ Preferred

```python
total = price * quantity
```

This improves readability and maintainability.

---

# 14. Assuming All Arithmetic Results Are Integers

Arithmetic expressions can produce floating-point values.

Example

```python
average = 17 / 2
print(average)
```

Output

```text
8.5
```

Always consider the resulting data type.

---

# 15. Not Testing Edge Cases

Programs should be tested with a variety of inputs.

Examples:

- Zero
- Negative numbers
- Large numbers
- Decimal values
- Equal values

Testing different cases helps identify hidden bugs.

---

# Best Practices to Avoid Mistakes

- Use `**` for exponentiation.
- Understand the difference between `/` and `//`.
- Remember that `%` returns the remainder.
- Use parentheses to clarify complex expressions.
- Convert user input to the correct numeric type.
- Check for division by zero.
- Use descriptive variable names.
- Follow Python's operator precedence rules.
- Write clean, readable expressions.
- Test your code with different input values.

---

# Summary

Most arithmetic-related errors are caused by misunderstanding operator behavior, data types, or evaluation order. By understanding these common mistakes and following Python best practices, you can write more accurate, reliable, and maintainable programs.