# Common Mistakes in Input and Output

Learning input and output is exciting, but beginners often make a few recurring mistakes. Understanding these mistakes early can save you time and frustration.

---

## 1. Forgetting That `input()` Returns a String

This is one of the most common beginner errors.

### Incorrect

```python
age = input("Enter your age: ")
result = age + 1
print(result)
```

### Why it fails

`age` is a string, so Python cannot add an integer to it directly.

### Correct

```python
age = int(input("Enter your age: "))
result = age + 1
print(result)
```

---

## 2. Using `print` Without Parentheses

In Python 3, `print()` must always include parentheses.

### Incorrect

```python
print "Hello"
```

### Correct

```python
print("Hello")
```

---

## 3. Forgetting to Put Quotes Around Strings

Strings must be enclosed in quotes.

### Incorrect

```python
print(Hello)
```

### Correct

```python
print("Hello")
```

---

## 4. Confusing `sep` and `end`

These two parameters are easy to mix up.

- `sep` controls the separator between arguments
- `end` controls the end of the printed line

### Example

```python
print("A", "B", "C", sep="-")
print("Hello", end="!")
```

---

## 5. Writing Unclear Prompts

A vague prompt creates confusion.

### Poor prompt

```python
name = input("Enter: ")
```

### Better prompt

```python
name = input("Enter your full name: ")
```

---

## 6. Not Handling Invalid Input

If a user enters a value that does not match expectations, the program may crash.

### Example

```python
age = int(input("Enter age: "))
```

If the user enters `abc`, this fails.

### Better approach

```python
value = input("Enter age: ")
if value.isdigit():
    age = int(value)
    print(age)
else:
    print("Please enter a valid number")
```

---

## 7. Printing Too Much Information at Once

Too much output can make a program look messy.

### Better approach

```python
print(f"Name: {name}")
print(f"Age: {age}")
```

---

## 8. Not Using New Lines Properly

When output is not organized, it becomes harder to read.

### Example

```python
print("Name:", name, "Age:", age)
```

This is acceptable, but separate output lines are often clearer.

---

## 9. Using the Wrong Formatting Style

Older formatting methods are still valid, but f-strings are usually easier.

### Older style

```python
print("Hello {}".format(name))
```

### Modern style

```python
print(f"Hello {name}")
```

---

## 10. Assuming Input Is Always Correct

User input cannot always be trusted. Good programs prepare for invalid input.

---

## 11. Mistake Summary Table

| Mistake | Problem | Fix |
|---|---|---|
| Not converting input | Arithmetic fails | Use `int()` or `float()` |
| Missing parentheses | Syntax error | Use `print()` |
| Missing quotes | Name error or syntax error | Wrap strings in quotes |
| Confusing `sep` and `end` | Unexpected formatting | Use each parameter correctly |
| Vague prompts | User confusion | Write clear prompts |
| No input validation | Crashes on bad input | Check input before processing |

---

## 12. Final Advice

Most mistakes in input and output are simple and easy to fix. The key is to practice, read error messages carefully, and write code slowly and clearly.
