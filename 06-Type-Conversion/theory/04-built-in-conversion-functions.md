# Built-in Conversion Functions

---

# Introduction

Python provides several built-in functions that allow you to convert values from one data type to another. These functions are simple to use and are essential for writing practical programs.

The most commonly used conversion functions are:

- `int()`
- `float()`
- `str()`
- `bool()`
- `type()`

As a beginner, you will use these functions frequently, especially when working with user input and arithmetic operations.

---

# 1. The `int()` Function

## Purpose

The `int()` function converts a value into an integer (whole number).

### Syntax

```python
int(value)
```

### Example 1: Convert a String to an Integer

```python
age = "20"

age = int(age)

print(age)
print(type(age))
```

### Output

```
20
<class 'int'>
```

---

### Example 2: Convert a Float to an Integer

```python
price = 49.99

price = int(price)

print(price)
```

### Output

```
49
```

**Important:** `int()` removes the decimal part. It does **not** round the number.

---

### Invalid Example

```python
number = int("3.5")
```

### Result

```
ValueError
```

Reason: `"3.5"` is not a valid integer.

---

# 2. The `float()` Function

## Purpose

The `float()` function converts a value into a floating-point number (decimal number).

### Syntax

```python
float(value)
```

### Example 1: Convert an Integer to a Float

```python
marks = 90

marks = float(marks)

print(marks)
print(type(marks))
```

### Output

```
90.0
<class 'float'>
```

---

### Example 2: Convert a String to a Float

```python
height = "1.75"

height = float(height)

print(height)
print(type(height))
```

### Output

```
1.75
<class 'float'>
```

---

### Invalid Example

```python
value = float("Python")
```

### Result

```
ValueError
```

Reason: `"Python"` is not a numeric value.

---

# 3. The `str()` Function

## Purpose

The `str()` function converts a value into a string.

### Syntax

```python
str(value)
```

### Example 1: Convert an Integer to a String

```python
score = 95

score = str(score)

print(score)
print(type(score))
```

### Output

```
95
<class 'str'>
```

---

### Example 2: Combine Text and Numbers

```python
age = 18

message = "Age: " + str(age)

print(message)
```

### Output

```
Age: 18
```

Without `str()`, Python would raise a `TypeError`.

---

# 4. The `bool()` Function

## Purpose

The `bool()` function converts a value into either `True` or `False`.

### Syntax

```python
bool(value)
```

### Example 1

```python
print(bool(1))
print(bool(0))
```

### Output

```
True
False
```

---

### Example 2

```python
print(bool("Python"))
print(bool(""))
```

### Output

```
True
False
```

---

### Boolean Conversion Rules

| Value | Result |
|--------|--------|
| `0` | `False` |
| Any non-zero number | `True` |
| `""` (empty string) | `False` |
| Any non-empty string | `True` |

---

# 5. The `type()` Function

## Purpose

The `type()` function returns the data type of a value or variable.

It is very useful while learning Python because it helps you verify the type of your data.

### Syntax

```python
type(value)
```

### Example

```python
number = 25
price = 10.5
name = "Ali"
is_student = True

print(type(number))
print(type(price))
print(type(name))
print(type(is_student))
```

### Output

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

---

# Comparison of Conversion Functions

| Function | Converts To | Example |
|----------|-------------|---------|
| `int()` | Integer | `int("25")` → `25` |
| `float()` | Float | `float("2.5")` → `2.5` |
| `str()` | String | `str(100)` → `"100"` |
| `bool()` | Boolean | `bool(0)` → `False` |
| `type()` | Data type information | `type(5)` → `<class 'int'>` |

---

# Practical Example

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

print("Name:", name)
print("Age:", age)
print("Height:", height)

print(type(name))
print(type(age))
print(type(height))
```

### Sample Input

```
Ali
20
1.72
```

### Output

```
Name: Ali
Age: 20
Height: 1.72
<class 'str'>
<class 'int'>
<class 'float'>
```

---

# Common Mistakes

## Mistake 1

```python
number = int("25.5")
```

Result:

```
ValueError
```

Correct:

```python
number = float("25.5")
```

---

## Mistake 2

```python
print("Age: " + 20)
```

Result:

```
TypeError
```

Correct:

```python
print("Age: " + str(20))
```

---

## Mistake 3

Assuming `input()` returns an integer.

```python
number = input("Enter a number: ")
```

The value stored is a **string**.

Convert it before performing calculations:

```python
number = int(input("Enter a number: "))
```

---

# Best Practices

- Use `int()` for whole numbers.
- Use `float()` for decimal numbers.
- Use `str()` when combining text and numbers.
- Use `bool()` only when you need Boolean values.
- Use `type()` to check your variables while practicing.
- Convert user input immediately after reading it.

---

# Memory Tip

Remember the following:

- **`int()` → Whole numbers**
- **`float()` → Decimal numbers**
- **`str()` → Text**
- **`bool()` → True or False**
- **`type()` → Check the data type**

---

# Key Points

- Python provides built-in functions for type conversion.
- `int()`, `float()`, `str()`, and `bool()` convert values into different data types.
- `type()` displays the data type of a value.
- These functions are widely used in real-world Python programs.
- Correct type conversion helps prevent errors and ensures your programs behave as expected.

---

# Summary

Python's built-in conversion functions make it easy to work with different data types. By understanding when and how to use `int()`, `float()`, `str()`, `bool()`, and `type()`, you can correctly process user input, perform calculations, display information, and write reliable Python programs.