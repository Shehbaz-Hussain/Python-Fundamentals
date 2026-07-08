# Revision Notes: Type Conversion in Python

## Module Information

**Module:** 06 – Type Conversion

These revision notes provide a quick summary of the most important concepts from this module. They are ideal for last-minute exam preparation and interview revision.

---

# Definition

**Type conversion** is the process of changing a value from one data type to another.

Example:

```python
age = int("20")
```

---

# Types of Type Conversion

## 1. Implicit Type Conversion

- Performed automatically by Python.
- Usually occurs during arithmetic operations.
- No conversion function is required.

Example:

```python
result = 5 + 2.5

print(result)
```

Output:

```
7.5
```

---

## 2. Explicit Type Conversion

- Performed manually by the programmer.
- Uses built-in conversion functions.

Example:

```python
number = float("15")
```

---

# Built-in Conversion Functions

## int()

Converts a compatible value into an integer.

Example:

```python
int("50")
```

Result:

```
50
```

---

## float()

Converts a compatible value into a floating-point number.

Example:

```python
float("3.14")
```

Result:

```
3.14
```

---

## str()

Converts a value into a string.

Example:

```python
str(100)
```

Result:

```
"100"
```

---

## bool()

Converts a value into a Boolean.

Examples:

```python
bool(0)
```

Output:

```
False
```

```python
bool(1)
```

Output:

```
True
```

```python
bool("")
```

Output:

```
False
```

```python
bool("Python")
```

Output:

```
True
```

---

## type()

Displays the data type of a value or variable.

Example:

```python
score = 95

print(type(score))
```

Output:

```
<class 'int'>
```

---

# Key Facts

- `input()` always returns a string.
- Use `int()` for whole numbers.
- Use `float()` for decimal values.
- Use `str()` to convert numbers into text.
- Use `bool()` to convert values into `True` or `False`.
- Use `type()` to check a variable's data type.

---

# Quick Comparison Table

| Function | Purpose | Example |
|----------|---------|---------|
| `int()` | Convert to integer | `int("25")` |
| `float()` | Convert to float | `float("2.5")` |
| `str()` | Convert to string | `str(50)` |
| `bool()` | Convert to Boolean | `bool(1)` |
| `type()` | Display data type | `type(10)` |

---

# Common Mistakes

❌ Forgetting to convert user input before calculations.

```python
age = input("Age: ")
```

✔ Correct:

```python
age = int(input("Age: "))
```

---

❌ Using `int()` with decimal strings.

```python
int("10.5")
```

✔ Correct:

```python
float("10.5")
```

---

❌ Assuming `int()` rounds numbers.

```python
int(9.9)
```

Output:

```
9
```

The decimal part is removed; it is **not** rounded.

---

# Memory Tricks

- **int** → Integer → Whole numbers
- **float** → Decimal numbers
- **str** → Text
- **bool** → True or False
- **type()** → Shows the data type

---

# Last-Minute Exam Checklist

- ✅ Define type conversion.
- ✅ Explain implicit conversion.
- ✅ Explain explicit conversion.
- ✅ Know the syntax of `int()`, `float()`, `str()`, `bool()`, and `type()`.
- ✅ Remember that `input()` returns a string.
- ✅ Understand that `/` returns a floating-point value.
- ✅ Practice converting user input before performing calculations.

---

# Summary

- Type conversion changes one data type into another.
- Python supports implicit and explicit conversion.
- Built-in conversion functions make explicit conversion simple.
- Correct type conversion helps prevent errors and enables mathematical operations on user input.

---

# End of Revision Notes