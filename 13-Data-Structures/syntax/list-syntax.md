# List Syntax

## Overview

A **list** is one of Python's most commonly used built-in data structures. It stores an ordered collection of items and allows duplicate values. Lists are **mutable**, meaning their contents can be modified after creation.

Lists can store values of the same type or different types in a single collection.

Examples of data that can be stored in lists include:

- Student names
- Exam marks
- Product prices
- Daily temperatures
- Programming languages

Lists are created using square brackets (`[]`).

---

# Basic Syntax

## Creating an Empty List

```python
empty_list = []
```

Explanation:

- `[]` creates an empty list.
- The list currently contains no elements.

---

## Creating a List with Values

```python
numbers = [10, 20, 30, 40]
```

Explanation:

- Elements are separated by commas.
- The order of elements is preserved.

---

## Creating a List of Strings

```python
languages = ["Python", "Java", "C++"]
```

Explanation:

This list stores three string values.

---

## Creating a Mixed-Type List

```python
student = ["Ali", 20, 3.85, True]
```

Explanation:

Lists can contain different data types.

Although Python allows mixed types, using similar types in the same list often improves readability.

---

## Nested Lists

```python
matrix = [
    [1, 2],
    [3, 4]
]
```

Explanation:

Each element of the outer list is another list.

---

# Syntax Variations

## Single Element List

```python
numbers = [10]
```

A single value still requires square brackets.

---

## List Containing Duplicate Values

```python
colors = ["Red", "Blue", "Red"]
```

Lists allow duplicate elements.

---

## List Containing Other Data Structures

```python
data = [
    [1, 2],
    (3, 4),
    {"name": "Ali"}
]
```

Lists can store almost any Python object, including other data structures.

---

# Parameters

Lists themselves do not require parameters when created using square brackets.

However, the `list()` constructor accepts one optional iterable.

Example:

```python
letters = list("Python")

print(letters)
```

Output:

```text
['P', 'y', 't', 'h', 'o', 'n']
```

The string is converted into a list of individual characters.

---

# Return Values

Creating a list returns a new list object.

Example:

```python
numbers = [1, 2, 3]

print(type(numbers))
```

Output:

```text
<class 'list'>
```

---

# Common Patterns

## Accessing an Element

```python
numbers = [10, 20, 30]

print(numbers[1])
```

Output:

```text
20
```

---

## Accessing the Last Element

```python
numbers = [10, 20, 30]

print(numbers[-1])
```

Output:

```text
30
```

---

## Modifying an Element

```python
numbers = [10, 20, 30]

numbers[1] = 25

print(numbers)
```

Output:

```text
[10, 25, 30]
```

Lists are mutable, so elements can be changed.

---

## Appending an Element

```python
numbers = [10, 20]

numbers.append(30)

print(numbers)
```

Output:

```text
[10, 20, 30]
```

The new element is added to the end of the list.

---

## Removing an Element

```python
numbers = [10, 20, 30]

numbers.remove(20)

print(numbers)
```

Output:

```text
[10, 30]
```

The first matching value is removed.

---

## Finding the Length

```python
numbers = [10, 20, 30]

print(len(numbers))
```

Output:

```text
3
```

---

## Iterating Over a List

```python
languages = ["Python", "Java", "C++"]

for language in languages:
    print(language)
```

Output:

```text
Python
Java
C++
```

---

## Checking Membership

```python
languages = ["Python", "Java", "C++"]

print("Python" in languages)
```

Output:

```text
True
```

---

## Slicing a List

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

---

# Common Mistakes

## Forgetting Commas

Incorrect:

```python
numbers = [10 20 30]
```

Correct:

```python
numbers = [10, 20, 30]
```

Elements must be separated by commas.

---

## Using Parentheses Instead of Square Brackets

Incorrect:

```python
numbers = (10, 20, 30)
```

This creates a tuple, not a list.

Correct:

```python
numbers = [10, 20, 30]
```

---

## Accessing an Invalid Index

Incorrect:

```python
numbers = [10, 20]

print(numbers[5])
```

This raises an `IndexError`.

Always ensure the index exists.

---

## Assuming Lists Cannot Be Modified

Some beginners believe lists are immutable.

Lists are mutable.

```python
numbers = [10, 20]

numbers[0] = 15
```

This is valid.

---

## Confusing `append()` and `extend()`

```python
numbers = [1, 2]

numbers.append([3, 4])

print(numbers)
```

Output:

```text
[1, 2, [3, 4]]
```

`append()` adds one object to the list. It does not add each element individually.

---

# Best Practices

- Use descriptive variable names.
- Keep similar types of data together whenever practical.
- Use lists when the collection is expected to change.
- Avoid unnecessary nesting.
- Prefer built-in list methods over manual implementations.
- Follow PEP 8 naming and formatting conventions.

---

# Examples

## Example 1

```python
cities = [
    "Gilgit",
    "Islamabad",
    "Lahore"
]

print(cities)
```

Output:

```text
['Gilgit', 'Islamabad', 'Lahore']
```

---

## Example 2

```python
marks = [78, 85, 91]

marks.append(88)

print(marks)
```

Output:

```text
[78, 85, 91, 88]
```

---

## Example 3

```python
students = [
    "Ali",
    "Sara",
    "Ahmed"
]

students[2] = "Fatima"

print(students)
```

Output:

```text
['Ali', 'Sara', 'Fatima']
```

---

## Example 4

```python
prices = [250, 180, 320, 150]

print(min(prices))
print(max(prices))
```

Output:

```text
150
320
```

---

## Summary

Lists are ordered, mutable collections that can store multiple values, including duplicate elements. They are created using square brackets (`[]`) and support indexing, slicing, iteration, membership testing, and a wide range of built-in methods. Because of their flexibility, lists are among the most frequently used data structures in Python and are suitable for many real-world programming tasks.