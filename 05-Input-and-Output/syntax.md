# Syntax Guide: Input and Output in Python

## 1. Printing Output

### Basic print syntax

```python
print(value)
```

### Example

```python
print("Hello")
```

### Printing multiple values

```python
print(value1, value2, value3)
```

### Example

```python
print("Name:", "Aisha")
```

---

## 2. Using `sep`

### Syntax

```python
print(value1, value2, sep="separator")
```

### Example

```python
print("Python", "Java", "C++", sep=" | ")
```

---

## 3. Using `end`

### Syntax

```python
print(value, end="ending")
```

### Example

```python
print("Hello", end=" ")
print("World")
```

---

## 4. Taking Input

### Syntax

```python
variable_name = input("prompt")
```

### Example

```python
name = input("Enter your name: ")
```

---

## 5. Type Conversion with Input

### Integer conversion

```python
age = int(input("Enter your age: "))
```

### Float conversion

```python
height = float(input("Enter your height: "))
```

### String conversion

```python
text = str(value)
```

---

## 6. Escape Characters

### Common escape sequences

```python
print("Line 1\nLine 2")
print("Tab\tSpace")
print("He said \"Hello\"")
```

---

## 7. Formatting Output with f-strings

### Syntax

```python
print(f"Text {variable}")
```

### Example

```python
name = "Zara"
print(f"Hello, {name}")
```

---

## 8. Formatting Output with `format()`

### Syntax

```python
print("Text {}".format(variable))
```

### Example

```python
name = "Zara"
print("Hello, {}".format(name))
```

---

## 9. Basic Input and Output Program Pattern

```python
name = input("Enter your name: ")
print(f"Welcome, {name}!")
```

---

## 10. A Small Calculator Pattern

```python
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
result = first_number + second_number
print(f"The sum is: {result}")
```

---

## 11. Syntax Rules to Remember

- Use parentheses with `print()`.
- Use quotes for strings.
- `input()` always returns a string.
- Convert input when needed.
- Use `f-strings` for modern formatting.
- Use `sep` to change separators between multiple values.
- Use `end` to change the end of the printed line.

---

## 12. Quick Reference Table

| Feature | Syntax | Purpose |
|---|---|---|
| Print | `print()` | Display output |
| Input | `input()` | Read user input |
| Multiple arguments | `print(a, b)` | Print more than one value |
| Separator | `sep="|"` | Change the separator |
| Ending character | `end=" "` | Change line ending |
| Escape sequence | `"\n"` | Insert special characters |
| f-string | `f"...{var}"` | Format strings efficiently |
| `format()` | `"{}".format(var)` | Alternative formatting method |
