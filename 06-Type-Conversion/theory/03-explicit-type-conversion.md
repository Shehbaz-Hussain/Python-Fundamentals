# Explicit Type Conversion

---

# Introduction

In many situations, Python cannot automatically convert one data type into another. In these cases, the programmer must perform the conversion manually.

This process is called **Explicit Type Conversion**.

It is also known as **Manual Type Conversion** or **Type Casting**.

Explicit type conversion is one of the most commonly used features in Python because user input is always received as a string.

---

# Definition

**Explicit Type Conversion** is the process of manually converting a value from one data type to another using Python's built-in conversion functions.

Unlike implicit conversion, the programmer decides when and how the conversion should happen.

---

# Why Do We Need Explicit Type Conversion?

Explicit type conversion is necessary when:

- Working with user input.
- Performing mathematical calculations.
- Converting numbers into text for display.
- Changing decimal numbers into whole numbers.
- Preparing data for processing.

Without explicit conversion, many programs would produce errors.

---

# Built-in Conversion Functions

Python provides several functions for explicit type conversion.

| Function | Converts To |
|----------|-------------|
| `int()` | Integer |
| `float()` | Floating-point number |
| `str()` | String |
| `bool()` | Boolean |

These functions are safe and commonly used in beginner Python programs.

---

# Converting a String to an Integer

Suppose a user enters their age.

```python
age = input("Enter your age: ")

print(type(age))
```

### User Input

```
21
```

### Output

```
<class 'str'>
```

Although the user entered a number, `input()` stores it as a string.

Convert it to an integer:

```python
age = int(input("Enter your age: "))

print(type(age))
```

### Output

```
<class 'int'>
```

Now you can perform arithmetic operations.

```python
age = int(input("Enter your age: "))

next_year = age + 1

print("Your age next year is:", next_year)
```

---

# Converting a String to a Float

Some values contain decimal points.

Example:

```python
height = float(input("Enter your height in meters: "))

print(height)
print(type(height))
```

### User Input

```
1.75
```

### Output

```
1.75
<class 'float'>
```

---

# Converting an Integer to a Float

```python
marks = 90

average = float(marks)

print(average)
print(type(average))
```

### Output

```
90.0
<class 'float'>
```

---

# Converting a Float to an Integer

```python
price = 199.95

whole_price = int(price)

print(whole_price)
```

### Output

```
199
```

### Important Note

`int()` **removes the decimal part**.

It does **not** round the number.

Examples:

| Original | After `int()` |
|----------|---------------|
| 9.8 | 9 |
| 15.99 | 15 |
| 100.2 | 100 |

---

# Converting a Number to a String

Sometimes numbers need to be displayed as part of a message.

```python
score = 95

message = "Your score is " + str(score)

print(message)
```

### Output

```
Your score is 95
```

Without `str()`, Python would produce a `TypeError`.

---

# Converting Values to Boolean

The `bool()` function converts values into either `True` or `False`.

Examples:

```python
print(bool(1))
print(bool(0))
print(bool("Python"))
print(bool(""))
```

### Output

```
True
False
True
False
```

### General Rules

| Value | Result |
|--------|--------|
| `0` | `False` |
| Non-zero number | `True` |
| Empty string `""` | `False` |
| Non-empty string | `True` |

---

# Multiple Conversions

You can perform more than one conversion in a program.

```python
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print(age)
print(height)

print(type(age))
print(type(height))
```

---

# Practical Example

```python
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("Total Bill:", total)
```

Example Input

```
Price: 50.5
Quantity: 3
```

Output

```
Total Bill: 151.5
```

---

# Common Conversion Errors

### Error 1

```python
number = int("3.5")
```

Result:

```
ValueError
```

Reason:

`"3.5"` is not a valid integer.

Correct:

```python
number = float("3.5")
```

---

### Error 2

```python
value = int("Hello")
```

Result:

```
ValueError
```

Reason:

The text `"Hello"` cannot be converted into an integer.

---

### Error 3

```python
age = input("Age: ")

print(age + 5)
```

Result:

```
TypeError
```

Correct:

```python
age = int(input("Age: "))

print(age + 5)
```

---

# Best Practices

- Convert user input immediately after reading it.
- Use `int()` for whole numbers.
- Use `float()` for decimal numbers.
- Use `str()` when combining text and numbers.
- Check data types with `type()` while learning.
- Use meaningful variable names.

---

# Memory Tip

Remember this sentence:

> **If Python does not convert a value automatically, use a conversion function such as `int()`, `float()`, `str()`, or `bool()`.**

---

# Key Points

- Explicit type conversion is performed manually.
- It is also called **type casting**.
- `input()` always returns a string.
- `int()` converts values to integers.
- `float()` converts values to floating-point numbers.
- `str()` converts values to strings.
- `bool()` converts values to Boolean values.
- Incorrect conversions can produce `ValueError` or `TypeError`.

---

# Summary

Explicit type conversion allows programmers to manually change the data type of a value using Python's built-in conversion functions. It is essential for handling user input, performing calculations, formatting output, and writing practical Python programs. Mastering explicit type conversion will help you avoid common errors and build reliable applications.