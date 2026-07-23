# Sets

## Introduction

A **set** is one of Python's built-in data structures used to store a collection of **unique** items. Unlike lists and tuples, sets do not maintain the order of elements and automatically remove duplicate values.

Sets are particularly useful when you need to:

- Store unique data
- Remove duplicate values
- Check whether an item exists in a collection
- Perform mathematical set operations such as union, intersection, and difference

Examples include storing unique student IDs, programming languages known by employees, or unique words in a document.

Because of their efficient membership testing and support for mathematical operations, sets are widely used in data processing, web development, machine learning, and many other applications.

---

# Learning Objectives

After completing this lesson, you should be able to:

- Define a Python set.
- Create sets in different ways.
- Understand the characteristics of sets.
- Add and remove elements from a set.
- Perform common set operations.
- Recognize when a set is the appropriate data structure.
- Avoid common mistakes when using sets.

---

# Why This Topic Matters

Suppose you are collecting the names of students enrolled in a course.

Using a list:

```python
students = ["Ali", "Sara", "Ali", "Ahmed", "Sara"]
```

The list contains duplicate names.

If duplicates are not allowed, a set is a better choice:

```python
students = {"Ali", "Sara", "Ahmed"}
```

A set automatically stores only unique values.

Sets also provide very fast membership testing, making them useful when working with large collections of data.

---

# Concept Explanation

## What Is a Set?

A set is an **unordered, mutable collection of unique elements**.

Characteristics:

- Unordered
- Mutable
- Does not allow duplicate values
- Cannot be indexed
- Supports mathematical set operations

Example:

```python
numbers = {10, 20, 30, 40}
```

---

## Creating Sets

### Empty Set

An empty set must be created using the `set()` function.

```python
numbers = set()

print(numbers)
```

Output:

```text
set()
```

Using `{}` creates an empty dictionary, not an empty set.

---

### Set of Integers

```python
numbers = {1, 2, 3, 4, 5}

print(numbers)
```

Possible output:

```text
{1, 2, 3, 4, 5}
```

The display order is not guaranteed.

---

### Set of Strings

```python
languages = {"Python", "Java", "C++"}

print(languages)
```

Possible output:

```text
{'Python', 'Java', 'C++'}
```

---

## Duplicate Values

Duplicate elements are automatically removed.

```python
numbers = {10, 20, 20, 30, 10, 40}

print(numbers)
```

Output:

```text
{10, 20, 30, 40}
```

Although the printed order may vary, each value appears only once.

---

## Sets Are Unordered

Unlike lists and tuples, sets do not assign positions to elements.

```python
colors = {"Red", "Green", "Blue"}

print(colors)
```

The output order may differ between program executions.

Because sets are unordered, indexing is not supported.

Incorrect:

```python
colors[0]
```

This raises a `TypeError`.

---

## Adding Elements

### add()

Adds a single element.

```python
fruits = {"Apple", "Banana"}

fruits.add("Orange")

print(fruits)
```

Output:

```text
{'Apple', 'Banana', 'Orange'}
```

---

## Removing Elements

### remove()

Removes a specific element.

```python
fruits = {"Apple", "Banana", "Orange"}

fruits.remove("Banana")

print(fruits)
```

Output:

```text
{'Apple', 'Orange'}
```

If the value does not exist, `remove()` raises a `KeyError`.

---

### discard()

Removes an element if it exists.

```python
fruits = {"Apple", "Banana"}

fruits.discard("Mango")

print(fruits)
```

Output:

```text
{'Apple', 'Banana'}
```

Unlike `remove()`, `discard()` does not raise an error if the element is missing.

---

### pop()

Removes and returns an arbitrary element.

```python
numbers = {10, 20, 30}

removed = numbers.pop()

print(removed)
print(numbers)
```

The removed element is not predictable because sets are unordered.

---

### clear()

Removes all elements.

```python
numbers = {1, 2, 3}

numbers.clear()

print(numbers)
```

Output:

```text
set()
```

---

## Membership Testing

Sets provide fast membership testing.

```python
languages = {"Python", "Java", "C++"}

print("Python" in languages)
```

Output:

```text
True
```

---

## Iterating Through a Set

Although sets are unordered, they can be iterated over.

```python
animals = {"Cat", "Dog", "Bird"}

for animal in animals:
    print(animal)
```

The order of output is not guaranteed.

---

## Common Set Operations

### Union

Combines all unique elements.

```python
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a | set_b)
```

Output:

```text
{1, 2, 3, 4, 5}
```

---

### Intersection

Returns elements common to both sets.

```python
set_a = {1, 2, 3}
set_b = {2, 3, 4}

print(set_a & set_b)
```

Output:

```text
{2, 3}
```

---

### Difference

Returns elements present in the first set but not the second.

```python
set_a = {1, 2, 3}
set_b = {2, 3, 4}

print(set_a - set_b)
```

Output:

```text
{1}
```

---

## Practical Example

Store unique programming languages known by students.

```python
languages = {"Python", "Java", "Python", "C++", "Java"}

print(languages)
```

Output:

```text
{'Python', 'Java', 'C++'}
```

Duplicate entries are automatically removed.

---

## Advantages

Sets offer several advantages:

- Automatically remove duplicate values.
- Fast membership testing.
- Support mathematical set operations.
- Easy to add and remove elements.
- Useful for comparing collections.

---

## Limitations

Sets also have some limitations.

- Elements are unordered.
- Indexing is not supported.
- Duplicate values cannot be stored.
- Mutable elements such as lists cannot be stored inside a set.

---

## Common Beginner Mistakes

### Creating an Empty Set with `{}`

Incorrect:

```python
data = {}
```

This creates an empty dictionary.

Correct:

```python
data = set()
```

---

### Expecting Items to Remain in Order

Incorrect assumption:

```python
colors = {"Red", "Green", "Blue"}
```

Do not expect the elements to appear in a fixed order.

---

### Trying to Access Elements by Index

Incorrect:

```python
numbers = {1, 2, 3}

print(numbers[0])
```

Sets do not support indexing.

---

### Assuming Duplicate Values Are Preserved

```python
values = {5, 5, 5, 5}
```

Output:

```text
{5}
```

Only one copy of each value is stored.

---

## Best Practices

- Use sets when duplicate values are not allowed.
- Use sets for fast membership testing.
- Do not rely on the order of elements.
- Use descriptive variable names.
- Choose sets only when ordering is unimportant.
- Follow PEP 8 naming conventions.

---

## Performance Considerations

Sets are implemented using a hash table.

As a result:

- Membership testing is typically very fast.
- Adding elements is typically very fast.
- Removing elements is typically very fast.
- There is no support for indexing because elements are not stored by position.

For applications that frequently check whether a value exists, sets are often more efficient than lists.

---

## Real-World Use Cases

Sets are commonly used for:

- Removing duplicate records
- Unique student IDs
- Unique email addresses
- Tags assigned to articles
- Programming languages known by employees
- Comparing collections of data
- Data cleaning
- Machine learning preprocessing
- Keyword matching
- Access control and permissions

---

# Summary

Sets are unordered collections that store only unique elements. They automatically remove duplicates and provide efficient membership testing and mathematical set operations. Sets are an excellent choice when uniqueness is more important than preserving order.

---

# Key Takeaways

- Sets store unique values.
- Sets are unordered.
- Sets are mutable.
- Duplicate elements are automatically removed.
- Sets do not support indexing.
- Empty sets are created using `set()`.
- Common methods include `add()`, `remove()`, `discard()`, `pop()`, and `clear()`.
- Sets support union, intersection, and difference operations.

---

# What's Next

In the next lesson, **Dictionaries**, you will learn:

- How key-value pairs work
- Creating and modifying dictionaries
- Accessing values using keys
- Dictionary methods
- Practical uses of dictionaries in Python programs