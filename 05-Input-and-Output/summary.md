# Summary: Input and Output in Python

## Core Idea

Input and output are the two main ways a Python program communicates with the user.

- Input receives data from the user.
- Output displays data to the user.

---

## Main Functions

### `print()`
Used to show output.

```python
print("Hello")
```

### `input()`
Used to read input from the user.

```python
name = input("Enter your name: ")
```

---

## Important Points

- `input()` always returns a string.
- Use `int()` or `float()` when numerical input is needed.
- `print()` can display multiple values.
- `sep` changes the separator between values.
- `end` changes the ending of the printed line.
- `f-strings` are the modern and recommended way to format output.

---

## Example

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old")
```

---

## Final Takeaway

Mastering input and output helps you create interactive, useful, and professional Python programs.
