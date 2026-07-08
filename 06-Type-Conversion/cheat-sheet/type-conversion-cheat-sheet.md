# Python Type Conversion Cheat Sheet

## Module 06 – Type Conversion

A quick reference guide for revision, exams, interviews, and daily Python programming.

---

# What is Type Conversion?

**Type conversion** is the process of changing a value from one data type to another.

Example:

```python
age_text = "20"
age = int(age_text)
```

---

# Types of Type Conversion

## 1. Implicit Type Conversion

- Performed automatically by Python.
- Usually occurs during arithmetic operations.
- No conversion function is required.

Example:

```python
result = 10 + 2.5

print(result)
```

Output:

```
12.5
```

---

## 2. Explicit Type Conversion

- Performed manually by the programmer.
- Uses Python's built-in conversion functions.

Example:

```python
number = int("25")
```

---

# Conversion Functions

| Function | Purpose | Example | Result |
|----------|---------|---------|--------|
| `int()` | Convert to integer | `int("25")` | `25` |
| `float()` | Convert to float | `float("3.14")` | `3.14` |
| `str()` | Convert to string | `str(100)` | `"100"` |
| `bool()` | Convert to Boolean | `bool(1)` | `True` |
| `type()` | Display data type | `type(25)` | `<class 'int'>` |

---

# Syntax Reference

## int()

```python
number = int(value)
```

Example:

```python
age = int("18")
```

---

## float()

```python
price = float(value)
```

Example:

```python
price = float("99.95")
```

---

## str()

```python
text = str(value)
```

Example:

```python
roll_number = str(101)
```

---

## bool()

```python
status = bool(value)
```

Examples:

```python
bool(0)
```

Output:

```
False
```

```python
bool(10)
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

```python
type(variable)
```

Example:

```python
marks = 95

print(type(marks))
```

Output:

```
<class 'int'>
```

---

# Common Conversions

| Original Value | Conversion | Result |
|---------------|------------|--------|
| `"25"` | `int("25")` | `25` |
| `"3.5"` | `float("3.5")` | `3.5` |
| `100` | `str(100)` | `"100"` |
| `0` | `bool(0)` | `False` |
| `1` | `bool(1)` | `True` |
| `""` | `bool("")` | `False` |
| `"Hello"` | `bool("Hello")` | `True` |

---

# Implicit vs Explicit Conversion

| Implicit Conversion | Explicit Conversion |
|---------------------|--------------------|
| Automatic | Manual |
| Performed by Python | Performed by the programmer |
| No conversion function | Uses `int()`, `float()`, `str()`, `bool()` |
| Happens during compatible operations | Used when a specific type is required |

---

# Common Mistakes

❌ Forgetting that `input()` returns a string.

```python
age = input("Enter your age: ")
```

✔ Correct:

```python
age = int(input("Enter your age: "))
```

---

❌ Using `int()` for decimal strings.

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
int(8.9)
```

Output:

```
8
```

The decimal part is removed; it is **not** rounded.

---

# Best Practices

- Always convert user input before performing calculations.
- Use `int()` for whole numbers.
- Use `float()` for decimal values.
- Use `str()` when displaying numbers as text.
- Use `bool()` when a Boolean value is required.
- Use `type()` to verify the data type during debugging.
- Choose the correct conversion function based on the expected input.

---

# Memory Tips

- **int** → Integer → Whole numbers
- **float** → Floating-point → Decimal numbers
- **str** → String → Text
- **bool** → Boolean → `True` or `False`
- **type()** → Shows the data type

---

# Exam Quick Revision

- `input()` always returns a string.
- Type conversion changes one data type into another.
- Two types of conversion:
  - Implicit
  - Explicit
- Main conversion functions:
  - `int()`
  - `float()`
  - `str()`
  - `bool()`
  - `type()`
- Division (`/`) produces a floating-point result.
- Use explicit conversion before performing arithmetic on user input.

---

# One-Line Summary

**Convert user input to the appropriate data type before processing it, and use `type()` to verify your results when learning or debugging.**