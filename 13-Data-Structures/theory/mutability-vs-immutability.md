# Mutability vs Immutability

## Introduction

When working with Python data structures, an important concept to understand is **mutability**.

Some Python objects can be modified after they are created, while others cannot. This distinction affects how your programs behave, how memory is used, and which data structure you should choose for a particular task.

An object that can be changed after creation is called **mutable**.

An object that cannot be changed after creation is called **immutable**.

Understanding this difference will help you write correct, predictable, and maintainable Python programs.

---

# Learning Objectives

After completing this lesson, you should be able to:

- Define mutability and immutability.
- Identify mutable and immutable Python objects.
- Understand how modifying objects works.
- Explain the difference between changing an object and creating a new one.
- Choose appropriate data structures based on whether data should change.
- Recognize common mistakes related to mutability.

---

# Why This Topic Matters

Consider storing a list of daily temperatures.

```python
temperatures = [30, 31, 29]
```

As new measurements become available, you can update the list.

```python
temperatures[1] = 32

print(temperatures)
```

Output:

```text
[30, 32, 29]
```

Now consider storing the days of a weekend.

```python
weekend = ("Saturday", "Sunday")
```

These values should remain fixed.

Using a tuple prevents accidental changes.

Choosing between mutable and immutable data structures helps protect data and makes programs easier to understand.

---

# Concept Explanation

## What Is Mutability?

A **mutable object** can be modified after it has been created.

You can:

- Change existing elements.
- Add new elements.
- Remove existing elements.

The object itself continues to exist while its contents change.

Example:

```python
colors = ["Red", "Green", "Blue"]

colors[1] = "Yellow"

print(colors)
```

Output:

```text
['Red', 'Yellow', 'Blue']
```

The same list object now contains different data.

---

## What Is Immutability?

An **immutable object** cannot be modified after creation.

If you appear to change it, Python actually creates a new object instead.

Example:

```python
coordinates = (10, 20)
```

Attempting to modify the tuple:

```python
coordinates[0] = 15
```

Produces:

```text
TypeError
```

The tuple remains unchanged.

---

## Mutable Data Structures

The following built-in data structures are mutable:

### Lists

```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
```

Output:

```text
[1, 2, 3, 4]
```

---

### Sets

```python
languages = {"Python", "Java"}

languages.add("C++")

print(languages)
```

Possible output:

```text
{'Python', 'Java', 'C++'}
```

---

### Dictionaries

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

## Immutable Data Structures

### Tuples

```python
point = (5, 10)
```

Elements cannot be changed.

---

### Strings

Strings are also immutable.

```python
word = "Python"
```

Incorrect:

```python
word[0] = "J"
```

This raises a `TypeError`.

To obtain a different string, create a new one.

```python
word = "J" + word[1:]

print(word)
```

Output:

```text
Jython
```

The original string was not modified. A new string was created and assigned to `word`.

---

## Comparing Mutable and Immutable Objects

| Property | Mutable | Immutable |
|----------|---------|-----------|
| Can be modified after creation | Yes | No |
| Can add elements | Yes (if supported) | No |
| Can remove elements | Yes (if supported) | No |
| Can change existing elements | Yes | No |

---

## Choosing Between Mutable and Immutable Objects

Use a **mutable** data structure when:

- Data changes frequently.
- Elements need to be added.
- Elements need to be removed.
- Values need to be updated.

Examples:

- Shopping cart
- Student attendance
- Inventory list

Use an **immutable** data structure when:

- Data should remain constant.
- Accidental modification should be prevented.
- The collection represents fixed information.

Examples:

- GPS coordinates
- Days of the weekend
- Months of the year
- RGB color values

---

## Understanding Assignment

Consider the following list.

```python
numbers = [10, 20, 30]
```

Modify the second element.

```python
numbers[1] = 25

print(numbers)
```

Output:

```text
[10, 25, 30]
```

The list itself remains the same object, but one of its elements has changed.

Now consider a tuple.

```python
numbers = (10, 20, 30)
```

Attempting:

```python
numbers[1] = 25
```

Raises:

```text
TypeError
```

because tuples are immutable.

---

## Practical Example

Store classroom information.

Room number:

```python
room_number = 205
```

Student names:

```python
students = ["Ali", "Sara", "Ahmed"]
```

Coordinates of the classroom:

```python
location = (35.90, 74.34)
```

The student list may change during the semester.

The classroom coordinates remain fixed.

Different kinds of data benefit from different levels of mutability.

---

## Advantages of Mutable Objects

Mutable objects are useful because they:

- Can be updated easily.
- Support adding and removing elements.
- Are convenient for dynamic data.
- Reduce the need to create new objects for every change.

---

## Advantages of Immutable Objects

Immutable objects provide several benefits.

- Prevent accidental modification.
- Represent constant information clearly.
- Simplify reasoning about program behavior.
- Can improve reliability in many applications.

---

## Limitations

### Mutable Objects

- Can be changed accidentally.
- Programs may become harder to understand if many parts modify the same data.

### Immutable Objects

- Cannot be updated directly.
- Modifications require creating a new object.

---

## Common Beginner Mistakes

### Trying to Modify a Tuple

Incorrect:

```python
coordinates = (10, 20)

coordinates[0] = 15
```

This raises a `TypeError`.

---

### Assuming Strings Are Mutable

Incorrect:

```python
word = "Python"

word[2] = "X"
```

Strings cannot be modified by index.

---

### Using a Tuple When Frequent Changes Are Needed

If elements will change often, use a list instead.

---

### Using a List for Constant Data

If the data should never change, consider using a tuple.

This communicates your intention more clearly.

---

## Best Practices

- Use lists for collections that change.
- Use tuples for fixed collections.
- Choose dictionaries for structured information that changes.
- Use sets when uniqueness is important.
- Select the data structure that best matches the problem rather than using the same one everywhere.
- Follow PEP 8 naming conventions.

---

## Performance Considerations

Mutable objects allow in-place modification, which is convenient for changing data.

Immutable objects cannot be changed after creation. When a different value is needed, a new object is created.

In many programs, the performance difference is small. The more important consideration is choosing the data structure that accurately represents the data and its intended use.

---

## Real-World Use Cases

Mutable objects are commonly used for:

- Shopping carts
- Inventory systems
- Attendance records
- Task lists
- Sensor readings

Immutable objects are commonly used for:

- Geographic coordinates
- Calendar dates
- Configuration values
- Mathematical constants
- Fixed application settings

---

# Summary

Mutability determines whether an object can be modified after it is created. Lists, sets, and dictionaries are mutable, making them suitable for data that changes over time. Tuples and strings are immutable, making them appropriate for fixed data that should remain unchanged. Understanding this distinction helps you choose the correct data structure and write more reliable Python programs.

---

# Key Takeaways

- Mutable objects can be modified after creation.
- Immutable objects cannot be modified after creation.
- Lists, sets, and dictionaries are mutable.
- Tuples and strings are immutable.
- Choose mutable objects for changing data.
- Choose immutable objects for fixed data.
- Selecting the correct data structure improves code clarity and reliability.

---

# What's Next

In the next lesson, **Nested Data Structures**, you will learn how to combine lists, tuples, sets, and dictionaries to represent more complex data and solve real-world programming problems.