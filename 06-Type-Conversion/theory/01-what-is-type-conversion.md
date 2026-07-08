# What is Type Conversion?

---

# Introduction

In Python, every value has a **data type**.

For example:

```python
10          # Integer (int)
3.14        # Float (float)
"Python"    # String (str)
True        # Boolean (bool)
```

Sometimes, you need to change one data type into another. This process is called **type conversion**.

Type conversion is one of the most important concepts in Python because different operations require different data types.

---

# Definition

**Type conversion** is the process of changing a value from one data type to another.

Python supports two kinds of type conversion:

1. **Implicit Type Conversion** (Automatic)
2. **Explicit Type Conversion** (Manual)

---

# Why is Type Conversion Important?

Type conversion allows Python programs to:

- Perform mathematical calculations
- Process user input correctly
- Combine different data types
- Store data in the required format
- Avoid type-related errors

Without type conversion, many Python programs would not work correctly.

---

# Real-World Example

Imagine a user enters their age.

```python
age = input("Enter your age: ")
```

If the user types:

```
20
```

The value is stored as:

```python
"20"
```

This is a **string**, not a number.

If you try:

```python
print(age + 5)
```

Python will produce an error because it cannot add a string and an integer.

The correct approach is:

```python
age = int(input("Enter your age: "))
print(age + 5)
```

Output:

```
25
```

Here, `int()` converts the string `"20"` into the integer `20`.

---

# Understanding Data Types

Before converting data, you should know the common Python data types.

| Data Type | Example | Description |
|-----------|---------|-------------|
| int | 25 | Whole numbers |
| float | 3.5 | Decimal numbers |
| str | "Hello" | Text |
| bool | True | True or False |

---

# Checking the Type of a Value

Python provides the `type()` function to determine a value's data type.

Example:

```python
number = 50

print(type(number))
```

Output:

```
<class 'int'>
```

Another example:

```python
name = "Ali"

print(type(name))
```

Output:

```
<class 'str'>
```

---

# Example: Integer to Float

```python
number = 10

decimal_number = float(number)

print(decimal_number)
print(type(decimal_number))
```

Output:

```
10.0
<class 'float'>
```

---

# Example: Float to Integer

```python
price = 99.99

whole_number = int(price)

print(whole_number)
```

Output:

```
99
```

**Note:** `int()` removes the decimal part; it does **not** round the value.

---

# Example: Number to String

```python
score = 95

text = str(score)

print(text)
print(type(text))
```

Output:

```
95
<class 'str'>
```

---

# Everyday Situations Where Type Conversion is Used

Type conversion is common in many applications, including:

- Student marks calculators
- Age calculators
- Shopping bill systems
- BMI calculators
- Banking software
- Salary calculators
- Online forms
- AI data preprocessing
- Data analysis programs

---

# Implicit vs Explicit Type Conversion

| Implicit Conversion | Explicit Conversion |
|---------------------|---------------------|
| Done automatically by Python | Done by the programmer |
| No conversion function is used | Uses functions like `int()` or `float()` |
| Usually occurs in numeric expressions | Used whenever manual conversion is needed |

Examples of both methods are covered in the next theory files.

---

# Common Beginner Mistakes

### Mistake 1

Trying to add a string and an integer:

```python
age = "20"

print(age + 5)
```

Result:

```
TypeError
```

Correct:

```python
age = int(age)

print(age + 5)
```

---

### Mistake 2

Assuming `input()` returns a number.

```python
number = input("Enter a number: ")
```

The value stored is always a **string**.

Convert it when numerical calculations are required:

```python
number = int(input("Enter a number: "))
```

---

# Memory Tip

Remember this simple rule:

> **Python stores values with data types. If an operation requires a different type, convert the value before using it.**

---

# Key Points

- Every value in Python has a data type.
- Type conversion changes one data type into another.
- Python supports implicit and explicit type conversion.
- `input()` always returns a string.
- `type()` helps identify a value's data type.
- Type conversion is essential for mathematical calculations and user input.

---

# Summary

Type conversion is the process of changing a value from one data type to another. It helps Python perform calculations, process user input, and work with different kinds of data correctly.

Mastering type conversion is an essential skill because it is used in almost every real-world Python program.