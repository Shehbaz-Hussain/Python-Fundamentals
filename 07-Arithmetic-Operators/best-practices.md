# Best Practices

## Module

**07 – Arithmetic Operators**

---

# Introduction

Writing correct arithmetic expressions is only part of becoming a good Python programmer. Professional developers also focus on readability, maintainability, accuracy, and efficiency. The following best practices will help you write clean and reliable Python code when working with arithmetic operators.

---

# 1. Use Meaningful Variable Names

Choose variable names that clearly describe the values they store.

❌ Poor

```python
a = 1200
b = 5
c = a * b
```

✅ Better

```python
hourly_rate = 1200
hours_worked = 5

weekly_salary = hourly_rate * hours_worked
```

Meaningful names make programs easier to understand and maintain.

---

# 2. Follow Python Naming Conventions

Use **snake_case** for variable names.

✅ Good

```python
student_marks = 450
average_score = 90
```

❌ Avoid

```python
StudentMarks = 450
studentMarks = 450
```

---

# 3. Add Spaces Around Operators

Follow **PEP 8** formatting guidelines by placing one space around arithmetic operators.

❌ Less Readable

```python
total=price*quantity
```

✅ Recommended

```python
total = price * quantity
```

This improves readability without changing program behavior.

---

# 4. Use Parentheses to Improve Clarity

Even when Python evaluates an expression correctly, parentheses can make the intended calculation easier to understand.

❌ Less Clear

```python
final_price = price + tax * quantity
```

✅ Clearer

```python
final_price = price + (tax * quantity)
```

Use parentheses whenever they improve readability.

---

# 5. Store Intermediate Results

Avoid repeating the same calculation multiple times.

❌ Repeated Calculation

```python
print(length * width)
print((length * width) * 2)
```

✅ Better

```python
area = length * width

print(area)
print(area * 2)
```

This reduces repetition and simplifies future changes.

---

# 6. Convert User Input Before Calculations

The `input()` function always returns a string.

✅ Correct

```python
age = int(input("Enter your age: "))
```

or

```python
price = float(input("Enter price: "))
```

Always convert input to the appropriate numeric type before performing arithmetic.

---

# 7. Choose the Correct Numeric Type

Use the data type that best fits the problem.

Use `int` for:

- Counts
- Ages
- Quantities
- Indexes

Use `float` for:

- Prices
- Measurements
- Percentages
- Scientific values

Example

```python
price = 19.99
quantity = 3

total = price * quantity
```

---

# 8. Check Before Dividing

Division by zero causes a runtime error.

❌ Risky

```python
result = total / divisor
```

✅ Safe

```python
if divisor != 0:
    result = total / divisor
else:
    print("Cannot divide by zero.")
```

Always validate the denominator before using `/`, `//`, or `%`.

---

# 9. Understand Operator Behavior

Know the purpose of each arithmetic operator.

| Operator | Purpose |
|----------|---------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `//` | Floor Division |
| `%` | Modulus |
| `**` | Exponentiation |

Choosing the correct operator leads to more accurate programs.

---

# 10. Keep Expressions Simple

Break complex calculations into smaller steps.

❌ Difficult to Read

```python
result = (salary + bonus - tax) * months / employees
```

✅ Better

```python
annual_income = salary + bonus
taxable_income = annual_income - tax

result = taxable_income * months / employees
```

Smaller expressions are easier to read, debug, and maintain.

---

# 11. Use Constants for Fixed Values

Store values that do not change in variables with descriptive names.

Example

```python
PI = 3.14159

area = PI * radius ** 2
```

Another example

```python
TAX_RATE = 0.15

tax = subtotal * TAX_RATE
```

Using constants improves readability and simplifies updates.

---

# 12. Comment Complex Calculations

Simple expressions usually do not need comments, but formulas and business logic often benefit from brief explanations.

Example

```python
# Calculate simple interest
interest = (principal * rate * time) / 100
```

Avoid comments that merely repeat the code.

---

# 13. Test with Different Inputs

Verify your programs using a variety of values, including:

- Positive numbers
- Negative numbers
- Zero
- Decimal values
- Large values

Testing different scenarios helps uncover logic errors.

---

# 14. Verify Mathematical Formulas

Before implementing a calculation, confirm that the formula is correct.

Example

Rectangle Area

```python
area = length * width
```

Simple Interest

```python
interest = (principal * rate * time) / 100
```

Accurate formulas are essential for correct results.

---

# 15. Keep Output Clear and Informative

Use descriptive labels in your output.

❌ Poor

```python
print(total)
```

✅ Better

```python
print("Total Cost:", total)
```

Clear output makes programs easier to use and debug.

---

# 16. Write Reusable Calculations

If the same calculation appears in multiple places, consider placing it in a function.

Example

```python
def calculate_area(length, width):
    return length * width

area = calculate_area(8, 5)
```

Reusable code reduces duplication and improves maintainability.

---

# 17. Follow Operator Precedence Rules

Remember Python's order of evaluation:

1. Parentheses `()`
2. Exponentiation `**`
3. Multiplication `*`, Division `/`, Floor Division `//`, Modulus `%`
4. Addition `+`, Subtraction `-`

When in doubt, use parentheses to make the intended order explicit.

---

# 18. Write Code That Others Can Read

Readable code is easier to maintain than clever but confusing code.

Aim for:

- Meaningful variable names
- Consistent formatting
- Simple expressions
- Logical organization
- Clear output

Readability is a key characteristic of professional software.

---

# Best Practices Checklist

Before finishing a program, verify that you have:

- Used meaningful variable names.
- Followed Python naming conventions.
- Added spaces around operators.
- Used parentheses where appropriate.
- Converted user input correctly.
- Chosen the correct numeric data type.
- Checked for division by zero.
- Avoided repeated calculations.
- Verified mathematical formulas.
- Tested with multiple input values.
- Produced clear, labeled output.
- Written readable and maintainable code.

---

# Summary

Following these best practices will help you write arithmetic expressions that are accurate, readable, and maintainable. As programs become more complex, these habits become increasingly important and form the foundation of professional Python development.