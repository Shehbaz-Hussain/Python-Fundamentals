# Common Mistakes When Working with Functions

## Introduction

Functions are one of the most useful features in Python. They allow you to organize your code, avoid repetition, and solve problems more efficiently.

However, beginners often make similar mistakes when they first start writing functions. Most of these mistakes are easy to fix once you understand why they happen.

This chapter explains the most common mistakes related to functions, why they occur, and how to avoid them.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Identify common mistakes when writing functions.
- Understand why these mistakes occur.
- Correct common function-related errors.
- Write cleaner and more reliable functions.
- Develop good programming habits.

---

# Mistake 1: Forgetting to Call the Function

## What Happens?

Some beginners define a function but never call it.

### Incorrect Example

```python
def greet():
    print("Welcome to Python!")
```

### Expected Output

```
No output
```

### Explanation

The function has been **defined**, but it has not been **called**.

Python stores the function and waits until it is called.

### Correct Example

```python
def greet():
    print("Welcome to Python!")

greet()
```

### Expected Output

```
Welcome to Python!
```

---

# Mistake 2: Incorrect Indentation

Python uses indentation to determine which statements belong to a function.

### Incorrect Example

```python
def greet():
print("Hello")
```

### Result

```
IndentationError
```

### Correct Example

```python
def greet():
    print("Hello")
```

### Expected Output

```
Hello
```

---

# Mistake 3: Forgetting Parentheses When Calling a Function

### Incorrect Example

```python
def greet():
    print("Hello")

greet
```

### Expected Output

```
No output
```

### Explanation

`greet` refers to the function itself.

`greet()` executes the function.

### Correct Example

```python
def greet():
    print("Hello")

greet()
```

### Expected Output

```
Hello
```

---

# Mistake 4: Using a Variable That Does Not Exist Inside the Function

### Incorrect Example

```python
def display_name():
    print(name)

display_name()
```

### Result

```
NameError
```

### Explanation

The variable `name` has not been created.

Python cannot print something that does not exist.

### Correct Example

```python
def display_name():
    name = "Ali"
    print(name)

display_name()
```

### Expected Output

```
Ali
```

---

# Mistake 5: Forgetting Required Arguments

### Incorrect Example

```python
def greet(name):
    print("Hello,", name)

greet()
```

### Result

Python reports that a required argument is missing.

### Explanation

The function expects one argument, but none was provided.

### Correct Example

```python
def greet(name):
    print("Hello,", name)

greet("Sara")
```

### Expected Output

```
Hello, Sara
```

---

# Mistake 6: Passing Arguments in the Wrong Order

### Incorrect Example

```python
def student(name, age):
    print(name)
    print(age)

student(20, "Ali")
```

### Expected Output

```
20
Ali
```

### Explanation

The values are accepted, but they are assigned to the wrong parameters.

### Correct Example

```python
student("Ali", 20)
```

### Expected Output

```
Ali
20
```

---

# Mistake 7: Forgetting the Return Statement

### Incorrect Example

```python
def add(a, b):
    total = a + b

result = add(4, 5)

print(result)
```

### Expected Output

```
None
```

### Explanation

The calculation is performed, but nothing is returned.

### Correct Example

```python
def add(a, b):
    return a + b

result = add(4, 5)

print(result)
```

### Expected Output

```
9
```

---

# Mistake 8: Confusing `print()` with `return`

Many beginners think these are the same.

### Example Using `print()`

```python
def square(number):
    print(number * number)

result = square(5)

print(result)
```

### Expected Output

```
25
None
```

### Explanation

The function prints the value but does not return it.

---

### Example Using `return`

```python
def square(number):
    return number * number

result = square(5)

print(result)
```

### Expected Output

```
25
```

---

# Mistake 9: Giving Functions Unclear Names

### Poor Example

```python
def abc():
    print("Hello")
```

The name does not explain the purpose.

### Better Example

```python
def print_greeting():
    print("Hello")
```

The purpose is immediately clear.

---

# Mistake 10: Writing One Function That Does Too Many Things

### Poor Practice

```python
def everything():
    # Reads input
    # Performs calculations
    # Prints reports
    # Displays menus
```

Such functions become difficult to understand.

### Better Practice

Create separate functions for separate tasks.

For example:

- `calculate_total()`
- `display_menu()`
- `print_result()`

Each function performs one job.

---

# Mistake 11: Using Hard-Coded Values

### Less Flexible

```python
def greet():
    print("Hello, Ahmed")
```

This always prints the same name.

### Better

```python
def greet(name):
    print("Hello,", name)
```

Now the function can greet anyone.

---

# Mistake 12: Forgetting to Write a Docstring

### Without a Docstring

```python
def area(length, width):
    return length * width
```

Someone reading the code must inspect the implementation to understand it.

### Better

```python
def area(length, width):
    """Return the area of a rectangle."""
    return length * width
```

The purpose is immediately clear.

---

# Mistake 13: Using Confusing Parameter Names

### Poor Example

```python
def calculate(a, b):
    return a * b
```

### Better Example

```python
def calculate_area(length, width):
    return length * width
```

Meaningful names improve readability.

---

# Mistake 14: Forgetting That Local Variables Stay Inside the Function

### Example

```python
def show_message():
    message = "Hello"

show_message()

print(message)
```

### Result

```
NameError
```

### Explanation

`message` is a **local variable**.

It exists only inside the function.

---

# Mistake 15: Changing a Function Without Updating Its Docstring

### Incorrect

```python
def multiply(a, b):
    """Return the sum of two numbers."""
    return a * b
```

The docstring no longer matches the function.

### Correct

```python
def multiply(a, b):
    """Return the product of two numbers."""
    return a * b
```

Always keep documentation accurate.

---

# Summary Table

| Mistake | How to Avoid It |
|---------|------------------|
| Forgetting to call a function | Always use `()` to call it |
| Incorrect indentation | Follow Python's indentation rules |
| Missing parentheses | Call functions using `()` |
| Undefined variables | Create variables before using them |
| Missing arguments | Pass all required arguments |
| Wrong argument order | Match parameters correctly |
| Forgetting `return` | Return calculated values when needed |
| Confusing `print()` and `return` | Know that they serve different purposes |
| Poor function names | Use meaningful names |
| Large functions | Keep each function focused on one task |
| Hard-coded values | Use parameters instead |
| Missing docstrings | Document important functions |
| Poor parameter names | Use descriptive names |
| Using local variables outside the function | Remember variable scope |
| Outdated documentation | Update docstrings whenever code changes |

---

# Tips

> **Tip:** Read your function name aloud. If it clearly describes the task, it is probably a good name.

> **Tip:** Test each function after writing it to ensure it behaves as expected.

> **Tip:** If a function becomes difficult to understand, consider simplifying it or dividing its work into smaller functions.

---

# Warning

A program may run without errors and still produce incorrect results if arguments are passed in the wrong order or if a function prints a value when it should return one.

Always verify both the program's execution and its output.

---

# Key Takeaways

- Most beginner mistakes with functions are easy to identify and correct.
- Always define **and** call a function when you want it to execute.
- Use proper indentation and include parentheses when calling functions.
- Pass the required arguments in the correct order.
- Understand the difference between `print()` and `return`.
- Use meaningful function and parameter names.
- Keep functions simple and focused on a single task.
- Write clear docstrings and keep them synchronized with your code.
- Remember that local variables are only accessible inside the function where they are created.
- Following these practices will help you write cleaner, more reliable, and more maintainable Python programs.