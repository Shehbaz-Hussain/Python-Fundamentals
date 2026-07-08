# Exam Notes: Type Conversion in Python

## Module Information

**Module:** 06 – Type Conversion

Type conversion is one of the most important topics in Python because the
`input()` function always returns data as a string. Before performing
mathematical operations, the input must often be converted into an
appropriate numeric data type.

---

# What is Type Conversion?

**Type conversion** is the process of changing a value from one data type
to another.

Example:

```python
age_text = "20"
age = int(age_text)
```

Here, the string `"20"` is converted into the integer `20`.

---

# Types of Type Conversion

There are two types of type conversion in Python:

## 1. Implicit Type Conversion

- Done automatically by Python.
- No programmer intervention is required.
- Usually occurs during arithmetic operations.

Example:

```python
number = 10 + 5.5

print(number)
print(type(number))
```

Output:

```
15.5
<class 'float'>
```

Python automatically converts the integer into a float.

---

## 2. Explicit Type Conversion

- Done manually by the programmer.
- Uses built-in conversion functions.

Example:

```python
age_text = "18"
age = int(age_text)
```

---

# Important Type Conversion Functions

## int()

Converts a value to an integer.

Syntax:

```python
int(value)
```

Example:

```python
number = int("25")
```

Result:

```
25
```

Data Type:

```
<class 'int'>
```

---

## float()

Converts a value to a floating-point number.

Syntax:

```python
float(value)
```

Example:

```python
price = float("99.95")
```

Result:

```
99.95
```

Data Type:

```
<class 'float'>
```

---

## str()

Converts a value into a string.

Syntax:

```python
str(value)
```

Example:

```python
roll_number = str(105)
```

Result:

```
"105"
```

Data Type:

```
<class 'str'>
```

---

## bool()

Converts a value into a Boolean.

Syntax:

```python
bool(value)
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

Displays the data type of a variable.

Syntax:

```python
type(variable)
```

Example:

```python
age = 20

print(type(age))
```

Output:

```
<class 'int'>
```

---

# Common Exam Questions

- What is type conversion?
- Define implicit type conversion.
- Define explicit type conversion.
- Differentiate between implicit and explicit conversion.
- Explain the purpose of `int()`.
- Explain the purpose of `float()`.
- Explain the purpose of `str()`.
- Explain the purpose of `bool()`.
- What does the `type()` function do?
- Why does the `input()` function require type conversion?

---

# Important Points to Remember

- `input()` always returns a string.
- Use `int()` for whole numbers.
- Use `float()` for decimal numbers.
- Use `str()` to convert numbers into text.
- Use `bool()` to convert values into `True` or `False`.
- Use `type()` to verify the data type of a variable.
- Python performs implicit conversion automatically in many arithmetic expressions.
- Explicit conversion is controlled by the programmer.

---

# Common Mistakes

❌ Forgetting that `input()` returns a string.

```python
age = input("Age: ")
```

✔ Correct:

```python
age = int(input("Age: "))
```

---

❌ Using `int()` for decimal strings.

```python
int("10.5")
```

This is invalid because `"10.5"` is not an integer string.

✔ Correct:

```python
float("10.5")
```

---

❌ Assuming `int()` rounds numbers.

```python
int(9.8)
```

Output:

```
9
```

The decimal part is removed; the value is **not rounded**.

---

# Memory Tricks

- **int** → Integer → Whole Numbers
- **float** → Floating Decimal Numbers
- **str** → String → Text
- **bool** → Boolean → True or False
- **type()** → Shows the Data Type

---

# Quick Revision

✔ Type conversion changes one data type into another.

✔ Two types:
- Implicit
- Explicit

✔ Important functions:
- `int()`
- `float()`
- `str()`
- `bool()`
- `type()`

✔ `input()` always returns a string.

✔ Use explicit conversion before performing arithmetic on user input.

---

# End of Exam Notes