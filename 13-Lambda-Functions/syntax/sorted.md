# Using `sorted()` with Lambda Functions

## Introduction

The `sorted()` function is a built-in Python function used to sort elements from an iterable. By default, it sorts elements in ascending order.

When combined with lambda functions, `sorted()` becomes much more powerful because you can define **custom sorting rules** without writing a separate function.

This feature is widely used in software development, data analysis, automation, machine learning, and backend applications where data must be sorted according to specific criteria.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand the purpose of the `sorted()` function.
- Use lambda functions with the `key` parameter.
- Sort data using custom rules.
- Sort strings, numbers, and collections.
- Sort in ascending and descending order.
- Recognize when custom sorting is useful.

---

# What Is `sorted()`?

The `sorted()` function returns a **new sorted list** from an iterable.

Unlike the `sort()` list method, `sorted()` does **not** modify the original iterable.

Basic example:

```python
numbers = [8, 3, 6, 1, 5]

result = sorted(numbers)

print(result)
```

Output

```text
[1, 3, 5, 6, 8]
```

The original list remains unchanged.

---

# Syntax

```python
sorted(iterable)
```

The complete syntax is:

```python
sorted(iterable, *, key=None, reverse=False)
```

Parameters:

| Parameter | Description |
|-----------|-------------|
| `iterable` | The data to be sorted |
| `key` | Function used to determine the sorting rule |
| `reverse` | Sorts in descending order when `True` |

---

# Why Use Lambda with `sorted()`?

By default, Python sorts using the natural order of the elements.

Sometimes, you need a different rule.

For example:

- Sort words by length.
- Sort names alphabetically without considering case.
- Sort numbers based on their absolute values.
- Sort records by a specific field.

Lambda functions make these custom sorting rules concise.

---

# Default Sorting

Example:

```python
numbers = [9, 4, 2, 7, 1]

print(sorted(numbers))
```

Output

```text
[1, 2, 4, 7, 9]
```

---

# Sorting in Descending Order

Use the `reverse` parameter.

Example:

```python
numbers = [9, 4, 2, 7, 1]

print(sorted(numbers, reverse=True))
```

Output

```text
[9, 7, 4, 2, 1]
```

---

# Using the `key` Parameter

The `key` parameter specifies a function that returns the value used for sorting.

Example:

```python
numbers = [-10, 5, -3, 8]

result = sorted(
    numbers,
    key=lambda number: abs(number)
)

print(result)
```

Output

```text
[-3, 5, 8, -10]
```

Python compares the absolute values instead of the original numbers.

---

# Example 1 – Sort Words by Length

```python
words = ["banana", "kiwi", "apple", "fig"]

result = sorted(
    words,
    key=lambda word: len(word)
)

print(result)
```

Output

```text
['fig', 'kiwi', 'apple', 'banana']
```

The lambda function returns the length of each word.

---

# Example 2 – Sort Without Considering Letter Case

```python
names = ["Ali", "sara", "Ahmed", "zain"]

result = sorted(
    names,
    key=lambda name: name.lower()
)

print(result)
```

Output

```text
['Ahmed', 'Ali', 'sara', 'zain']
```

---

# Example 3 – Sort by Last Character

```python
words = ["apple", "banana", "grape", "kiwi"]

result = sorted(
    words,
    key=lambda word: word[-1]
)

print(result)
```

Output

```text
['banana', 'apple', 'grape', 'kiwi']
```

The sorting rule is based on the last character of each word.

---

# Example 4 – Sort Tuples by the Second Element

```python
students = [
    ("Ali", 82),
    ("Sara", 95),
    ("Ahmed", 76)
]

result = sorted(
    students,
    key=lambda student: student[1]
)

print(result)
```

Output

```text
[('Ahmed', 76), ('Ali', 82), ('Sara', 95)]
```

---

# Example 5 – Sort Tuples in Descending Order

```python
students = [
    ("Ali", 82),
    ("Sara", 95),
    ("Ahmed", 76)
]

result = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print(result)
```

Output

```text
[('Sara', 95), ('Ali', 82), ('Ahmed', 76)]
```

---

# Sorting Dictionaries

When iterating over dictionaries, `sorted()` sorts the keys by default.

Example:

```python
scores = {
    "Ali": 88,
    "Sara": 95,
    "Ahmed": 79
}

print(sorted(scores))
```

Output

```text
['Ahmed', 'Ali', 'Sara']
```

---

# Sorting Dictionary Items

You can sort dictionary items by value.

Example:

```python
scores = {
    "Ali": 88,
    "Sara": 95,
    "Ahmed": 79
}

result = sorted(
    scores.items(),
    key=lambda item: item[1]
)

print(result)
```

Output

```text
[('Ahmed', 79), ('Ali', 88), ('Sara', 95)]
```

---

# Using a Regular Function

A lambda function is optional.

```python
def get_length(word):
    return len(word)


words = ["banana", "kiwi", "apple"]

result = sorted(words, key=get_length)

print(result)
```

Output

```text
['kiwi', 'apple', 'banana']
```

---

# How the `key` Function Works

Suppose we have:

```python
words = ["pear", "banana", "fig"]
```

Python internally evaluates:

```text
pear    → 4
banana  → 6
fig     → 3
```

It sorts using these returned values.

Final result:

```text
['fig', 'pear', 'banana']
```

---

# Advantages of Using Lambda with `sorted()`

- Eliminates the need for small helper functions.
- Makes custom sorting concise.
- Improves readability for simple sorting rules.
- Supports sorting using almost any criterion.
- Frequently used in data processing.

---

# Limitations

- Complex lambda expressions reduce readability.
- Very complicated sorting logic should use a regular function.
- Beginners may find custom keys difficult at first.

---

# Common Mistakes

## Forgetting the `key=` Parameter

Incorrect:

```python
sorted(
    words,
    lambda word: len(word)
)
```

Correct:

```python
sorted(
    words,
    key=lambda word: len(word)
)
```

---

## Returning the Wrong Value

Incorrect:

```python
sorted(
    numbers,
    key=lambda number: print(number)
)
```

`print()` returns `None`, which cannot be used for sorting.

The key function should return a value that Python can compare.

---

## Writing Complex Lambda Expressions

Avoid expressions that are difficult to understand.

Instead of writing a long lambda expression, define a regular function with a descriptive name.

---

# Best Practices

- Keep lambda expressions short.
- Use meaningful parameter names.
- Prefer regular functions for complex sorting logic.
- Use `reverse=True` instead of reversing the result manually.
- Remember that `sorted()` returns a new list and leaves the original iterable unchanged.

---

# Real-World Applications

Sorting with lambda functions is commonly used for:

- Ranking students by marks
- Ordering products by price
- Sorting employees by salary
- Arranging files by size
- Organizing records by dates
- Machine learning data preprocessing
- Data analysis
- Backend applications

Example:

```python
products = [
    ("Keyboard", 35),
    ("Mouse", 15),
    ("Monitor", 220)
]

result = sorted(
    products,
    key=lambda product: product[1]
)

print(result)
```

Output

```text
[('Mouse', 15), ('Keyboard', 35), ('Monitor', 220)]
```

---

# Summary

The `sorted()` function returns a new sorted list from an iterable. By using the `key` parameter with a lambda function, you can define custom sorting rules without creating a separate function. This approach is concise, readable, and widely used for sorting real-world data based on specific criteria.

---

# Key Takeaways

- `sorted()` returns a new sorted list.
- The original iterable is not modified.
- Use the `key` parameter to define custom sorting rules.
- Lambda functions are commonly used as key functions.
- Use `reverse=True` for descending order.
- Keep lambda expressions simple and readable.
- Prefer regular functions when the sorting logic becomes complex.
- Custom sorting is widely used in data processing and software development.