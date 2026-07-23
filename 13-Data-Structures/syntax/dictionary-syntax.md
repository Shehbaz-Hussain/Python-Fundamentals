# Dictionary Syntax

## Overview

A **dictionary** is a built-in Python data structure that stores data as **key-value pairs**. Each key is unique and is associated with a specific value.

Unlike lists and tuples, which use numeric indexes, dictionaries use **keys** to access values.

Dictionaries are:

- Ordered (Python 3.7+ preserves insertion order)
- Mutable
- Dynamic in size
- Efficient for key-based lookups

Dictionaries are commonly used to represent structured information such as student records, employee details, product information, and application settings.

They are created using curly braces (`{}`) or the `dict()` constructor.

---

# Basic Syntax

## Creating an Empty Dictionary

```python
empty_dictionary = {}
```

Explanation:

- `{}` creates an empty dictionary.
- Unlike sets, empty curly braces create a dictionary.

---

## Creating a Dictionary

```python
student = {
    "name": "Ali",
    "age": 20,
    "program": "BSAI"
}
```

Explanation:

- Keys and values are separated by a colon (`:`).
- Each key-value pair is separated by a comma.
- Keys must be unique.

---

## Creating a Dictionary with Different Value Types

```python
employee = {
    "name": "Sara",
    "age": 25,
    "salary": 75000.50,
    "full_time": True
}
```

Explanation:

Dictionary values can have different data types.

---

## Nested Dictionary

```python
student = {
    "name": "Ahmed",
    "marks": {
        "Python": 90,
        "Statistics": 85
    }
}
```

Explanation:

The value associated with `"marks"` is another dictionary.

---

# Syntax Variations

## Using the `dict()` Constructor

```python
student = dict(
    name="Ali",
    age=20,
    city="Gilgit"
)
```

Output:

```text
{'name': 'Ali', 'age': 20, 'city': 'Gilgit'}
```

---

## Dictionary Containing Lists

```python
student = {
    "name": "Ali",
    "subjects": [
        "Python",
        "AI",
        "Statistics"
    ]
}
```

Explanation:

Dictionary values can be lists.

---

## Dictionary Containing Tuples

```python
location = {
    "coordinates": (
        35.90,
        74.34
    )
}
```

---

# Parameters

The `dict()` constructor accepts different forms of input.

Example:

```python
student = dict(name="Ali", age=20)

print(student)
```

Output:

```text
{'name': 'Ali', 'age': 20}
```

---

# Return Values

Creating a dictionary returns a dictionary object.

Example:

```python
student = {
    "name": "Ali"
}

print(type(student))
```

Output:

```text
<class 'dict'>
```

---

# Common Patterns

## Accessing a Value

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

## Modifying a Value

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

## Adding a New Key-Value Pair

```python
student = {
    "name": "Ali"
}

student["semester"] = 4

print(student)
```

Output:

```text
{'name': 'Ali', 'semester': 4}
```

---

## Removing a Key-Value Pair

```python
student = {
    "name": "Ali",
    "age": 20
}

del student["age"]

print(student)
```

Output:

```text
{'name': 'Ali'}
```

---

## Finding the Number of Items

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

## Checking Membership

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

The `in` operator checks for keys, not values.

---

## Iterating Over Keys

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

---

## Iterating Over Values

```python
student = {
    "name": "Ali",
    "age": 20
}

for value in student.values():
    print(value)
```

Output:

```text
Ali
20
```

---

## Iterating Over Keys and Values

```python
student = {
    "name": "Ali",
    "age": 20
}

for key, value in student.items():
    print(key, value)
```

Output:

```text
name Ali
age 20
```

---

# Common Mistakes

## Using Duplicate Keys

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

The second value replaces the first because dictionary keys must be unique.

---

## Accessing a Missing Key

Incorrect:

```python
student = {
    "name": "Ali"
}

print(student["age"])
```

This raises a `KeyError`.

Always ensure the key exists before accessing it.

---

## Confusing Keys and Values

Incorrect:

```python
student = {
    "name": "Ali"
}

print(student["Ali"])
```

`"Ali"` is a value, not a key.

Correct:

```python
print(student["name"])
```

---

## Assuming Membership Checks Values

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

The `in` operator checks dictionary keys by default.

---

## Forgetting the Colon

Incorrect:

```python
student = {
    "name", "Ali"
}
```

Correct:

```python
student = {
    "name": "Ali"
}
```

Each key must be separated from its value by a colon.

---

# Best Practices

- Use meaningful, descriptive keys.
- Keep related information together.
- Avoid duplicate keys.
- Use dictionaries when data naturally forms key-value relationships.
- Choose consistent key names throughout your program.
- Follow PEP 8 naming and formatting guidelines.

---

# Examples

## Example 1

```python
book = {
    "title": "Python Programming",
    "author": "John Smith",
    "year": 2025
}

print(book)
```

Output:

```text
{'title': 'Python Programming', 'author': 'John Smith', 'year': 2025}
```

---

## Example 2

```python
product = {
    "name": "Laptop",
    "price": 85000
}

product["price"] = 90000

print(product)
```

Output:

```text
{'name': 'Laptop', 'price': 90000}
```

---

## Example 3

```python
student = {
    "name": "Fatima",
    "semester": 4
}

student["program"] = "BSAI"

print(student)
```

Output:

```text
{'name': 'Fatima', 'semester': 4, 'program': 'BSAI'}
```

---

## Example 4

```python
employee = {
    "name": "Ahmed",
    "department": "IT"
}

for key, value in employee.items():
    print(key, value)
```

Output:

```text
name Ahmed
department IT
```

---

# Summary

A dictionary stores information as **key-value pairs**, making it an excellent choice for structured data. Dictionaries are mutable, preserve insertion order in Python 3.7 and later, and provide efficient access to values using keys. They support adding, updating, deleting, and iterating over data, making them one of the most versatile data structures in Python.