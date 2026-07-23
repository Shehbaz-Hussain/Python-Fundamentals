# Indexing

## Introduction

One of the most useful features of Python data structures is the ability to access individual elements directly. This is accomplished through **indexing**.

An **index** represents the position of an element within an ordered collection. Python uses indexes to retrieve, modify (when permitted), or process specific items efficiently.

Indexing is supported by several built-in data structures, including:

- Lists
- Tuples
- Strings
- Dictionaries (using keys instead of numeric indexes)

Understanding indexing is essential because it is used throughout Python programming. Whether you are processing names, numbers, text, or structured data, indexing allows you to work with individual pieces of information.

---

# Learning Objectives

After completing this lesson, you should be able to:

- Define indexing.
- Understand zero-based indexing.
- Use positive indexing.
- Use negative indexing.
- Access elements from lists and tuples.
- Access values from dictionaries using keys.
- Recognize indexing errors.
- Apply indexing correctly in practical programs.

---

# Why This Topic Matters

Suppose you have a list of programming languages.

```python
languages = ["Python", "Java", "C++", "JavaScript"]
```

If you need only `"Python"`, you should not process the entire list.

Instead, you can directly access it using its index.

```python
print(languages[0])
```

Output:

```text
Python
```

Indexing makes retrieving individual elements simple, readable, and efficient.

---

# Concept Explanation

## What Is an Index?

An **index** is the position of an element within an ordered collection.

Python begins counting from **0**, not 1.

Example:

```python
numbers = [10, 20, 30, 40]
```

Positions are:

| Index | Value |
|------:|-------|
| 0 | 10 |
| 1 | 20 |
| 2 | 30 |
| 3 | 40 |

To access the first element:

```python
print(numbers[0])
```

Output:

```text
10
```

---

## Why Does Python Start at Zero?

Python follows the convention used by many programming languages.

Zero-based indexing simplifies many internal memory calculations and makes slicing operations more consistent.

Although beginners often expect counting to begin at 1, Python always starts indexing from 0.

---

## Positive Indexing

Positive indexes count from the beginning.

Example:

```python
colors = ["Red", "Green", "Blue", "Yellow"]

print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])
```

Output:

```text
Red
Green
Blue
Yellow
```

---

## Negative Indexing

Negative indexes count from the end of the collection.

Example:

```python
colors = ["Red", "Green", "Blue", "Yellow"]
```

| Negative Index | Value |
|---------------:|-------|
| -1 | Yellow |
| -2 | Blue |
| -3 | Green |
| -4 | Red |

Example:

```python
print(colors[-1])
print(colors[-2])
```

Output:

```text
Yellow
Blue
```

Negative indexing is useful when you need the last few elements without knowing the total length.

---

## Indexing Lists

Lists support indexing because they are ordered.

```python
fruits = ["Apple", "Banana", "Orange"]

print(fruits[1])
```

Output:

```text
Banana
```

Since lists are mutable, indexed elements can also be modified.

```python
fruits[1] = "Mango"

print(fruits)
```

Output:

```text
['Apple', 'Mango', 'Orange']
```

---

## Indexing Tuples

Tuples also support indexing.

```python
coordinates = (25, 40)

print(coordinates[0])
print(coordinates[1])
```

Output:

```text
25
40
```

However, tuple elements cannot be modified because tuples are immutable.

Incorrect:

```python
coordinates[0] = 30
```

This raises a `TypeError`.

---

## Dictionaries Use Keys Instead of Numeric Indexes

Unlike lists and tuples, dictionaries are accessed using **keys**.

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

Although this looks similar to indexing, `"name"` is a key rather than a numeric index.

---

## Sets Do Not Support Indexing

Sets are unordered collections.

```python
numbers = {10, 20, 30}
```

Attempting to use an index:

```python
print(numbers[0])
```

raises a `TypeError`.

Because sets do not preserve element positions, indexing is not available.

---

## Using Variables as Indexes

Indexes can be stored in variables.

```python
animals = ["Cat", "Dog", "Bird"]

position = 2

print(animals[position])
```

Output:

```text
Bird
```

This is useful when processing collections inside loops.

---

## Using len() with Indexing

The `len()` function returns the number of elements.

```python
numbers = [5, 10, 15, 20]

print(len(numbers))
```

Output:

```text
4
```

The last valid positive index is always:

```text
len(collection) - 1
```

Example:

```python
numbers = [5, 10, 15, 20]

print(numbers[len(numbers) - 1])
```

Output:

```text
20
```

---

## Practical Example

Store the names of students.

```python
students = ["Ali", "Sara", "Ahmed", "Fatima"]

print("First student:", students[0])
print("Last student:", students[-1])
```

Output:

```text
First student: Ali
Last student: Fatima
```

---

## Index Errors

Consider the following list:

```python
numbers = [10, 20, 30]
```

Incorrect:

```python
print(numbers[5])
```

Output:

```text
IndexError: list index out of range
```

The list contains only three elements.

Valid indexes are:

- 0
- 1
- 2

Always ensure the requested index exists.

---

## Advantages

Indexing offers several benefits:

- Fast access to individual elements.
- Simple and readable syntax.
- Works naturally with loops.
- Supports both positive and negative positions.
- Makes processing collections more efficient.

---

## Limitations

Indexing also has limitations.

- Only ordered collections support numeric indexing.
- Invalid indexes raise an `IndexError`.
- Sets cannot be indexed.
- Dictionaries require keys instead of numeric indexes.

---

## Common Beginner Mistakes

### Assuming Indexes Start at One

Incorrect:

```python
numbers = [10, 20, 30]

print(numbers[1])
```

Expecting:

```text
10
```

Actual output:

```text
20
```

Python starts indexing at zero.

---

### Accessing an Invalid Index

```python
numbers = [1, 2, 3]

print(numbers[10])
```

This raises an `IndexError`.

---

### Trying to Modify a Tuple

```python
coordinates = (10, 20)

coordinates[0] = 15
```

This raises a `TypeError`.

---

### Indexing a Set

```python
colors = {"Red", "Green"}

print(colors[0])
```

Sets do not support indexing.

---

### Confusing Dictionary Keys with Numeric Indexes

Incorrect:

```python
student = {
    "name": "Ali"
}

print(student[0])
```

Use the key instead.

```python
print(student["name"])
```

---

## Best Practices

- Remember that indexing starts at 0.
- Use negative indexing when accessing elements from the end.
- Check the size of a collection with `len()` when necessary.
- Use descriptive variable names for indexes.
- Avoid hardcoding index values unless appropriate.
- Ensure an index exists before accessing it.

---

## Performance Considerations

Accessing an element by index in a list or tuple is very efficient because Python stores these collections in a way that supports direct access by position.

Dictionary lookups by key are also highly efficient due to their hash table implementation.

Sets do not support indexing because they are optimized for fast membership testing rather than positional access.

---

## Real-World Use Cases

Indexing is commonly used for:

- Accessing the first or last item in a collection.
- Processing student records.
- Reading sensor measurements.
- Selecting menu options.
- Retrieving product information.
- Working with rows of data.
- Processing AI and machine learning datasets.
- Handling sequences of values in scientific computing.

---

# Summary

Indexing allows you to access individual elements within ordered Python collections. Python uses zero-based indexing, meaning the first element has an index of `0`. Lists and tuples support both positive and negative indexing, while dictionaries use keys instead of numeric indexes, and sets do not support indexing at all.

---

# Key Takeaways

- Indexing retrieves individual elements from a collection.
- Python uses zero-based indexing.
- Negative indexes count from the end.
- Lists and tuples support numeric indexing.
- Dictionaries use keys instead of numeric indexes.
- Sets cannot be indexed.
- Invalid indexes raise an `IndexError`.

---

# What's Next

In the next lesson, **Slicing**, you will learn how to extract multiple elements from lists, tuples, and other ordered collections using Python's slicing syntax.