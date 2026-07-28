# Using `filter()` with Lambda Functions

## Introduction

The `filter()` function is another powerful built-in function in Python that is frequently used with lambda functions. It allows you to select only those elements from an iterable that satisfy a specified condition.

Instead of transforming data like `map()`, `filter()` removes elements that do not meet the given condition.

This makes it particularly useful for data validation, searching, preprocessing, and cleaning datasets.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand the purpose of the `filter()` function.
- Explain how `filter()` works.
- Use lambda functions with `filter()`.
- Filter data based on different conditions.
- Distinguish between `map()` and `filter()`.
- Apply `filter()` in real-world scenarios.

---

# What Is `filter()`?

`filter()` is a built-in Python function that selects elements from an iterable based on a condition.

The condition is provided as a function that returns either:

- `True`
- `False`

If the function returns:

- `True` → the element is kept.
- `False` → the element is discarded.

---

# Syntax

```python
filter(function, iterable)
```

Using a lambda function:

```python
filter(lambda parameter: condition, iterable)
```

---

# How `filter()` Works

Suppose we have:

```python
numbers = [2, 5, 8, 11]
```

Python evaluates each element:

```text
2  → True
5  → False
8  → True
11 → False
```

Only the values that produce `True` remain.

Result:

```text
[2, 8]
```

---

# The Result Is a Filter Object

Like `map()`, the `filter()` function returns an iterator.

Example:

```python
numbers = [1, 2, 3, 4]

result = filter(lambda number: number % 2 == 0, numbers)

print(result)
```

Output

```text
<filter object at ...>
```

Convert it to a list to view the values.

```python
numbers = [1, 2, 3, 4]

result = filter(lambda number: number % 2 == 0, numbers)

print(list(result))
```

Output

```text
[2, 4]
```

---

# Example 1 – Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print(even_numbers)
```

Output

```text
[2, 4, 6]
```

---

# Example 2 – Odd Numbers

```python
numbers = [1, 2, 3, 4, 5, 6]

odd_numbers = list(
    filter(lambda number: number % 2 != 0, numbers)
)

print(odd_numbers)
```

Output

```text
[1, 3, 5]
```

---

# Example 3 – Numbers Greater Than 50

```python
marks = [35, 48, 65, 82, 40, 91]

passed = list(
    filter(lambda mark: mark >= 50, marks)
)

print(passed)
```

Output

```text
[65, 82, 91]
```

---

# Example 4 – Long Words

```python
words = [
    "AI",
    "Python",
    "Machine",
    "Code",
    "Automation"
]

long_words = list(
    filter(lambda word: len(word) > 5, words)
)

print(long_words)
```

Output

```text
['Python', 'Machine', 'Automation']
```

---

# Example 5 – Positive Numbers

```python
numbers = [-5, 8, -2, 15, 0, 21]

positive_numbers = list(
    filter(lambda number: number > 0, numbers)
)

print(positive_numbers)
```

Output

```text
[8, 15, 21]
```

---

# Filtering Strings

Example:

```python
names = ["Ali", "", "Sara", "", "Ahmed"]

valid_names = list(
    filter(lambda name: name != "", names)
)

print(valid_names)
```

Output

```text
['Ali', 'Sara', 'Ahmed']
```

---

# Filtering Boolean Values

Example:

```python
values = [True, False, True, False, True]

true_values = list(
    filter(lambda value: value, values)
)

print(true_values)
```

Output

```text
[True, True, True]
```

---

# Using a Regular Function

A lambda function is optional.

Example:

```python
def is_even(number):
    return number % 2 == 0


numbers = [1, 2, 3, 4, 5]

result = list(filter(is_even, numbers))

print(result)
```

Output

```text
[2, 4]
```

---

# `filter()` vs `map()`

| `filter()` | `map()` |
|------------|----------|
| Selects elements | Transforms elements |
| Returns fewer or equal elements | Returns the same number of elements |
| Requires a condition | Requires a transformation |
| Function returns `True` or `False` | Function returns a new value |

Example using `filter()`:

```python
numbers = [1, 2, 3, 4]

result = list(
    filter(lambda number: number > 2, numbers)
)

print(result)
```

Output

```text
[3, 4]
```

Example using `map()`:

```python
numbers = [1, 2, 3, 4]

result = list(
    map(lambda number: number * 2, numbers)
)

print(result)
```

Output

```text
[2, 4, 6, 8]
```

---

# Combining `filter()` and `map()`

These functions are often used together.

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(
    lambda number: number % 2 == 0,
    numbers
)

squares = list(
    map(lambda number: number ** 2, even_numbers)
)

print(squares)
```

Output

```text
[4, 16, 36]
```

First:

- `filter()` selects even numbers.

Then:

- `map()` squares them.

---

# Advantages of `filter()`

- Produces concise code.
- Eliminates unnecessary loops.
- Works naturally with lambda functions.
- Returns an iterator for efficient memory usage.
- Makes filtering operations easy to read.

---

# Limitations of `filter()`

- Only removes elements.
- Cannot modify elements.
- Complex conditions reduce readability.
- A regular loop may be clearer for beginners.

---

# Common Mistakes

## Forgetting to Convert the Result

Incorrect:

```python
numbers = [1, 2, 3]

result = filter(
    lambda number: number > 1,
    numbers
)

print(result)
```

Output

```text
<filter object at ...>
```

Correct:

```python
print(list(result))
```

---

## Returning Something Other Than a Boolean

Incorrect:

```python
filter(lambda number: number * 2, numbers)
```

Although Python evaluates non-zero values as truthy, this is poor practice.

Correct:

```python
filter(
    lambda number: number % 2 == 0,
    numbers
)
```

The condition clearly returns either `True` or `False`.

---

## Using Complex Conditions

Avoid writing overly complicated lambda expressions.

Instead of:

```python
lambda value: ...
```

Create a regular function when the logic becomes difficult to read.

---

# Best Practices

- Return a clear Boolean condition.
- Keep lambda expressions short.
- Convert the iterator into a list when necessary.
- Use descriptive variable names.
- Prefer regular functions for complex filtering rules.
- Combine `filter()` with `map()` only when it improves readability.

---

# Real-World Applications

The `filter()` function is commonly used for:

- Data cleaning
- Data validation
- Removing invalid records
- Selecting passing students
- Searching collections
- Preprocessing datasets
- Machine learning data preparation
- Automation scripts

Example:

```python
temperatures = [18, 24, 30, 15, 27, 12]

warm_days = list(
    filter(lambda temperature: temperature >= 25, temperatures)
)

print(warm_days)
```

Output

```text
[30, 27]
```

---

# Summary

The `filter()` function selects elements that satisfy a specified condition. When combined with lambda functions, it provides a concise and efficient way to remove unwanted data from an iterable. Unlike `map()`, which transforms every element, `filter()` only keeps elements whose condition evaluates to `True`.

---

# Key Takeaways

- `filter()` selects elements based on a condition.
- The filtering function should return `True` or `False`.
- `filter()` returns a **filter object**, which is an iterator.
- Convert the result to a list when immediate output is required.
- Lambda functions are commonly used with `filter()`.
- `filter()` reduces the number of elements, while `map()` transforms them.
- Keep filtering conditions simple and readable.
- Use a regular function when the filtering logic becomes complex.