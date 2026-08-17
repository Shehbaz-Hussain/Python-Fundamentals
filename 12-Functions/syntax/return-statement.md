# Return Statement Syntax

## Introduction

Many functions perform calculations or process information. After completing their task, they often need to send a result back to the part of the program that called them.

Python uses the **`return` statement** for this purpose.

Understanding the syntax of the `return` statement is important because it allows functions to produce values that can be stored, displayed, or used in further calculations.

This chapter explains the syntax of the `return` statement and demonstrates how it is used in beginner-level Python programs.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the syntax of the `return` statement.
- Write functions that return values.
- Distinguish between `return` and `print()`.
- Store and use returned values.
- Avoid common mistakes related to the `return` statement.

---

# Basic Return Syntax

The simplest syntax is:

```python
return value
```

The value may be:

- A number
- A string
- A variable
- The result of an expression

When Python executes a `return` statement, it immediately sends the value back to the place where the function was called.

---

# General Function Syntax with `return`

```python
def function_name(parameters):
    # Statements

    return value
```

The `return` statement is usually the last statement in the function.

---

# Returning a Number

```python
def get_number():
    return 10
```

Calling the function:

```python
result = get_number()

print(result)
```

### Expected Output

```
10
```

### Explanation

The function returns the value `10`, which is stored in the variable `result`.

---

# Returning a String

```python
def get_message():
    return "Welcome to Python!"
```

Calling the function:

```python
message = get_message()

print(message)
```

### Expected Output

```
Welcome to Python!
```

### Explanation

The function returns a string instead of printing it directly.

---

# Returning the Result of a Calculation

```python
def add(number1, number2):
    return number1 + number2
```

Calling the function:

```python
total = add(8, 5)

print(total)
```

### Expected Output

```
13
```

### Explanation

The function calculates the sum and returns the result.

---

# Returning a Variable

A function can return the value stored in a variable.

```python
def calculate_square(number):
    square = number * number

    return square
```

Calling the function:

```python
result = calculate_square(6)

print(result)
```

### Expected Output

```
36
```

---

# Using a Returned Value

Returned values can be stored in variables and used later.

```python
def multiply(number1, number2):
    return number1 * number2


product = multiply(4, 7)

print("Product:", product)
```

### Expected Output

```
Product: 28
```

### Explanation

The function returns the calculated value, allowing the program to use it after the function finishes.

---

# `return` vs `print()`

Although they may appear similar, they serve different purposes.

## Using `print()`

```python
def add(number1, number2):
    print(number1 + number2)
```

Calling the function:

```python
result = add(5, 4)

print(result)
```

### Expected Output

```
9
None
```

### Explanation

The function prints `9`, but it does not return anything.

As a result, the variable `result` contains `None`.

---

## Using `return`

```python
def add(number1, number2):
    return number1 + number2


result = add(5, 4)

print(result)
```

### Expected Output

```
9
```

### Explanation

The function returns the value, which is stored in `result`.

---

# Returning Different Types of Values

A function may return different kinds of data.

### Number

```python
return 100
```

### String

```python
return "Python"
```

### Variable

```python
return total
```

### Expression

```python
return length * width
```

---

# Complete Example

```python
def calculate_area(length, width):
    """Return the area of a rectangle."""
    return length * width


area = calculate_area(8, 5)

print("Area:", area)
```

### Expected Output

```
Area: 40
```

### Explanation

The function calculates the area and returns the result.

The returned value is stored in the variable `area` and then displayed.

---

# Syntax Rules

When using `return`:

1. Write `return` inside a function.
2. Place a value after the `return` keyword.
3. Return the final result of the function.
4. Store or use the returned value if needed.
5. Keep the `return` statement near the end of the function.

---

# Common Mistakes

## Forgetting the `return` Statement

Incorrect:

```python
def add(a, b):
    total = a + b
```

The function calculates the result but does not return it.

Correct:

```python
def add(a, b):
    total = a + b

    return total
```

---

## Confusing `print()` with `return`

Incorrect:

```python
def square(number):
    print(number * number)
```

This only displays the value.

Correct:

```python
def square(number):
    return number * number
```

This sends the value back to the caller.

---

## Writing `return` Outside a Function

Incorrect:

```python
return 10
```

This produces a syntax error because `return` can only be used inside a function.

Correct:

```python
def get_number():
    return 10
```

---

# Best Practices

- Return calculated values instead of printing them when the result may be reused.
- Keep the `return` statement simple and easy to understand.
- Use descriptive variable names for returned values.
- Write a docstring explaining what the function returns.
- Test returned values to verify they are correct.

---

# Summary Table

| Syntax | Purpose |
|--------|---------|
| `return value` | Returns a value |
| `return number1 + number2` | Returns the result of an expression |
| `return variable_name` | Returns the value stored in a variable |
| `result = function()` | Stores the returned value |

---

# Tips

> **Tip:** Use `return` when another part of your program needs to use the result of a function.

> **Tip:** Store returned values in clearly named variables to improve readability.

> **Tip:** If a function performs a calculation, returning the result is usually more useful than printing it directly.

---

# Warning

Do not confuse displaying a value with returning a value.

- `print()` shows information on the screen.
- `return` sends information back to the caller.

A function that prints a result cannot automatically provide that result to the rest of the program.

---

# Key Takeaways

- The `return` statement sends a value back to the code that called the function.
- Returned values can be stored in variables and used later.
- A function can return numbers, strings, variables, or the results of expressions.
- `return` and `print()` have different purposes and should not be used interchangeably.
- The `return` statement can only be used inside a function.
- Returning values makes functions more flexible, reusable, and easier to integrate into larger programs.