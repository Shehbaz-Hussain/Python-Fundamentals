# Using `reduce()` with Lambda Functions

## Introduction

The `reduce()` function is a functional programming tool that repeatedly applies a function to the elements of an iterable until a **single final value** is produced.

Unlike:

- `map()`, which transforms every element
- `filter()`, which selects certain elements

`reduce()` combines all elements into one result.

Because `reduce()` is commonly used with lambda functions, understanding both together is an important step toward writing concise and expressive Python code.

> **Note:** Unlike `map()` and `filter()`, the `reduce()` function is **not** a built-in function. It is available in Python's `functools` module.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand the purpose of `reduce()`.
- Import `reduce()` from the `functools` module.
- Use lambda functions with `reduce()`.
- Explain how `reduce()` processes data.
- Use an initial value with `reduce()`.
- Identify situations where `reduce()` is appropriate.

---

# What Is `reduce()`?

`reduce()` repeatedly applies a function to an iterable until only one value remains.

It combines elements one by one.

For example, adding all numbers in a list:

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, numbers)

print(result)
```

Output

```text
10
```

---

# Why Is `reduce()` in `functools`?

Unlike `map()` and `filter()`, `reduce()` is not a built-in function.

You must import it before using it.

```python
from functools import reduce
```

Without importing it, Python raises a `NameError`.

---

# Syntax

```python
from functools import reduce

reduce(function, iterable)
```

or

```python
reduce(function, iterable, initial_value)
```

Where:

- `function` accepts two arguments.
- `iterable` provides the data.
- `initial_value` is optional.

---

# How `reduce()` Works

Consider:

```python
numbers = [1, 2, 3, 4]
```

Python performs these steps:

```text
1 + 2 = 3

3 + 3 = 6

6 + 4 = 10
```

Final result:

```text
10
```

Each result becomes the first argument in the next step.

---

# Visual Representation

```
        1   2   3   4
         \ /
          3
         / \
        3   3
         \ /
          6
         / \
        6   4
         \ /
         10
```

---

# Example 1 – Sum of Numbers

```python
from functools import reduce

numbers = [5, 10, 15, 20]

total = reduce(
    lambda a, b: a + b,
    numbers
)

print(total)
```

Output

```text
50
```

---

# Example 2 – Product of Numbers

```python
from functools import reduce

numbers = [2, 3, 4]

product = reduce(
    lambda a, b: a * b,
    numbers
)

print(product)
```

Output

```text
24
```

---

# Example 3 – Largest Number

```python
from functools import reduce

numbers = [15, 42, 8, 91, 37]

largest = reduce(
    lambda a, b: a if a > b else b,
    numbers
)

print(largest)
```

Output

```text
91
```

---

# Example 4 – Smallest Number

```python
from functools import reduce

numbers = [15, 42, 8, 91, 37]

smallest = reduce(
    lambda a, b: a if a < b else b,
    numbers
)

print(smallest)
```

Output

```text
8
```

---

# Example 5 – Joining Strings

```python
from functools import reduce

words = ["Python", "is", "powerful"]

sentence = reduce(
    lambda a, b: a + " " + b,
    words
)

print(sentence)
```

Output

```text
Python is powerful
```

---

# Using an Initial Value

An optional third argument specifies the initial value.

Example:

```python
from functools import reduce

numbers = [1, 2, 3]

result = reduce(
    lambda a, b: a + b,
    numbers,
    10
)

print(result)
```

Output

```text
16
```

Python performs:

```text
10 + 1 = 11

11 + 2 = 13

13 + 3 = 16
```

---

# Using a Regular Function

A lambda function is optional.

```python
from functools import reduce


def multiply(a, b):
    return a * b


numbers = [2, 3, 4]

result = reduce(multiply, numbers)

print(result)
```

Output

```text
24
```

---

# `reduce()` vs `map()` vs `filter()`

| Function | Purpose | Result |
|----------|---------|--------|
| `map()` | Transform each element | New iterable |
| `filter()` | Select matching elements | Smaller iterable |
| `reduce()` | Combine all elements | Single value |

Example:

```python
numbers = [1, 2, 3, 4]
```

Using `map()`:

```python
list(map(lambda number: number * 2, numbers))
```

Output

```text
[2, 4, 6, 8]
```

Using `filter()`:

```python
list(filter(lambda number: number > 2, numbers))
```

Output

```text
[3, 4]
```

Using `reduce()`:

```python
from functools import reduce

reduce(lambda a, b: a + b, numbers)
```

Output

```text
10
```

---

# Combining `map()` and `reduce()`

Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4]

squares = map(
    lambda number: number ** 2,
    numbers
)

total = reduce(
    lambda a, b: a + b,
    squares
)

print(total)
```

Output

```text
30
```

Explanation:

- `map()` produces the squares.
- `reduce()` adds them together.

---

# Advantages of `reduce()`

- Produces a single result efficiently.
- Reduces repetitive looping code.
- Works well with lambda functions.
- Useful in functional programming.
- Ideal for cumulative operations.

---

# Limitations of `reduce()`

- May be difficult for beginners to read.
- Complex lambda expressions reduce readability.
- Not appropriate for every aggregation task.
- Often less readable than a simple loop.

---

# Common Mistakes

## Forgetting to Import `reduce()`

Incorrect:

```python
numbers = [1, 2, 3]

reduce(lambda a, b: a + b, numbers)
```

Result:

```text
NameError
```

Correct:

```python
from functools import reduce
```

---

## Using a Function with the Wrong Number of Parameters

Incorrect:

```python
reduce(
    lambda number: number * 2,
    [1, 2, 3]
)
```

The function supplied to `reduce()` must accept **two** arguments.

Correct:

```python
reduce(
    lambda a, b: a + b,
    [1, 2, 3]
)
```

---

## Using `reduce()` for Simple Tasks

Avoid using `reduce()` when a clearer solution exists.

Instead of:

```python
from functools import reduce

reduce(
    lambda a, b: a + b,
    numbers
)
```

You can often write:

```python
sum(numbers)
```

The second approach is usually more readable.

---

# Best Practices

- Import `reduce()` from `functools`.
- Keep lambda expressions simple.
- Use descriptive variable names.
- Prefer built-in functions like `sum()`, `min()`, or `max()` when they clearly express the intent.
- Use `reduce()` when repeatedly combining values into one result.
- Switch to a regular function if the reduction logic becomes complex.

---

# Real-World Applications

The `reduce()` function is commonly used for:

- Calculating totals
- Multiplying values
- Aggregating statistics
- Combining strings
- Data processing pipelines
- Functional programming
- Machine learning preprocessing
- Automation scripts

Example:

```python
from functools import reduce

sales = [1200, 850, 940, 1310]

total_sales = reduce(
    lambda total, sale: total + sale,
    sales
)

print(total_sales)
```

Output

```text
4300
```

---

# Summary

The `reduce()` function repeatedly combines elements from an iterable into a single value. It requires a function that accepts two arguments and is imported from the `functools` module. When paired with lambda functions, `reduce()` provides a concise way to perform cumulative operations such as summing numbers, multiplying values, or combining strings.

---

# Key Takeaways

- `reduce()` combines all elements into one final value.
- It is available in the `functools` module.
- The supplied function must accept two arguments.
- An optional initial value can be provided.
- `reduce()` is commonly used with lambda functions.
- Use `reduce()` for cumulative operations rather than transformations or filtering.
- Prefer built-in functions such as `sum()` or `max()` when they express the task more clearly.
- Keep reduction logic simple and readable.