# Set Syntax

## Overview

A **set** is an unordered collection of unique elements. Unlike lists and tuples, sets do not preserve the position of their elements, and duplicate values are automatically removed.

Sets are useful when:

- Duplicate values should not exist.
- Fast membership testing is required.
- The order of elements is not important.

Sets are **mutable**, meaning elements can be added or removed after the set has been created.

Sets are created using curly braces (`{}`) or the `set()` constructor.

---

# Basic Syntax

## Creating a Set

```python
numbers = {10, 20, 30, 40}
```

Explanation:

- Elements are enclosed in curly braces.
- Elements are separated by commas.
- Duplicate values are removed automatically.

---

## Creating a Set of Strings

```python
languages = {"Python", "Java", "C++"}
```

Explanation:

This set stores three unique string values.

---

## Creating a Mixed-Type Set

```python
data = {"Ali", 20, 3.85, True}
```

Explanation:

A set can store different data types.

---

## Creating an Empty Set

```python
empty_set = set()
```

Explanation:

Use the `set()` constructor to create an empty set.

Incorrect:

```python
empty_set = {}
```

This creates an empty dictionary, not a set.

---

# Syntax Variations

## Creating a Set from a List

```python
numbers = [10, 20, 20, 30]

unique_numbers = set(numbers)

print(unique_numbers)
```

Possible output:

```text
{10, 20, 30}
```

Duplicate values are removed.

---

## Creating a Set from a String

```python
letters = set("Python")

print(letters)
```

Possible output:

```text
{'P', 'y', 't', 'h', 'o', 'n'}
```

Each unique character becomes an element of the set.

---

## Nested Sets

Sets cannot contain other mutable sets because sets themselves are mutable.

Incorrect:

```python
values = {{1, 2}, {3, 4}}
```

This raises a `TypeError`.

---

# Parameters

The `set()` constructor accepts one optional iterable.

Example:

```python
letters = set(["A", "B", "A"])

print(letters)
```

Output:

```text
{'A', 'B'}
```

---

# Return Values

Creating a set returns a new set object.

Example:

```python
numbers = {1, 2, 3}

print(type(numbers))
```

Output:

```text
<class 'set'>
```

---

# Common Patterns

## Adding an Element

```python
numbers = {10, 20}

numbers.add(30)

print(numbers)
```

Possible output:

```text
{10, 20, 30}
```

---

## Removing an Element

```python
numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)
```

Possible output:

```text
{10, 30}
```

---

## Finding the Length

```python
numbers = {10, 20, 30}

print(len(numbers))
```

Output:

```text
3
```

---

## Checking Membership

```python
languages = {"Python", "Java", "C++"}

print("Python" in languages)
```

Output:

```text
True
```

---

## Iterating Over a Set

```python
languages = {"Python", "Java", "C++"}

for language in languages:
    print(language)
```

Possible output:

```text
Python
Java
C++
```

The order may differ.

---

## Using Built-in Functions

```python
numbers = {15, 8, 22, 11}

print(min(numbers))
print(max(numbers))
print(sum(numbers))
```

Output:

```text
8
22
56
```

---

## Removing Duplicate Values

```python
names = ["Ali", "Sara", "Ali", "Ahmed"]

unique_names = set(names)

print(unique_names)
```

Possible output:

```text
{'Ali', 'Sara', 'Ahmed'}
```

---

# Common Mistakes

## Creating an Empty Set Incorrectly

Incorrect:

```python
empty_set = {}
```

This creates a dictionary.

Correct:

```python
empty_set = set()
```

---

## Assuming Sets Preserve Order

```python
numbers = {3, 1, 2}

print(numbers)
```

Do not expect the output to match the order in which elements were added.

---

## Trying to Access Elements by Index

Incorrect:

```python
numbers = {10, 20, 30}

print(numbers[0])
```

This raises a `TypeError`.

Sets do not support indexing.

---

## Expecting Duplicate Values to Be Stored

```python
numbers = {10, 20, 20, 30}

print(numbers)
```

Output:

```text
{10, 20, 30}
```

Duplicate values are removed automatically.

---

## Removing a Value That Does Not Exist

```python
numbers = {10, 20}

numbers.remove(30)
```

This raises a `KeyError`.

Ensure the element exists before removing it.

---

# Best Practices

- Use sets when uniqueness is required.
- Do not rely on the order of elements.
- Use descriptive variable names.
- Use `set()` to remove duplicates from collections.
- Avoid unnecessary conversions between lists and sets.
- Follow PEP 8 naming and formatting conventions.

---

# Examples

## Example 1

```python
colors = {
    "Red",
    "Green",
    "Blue"
}

print(colors)
```

Possible output:

```text
{'Red', 'Green', 'Blue'}
```

---

## Example 2

```python
skills = {
    "Python",
    "AI"
}

skills.add("Machine Learning")

print(skills)
```

Possible output:

```text
{'Python', 'AI', 'Machine Learning'}
```

---

## Example 3

```python
cities = {
    "Gilgit",
    "Islamabad",
    "Lahore"
}

print("Lahore" in cities)
```

Output:

```text
True
```

---

## Example 4

```python
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = set(numbers)

print(unique_numbers)
```

Possible output:

```text
{1, 2, 3, 4, 5}
```

---

# Summary

Sets are mutable collections that store only unique elements. They are created using curly braces (`{}`) or the `set()` constructor and support operations such as adding, removing, iterating, and membership testing. Because sets do not preserve element order and automatically eliminate duplicates, they are well suited for problems involving unique values and efficient membership checks.