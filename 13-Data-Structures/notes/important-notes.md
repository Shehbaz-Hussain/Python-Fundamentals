# Module 13 – Data Structures

# Important Notes

This document summarizes the most important concepts covered in **Module 13 – Data Structures**. Review these notes regularly to reinforce your understanding before attempting exercises, assignments, quizzes, interviews, or examinations.

---

# Revision Summary

In this module, you learned how to:

- Create and use lists, tuples, sets, and dictionaries.
- Access elements using indexing.
- Extract multiple elements using slicing.
- Check membership using `in` and `not in`.
- Iterate over different data structures using `for` loops.
- Use tuple unpacking.
- Work with nested data structures.
- Apply commonly used built-in functions.
- Understand the difference between mutable and immutable data structures.
- Choose the appropriate data structure for different programming tasks.

---

# Core Concepts

## Lists

- Ordered collection.
- Mutable (can be modified).
- Allows duplicate elements.
- Supports indexing and slicing.

Example:

```python
numbers = [10, 20, 30]
```

---

## Tuples

- Ordered collection.
- Immutable (cannot be modified after creation).
- Allows duplicate elements.
- Supports indexing and slicing.

Example:

```python
coordinates = (10, 20)
```

---

## Sets

- Unordered collection.
- Mutable.
- Stores only unique elements.
- Does not support indexing.

Example:

```python
colors = {"Red", "Green", "Blue"}
```

> **Note:** The order of elements in a set is not guaranteed.

---

## Dictionaries

- Store data as key-value pairs.
- Keys must be unique.
- Values may be duplicated.
- Access values using keys.

Example:

```python
student = {
    "name": "Ali",
    "age": 20,
}
```

---

# Indexing

- Python uses zero-based indexing.
- The first element has index `0`.
- Negative indexing starts from the end.

Examples:

```python
numbers[0]
numbers[-1]
```

---

# Slicing

General syntax:

```python
sequence[start:stop:step]
```

Examples:

```python
numbers[1:4]
numbers[:3]
numbers[2:]
numbers[::-1]
```

---

# Membership Operators

Use `in` and `not in` to check whether an element exists.

Example:

```python
"Python" in courses
```

---

# Tuple Unpacking

Assign tuple elements directly to variables.

Example:

```python
point = (10, 20)

x, y = point
```

---

# Nested Data Structures

A data structure can contain other data structures.

Example:

```python
student = {
    "name": "Sara",
    "marks": [90, 95, 88],
}
```

---

# Iteration

Lists:

```python
for item in items:
    print(item)
```

Dictionary:

```python
for key, value in student.items():
    print(key, value)
```

---

# Frequently Confused Topics

## List vs Tuple

| List | Tuple |
|------|-------|
| Mutable | Immutable |
| Uses `[]` | Uses `()` |
| Can be modified | Cannot be modified |

---

## Set vs Dictionary

| Set | Dictionary |
|-----|------------|
| Stores values only | Stores key-value pairs |
| Uses `{}` | Uses `{}` with `key: value` |
| Unique elements | Unique keys |

---

## Indexing vs Slicing

| Indexing | Slicing |
|----------|---------|
| Returns one element | Returns multiple elements |
| Example: `data[2]` | Example: `data[1:4]` |

---

# Common Beginner Mistakes

- Confusing lists with tuples.
- Assuming sets preserve a fixed order.
- Trying to access set elements using indexes.
- Using duplicate dictionary keys.
- Forgetting that indexing starts at `0`.
- Confusing dictionary keys with dictionary values.
- Using parentheses instead of square brackets for lists.
- Using braces for an empty set (`{}` creates an empty dictionary).

---

# Best Practices

- Choose the simplest data structure that fits the problem.
- Use meaningful variable names.
- Keep related data together.
- Prefer dictionaries when data has meaningful keys.
- Use sets when uniqueness is important.
- Use tuples for fixed collections that should not change.
- Keep code readable and well-commented.
- Follow PEP 8 style guidelines.

---

# Interview Preparation Tips

Be prepared to answer questions such as:

- What is the difference between a list and a tuple?
- Why would you choose a set instead of a list?
- How are dictionaries organized?
- What is tuple unpacking?
- What is the difference between indexing and slicing?
- Which data structures are mutable?
- Which built-in functions work with data structures?
- How do membership operators work?
- How do you iterate through a dictionary?
- When should nested data structures be used?

---

# Examination Tips

- Read every question carefully.
- Pay attention to indexing positions.
- Remember that Python uses zero-based indexing.
- Do not assume the order of elements in a set.
- Distinguish between dictionary keys and values.
- Practice tracing code manually.
- Verify slicing ranges before answering.
- Use descriptive variable names in programming questions.

---

# Key Takeaways

- Lists are ordered and mutable.
- Tuples are ordered and immutable.
- Sets store unique elements and do not guarantee element order.
- Dictionaries store data as key-value pairs.
- Indexing accesses a single element.
- Slicing extracts a sequence of elements.
- Membership operators test whether an element exists.
- Tuple unpacking assigns multiple values in one statement.
- Nested data structures organize complex information.
- Iteration allows efficient processing of collections.
- Selecting the appropriate data structure improves code readability, maintainability, and efficiency.