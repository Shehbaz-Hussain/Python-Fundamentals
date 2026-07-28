# Parameters in Lambda Functions

## Introduction

Lambda functions can accept parameters just like regular functions created with the `def` keyword. Parameters allow a lambda function to receive input values and use them to produce a result.

Understanding how parameters work is essential because they determine what data a lambda function can process.

Although lambda functions are anonymous and limited to a single expression, their parameter rules are almost identical to those of regular Python functions.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand how parameters work in lambda functions.
- Create lambda functions with one or more parameters.
- Pass arguments correctly to lambda functions.
- Distinguish between parameters and arguments.
- Use lambda functions that accept different numbers of inputs.
- Recognize parameter-related limitations of lambda functions.

---

# What Are Parameters?

A **parameter** is a variable listed inside the function definition.

It acts as a placeholder that receives a value when the function is called.

For example:

```python
lambda number: number * 2
```

Here:

- `number` is the parameter.
- The lambda function expects one value.
- The received value is used in the expression.

---

# Parameters vs Arguments

These two terms are often confused.

| Parameter | Argument |
|-----------|----------|
| Variable defined by the function | Actual value passed to the function |
| Exists in the function definition | Exists when the function is called |

Example:

```python
double = lambda number: number * 2

print(double(10))
```

Here:

- Parameter → `number`
- Argument → `10`

Output

```text
20
```

---

# Lambda Function with One Parameter

The simplest lambda function accepts a single parameter.

## Syntax

```python
lambda parameter: expression
```

Example:

```python
square = lambda number: number ** 2

print(square(5))
```

Output

```text
25
```

Explanation:

- `number` receives `5`.
- The expression calculates `5 ** 2`.
- The result is returned automatically.

---

# Multiple Parameters

Lambda functions can accept multiple parameters separated by commas.

## Syntax

```python
lambda parameter1, parameter2: expression
```

Example:

```python
add = lambda a, b: a + b

print(add(8, 12))
```

Output

```text
20
```

Explanation:

- `a` receives `8`.
- `b` receives `12`.
- The expression returns their sum.

---

# Three Parameters

Lambda functions are not limited to one or two parameters.

Example:

```python
multiply = lambda x, y, z: x * y * z

print(multiply(2, 3, 4))
```

Output

```text
24
```

---

# Four Parameters

You can continue adding parameters whenever appropriate.

Example:

```python
average = lambda a, b, c, d: (a + b + c + d) / 4

print(average(10, 20, 30, 40))
```

Output

```text
25.0
```

---

# Lambda Function Without Parameters

A lambda function can also have no parameters.

Syntax:

```python
lambda: expression
```

Example:

```python
greeting = lambda: "Welcome to Python"

print(greeting())
```

Output

```text
Welcome to Python
```

Although valid, parameterless lambda functions are relatively uncommon.

---

# Using String Parameters

Parameters are not limited to numeric values.

Example:

```python
welcome = lambda name: f"Hello, {name}!"

print(welcome("Alice"))
```

Output

```text
Hello, Alice!
```

---

# Using Boolean Parameters

Example:

```python
status = lambda is_logged_in: (
    "Access Granted" if is_logged_in else "Access Denied"
)

print(status(True))
print(status(False))
```

Output

```text
Access Granted
Access Denied
```

---

# Parameters Can Accept Any Python Object

A parameter can receive any object, including numbers, strings, booleans, lists, tuples, dictionaries, or even functions.

Example:

```python
show_type = lambda value: type(value).__name__

print(show_type(100))
print(show_type(3.14))
print(show_type("Python"))
```

Output

```text
int
float
str
```

---

# Passing Expressions as Arguments

Arguments do not have to be simple variables.

Example:

```python
double = lambda number: number * 2

print(double(5 + 3))
```

Output

```text
16
```

Python evaluates the expression first.

The lambda function actually receives:

```python
8
```

---

# Using Variables as Arguments

Example:

```python
length = 15

double = lambda value: value * 2

print(double(length))
```

Output

```text
30
```

---

# Mixing Different Parameter Types

Example:

```python
student = lambda name, marks: f"{name} scored {marks} marks."

print(student("Ali", 92))
```

Output

```text
Ali scored 92 marks.
```

---

# Parameter Order Matters

Arguments are matched with parameters based on their position unless keyword arguments are used.

Example:

```python
subtract = lambda a, b: a - b

print(subtract(15, 5))
```

Output

```text
10
```

Changing the order changes the result.

```python
print(subtract(5, 15))
```

Output

```text
-10
```

---

# Keyword Arguments

Like regular functions, lambda functions support keyword arguments.

Example:

```python
calculate_area = lambda length, width: length * width

print(calculate_area(length=8, width=5))
```

Output

```text
40
```

Keyword arguments improve readability and reduce mistakes.

---

# Default Parameter Values

Lambda functions can define default parameter values.

Example:

```python
greet = lambda name="Guest": f"Hello, {name}!"

print(greet())
print(greet("Ayesha"))
```

Output

```text
Hello, Guest!
Hello, Ayesha!
```

---

# Variable-Length Parameters

Lambda functions also support `*args` and `**kwargs`.

Example using `*args`:

```python
total = lambda *numbers: sum(numbers)

print(total(1, 2, 3, 4, 5))
```

Output

```text
15
```

Example using `**kwargs`:

```python
show = lambda **details: details

print(show(name="Sara", age=20))
```

Output

```text
{'name': 'Sara', 'age': 20}
```

Although supported, these are generally more useful in regular functions than in lambda functions.

---

# Rules for Lambda Parameters

- Parameters appear before the colon (`:`).
- Multiple parameters are separated by commas.
- Parameters behave the same way as in regular functions.
- Required arguments must be provided when calling the lambda function.
- Default parameter values are supported.
- Keyword arguments are supported.
- Variable-length parameters (`*args` and `**kwargs`) are supported.
- The function body must consist of exactly one expression.

---

# Common Mistakes

## Forgetting Required Arguments

Incorrect:

```python
square = lambda x: x ** 2

square()
```

Result:

```text
TypeError
```

Correct:

```python
square(5)
```

---

## Passing Too Many Arguments

Incorrect:

```python
add = lambda a, b: a + b

add(1, 2, 3)
```

Result:

```text
TypeError
```

---

## Confusing Parameters with Arguments

Incorrect understanding:

```python
lambda x: x + 1
```

Here, `x` is a **parameter**, not an argument.

The argument is supplied later when the lambda function is called.

---

## Using Too Many Parameters

Although valid, this is difficult to read:

```python
lambda a, b, c, d, e, f, g, h: ...
```

If a lambda function needs many parameters or complex logic, prefer a regular function.

---

# Best Practices

- Use meaningful parameter names.
- Keep parameter lists short and readable.
- Prefer one or two parameters whenever possible.
- Use keyword arguments when they improve readability.
- Use default values where appropriate.
- Switch to a regular function if the lambda expression becomes difficult to understand.

---

# Lambda Parameters vs Regular Function Parameters

| Feature | Lambda Function | Regular Function |
|---------|-----------------|------------------|
| Single parameter | ✔ | ✔ |
| Multiple parameters | ✔ | ✔ |
| Default parameter values | ✔ | ✔ |
| Keyword arguments | ✔ | ✔ |
| `*args` | ✔ | ✔ |
| `**kwargs` | ✔ | ✔ |
| Type annotations | ✘ | ✔ |
| Multi-line function body | ✘ | ✔ |

---

# Real-World Applications

Lambda parameters are commonly used with:

- `map()` for transforming data
- `filter()` for selecting values
- `sorted()` with custom sorting keys
- Event handlers and callbacks
- Simple mathematical operations
- Data processing pipelines
- Functional programming patterns

Example:

```python
numbers = [1, 2, 3, 4, 5]

tripled = list(map(lambda number: number * 3, numbers))

print(tripled)
```

Output

```text
[3, 6, 9, 12, 15]
```

---

# Summary

Parameters define the inputs that a lambda function expects. They behave almost exactly like parameters in regular Python functions, supporting positional arguments, keyword arguments, default values, and variable-length arguments. Keeping parameter lists short and descriptive improves readability and maintainability.

---

# Key Takeaways

- Parameters define the inputs to a lambda function.
- Arguments are the values supplied when calling the function.
- Lambda functions can have zero, one, or many parameters.
- Default parameter values are supported.
- Keyword arguments can improve readability.
- Lambda functions support `*args` and `**kwargs`.
- A lambda function always evaluates and returns the result of a single expression.
- Keep parameter lists simple and use regular functions for complex logic.