# Nested Data Structures

## Introduction

So far, you have learned about Python's four primary built-in data structures:

- Lists
- Tuples
- Sets
- Dictionaries

In real-world applications, a single data structure is often not enough to represent complex information. Instead, one data structure is placed inside another. This is known as **nesting**.

A **nested data structure** is a data structure that contains one or more other data structures as its elements or values.

For example, a school management system may store multiple students, where each student has a name, age, and marks. Representing such information usually requires combining lists and dictionaries.

Nested data structures allow programmers to model real-world data more naturally and are widely used in web development, data analysis, artificial intelligence, machine learning, and many other fields.

---

# Learning Objectives

After completing this lesson, you should be able to:

- Define a nested data structure.
- Create nested lists.
- Create nested tuples.
- Create nested dictionaries.
- Combine different data structures.
- Access elements in nested structures.
- Modify nested mutable objects.
- Understand practical applications of nested data structures.
- Avoid common mistakes when working with nested collections.

---

# Why This Topic Matters

Suppose you need to store information about three students.

Using separate variables quickly becomes difficult.

```python
student1 = "Ali"
student2 = "Sara"
student3 = "Ahmed"
```

A better approach is to use a list.

```python
students = ["Ali", "Sara", "Ahmed"]
```

Now suppose you also need to store each student's age.

A simple list is no longer sufficient.

Instead, you can combine dictionaries and lists.

```python
students = [
    {"name": "Ali", "age": 20},
    {"name": "Sara", "age": 21},
    {"name": "Ahmed", "age": 19}
]
```

This structure is much more organized and easier to work with.

---

# Concept Explanation

## What Is a Nested Data Structure?

A nested data structure is a collection that contains another collection.

Examples include:

- List inside a list
- Tuple inside a tuple
- Dictionary inside a dictionary
- List inside a dictionary
- Dictionary inside a list

There is no fixed limit to how deeply data structures can be nested, although excessive nesting can make code harder to understand.

---

## Nested Lists

A list can contain other lists.

Example:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
```

Output:

```text
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Each element of the outer list is itself a list.

---

## Accessing Nested List Elements

To access an element, use multiple indexes.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])
```

Output:

```text
6
```

Explanation:

- `matrix[1]` returns the second list.
- `[2]` accesses the third element of that list.

---

## Modifying Nested Lists

Since lists are mutable, nested lists can also be modified.

```python
matrix = [
    [1, 2],
    [3, 4]
]

matrix[0][1] = 20

print(matrix)
```

Output:

```text
[[1, 20], [3, 4]]
```

---

## Nested Tuples

Tuples can contain other tuples.

```python
coordinates = (
    (10, 20),
    (30, 40),
    (50, 60)
)

print(coordinates)
```

Output:

```text
((10, 20), (30, 40), (50, 60))
```

Accessing an element:

```python
print(coordinates[2][0])
```

Output:

```text
50
```

Remember that tuples are immutable, so their elements cannot be modified.

---

## Nested Dictionaries

A dictionary can store another dictionary as one of its values.

```python
student = {
    "name": "Ali",
    "marks": {
        "Python": 90,
        "Mathematics": 85
    }
}

print(student)
```

Output:

```text
{'name': 'Ali', 'marks': {'Python': 90, 'Mathematics': 85}}
```

---

## Accessing Nested Dictionary Values

Use multiple keys.

```python
student = {
    "name": "Ali",
    "marks": {
        "Python": 90,
        "Mathematics": 85
    }
}

print(student["marks"]["Python"])
```

Output:

```text
90
```

---

## List of Dictionaries

One of the most common nested structures is a list containing dictionaries.

```python
students = [
    {"name": "Ali", "age": 20},
    {"name": "Sara", "age": 21},
    {"name": "Ahmed", "age": 19}
]

print(students)
```

Output:

```text
[
    {'name': 'Ali', 'age': 20},
    {'name': 'Sara', 'age': 21},
    {'name': 'Ahmed', 'age': 19}
]
```

Accessing a value:

```python
print(students[1]["name"])
```

Output:

```text
Sara
```

---

## Dictionary Containing Lists

A dictionary can also contain lists.

```python
student = {
    "name": "Ali",
    "subjects": ["Python", "Statistics", "AI"]
}

print(student)
```

Output:

```text
{'name': 'Ali', 'subjects': ['Python', 'Statistics', 'AI']}
```

Accessing a subject:

```python
print(student["subjects"][0])
```

Output:

```text
Python
```

---

## Combining Multiple Data Structures

Python allows different data structures to be combined.

Example:

```python
data = {
    "student": {
        "name": "Ali",
        "marks": [85, 90, 88],
        "location": (35.9, 74.3)
    }
}

print(data["student"]["marks"][1])
```

Output:

```text
90
```

This example combines:

- Dictionary
- Dictionary
- List
- Tuple

---

## Practical Example

Store classroom information.

```python
classroom = [
    {
        "name": "Ali",
        "subjects": ["Python", "AI"]
    },
    {
        "name": "Sara",
        "subjects": ["Statistics", "Python"]
    }
]

print(classroom[0]["subjects"][1])
```

Output:

```text
AI
```

---

## Advantages

Nested data structures provide several benefits:

- Represent complex information naturally.
- Keep related data together.
- Improve code organization.
- Make programs easier to maintain.
- Support real-world data modeling.

---

## Limitations

Nested structures also have some limitations.

- Code becomes more difficult to read as nesting increases.
- Access expressions may become lengthy.
- Deep nesting can make debugging more challenging.
- Choosing the wrong structure can make programs harder to maintain.

---

## Common Beginner Mistakes

### Forgetting Multiple Indexes

Incorrect:

```python
matrix = [
    [1, 2],
    [3, 4]
]

print(matrix[1])
```

Output:

```text
[3, 4]
```

To access `4`:

```python
print(matrix[1][1])
```

---

### Using the Wrong Key

```python
student = {
    "marks": {
        "Python": 90
    }
}

print(student["Python"])
```

This raises a `KeyError`.

Correct:

```python
print(student["marks"]["Python"])
```

---

### Assuming Every Nested Object Is Mutable

A tuple inside a list remains immutable.

```python
data = [(10, 20)]

data[0][0] = 15
```

This raises a `TypeError`.

---

### Excessive Nesting

Avoid creating structures that are unnecessarily deep.

Prefer clear, readable data organization.

---

## Best Practices

- Keep nesting as simple as possible.
- Use meaningful key names in dictionaries.
- Choose the appropriate data structure for each level.
- Keep related information together.
- Use descriptive variable names.
- Follow PEP 8 naming conventions.
- Add comments when nested structures become complex.

---

## Performance Considerations

Accessing elements in nested structures requires multiple indexing or key lookup operations.

For most beginner programs, this has little impact on performance.

However, very deeply nested structures can make code harder to read and maintain.

Prioritize clarity and correctness over unnecessary complexity.

---

## Real-World Use Cases

Nested data structures are commonly used for:

- Student management systems
- Product catalogs
- Shopping carts
- Employee records
- Weather reports
- Configuration files
- API responses
- JSON data
- Machine learning datasets
- Artificial intelligence applications

---

# Summary

Nested data structures combine multiple Python collections to represent complex information. Lists, tuples, sets, and dictionaries can be nested in various ways to model real-world data. Understanding how to create, access, and modify nested structures is an essential skill for writing practical Python programs.

---

# Key Takeaways

- A nested data structure contains one or more other data structures.
- Lists and dictionaries are commonly nested together.
- Multiple indexes or keys are used to access nested values.
- Mutable nested objects can be modified.
- Tuples remain immutable even when nested.
- Keep nested structures organized and easy to understand.
- Nested data structures are widely used in real-world Python applications.

---

# What's Next

In the next lesson, **Common Built-in Functions**, you will learn how Python's built-in functions such as `len()`, `max()`, `min()`, `sum()`, `sorted()`, and others can be used effectively with data structures.