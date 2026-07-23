# Introduction to Data Structures

## Introduction

In programming, data is rarely limited to a single value. Most applications need to store and process collections of related information. For example, a school management system stores lists of students, an online store maintains product inventories, and a weather application records temperature readings collected over time.

A **data structure** is a way of organizing and storing data so that it can be accessed, modified, and processed efficiently. Python provides several built-in data structures that are easy to use while remaining powerful enough for many real-world applications.

The four primary built-in data structures in Python are:

- Lists
- Tuples
- Sets
- Dictionaries

Each serves a different purpose and has unique characteristics. Choosing the appropriate data structure can make your programs simpler, more readable, and more efficient.

This module introduces these core data structures and explains when and why to use each one.

---

# Learning Objectives

After studying this topic, you should be able to:

- Define a data structure.
- Explain why data structures are important.
- Identify Python's built-in data structures.
- Understand how different data structures organize data.
- Recognize situations where a particular data structure is appropriate.
- Understand the relationship between data structures and efficient programming.

---

# Why This Topic Matters

As programs become larger, managing data efficiently becomes increasingly important.

Imagine writing a program that stores the names of 100 students. Creating 100 separate variables would be impractical:

```python
student1 = "Ali"
student2 = "Sara"
student3 = "Ahmed"
```

This approach quickly becomes difficult to maintain.

Instead, a data structure allows you to store related information together:

```python
students = ["Ali", "Sara", "Ahmed"]
```

Now the program is easier to understand, extend, and maintain.

Data structures are used in nearly every Python application, including:

- Web applications
- Mobile applications
- Automation scripts
- Scientific computing
- Artificial Intelligence
- Machine Learning
- Data Analysis
- Game development

Understanding data structures is therefore an essential programming skill.

---

# Concept Explanation

## What Is a Data Structure?

A data structure is a method of organizing multiple pieces of data into a single object.

Instead of storing many individual variables, related values are grouped together.

For example:

```python
numbers = [10, 20, 30, 40, 50]
```

Here, five integers are stored inside one list.

---

## Why Do Data Structures Exist?

Without data structures, programs would become difficult to manage.

Consider storing examination marks.

Without a data structure:

```python
mark1 = 75
mark2 = 82
mark3 = 90
mark4 = 68
```

With a list:

```python
marks = [75, 82, 90, 68]
```

The second approach is:

- Shorter
- Easier to read
- Easier to modify
- Easier to process using loops

---

## Python's Built-in Data Structures

Python provides four commonly used built-in data structures.

### 1. List

A list stores an ordered collection of items.

Example:

```python
colors = ["red", "green", "blue"]
```

Characteristics:

- Ordered
- Mutable (can be modified)
- Allows duplicate values

---

### 2. Tuple

A tuple also stores an ordered collection.

Example:

```python
coordinates = (15, 25)
```

Characteristics:

- Ordered
- Immutable (cannot be modified after creation)
- Allows duplicate values

---

### 3. Set

A set stores unique values.

Example:

```python
fruits = {"apple", "banana", "orange"}
```

Characteristics:

- Unordered
- Mutable
- Does not allow duplicate values

---

### 4. Dictionary

A dictionary stores data as key-value pairs.

Example:

```python
student = {
    "name": "Ali",
    "age": 20,
    "grade": "A"
}
```

Characteristics:

- Stores information using keys
- Mutable
- Keys must be unique

---

## How Python Stores Data Structures

Each data structure is represented internally as an object.

When you create a data structure:

```python
numbers = [1, 2, 3]
```

Python creates a list object in memory and stores a reference to that object in the variable `numbers`.

Although Python manages memory automatically, choosing the appropriate data structure affects:

- Memory usage
- Readability
- Performance
- Ease of maintenance

---

## Comparing the Main Data Structures

| Data Structure | Ordered | Mutable | Allows Duplicates |
|----------------|:------:|:-------:|:-----------------:|
| List | Yes | Yes | Yes |
| Tuple | Yes | No | Yes |
| Set | No | Yes | No |
| Dictionary | Preserves insertion order | Yes | Keys: No, Values: Yes |

---

## Practical Example

Suppose you are building a student information system.

Student names:

```python
students = ["Ali", "Sara", "Ahmed"]
```

Student ID and name:

```python
student = {
    "id": 101,
    "name": "Ali"
}
```

Unique course names:

```python
courses = {"Python", "AI", "Statistics"}
```

Fixed classroom coordinates:

```python
location = (35, 42)
```

Each data structure is selected because it best matches the type of information being stored.

---

## Syntax Examples

Creating a list:

```python
numbers = [1, 2, 3]
```

Creating a tuple:

```python
numbers = (1, 2, 3)
```

Creating a set:

```python
numbers = {1, 2, 3}
```

Creating a dictionary:

```python
student = {
    "name": "Ali",
    "age": 20
}
```

---

## Output Example

```python
numbers = [10, 20, 30]

print(numbers)
```

Output:

```text
[10, 20, 30]
```

---

# Advantages

Using data structures provides several benefits:

- Organize related data logically.
- Reduce the number of variables.
- Simplify code.
- Improve readability.
- Enable efficient searching and processing.
- Work naturally with loops and functions.
- Support larger and more complex programs.

---

# Limitations

Choosing the wrong data structure can create problems.

For example:

- Using a list when duplicate values should not exist.
- Using a tuple when the data needs to change later.
- Using a set when item order matters.
- Using a dictionary when only sequential data is required.

Understanding each structure's characteristics helps avoid these issues.

---

# Common Beginner Mistakes

### Confusing Lists and Tuples

Lists use square brackets:

```python
numbers = [1, 2, 3]
```

Tuples use parentheses:

```python
numbers = (1, 2, 3)
```

---

### Expecting Sets to Preserve Position

Sets are unordered.

Do not assume items will appear in the same position every time.

---

### Using Duplicate Dictionary Keys

Incorrect:

```python
student = {
    "name": "Ali",
    "name": "Sara"
}
```

The second `"name"` replaces the first because dictionary keys must be unique.

---

### Choosing a Data Structure Without Considering the Problem

Always think about:

- Does order matter?
- Can the data change?
- Should duplicates be allowed?
- Do I need key-value pairs?

Answering these questions helps you choose the right structure.

---

# Best Practices

- Choose the simplest data structure that solves the problem.
- Use descriptive variable names.
- Keep related information together.
- Avoid unnecessary nesting.
- Learn the strengths of each data structure.
- Write readable code rather than overly clever code.
- Follow PEP 8 naming and formatting conventions.

---

# Performance Considerations

Different data structures are optimized for different tasks.

For example:

- Lists are efficient for ordered collections.
- Tuples are lightweight and suitable for fixed data.
- Sets provide fast membership testing because they use hash-based lookup.
- Dictionaries provide fast access to values through unique keys.

Selecting the appropriate structure can improve both program performance and code clarity.

---

# Real-World Use Cases

Data structures appear in almost every software system.

Examples include:

- Contact lists
- Shopping carts
- Product catalogs
- Student records
- Banking transactions
- Weather measurements
- AI datasets
- Machine learning feature collections
- Configuration settings
- Game scoreboards

Learning data structures prepares you for building practical Python applications.

---

# Summary

Data structures allow programmers to organize and manage collections of related data efficiently. Python includes four primary built-in data structures—lists, tuples, sets, and dictionaries—each designed for different types of tasks. Understanding their characteristics enables you to write programs that are cleaner, easier to maintain, and better suited to real-world problems.

---

# Key Takeaways

- A data structure organizes multiple values.
- Python provides lists, tuples, sets, and dictionaries.
- Each data structure has unique strengths and limitations.
- Choosing the appropriate data structure improves program design.
- Data structures are fundamental to nearly every Python application.

---

# What's Next

In the next lesson, **Lists**, you will learn how to:

- Create lists
- Access list elements
- Modify list contents
- Add and remove items
- Use common list operations
- Apply lists in practical programming scenarios