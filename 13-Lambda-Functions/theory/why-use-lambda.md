# Why Use Lambda Functions?

## Introduction

Python emphasizes writing code that is **clear, readable, and expressive**. While regular functions defined with the `def` keyword are suitable for most programming tasks, there are situations where writing an entire named function is unnecessary.

Imagine you need a simple function that is used only once—for example, doubling numbers in a list or sorting records based on a specific field. Writing a full function definition for such a small task can make the code longer than necessary.

To address these situations, Python provides **lambda functions**. Lambda functions allow developers to write short, anonymous functions using a compact syntax while maintaining the full behavior of a function object.

Understanding **why lambda functions exist** is more important than simply learning their syntax. Good Python developers choose lambda functions only when they improve readability and use regular functions when they provide better clarity.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Explain why lambda functions exist.
- Understand the problems lambda functions solve.
- Identify situations where lambda functions are appropriate.
- Recognize situations where regular functions are a better choice.
- Understand the benefits and limitations of lambda functions.
- Apply Python best practices when deciding between `lambda` and `def`.

---

# Why Were Lambda Functions Introduced?

Without lambda functions, every operation that required a function—even a very small one—would need a complete function definition.

Example:

```python
def square(number):
    return number * number

print(square(5))
```

Output:

```text
25
```

Although this code is perfectly valid, imagine that the function is used only once.

Python allows the same logic to be written more concisely:

```python
square = lambda number: number * number

print(square(5))
```

Output:

```text
25
```

Both versions produce identical results.

Lambda functions reduce unnecessary boilerplate code for simple operations.

---

# Making Code More Concise

One of the main reasons to use lambda functions is to make code shorter without sacrificing clarity.

Regular function:

```python
def double(number):
    return number * 2

print(double(10))
```

Lambda function:

```python
double = lambda number: number * 2

print(double(10))
```

Output:

```text
20
```

For simple expressions, the lambda version is often easier to read because the entire function fits on a single line.

---

# Temporary Functions

Sometimes a function is needed only once.

Example:

```python
numbers = [3, 6, 9]

result = list(map(lambda number: number * 2, numbers))

print(result)
```

Output:

```text
[6, 12, 18]
```

The function is used immediately and never reused.

Creating a separate named function would add unnecessary code.

---

# Passing Functions as Arguments

Many Python functions accept **other functions** as arguments.

These are called **higher-order functions**.

Examples include:

- `map()`
- `filter()`
- `sorted()`
- `reduce()`

Lambda functions work naturally with these functions.

Example:

```python
numbers = [5, 8, 12]

squared_numbers = list(map(lambda number: number ** 2, numbers))

print(squared_numbers)
```

Output:

```text
[25, 64, 144]
```

The lambda function provides the transformation directly where it is needed.

---

# Simplifying Sorting Operations

Suppose you have student records.

```python
students = [
    ("Ali", 85),
    ("Sara", 96),
    ("Ahmed", 78)
]
```

Sorting by marks:

```python
students.sort(key=lambda student: student[1])

print(students)
```

Output:

```text
[('Ahmed', 78), ('Ali', 85), ('Sara', 96)]
```

Using a lambda function removes the need for a separate helper function.

---

# Improving Data Processing

Lambda functions are especially useful for transforming collections of data.

Example:

```python
prices = [100, 250, 400]

discounted_prices = list(map(lambda price: price * 0.90, prices))

print(discounted_prices)
```

Output:

```text
[90.0, 225.0, 360.0]
```

This style is common in data analysis and automation scripts.

---

# Functional Programming

Python supports several ideas from **functional programming**.

These include:

- Functions as objects
- Higher-order functions
- Anonymous functions
- Immutable programming patterns

Lambda functions make these programming styles more convenient.

Example:

```python
numbers = [1, 2, 3, 4, 5]

odd_numbers = list(filter(lambda number: number % 2 != 0, numbers))

print(odd_numbers)
```

Output:

```text
[1, 3, 5]
```

---

# Better Readability for Simple Operations

Compare the following examples.

Using `def`:

```python
def get_length(text):
    return len(text)

words = ["Python", "AI", "Programming"]

words.sort(key=get_length)

print(words)
```

Using `lambda`:

```python
words = ["Python", "AI", "Programming"]

words.sort(key=lambda word: len(word))

print(words)
```

Output:

```text
['AI', 'Python', 'Programming']
```

For such a simple operation, many Python developers consider the lambda version easier to follow because the logic is located exactly where it is used.

---

# Avoiding Unnecessary Function Names

Sometimes naming a function provides no additional value.

Example:

```python
numbers = [2, 4, 6]

tripled = list(map(lambda number: number * 3, numbers))

print(tripled)
```

Output:

```text
[6, 12, 18]
```

Creating a function named `triple()` would add another identifier to the program without improving readability.

---

# Common Use Cases

Lambda functions are commonly used for:

- Sorting records
- Filtering data
- Transforming collections
- Event callbacks
- GUI programming
- Data preprocessing
- Configuration functions
- Quick mathematical operations
- Automation scripts
- Temporary helper functions

They are widely used in libraries such as:

- pandas
- NumPy
- scikit-learn
- TensorFlow
- PyTorch
- PySpark

---

# When Should You Use Lambda Functions?

A lambda function is a good choice when:

- The function is short.
- The function contains one simple expression.
- The function is used only once.
- The function is passed directly as an argument.
- Using `lambda` improves readability.

Example:

```python
maximum = lambda first, second: first if first > second else second

print(maximum(14, 22))
```

Output:

```text
22
```

---

# When Should You Avoid Lambda Functions?

Do **not** use lambda functions when:

- The logic requires multiple statements.
- The function performs several calculations.
- You need loops or multiple conditional branches.
- The function requires documentation.
- The function will be reused in many places.
- The lambda expression becomes difficult to read.

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

This regular function is much clearer than trying to express the same logic in a single lambda expression.

---

# Internal Behavior

A lambda function creates a normal Python function object.

Example:

```python
increment = lambda value: value + 1

print(type(increment))
```

Output:

```text
<class 'function'>
```

Internally, Python:

1. Creates a function object.
2. Stores the function in memory.
3. Assigns it to a variable or passes it directly.
4. Executes the expression when called.
5. Returns the result automatically.

---

# Advantages

Lambda functions provide several benefits.

- Concise syntax.
- Less boilerplate code.
- Useful for one-time functions.
- Integrate naturally with higher-order functions.
- Improve readability for simple operations.
- Reduce unnecessary helper functions.

---

# Disadvantages

Lambda functions also have limitations.

- Only one expression is allowed.
- Complex expressions reduce readability.
- Cannot contain multiple statements.
- Limited documentation support.
- Not suitable for large algorithms.

For substantial logic, a regular function is almost always the better choice.

---

# Best Practices

Follow these recommendations:

- Keep lambda expressions short.
- Use descriptive parameter names.
- Prefer readability over brevity.
- Use lambda mainly for temporary functions.
- Replace complex lambda expressions with regular functions.
- Follow PEP 8 coding conventions.

Good example:

```python
square = lambda number: number * number
```

Less readable example:

```python
calculate = lambda a, b, c, d: ((a + b) * c - d) / d if d else 0
```

The second example should generally be written as a regular function.

---

# Common Mistakes

## Using Lambda Everywhere

Not every function should be a lambda.

Choose the form that makes the program easiest to understand.

---

## Writing Long Expressions

Long lambda expressions are difficult to read and maintain.

If the expression spans multiple logical steps, use `def`.

---

## Forgetting That Lambda Returns Automatically

Incorrect:

```python
lambda x: return x + 1
```

Correct:

```python
lambda x: x + 1
```

---

## Trying to Write Multiple Statements

Incorrect:

```python
lambda x:
    print(x)
    x += 1
```

Lambda functions can contain only a single expression.

---

# Comparison with Related Concepts

| Feature | Lambda Function | Regular Function |
|---------|-----------------|------------------|
| Intended Use | Short, temporary tasks | General-purpose programming |
| Function Name | Optional | Required |
| Multiple Statements | No | Yes |
| Automatic Return | Yes | No |
| Best for Reuse | No | Yes |
| Readability for Complex Logic | Poor | Excellent |

---

# Illustrative Examples

## Example 1 — Double a Number

```python
double = lambda number: number * 2

print(double(12))
```

Output:

```text
24
```

---

## Example 2 — Filter Positive Numbers

```python
numbers = [-4, -1, 0, 3, 8]

positive_numbers = list(filter(lambda number: number > 0, numbers))

print(positive_numbers)
```

Output:

```text
[3, 8]
```

---

## Example 3 — Sort by String Length

```python
cities = ["Gilgit", "Lahore", "AI", "Karachi"]

sorted_cities = sorted(cities, key=lambda city: len(city))

print(sorted_cities)
```

Output:

```text
['AI', 'Gilgit', 'Lahore', 'Karachi']
```

---

## Example 4 — Convert Temperatures

```python
temperatures_celsius = [0, 20, 30]

temperatures_fahrenheit = list(
    map(lambda celsius: (celsius * 9 / 5) + 32, temperatures_celsius)
)

print(temperatures_fahrenheit)
```

Output:

```text
[32.0, 68.0, 86.0]
```

---

# Summary

Lambda functions exist to provide a concise way of defining small, anonymous functions. They are especially valuable when a function is simple, temporary, and passed directly to another function.

Although lambda functions reduce the amount of code required for straightforward operations, they are not intended to replace regular functions. Whenever the logic becomes complex, reusable, or requires multiple statements, a function defined with `def` is the better choice.

Choosing between `lambda` and `def` is not about writing fewer lines of code—it is about writing code that is clear, maintainable, and appropriate for the task.

---

# Key Takeaways

- Lambda functions exist to simplify small, temporary functions.
- They eliminate unnecessary boilerplate code for simple operations.
- They are commonly used with `map()`, `filter()`, `reduce()`, and `sorted()`.
- Lambda functions improve readability only when the expression is short and clear.
- They automatically return the value of their single expression.
- Use regular functions for complex, reusable, or multi-step logic.
- Readability should always take precedence over brevity.
```