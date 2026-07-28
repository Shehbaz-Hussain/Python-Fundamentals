# Lambda Function Syntax

## Introduction

Lambda functions provide a shorter way to create small anonymous functions in Python.

Unlike regular functions created using the `def` keyword, lambda functions are written in a single line and contain only one expression.

Understanding lambda syntax is the foundation for using lambda functions effectively with tools such as `map()`, `filter()`, and `sorted()`.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand the basic structure of a lambda function.
- Identify lambda parameters and expressions.
- Create simple lambda functions.
- Call lambda functions correctly.
- Understand the limitations of lambda syntax.
- Recognize when lambda syntax is appropriate.

---

# Basic Lambda Syntax

The general syntax of a lambda function is:

```python
lambda parameters: expression
```

A lambda function consists of three main parts:

| Part | Description |
|------|-------------|
| `lambda` | Keyword used to create a lambda function |
| `parameters` | Inputs received by the function |
| `expression` | Operation performed and returned automatically |

Example:

```python
lambda number: number * 2
```

Explanation:

- `lambda` creates the anonymous function.
- `number` is the parameter.
- `number * 2` is the expression.
- The result is automatically returned.

---

# Creating a Lambda Function

A lambda function can be assigned to a variable.

Example:

```python
double = lambda number: number * 2

print(double(5))
```

Output:

```text
10
```

Explanation:

The lambda function receives `5`, multiplies it by `2`, and returns the result.

---

# Calling a Lambda Function

A lambda function is called the same way as a regular function.

Example:

```python
square = lambda number: number ** 2

result = square(6)

print(result)
```

Output:

```text
36
```

---

# Lambda Function Without Parameters

A lambda function can have no parameters.

Syntax:

```python
lambda: expression
```

Example:

```python
message = lambda: "Hello Python"

print(message())
```

Output:

```text
Hello Python
```

---

# Lambda Function With One Parameter

A single parameter does not require parentheses.

Example:

```python
cube = lambda number: number ** 3

print(cube(3))
```

Output:

```text
27
```

---

# Lambda Function With Multiple Parameters

Multiple parameters are separated using commas.

Syntax:

```python
lambda parameter1, parameter2: expression
```

Example:

```python
add = lambda first, second: first + second

print(add(10, 20))
```

Output:

```text
30
```

---

# Lambda Function Expression

The expression is the part executed when the lambda function is called.

Example:

```python
calculate = lambda value: value + 10

print(calculate(15))
```

Output:

```text
25
```

The expression:

```python
value + 10
```

is evaluated and returned automatically.

---

# Automatic Return Value

Lambda functions do not use the `return` keyword.

Example:

```python
multiply = lambda a, b: a * b

print(multiply(4, 5))
```

Output:

```text
20
```

Python automatically returns the result.

Equivalent regular function:

```python
def multiply(a, b):
    return a * b
```

---

# Lambda Syntax Rules

Lambda functions follow these rules:

## Rule 1: The `lambda` Keyword Is Required

Correct:

```python
lambda x: x + 1
```

Incorrect:

```python
x: x + 1
```

---

## Rule 2: A Colon Separates Parameters and Expression

Correct:

```python
lambda x: x * 2
```

Incorrect:

```python
lambda x x * 2
```

---

## Rule 3: Only One Expression Is Allowed

Correct:

```python
lambda x: x * 2
```

Incorrect:

```python
lambda x:
    y = x * 2
    return y
```

Lambda functions cannot contain multiple statements.

---

## Rule 4: Parentheses Are Optional for Parameters

Single parameter:

```python
lambda x: x + 5
```

Multiple parameters:

```python
lambda x, y: x + y
```

Parentheses are not required.

---

# Lambda Syntax Compared With Regular Functions

| Feature | Lambda Function | Regular Function |
|---------|-----------------|------------------|
| Keyword | `lambda` | `def` |
| Name | Usually anonymous | Named |
| Parameters | Supported | Supported |
| Multiple expressions | Not allowed | Allowed |
| `return` keyword | Not used | Required |
| Best for | Small operations | Complex logic |

---

# Lambda With Conditional Expression

Lambda functions can contain conditional expressions.

Example:

```python
check_number = lambda number: "Positive" if number > 0 else "Negative"

print(check_number(5))
```

Output:

```text
Positive
```

---

# Lambda as an Argument

Lambda functions are often passed directly into other functions.

Example:

```python
numbers = [1, 2, 3, 4]

result = list(
    map(lambda number: number * 2, numbers)
)

print(result)
```

Output:

```text
[2, 4, 6, 8]
```

---

# Common Syntax Mistakes

## Using Parentheses Incorrectly

Incorrect:

```python
lambda(x): x * 2
```

Correct:

```python
lambda x: x * 2
```

---

## Adding Multiple Statements

Incorrect:

```python
lambda x:
    y = x + 1
    y * 2
```

Lambda functions support only one expression.

---

## Forgetting the Colon

Incorrect:

```python
lambda x x * 2
```

Correct:

```python
lambda x: x * 2
```

---

# Best Practices

- Keep lambda expressions short.
- Use meaningful parameter names.
- Use lambda functions for simple operations.
- Avoid complex nested expressions.
- Use regular functions when readability decreases.
- Prefer clarity over reducing the number of lines.

---

# Real-World Applications

Lambda syntax is commonly used in:

- Data transformation
- Sorting operations
- Filtering data
- Machine learning preprocessing
- Automation scripts
- Event handling
- Functional programming

Example:

```python
prices = [100, 200, 300]

discounted = list(
    map(lambda price: price * 0.9, prices)
)

print(discounted)
```

Output:

```text
[90.0, 180.0, 270.0]
```

---

# Summary

Lambda syntax provides a concise way to create small anonymous functions in Python. A lambda function contains the `lambda` keyword, optional parameters, and a single expression that is automatically returned. While lambda functions are powerful for simple operations, regular functions are preferred for complex logic.

---

# Key Takeaways

- Lambda functions use the syntax `lambda parameters: expression`.
- Parameters define the inputs.
- The expression is automatically returned.
- Lambda functions do not use the `return` keyword.
- Only one expression is allowed.
- Lambda functions can accept multiple parameters.
- Lambda functions are commonly used with `map()`, `filter()`, and `sorted()`.
- Use regular functions when lambda expressions become difficult to read.