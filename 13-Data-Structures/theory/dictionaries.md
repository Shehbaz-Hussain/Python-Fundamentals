# Dictionaries

## Introduction

A **dictionary** is one of Python's most powerful built-in data structures. Unlike lists, tuples, and sets, which primarily store collections of values, a dictionary stores data as **key-value pairs**.

Each key uniquely identifies a value, allowing you to retrieve information quickly without relying on its position.

For example, instead of storing a student's information as a list:

```python
student = ["Ali", 20, "BSAI"]
```

you can store it in a dictionary:

```python
student = {
    "name": "Ali",
    "age": 20,
    "program": "BSAI"
}
```

The second approach is much easier to understand because every value has a descriptive key.

Dictionaries are widely used in Python programming because many real-world problems naturally involve mapping one piece of information to another.

---

# Learning Objectives

After completing this lesson, you should be able to:

- Define a Python dictionary.
- Create dictionaries in different ways.
- Access values using keys.
- Add, modify, and remove key-value pairs.
- Understand dictionary characteristics.
- Use common dictionary methods.
- Choose dictionaries for appropriate programming tasks.
- Avoid common beginner mistakes.

---

# Why This Topic Matters

Suppose you need to store information about a student.

Using a list:

```python
student = ["Ali", 20, "BSAI", "A"]
```

Someone reading the code must remember what each position represents.

Using a dictionary:

```python
student = {
    "name": "Ali",
    "age": 20,
    "program": "BSAI",
    "grade": "A"
}
```

The meaning of every value is immediately clear.

Dictionaries improve code readability, simplify data retrieval, and make programs easier to maintain.

---

# Concept Explanation

## What Is a Dictionary?

A dictionary is a **mutable collection of key-value pairs**.

Characteristics:

- Stores data as key-value pairs
- Mutable
- Keys must be unique
- Values may be duplicated
- Preserves insertion order (Python 3.7 and later)

Example:

```python
student = {
    "name": "Ali",
    "age": 20,
    "city": "Gilgit"
}
```

---

## Creating Dictionaries

### Empty Dictionary

```python
student = {}

print(student)
```

Output:

```text
{}
```

---

### Dictionary with Data

```python
student = {
    "name": "Sara",
    "age": 21,
    "department": "Computer Science"
}

print(student)
```

Output:

```text
{'name': 'Sara', 'age': 21, 'department': 'Computer Science'}
```

---

## Understanding Keys and Values

Each dictionary entry consists of:

- A **key**
- Its associated **value**

Example:

```python
book = {
    "title": "Python Basics",
    "pages": 350
}
```

Here:

- `"title"` is a key.
- `"Python Basics"` is its value.
- `"pages"` is a key.
- `350` is its value.

---

## Accessing Values

Values are accessed using their keys.

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

Another example:

```python
print(student["age"])
```

Output:

```text
20
```

---

## Adding New Key-Value Pairs

Simply assign a value to a new key.

```python
student = {
    "name": "Ali"
}

student["age"] = 20

print(student)
```

Output:

```text
{'name': 'Ali', 'age': 20}
```

---

## Modifying Existing Values

Assign a new value to an existing key.

```python
student = {
    "name": "Ali",
    "age": 20
}

student["age"] = 21

print(student)
```

Output:

```text
{'name': 'Ali', 'age': 21}
```

---

## Removing Key-Value Pairs

### pop()

Removes a key and returns its value.

```python
student = {
    "name": "Ali",
    "age": 20
}

removed = student.pop("age")

print(removed)
print(student)
```

Output:

```text
20
{'name': 'Ali'}
```

---

### clear()

Removes all key-value pairs.

```python
student = {
    "name": "Ali",
    "age": 20
}

student.clear()

print(student)
```

Output:

```text
{}
```

---

## Dictionary Length

Use `len()` to count key-value pairs.

```python
student = {
    "name": "Ali",
    "age": 20,
    "city": "Gilgit"
}

print(len(student))
```

Output:

```text
3
```

---

## Membership Testing

The `in` operator checks **keys**, not values.

```python
student = {
    "name": "Ali",
    "age": 20
}

print("name" in student)
```

Output:

```text
True
```

Example:

```python
print("Ali" in student)
```

Output:

```text
False
```

The value exists, but membership testing checks keys by default.

---

## Iterating Through a Dictionary

Loop through keys.

```python
student = {
    "name": "Ali",
    "age": 20
}

for key in student:
    print(key)
```

Output:

```text
name
age
```

Loop through values.

```python
for value in student.values():
    print(value)
```

Output:

```text
Ali
20
```

Loop through both keys and values.

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Ali
age 20
```

---

## Common Dictionary Methods

### keys()

Returns all keys.

```python
student = {
    "name": "Ali",
    "age": 20
}

print(student.keys())
```

---

### values()

Returns all values.

```python
print(student.values())
```

---

### items()

Returns key-value pairs.

```python
print(student.items())
```

---

### get()

Returns the value associated with a key.

```python
student = {
    "name": "Ali"
}

print(student.get("name"))
```

Output:

```text
Ali
```

If the key does not exist:

```python
print(student.get("age"))
```

Output:

```text
None
```

Unlike using square brackets, `get()` does not raise an error when the key is missing.

---

## Practical Example

Store information about a book.

```python
book = {
    "title": "Python Programming",
    "author": "John Smith",
    "pages": 420
}

print(book["title"])
print(book["author"])
```

Output:

```text
Python Programming
John Smith
```

---

## Advantages

Dictionaries provide several advantages:

- Fast lookup using keys.
- Clear relationship between keys and values.
- Easy to add or modify entries.
- Suitable for structured data.
- Improve code readability.

---

## Limitations

Dictionaries also have limitations.

- Keys must be unique.
- Dictionaries are generally less suitable when only sequential data is required.
- Access is based on keys rather than positions.

---

## Common Beginner Mistakes

### Using Duplicate Keys

Incorrect:

```python
student = {
    "name": "Ali",
    "name": "Sara"
}
```

Output:

```text
{'name': 'Sara'}
```

The second key replaces the first.

---

### Confusing Keys and Values

Incorrect:

```python
student = {
    "name": "Ali"
}

print(student["Ali"])
```

This raises a `KeyError` because `"Ali"` is a value, not a key.

---

### Accessing a Missing Key

```python
student = {
    "name": "Ali"
}

print(student["age"])
```

This raises a `KeyError`.

Use:

```python
print(student.get("age"))
```

when the key might not exist.

---

### Assuming Membership Checks Values

```python
student = {
    "name": "Ali"
}

print("Ali" in student)
```

Output:

```text
False
```

Membership testing checks keys.

---

## Best Practices

- Use meaningful and descriptive keys.
- Keep related information together.
- Avoid duplicate keys.
- Use `get()` when a key may not exist.
- Choose dictionaries for structured data.
- Follow PEP 8 naming conventions.

---

## Performance Considerations

Dictionaries are implemented using a hash table.

As a result:

- Looking up a value by key is typically very fast.
- Adding new key-value pairs is typically very fast.
- Updating existing values is typically very fast.
- Membership testing on keys is typically very fast.

These performance characteristics make dictionaries one of the most commonly used data structures in Python.

---

## Real-World Use Cases

Dictionaries are commonly used for:

- Student records
- Employee information
- Product catalogs
- User profiles
- Application settings
- Configuration files
- API responses
- Inventory management
- Banking records
- Machine learning feature mappings

---

# Summary

Dictionaries store information as key-value pairs, making them ideal for representing structured data. They are mutable, preserve insertion order, require unique keys, and provide efficient access to values through their associated keys. Dictionaries are one of the most useful and frequently used data structures in Python.

---

# Key Takeaways

- Dictionaries store key-value pairs.
- Keys must be unique.
- Values may be duplicated.
- Dictionaries are mutable.
- Curly braces `{}` are used to create dictionaries.
- Common methods include `get()`, `keys()`, `values()`, `items()`, `pop()`, and `clear()`.
- Membership testing checks keys by default.

---

# What's Next

In the next lesson, **Indexing**, you will learn:

- What indexing is
- Positive and negative indexing
- Accessing elements in different data structures
- Common indexing errors
- Best practices for working with indexes