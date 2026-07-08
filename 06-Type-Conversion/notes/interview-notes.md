# Interview Notes: Type Conversion in Python

## Module Information

**Module:** 06 – Type Conversion

These notes cover the most common interview questions related to type conversion in Python. Review them before technical interviews, coding assessments, or university viva examinations.

---

# Frequently Asked Interview Questions

## 1. What is type conversion in Python?

**Answer:**

Type conversion is the process of changing a value from one data type to another.

Example:

```python
age_text = "20"
age = int(age_text)
```

The string `"20"` is converted into the integer `20`.

---

## 2. What are the two types of type conversion?

**Answer:**

Python supports two types of type conversion:

- Implicit Type Conversion
- Explicit Type Conversion

---

## 3. What is implicit type conversion?

**Answer:**

Implicit type conversion is performed automatically by Python when it is safe to convert one data type into another.

Example:

```python
result = 10 + 5.5

print(result)
```

Output:

```
15.5
```

Python automatically converts the integer `10` into the floating-point number `10.0`.

---

## 4. What is explicit type conversion?

**Answer:**

Explicit type conversion is performed manually by the programmer using built-in conversion functions.

Example:

```python
number = int("25")
```

---

## 5. Why is type conversion important?

**Answer:**

Type conversion allows Python programs to:

- Accept user input correctly.
- Perform mathematical calculations.
- Prevent data type mismatches.
- Convert data into the required format.

---

## 6. What does the input() function return?

**Answer:**

The `input()` function always returns a value of type `str`.

Example:

```python
age = input("Enter your age: ")

print(type(age))
```

Output:

```
<class 'str'>
```

---

## 7. What does int() do?

**Answer:**

The `int()` function converts a compatible value into an integer.

Example:

```python
number = int("50")
```

Output:

```
50
```

---

## 8. What does float() do?

**Answer:**

The `float()` function converts a compatible value into a floating-point number.

Example:

```python
price = float("49.99")
```

Output:

```
49.99
```

---

## 9. What does str() do?

**Answer:**

The `str()` function converts a value into a string.

Example:

```python
roll_number = str(101)
```

Output:

```
"101"
```

---

## 10. What does bool() do?

**Answer:**

The `bool()` function converts a value into either `True` or `False`.

Examples:

```python
bool(0)
```

Output:

```
False
```

```python
bool(100)
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

## 11. What is the purpose of type()?

**Answer:**

The `type()` function displays the data type of a value or variable.

Example:

```python
number = 25

print(type(number))
```

Output:

```
<class 'int'>
```

---

## 12. What is the difference between int() and float()?

| int() | float() |
|-------|----------|
| Converts to an integer | Converts to a floating-point number |
| Produces whole numbers | Produces decimal numbers |
| Example: `int("10")` | Example: `float("10.5")` |

---

## 13. What is the difference between implicit and explicit conversion?

| Implicit Conversion | Explicit Conversion |
|---------------------|--------------------|
| Performed automatically | Performed by the programmer |
| No conversion function required | Uses conversion functions |
| Happens during expressions | Happens when called manually |

---

# Quick Interview Tips

- Remember that `input()` always returns a string.
- Know when to use `int()` and `float()`.
- Understand the difference between implicit and explicit conversion.
- Be able to explain why type conversion is necessary.
- Know the behavior of `bool()` with common values.
- Use `type()` to verify data types during debugging.

---

# Common Interview Mistakes

- Saying that `input()` returns an integer.
- Confusing `int()` with rounding.
- Forgetting that division (`/`) returns a floating-point value.
- Mixing up implicit and explicit conversion.
- Assuming every non-empty string can be converted using `int()`.

---

# One-Minute Revision

- Type conversion changes one data type into another.
- Two types: implicit and explicit.
- `int()` → integer.
- `float()` → decimal number.
- `str()` → string.
- `bool()` → Boolean value.
- `type()` → displays the data type.
- `input()` always returns a string.

---

# End of Interview Notes