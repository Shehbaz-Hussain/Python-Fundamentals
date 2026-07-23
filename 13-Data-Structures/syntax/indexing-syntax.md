# Indexing Syntax

## Overview

**Indexing** is the process of accessing an individual element from a data structure using its position or key.

Python supports indexing for several built-in data structures, including:

- Lists
- Tuples
- Strings

Dictionaries use **keys** instead of numeric indexes, while sets do not support indexing because they are unordered.

Understanding indexing is essential because it allows you to retrieve, update, and work with specific elements efficiently.

---

# Basic Syntax

## List Indexing

```python
list_name[index]
```

Example:

```python
fruits = ["Apple", "Banana", "Orange"]

print(fruits[0])
```

Output:

```text
Apple
```

Explanation:

- The first element is stored at index `0`.
- Python uses **zero-based indexing**.

---

## Tuple Indexing

```python
tuple_name[index]
```

Example:

```python
coordinates = (35.90, 74.34)

print(coordinates[1])
```

Output:

```text
74.34
```

---

## String Indexing

```python
string_name[index]
```

Example:

```python
language = "Python"

print(language[2])
```

Output:

```text
t
```

Strings behave like sequences of characters.

---

## Dictionary Access

Dictionaries use keys instead of numeric indexes.

```python
dictionary_name[key]
```

Example:

```python
student = {
    "name": "Ali",
    "age": 20
}

print(student["name"])
```

Output:

```text
Ali
```

---

# Syntax Variations

## Positive Indexing

Positive indexes start from the beginning.

```python
numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[2])
```

Output:

```text
10
30
```

---

## Negative Indexing

Negative indexes start from the end.

```python
numbers = [10, 20, 30, 40]

print(numbers[-1])
print(numbers[-2])
```

Output:

```text
40
30
```

Negative indexing is useful when you need the last few elements without knowing the length of the collection.

---

## Nested Indexing

You can access elements inside nested data structures.

Example:

```python
matrix = [
    [1, 2],
    [3, 4]
]

print(matrix[1][0])
```

Output:

```text
3
```

Explanation:

- `matrix[1]` accesses the second inner list.
- `[0]` accesses the first element of that inner list.

---

# Parameters

Indexing requires one index or one key.

### Numeric Index

```python
numbers[2]
```

### Negative Index

```python
numbers[-1]
```

### Dictionary Key

```python
student["age"]
```

The provided index or key must exist.

---

# Return Values

Indexing returns a single element.

Example:

```python
colors = ["Red", "Green", "Blue"]

result = colors[1]

print(result)
```

Output:

```text
Green
```

---

# Common Patterns

## Accessing the First Element

```python
numbers = [5, 10, 15]

print(numbers[0])
```

Output:

```text
5
```

---

## Accessing the Last Element

```python
numbers = [5, 10, 15]

print(numbers[-1])
```

Output:

```text
15
```

---

## Modifying a List Element

```python
numbers = [10, 20, 30]

numbers[1] = 25

print(numbers)
```

Output:

```text
[10, 25, 30]
```

Lists are mutable, so elements can be modified using indexing.

---

## Reading Tuple Elements

```python
days = ("Saturday", "Sunday")

print(days[0])
```

Output:

```text
Saturday
```

Tuples support indexing but cannot be modified.

---

## Reading Characters from a String

```python
word = "Python"

print(word[-1])
```

Output:

```text
n
```

---

## Accessing Dictionary Values

```python
employee = {
    "name": "Sara",
    "department": "IT"
}

print(employee["department"])
```

Output:

```text
IT
```

---

# Common Mistakes

## Forgetting That Indexes Start at Zero

Incorrect expectation:

```python
numbers = [10, 20, 30]

print(numbers[1])
```

Output:

```text
20
```

Some beginners expect this to print `10`, but indexing starts at `0`.

---

## Accessing an Invalid Index

```python
numbers = [10, 20]

print(numbers[5])
```

This raises an `IndexError`.

Always ensure the index is within the valid range.

---

## Trying to Modify a Tuple

```python
numbers = (10, 20, 30)

numbers[1] = 25
```

This raises a `TypeError` because tuples are immutable.

---

## Using Numeric Indexes with Dictionaries

Incorrect:

```python
student = {
    "name": "Ali"
}

print(student[0])
```

This raises a `KeyError`.

Use dictionary keys instead.

---

## Trying to Index a Set

Incorrect:

```python
numbers = {10, 20, 30}

print(numbers[0])
```

Sets do not support indexing because they are unordered.

---

# Best Practices

- Remember that indexing starts at `0`.
- Use negative indexing when accessing elements from the end.
- Verify that an index or key exists before using it.
- Use descriptive variable names.
- Keep nested indexing readable by avoiding excessive nesting.
- Choose the appropriate data structure for your indexing needs.

---

# Examples

## Example 1

```python
subjects = [
    "Python",
    "Statistics",
    "AI"
]

print(subjects[2])
```

Output:

```text
AI
```

---

## Example 2

```python
numbers = [100, 200, 300, 400]

print(numbers[-2])
```

Output:

```text
300
```

---

## Example 3

```python
student = {
    "name": "Fatima",
    "semester": 4
}

print(student["semester"])
```

Output:

```text
4
```

---

## Example 4

```python
matrix = [
    [5, 6],
    [7, 8]
]

print(matrix[0][1])
```

Output:

```text
6
```

---

# Summary

Indexing allows you to access individual elements in a collection. Lists, tuples, and strings use numeric indexes, while dictionaries use keys. Python supports both positive and negative indexing, making it easy to access elements from either end of a sequence. Understanding indexing is fundamental because it is used throughout Python programming when working with collections of data.