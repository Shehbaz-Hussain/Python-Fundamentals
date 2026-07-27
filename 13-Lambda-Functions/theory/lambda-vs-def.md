# Lambda Functions vs Regular Functions (`def`)

## Introduction

Python provides two primary ways to create functions:

1. Using the **`def` keyword** to create a named function.
2. Using the **`lambda` keyword** to create an anonymous function.

Both approaches create **function objects** and can accept arguments, perform computations, and return values. However, they are designed for different purposes.

Understanding the differences between `lambda` and `def` is essential for writing clean, readable, and maintainable Python programs. Choosing the appropriate approach depends on the complexity, readability, and intended use of the function.

---

# Learning Objectives

After studying this document, you will be able to:

- Compare lambda functions with regular functions.
- Understand the similarities between `lambda` and `def`.
- Identify the differences in syntax and capabilities.
- Choose the appropriate function type for different scenarios.
- Follow Python best practices when defining functions.

---

# Definition

## Regular Function (`def`)

A regular function is created using the `def` keyword and has a name.

Example:

```python
def square(number):
    return number * number

print(square(6))
```

**Output**

```text
36
```

---

## Lambda Function

A lambda function is an anonymous function created using the `lambda` keyword.

Example:

```python
square = lambda number: number * number

print(square(6))
```

**Output**

```text
36
```

Both functions produce the same result.

---

# Syntax Comparison

## Regular Function

```python
def function_name(parameters):
    return expression
```

Example:

```python
def add(first, second):
    return first + second
```

---

## Lambda Function

```python
lambda parameters: expression
```

Example:

```python
add = lambda first, second: first + second
```

The lambda version is more compact because:

- No `def` keyword is required.
- No function name is required during creation.
- No `return` statement is needed.
- The expression is returned automatically.

---

# Side-by-Side Comparison

Regular function:

```python
def multiply(first, second):
    return first * second

print(multiply(4, 5))
```

Lambda function:

```python
multiply = lambda first, second: first * second

print(multiply(4, 5))
```

Output for both:

```text
20
```

---

# Similarities

Both `lambda` and `def` create function objects.

They can:

- Accept parameters.
- Return values.
- Be assigned to variables.
- Be passed as arguments.
- Be stored in data structures.
- Be called like any other function.

Example:

```python
def increment_def(number):
    return number + 1

increment_lambda = lambda number: number + 1

print(increment_def(10))
print(increment_lambda(10))
```

Output:

```text
11
11
```

---

# Differences

| Feature | `lambda` | `def` |
|---------|----------|--------|
| Keyword | `lambda` | `def` |
| Function Name | Optional | Required |
| Number of Expressions | One | Unlimited |
| Multiple Statements | No | Yes |
| Automatic Return | Yes | No |
| Explicit `return` | Not Allowed | Required when returning a value |
| Docstrings | Not Practical | Fully Supported |
| Best Use | Small, temporary functions | General-purpose functions |

---

# Readability Comparison

## Using `def`

```python
def calculate_discount(price):
    return price * 0.90

print(calculate_discount(1000))
```

Output:

```text
900.0
```

---

## Using `lambda`

```python
calculate_discount = lambda price: price * 0.90

print(calculate_discount(1000))
```

Output:

```text
900.0
```

For very small operations, the lambda version is concise.

---

# Multi-Step Logic

One of the biggest differences is that regular functions support multiple statements.

Example:

```python
def calculate_total(price, tax_rate):
    tax = price * tax_rate
    total = price + tax
    return total

print(calculate_total(1000, 0.18))
```

Output:

```text
1180.0
```

A lambda function cannot express this logic clearly because it is limited to a single expression.

---

# Conditional Logic

Both approaches can use conditional expressions.

Regular function:

```python
def maximum(first, second):
    if first > second:
        return first
    return second

print(maximum(8, 12))
```

Lambda function:

```python
maximum = lambda first, second: first if first > second else second

print(maximum(8, 12))
```

Output:

```text
12
```

For simple conditions, both are acceptable.

---

# Documentation

Regular functions support docstrings.

```python
def square(number):
    """Return the square of a number."""
    return number * number
```

Lambda functions do not provide a practical place for docstrings.

For reusable public functions, `def` is the preferred choice.

---

# Debugging

Regular functions are generally easier to debug.

Example:

```python
def calculate_area(length, width):
    return length * width
```

The function has a descriptive name, making stack traces easier to understand.

Anonymous lambda functions can make debugging more difficult if overused.

---

# Reusability

If a function will be used throughout a project, define it with `def`.

Example:

```python
def is_even(number):
    return number % 2 == 0
```

This function can be imported into other modules and documented properly.

Lambda functions are better suited for temporary logic.

---

# Using with Higher-Order Functions

Lambda functions are commonly used with higher-order functions.

Example:

```python
numbers = [1, 2, 3, 4]

squares = list(map(lambda number: number ** 2, numbers))

print(squares)
```

Output:

```text
[1, 4, 9, 16]
```

Using `def`:

```python
def square(number):
    return number ** 2

numbers = [1, 2, 3, 4]

squares = list(map(square, numbers))

print(squares)
```

Both versions are correct.

---

# Performance

A common misconception is that lambda functions are faster than regular functions.

This is **not true**.

Both create function objects and have very similar runtime performance.

Choose between them based on readability and maintainability, not speed.

---

# Internal Behavior

Internally, both approaches create objects of type `function`.

Example:

```python
def add_def(a, b):
    return a + b

add_lambda = lambda a, b: a + b

print(type(add_def))
print(type(add_lambda))
```

Output:

```text
<class 'function'>
<class 'function'>
```

The difference is primarily syntactic.

---

# When to Use `lambda`

Use a lambda function when:

- The function is very small.
- It contains one simple expression.
- It is used only once.
- It is passed directly as an argument.
- Using lambda improves readability.

Example:

```python
words = ["Python", "AI", "Programming"]

words.sort(key=lambda word: len(word))

print(words)
```

---

# When to Use `def`

Use a regular function when:

- The function contains multiple statements.
- Complex logic is required.
- Documentation is important.
- The function will be reused.
- Readability would improve with a named function.
- Error handling is needed.

Example:

```python
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

print(calculate_average([10, 20, 30]))
```

---

# Advantages of Lambda

- Concise syntax.
- Less boilerplate code.
- Excellent for temporary helper functions.
- Integrates naturally with `map()`, `filter()`, and `sorted()`.

---

# Advantages of `def`

- Supports complex logic.
- Easier to document.
- Easier to debug.
- Better readability for large functions.
- Preferred for reusable code.

---

# Disadvantages of Lambda

- Limited to one expression.
- Can become unreadable when overused.
- Poor choice for complex algorithms.
- Limited documentation.

---

# Disadvantages of `def`

- More verbose for very small functions.
- Can introduce unnecessary helper functions for one-time operations.

---

# Best Practices

Follow these recommendations:

- Use `lambda` only for short, simple expressions.
- Use `def` for reusable or complex functionality.
- Prefer readability over writing fewer lines of code.
- Give regular functions descriptive names.
- Avoid deeply nested lambda expressions.
- Follow PEP 8 style guidelines.

---

# Common Mistakes

## Using Lambda for Complex Logic

Avoid writing long expressions like:

```python
calculate = lambda a, b, c, d: ((a + b) * c - d) / d if d else 0
```

A regular function is much easier to read.

---

## Creating Unnecessary Named Functions

Avoid writing:

```python
def double(number):
    return number * 2

numbers = [1, 2, 3]
result = list(map(double, numbers))
```

if the function is never reused.

Instead:

```python
numbers = [1, 2, 3]

result = list(map(lambda number: number * 2, numbers))
```

---

## Choosing Brevity Over Clarity

Shorter code is not always better.

If a lambda expression makes the code harder to understand, use `def`.

---

# Comparison Summary

| Aspect | Lambda | Regular Function (`def`) |
|--------|---------|---------------------------|
| Best For | Temporary operations | General programming |
| Complexity | Simple | Simple to complex |
| Readability | Good for short expressions | Better for larger logic |
| Reusability | Limited | Excellent |
| Documentation | Limited | Excellent |
| Maintainability | Lower for complex code | Higher |

---

# Illustrative Examples

## Example 1 — Square a Number

Regular function:

```python
def square(number):
    return number ** 2

print(square(7))
```

Lambda function:

```python
square = lambda number: number ** 2

print(square(7))
```

Output:

```text
49
```

---

## Example 2 — Find the Larger Number

```python
maximum = lambda first, second: first if first > second else second

print(maximum(15, 22))
```

Output:

```text
22
```

---

## Example 3 — Sort by Length

```python
languages = ["Python", "C", "Java", "Go"]

languages.sort(key=lambda language: len(language))

print(languages)
```

Output:

```text
['C', 'Go', 'Java', 'Python']
```

---

## Example 4 — Reusable Function

```python
def calculate_bmi(weight, height):
    return weight / (height ** 2)

print(calculate_bmi(70, 1.75))
```

Output:

```text
22.857142857142858
```

This example is better suited to `def` because the function is meaningful, reusable, and could later include validation or documentation.

---

# Summary

Both `lambda` and `def` create Python function objects, but they serve different purposes.

Lambda functions are ideal for short, simple, and temporary operations, especially when passing functions as arguments. Regular functions defined with `def` are better for reusable, documented, and complex logic.

Choosing between `lambda` and `def` should be based on readability, maintainability, and the specific requirements of your program rather than the number of lines of code.

---

# Key Takeaways

- Both `lambda` and `def` create function objects.
- Lambda functions are anonymous and limited to a single expression.
- Regular functions support multiple statements, docstrings, and complex logic.
- Lambda functions automatically return the value of their expression.
- Use `lambda` for simple, one-time operations.
- Use `def` for reusable, maintainable, and well-documented functions.
- Prioritize code readability over brevity.