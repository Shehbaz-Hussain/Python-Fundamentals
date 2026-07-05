# Cheat Sheet: Input and Output in Python

## 1. Common Functions

### `print()`

```python
print("Hello")
```

### `input()`

```python
name = input("Enter your name: ")
```

---

## 2. Printing Multiple Values

```python
print("A", "B", "C")
```

### With custom separator

```python
print("A", "B", "C", sep=" | ")
```

---

## 3. Controlling the End of Output

```python
print("Hello", end=" ")
print("World")
```

---

## 4. Escape Sequences

| Sequence | Meaning |
|---|---|
| `\n` | New line |
| `\t` | Tab |
| `\"` | Double quote |
| `\\` | Backslash |

---

## 5. Formatting with f-strings

```python
name = "Sara"
print(f"Hello, {name}")
```

---

## 6. Formatting with `format()`

```python
name = "Sara"
print("Hello, {}".format(name))
```

---

## 7. Type Conversion with Input

```python
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
```

---

## 8. Quick Tips

- Use `print()` for output.
- Use `input()` for reading values.
- `input()` returns a string.
- Convert input when using numbers.
- Use `f-strings` for modern formatting.
- Write clear prompts for users.

---

## 9. Mini Template

```python
name = input("Enter your name: ")
print(f"Welcome, {name}!")
```
