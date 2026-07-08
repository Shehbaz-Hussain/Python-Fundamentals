# Quiz Answers

This document contains the complete solutions for the Module Quiz and the Arithmetic Operators MCQ Assessment.

---

# Part A Answers

## 1. What is an arithmetic operator in Python? Give three examples.

**Answer:**

An arithmetic operator is a symbol used to perform mathematical calculations on numeric values.

Examples include:

- `+` (Addition)
- `-` (Subtraction)
- `*` (Multiplication)

Other arithmetic operators are `/`, `//`, `%`, and `**`.

---

## 2. Explain the difference between the `/` operator and the `//` operator.

**Answer:**

| Operator | Description | Example | Result |
|-----------|-------------|---------|--------|
| `/` | Performs floating-point division | `7 / 2` | `3.5` |
| `//` | Performs floor division | `7 // 2` | `3` |

The `/` operator always returns a floating-point value, whereas `//` returns the quotient after removing the fractional part.

---

## 3. What does the modulus (`%`) operator return?

**Answer:**

The modulus operator returns the **remainder** after division.

Example:

```python
10 % 3
```

Output:

```text
1
```

A practical use case is determining whether a number is even or odd.

```python
number % 2
```

If the result is `0`, the number is even.

---

## 4. What is the purpose of the exponentiation (`**`) operator?

**Answer:**

The exponentiation operator raises one number to the power of another.

Example:

```python
3 ** 4
```

Calculation:

```text
3 × 3 × 3 × 3 = 81
```

Output:

```text
81
```

---

## 5. What will be the data type of the result produced by the `/` operator when dividing two integers?

**Answer:**

The result will be a **float**.

Example:

```python
8 / 2
```

Output:

```python
4.0
```

Even though the mathematical result is a whole number, Python returns a floating-point value.

---

## 6. What is operator precedence?

**Answer:**

Operator precedence is the order in which Python evaluates operators in an expression.

For arithmetic operators, a simplified order is:

1. Parentheses `()`
2. Exponentiation `**`
3. Multiplication `*`, Division `/`, Floor Division `//`, Modulus `%`
4. Addition `+`, Subtraction `-`

Understanding precedence helps avoid unexpected results.

---

## 7. How can parentheses change the result of an arithmetic expression?

**Answer:**

Parentheses force Python to evaluate part of an expression first.

Example:

Without parentheses:

```python
5 + 3 * 2
```

Output:

```text
11
```

With parentheses:

```python
(5 + 3) * 2
```

Output:

```text
16
```

---

## 8. Differentiate between integer division and floating-point division.

**Answer:**

| Integer (Floor) Division | Floating-Point Division |
|---------------------------|--------------------------|
| Uses `//` | Uses `/` |
| Removes the fractional part | Preserves the fractional part |
| Usually returns an integer (or a float if operands are floats) | Always returns a float |

Example:

```python
9 // 2
```

Output:

```text
4
```

```python
9 / 2
```

Output:

```text
4.5
```

---

## 9. Predict whether each expression returns an integer or a floating-point number.

| Expression | Result Type |
|------------|-------------|
| `20 // 4` | Integer |
| `20 / 4` | Float |
| `5 ** 2` | Integer |
| `7 % 3` | Integer |

---

## 10. A student wants to calculate the total cost of purchasing multiple items with tax. Which arithmetic operators would most likely be required?

**Answer:**

Possible operators include:

- `*` for calculating item totals.
- `+` for adding multiple prices.
- `/` for calculating percentages.
- `-` if discounts are applied.

Example:

```python
subtotal = price * quantity
tax = subtotal * tax_rate / 100
total = subtotal + tax
```

---

# Part B Outputs

## 1.

```python
print(12 + 8)
```

**Output**

```text
20
```

**Explanation**

Python performs addition.

---

## 2.

```python
print(25 - 9)
```

**Output**

```text
16
```

**Explanation**

Subtract 9 from 25.

---

## 3.

```python
print(7 * 6)
```

**Output**

```text
42
```

**Explanation**

Python multiplies the two integers.

---

## 4.

```python
print(15 / 4)
```

**Output**

```text
3.75
```

**Explanation**

The `/` operator performs floating-point division.

---

## 5.

```python
print(15 // 4)
```

**Output**

```text
3
```

**Explanation**

The `//` operator removes the fractional part of the quotient.

---

## 6.

```python
print(15 % 4)
```

**Output**

```text
3
```

**Explanation**

15 divided by 4 gives a quotient of 3 with a remainder of 3.

---

## 7.

```python
print(3 ** 4)
```

**Output**

```text
81
```

**Explanation**

Exponentiation is evaluated as:

```text
3 × 3 × 3 × 3 = 81
```

---

## 8.

```python
print(5 + 3 * 2)
```

**Output**

```text
11
```

**Step-by-step**

```text
3 * 2 = 6
5 + 6 = 11
```

Multiplication has higher precedence than addition.

---

## 9.

```python
print((5 + 3) * 2)
```

**Output**

```text
16
```

**Step-by-step**

```text
5 + 3 = 8
8 * 2 = 16
```

Parentheses are evaluated first.

---

## 10.

```python
result = 18 + 6 / 3 * 2 - 4
print(result)
```

**Output**

```text
18.0
```

**Step-by-step**

```text
6 / 3 = 2.0
2.0 * 2 = 4.0
18 + 4.0 = 22.0
22.0 - 4 = 18.0
```

The expression follows Python's operator precedence rules.

---

# Part C Sample Solutions

The following solutions demonstrate one correct approach for each programming task. In Python, many problems can be solved in multiple valid ways. The provided solutions emphasize readability and beginner-friendly coding practices.

---

## 1. Rectangle Area

### Sample Solution

```python
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print("Area:", area)
```

### Explanation

1. Read the length and width from the user.
2. Multiply them using the `*` operator.
3. Store the result in `area`.
4. Display the calculated area.

### Alternative Approach

The calculation can also be written directly inside `print()`:

```python
print("Area:", length * width)
```

---

## 2. Average Calculator

### Sample Solution

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average:", average)
```

### Explanation

- Add all three numbers.
- Divide the total by 3.
- Store and display the result.

### Alternative Approach

```python
numbers = [num1, num2, num3]
print(sum(numbers) / len(numbers))
```

---

## 3. Unit Conversion

### Sample Solution

```python
kilometers = float(input("Enter distance in kilometers: "))

meters = kilometers * 1000

print("Meters:", meters)
```

### Explanation

Since **1 kilometer = 1000 meters**, multiply the input value by `1000`.

### Alternative Approach

```python
print(kilometers * 1000)
```

---

## 4. Simple Calculator

### Sample Solution

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division by zero is not allowed.")
```

### Explanation

The program performs four arithmetic operations on two user-provided numbers. Before division, it checks whether the second number is zero to avoid a runtime error.

### Alternative Approach

Store each result in a separate variable before printing.

---

## 5. Temperature Difference

### Sample Solution

```python
temp1 = float(input("Enter first temperature: "))
temp2 = float(input("Enter second temperature: "))

difference = temp1 - temp2

print("Temperature Difference:", difference)
```

### Explanation

Subtract the second temperature from the first.

### Alternative Approach

To always display a positive difference:

```python
difference = abs(temp1 - temp2)
```

---

## 6. Discount Calculator

### Sample Solution

```python
price = float(input("Enter original price: "))
discount_percent = float(input("Enter discount percentage: "))

discount = price * discount_percent / 100
final_price = price - discount

print("Discount:", discount)
print("Final Price:", final_price)
```

### Explanation

1. Calculate the discount amount.
2. Subtract it from the original price.
3. Display both values.

### Alternative Approach

```python
final_price = price * (1 - discount_percent / 100)
```

---

## 7. Remainder Finder

### Sample Solution

```python
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

remainder = num1 % num2

print("Remainder:", remainder)
```

### Explanation

The modulus operator `%` returns the remainder after division.

### Alternative Approach

Add validation to ensure `num2` is not zero before performing the operation.

---

## 8. Power Calculator

### Sample Solution

```python
base = float(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = base ** exponent

print("Result:", result)
```

### Explanation

The exponentiation operator `**` raises the base to the specified exponent.

Example:

```text
2 ** 5 = 32
```

### Alternative Approach

For advanced mathematical operations, the `math` module also provides functions that can be useful in other contexts.

---

## 9. Total Monthly Salary

### Sample Solution

```python
salary = float(input("Enter monthly salary: "))
bonus = float(input("Enter monthly bonus: "))

total = salary + bonus

print("Total Earnings:", total)
```

### Explanation

The total earnings are calculated by adding the monthly salary and bonus.

### Alternative Approach

Additional allowances or deductions can be included if required.

---

## 10. Expression Evaluation

Given:

```python
a = 12
b = 5
c = 3
```

### Sample Solution

```python
a = 12
b = 5
c = 3

result = (a + b) * c - a // b

print(result)
```

### Output

```text
49
```

### Step-by-Step Evaluation

```text
a + b = 17
17 * 3 = 51
12 // 5 = 2
51 - 2 = 49
```

### Explanation

- Parentheses are evaluated first.
- Multiplication is performed next.
- Floor division computes the integer quotient.
- Finally, subtraction produces the result.

### Alternative Approach

The calculation may also be written directly inside `print()`:

```python
print((a + b) * c - a // b)
```

---

# Part D Debugging Solutions

Each program below contains one or more errors. The corrected solution and explanation are provided.

---

## 1.

### Original Code

```python
number = 25

print(number %)
```

### Bug

The modulus operator (`%`) requires **two operands**. The expression is incomplete, resulting in a `SyntaxError`.

### Corrected Code

```python
number = 25

print(number % 4)
```

### Explanation

The `%` operator returns the remainder after division.

```text
25 ÷ 4 = 6 remainder 1
```

Output:

```text
1
```

---

## 2.

### Original Code

```python
length = 8
width = 5

area = length width

print(area)
```

### Bug

Python requires an arithmetic operator between `length` and `width`. Without one, the code produces a `SyntaxError`.

### Corrected Code

```python
length = 8
width = 5

area = length * width

print(area)
```

### Explanation

The area of a rectangle is calculated using multiplication.

Output:

```text
40
```

---

## 3.

### Original Code

```python
base = 2
power = 5

print(base ^ power)
```

### Bug

The `^` operator is **not** the exponentiation operator in Python. It performs a **bitwise XOR** operation.

### Corrected Code

```python
base = 2
power = 5

print(base ** power)
```

### Explanation

Use `**` to raise a number to a power.

Output:

```text
32
```

---

## 4.

### Original Code

```python
num1 = 20
num2 = 0

print(num1 / num2)
```

### Bug

Division by zero is not allowed and raises a `ZeroDivisionError`.

### Corrected Code

```python
num1 = 20
num2 = 0

if num2 != 0:
    print(num1 / num2)
else:
    print("Division by zero is not allowed.")
```

### Explanation

Always validate the divisor before performing division.

---

## 5.

### Original Code

```python
value = 18

result = value + * 5

print(result)
```

### Bug

The expression contains an invalid operator sequence (`+ *`), which causes a `SyntaxError`.

### Corrected Code

```python
value = 18

result = value + 5

print(result)
```

### Explanation

Every arithmetic expression must follow valid Python syntax.

Output:

```text
23
```

---

# MCQ Answer Key

| Question | Answer | Explanation |
|----------|:------:|-------------|
| 1 | A | `+` is the addition operator. |
| 2 | C | `-` performs subtraction. |
| 3 | B | `*` is the multiplication operator. |
| 4 | C | `/` performs floating-point division. |
| 5 | B | `%` returns the remainder after division. |
| 6 | B | `**` raises a number to a power. |
| 7 | B | `9 + 6 = 15`. |
| 8 | A | `20 - 8 = 12`. |
| 9 | B | `5 × 4 = 20`. |
| 10 | B | `12 / 3` returns `4.0` because `/` always produces a float. |
| 11 | C | `10 ** 3` means 10 raised to the power of 3. |
| 12 | B | The modulus operator returns the remainder. |
| 13 | B | `//` performs floor division. |
| 14 | A | `2 ** 4 = 16`. |
| 15 | C | `/` always returns a floating-point result. |
| 16 | A | `17 // 5 = 3`. |
| 17 | A | `17 % 5 = 2`. |
| 18 | B | Multiplication first: `3 × 4 = 12`; `2 + 12 = 14`. |
| 19 | B | Parentheses first: `(2 + 3) × 4 = 20`. |
| 20 | D | `*`, `%`, and `**` all have higher precedence than `+`. |
| 21 | B | `25 / 5 = 5.0`; `5.0 + 2 = 7.0`. |
| 22 | A | `8 % 3 = 2`. |
| 23 | B | `4 ** 2 = 16`; `16 + 1 = 17`. |
| 24 | B | Multiplication is evaluated before addition. |
| 25 | A | `9 // 2 = 4`. |
| 26 | B | Parentheses preserve the intended order of operations. |
| 27 | B | Subtraction removes the discount from the original price. |
| 28 | A | The average is the sum divided by the number of values. |
| 29 | B | `4 ** 2 = 16`; `16 + 3 = 19`. |
| 30 | C | `/` performs floating-point division. |
| 31 | B | `4 × 3 = 12`; `20 - 12 + 2 = 10`. |
| 32 | B | `18 // 5 = 3`; `18 % 5 = 3`; total = `6`. |
| 33 | B | Exponentiation is right-associative: `2 ** (3 ** 2) = 2 ** 9 = 512`. |
| 34 | A | `(9 + 3) = 12`; `12 // 5 = 2`. |
| 35 | B | Rectangle area = length × width. |
| 36 | B | Floor division counts only completely filled boxes. |
| 37 | B | `% 2` determines whether a number is even or odd. |
| 38 | A | `(5 + 7) = 12`; `2 ** 2 = 4`; `12 × 4 = 48`. |
| 39 | B | `50 // 6 = 8`; `50 % 6 = 2`; total = `10`. |
| 40 | A | `P * (1 + r) ** n` correctly implements the compound interest formula. |

---

# Summary

After completing this module, you should be able to:

- Use all Python arithmetic operators correctly.
- Distinguish between floating-point division and floor division.
- Apply the modulus operator to solve practical problems.
- Use exponentiation to calculate powers.
- Predict the output of arithmetic expressions using operator precedence.
- Write Python programs that perform real-world calculations.
- Identify and correct common arithmetic-related programming errors.
- Evaluate expressions accurately and confidently using Python 3.x arithmetic operators.