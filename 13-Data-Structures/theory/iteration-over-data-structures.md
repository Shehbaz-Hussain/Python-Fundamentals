# Iteration over Data Structures

## Introduction

Many programming tasks require processing every element in a collection. For example, you may need to calculate the total marks of students, display all products in an inventory, or count the number of completed tasks.

Instead of accessing each element individually, Python allows you to **iterate** over a data structure. Iteration means visiting each element in a collection one at a time and performing an operation on it.

Python provides the `for` loop as the primary way to iterate over data structures. Iteration works naturally with:

- Lists
- Tuples
- Sets
- Dictionaries
- Strings

Understanding iteration is essential because it is one of the most frequently used techniques in Python programming.

---

# Learning Objectives

After completing this lesson, you should be able to:

- Define iteration.
- Iterate over lists.
- Iterate over tuples.
- Iterate over sets.
- Iterate over dictionaries.
- Use the `enumerate()` function during iteration.
- Combine loops with built-in functions.
- Apply iteration to solve practical programming problems.
- Avoid common mistakes when iterating over data structures.

---

# Why This Topic Matters

Suppose you have a list of exam marks.

```python
marks = [78, 85, 91, 67, 88]
```

Without iteration, you would need to print each mark individually.

```python
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
```

As the number of marks grows, this approach becomes impractical.

Using iteration:

```python
for mark in marks:
    print(mark)
```

The same code works whether the list contains 5 items or 5,000 items.

---

# Concept Explanation

## What Is Iteration?

Iteration is the process of visiting each element in a collection one after another.

Python automatically retrieves each element during a `for` loop.

General syntax:

```python
for item in collection:
    print(item)
```

The loop continues until every element has been processed.

---

## Iterating over a List

Lists are commonly processed using `for` loops.

```python
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)
```

Output:

```text
Apple
Banana
Orange
```

Each iteration assigns the next element to the variable `fruit`.

---

## Iterating over a Tuple

Tuples are also iterable.

```python
coordinates = (10, 20, 30)

for value in coordinates:
    print(value)
```

Output:

```text
10
20
30
```

Although tuples are immutable, their elements can still be read during iteration.

---

## Iterating over a Set

Sets can be iterated over, but the order of elements is not guaranteed.

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

The output order may differ because sets are unordered.

---

## Iterating over a Dictionary

By default, iterating over a dictionary returns its keys.

```python
student = {
    "name": "Ali",
    "age": 20,
    "program": "BSAI"
}

for key in student:
    print(key)
```

Output:

```text
name
age
program
```

---

## Iterating over Dictionary Values

Use the `values()` method.

```python
student = {
    "name": "Ali",
    "age": 20,
    "program": "BSAI"
}

for value in student.values():
    print(value)
```

Output:

```text
Ali
20
BSAI
```

---

## Iterating over Dictionary Keys and Values

Use the `items()` method.

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

This is the most common way to process dictionaries.

---

## Using enumerate()

The `enumerate()` function provides both the index and the value during iteration.

```python
subjects = ["Python", "AI", "Statistics"]

for index, subject in enumerate(subjects):
    print(index, subject)
```

Output:

```text
0 Python
1 AI
2 Statistics
```

This removes the need to manually maintain a counter.

---

## Combining Iteration with Built-in Functions

Iteration is often used together with built-in functions.

Example:

```python
marks = [75, 82, 91, 68]

total = sum(marks)

print(total)
```

Output:

```text
316
```

You can also combine iteration with conditional statements.

```python
marks = [75, 82, 91, 68]

for mark in marks:
    if mark >= 80:
        print(mark)
```

Output:

```text
82
91
```

---

## Practical Example

Display student information.

```python
students = [
    {"name": "Ali", "age": 20},
    {"name": "Sara", "age": 21},
    {"name": "Ahmed", "age": 19}
]

for student in students:
    print(student["name"], student["age"])
```

Output:

```text
Ali 20
Sara 21
Ahmed 19
```

This example combines iteration with nested data structures.

---

## Advantages

Iteration provides several benefits:

- Eliminates repetitive code.
- Works with collections of any size.
- Improves readability.
- Makes programs easier to maintain.
- Integrates naturally with Python's built-in data structures.

---

## Limitations

Iteration also has some limitations.

- Processing very large collections can take time.
- Modifying a collection while iterating over it can lead to unexpected behavior.
- Sets do not preserve order during iteration.

---

## Common Beginner Mistakes

### Modifying a List While Iterating

Incorrect:

```python
numbers = [1, 2, 3]

for number in numbers:
    numbers.remove(number)
```

Changing a collection while iterating over it can produce unexpected results.

---

### Assuming Set Order

```python
colors = {"Red", "Green", "Blue"}

for color in colors:
    print(color)
```

Do not expect the elements to appear in a particular order.

---

### Forgetting `.items()` for Dictionaries

Incorrect:

```python
student = {
    "name": "Ali"
}

for key, value in student:
    print(key, value)
```

This raises an error because iterating directly over a dictionary returns only its keys.

Correct:

```python
for key, value in student.items():
    print(key, value)
```

---

### Using Unclear Variable Names

Less readable:

```python
for x in numbers:
    print(x)
```

More readable:

```python
for number in numbers:
    print(number)
```

Choose descriptive variable names whenever possible.

---

## Best Practices

- Use meaningful loop variable names.
- Choose `enumerate()` when you need both indexes and values.
- Use `.items()` when processing dictionary keys and values together.
- Avoid modifying collections during iteration.
- Keep loop bodies simple and readable.
- Follow PEP 8 formatting guidelines.

---

## Performance Considerations

Python's `for` loop is efficient for most applications.

When working with very large collections:

- Avoid unnecessary operations inside the loop.
- Use built-in functions such as `sum()` or `max()` when appropriate.
- Keep the loop body as simple as possible.

Readable and correct code is generally more important than small performance optimizations.

---

## Real-World Use Cases

Iteration is commonly used for:

- Displaying student records.
- Processing customer information.
- Reading sensor measurements.
- Generating reports.
- Analyzing datasets.
- Cleaning data.
- Training machine learning models.
- Processing API responses.
- Managing inventory systems.
- Automating repetitive tasks.

---

# Summary

Iteration is the process of visiting each element in a collection one at a time. Python's `for` loop provides a simple and readable way to iterate over lists, tuples, sets, dictionaries, and strings. By combining iteration with built-in functions and conditional statements, you can efficiently process collections of any size.

---

# Key Takeaways

- Iteration processes one element at a time.
- The `for` loop is the primary tool for iteration in Python.
- Lists, tuples, sets, dictionaries, and strings are iterable.
- Dictionaries can be iterated using `keys()`, `values()`, or `items()`.
- `enumerate()` returns both indexes and values.
- Avoid modifying collections while iterating.
- Use descriptive variable names to improve readability.

---

# What's Next

In the next lesson, **Choosing the Right Data Structure**, you will learn how to decide whether a list, tuple, set, or dictionary is the best choice for a particular programming problem based on factors such as ordering, mutability, uniqueness, and data organization.