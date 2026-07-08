# Module 06 – Type Conversion

> Learn how to convert data between different Python data types.

---

# Module Overview

Welcome to **Module 06: Type Conversion**.

In previous modules, you learned about:

- Python basics
- Variables
- Data types
- User input and output

Now it's time to learn how to **change one data type into another**.

Type conversion is one of the most frequently used concepts in Python programming. Since user input is always received as text (`str`), converting data into the correct type is essential for performing calculations, making comparisons, and building real-world applications.

Understanding type conversion is an important step toward writing practical Python programs and preparing for future topics such as conditional statements, loops, functions, and object-oriented programming.

---

# Learning Objectives

After completing this module, you will be able to:

- Understand what type conversion is.
- Explain why type conversion is important.
- Differentiate between implicit and explicit type conversion.
- Use Python's built-in conversion functions.
- Convert strings to integers and floating-point numbers.
- Convert numbers to strings.
- Convert values to Boolean.
- Check the type of variables using `type()`.
- Handle user input correctly using type conversion.
- Avoid common conversion mistakes.

---

# Prerequisites

Before starting this module, you should already know:

- Python installation
- Running Python programs
- Variables
- Basic data types
- Comments
- print()
- input()
- Basic arithmetic operators

If you have completed Modules **01–05**, you are ready.

---

# Folder Structure

```
06-Type-Conversion/
│
├── README.md
│
├── theory/
│   ├── 01-what-is-type-conversion.md
│   ├── 02-implicit-type-conversion.md
│   ├── 03-explicit-type-conversion.md
│   ├── 04-built-in-conversion-functions.md
│   ├── 05-common-errors.md
│   ├── 06-best-practices.md
│   └── 07-summary.md
│
├── examples/
│
├── exercises/
│
├── projects/
│
├── notes/
│
├── quiz/
│
├── cheat-sheet/
│
├── assignments/
│
└── images/
```

---

# Topics Covered

This module covers the following concepts:

## 1. What is Type Conversion?

- Definition
- Purpose
- Real-world importance

---

## 2. Implicit Type Conversion

- Automatic conversion by Python
- Integer to float conversion
- Numeric expressions

---

## 3. Explicit Type Conversion

- Manual conversion
- Using built-in functions
- Practical examples

---

## 4. Built-in Conversion Functions

You will learn how to use:

- `int()`
- `float()`
- `str()`
- `bool()`
- `type()`

---

## 5. User Input Conversion

Since `input()` always returns a string, you will learn how to convert user input into:

- Integer
- Float
- Boolean (basic understanding)

---

## 6. Common Errors

Learn why these errors happen:

- Invalid integer conversion
- Invalid float conversion
- Incorrect arithmetic on strings
- Mixing incompatible data types

---

## 7. Best Practices

Learn professional coding habits such as:

- Convert input immediately.
- Use meaningful variable names.
- Check data types with `type()`.
- Keep code readable.
- Add comments where helpful.

---

# Why Type Conversion Matters

Almost every Python program uses type conversion.

Examples include:

- Age calculators
- BMI calculators
- Shopping bills
- Marks calculators
- AI data preprocessing
- Scientific calculations
- Data analysis

Without type conversion, many programs cannot perform calculations correctly.

---

# Learning Outcomes

After finishing this module, you should be able to write programs that:

- Accept numeric input from users.
- Perform arithmetic calculations.
- Display correct results.
- Convert between common data types.
- Understand Python's automatic conversions.
- Debug simple conversion problems.

---

# Practice Guide

For the best learning experience:

### Step 1

Read the theory carefully.

---

### Step 2

Run every example program.

---

### Step 3

Modify the example values.

---

### Step 4

Complete all exercises without looking at the solutions.

---

### Step 5

Build the mini projects.

---

### Step 6

Review the notes and cheat sheet.

---

### Step 7

Attempt the quiz.

---

# Common Mistakes

Beginners often make these mistakes:

❌ Forgetting that `input()` returns a string.

❌ Trying to add strings and numbers together.

❌ Using `int()` on decimal numbers written as text.

Example:

```python
int("3.5")
```

This causes an error.

Instead use:

```python
float("3.5")
```

---

❌ Forgetting to convert user input before calculations.

Incorrect:

```python
age = input("Age: ")
print(age + 5)
```

Correct:

```python
age = int(input("Age: "))
print(age + 5)
```

---

# Real-World Applications

Type conversion is used in:

- Banking software
- Student management systems
- Shopping applications
- Medical systems
- AI data preprocessing
- Machine learning datasets
- Data science
- Scientific computing
- Business analytics

---

# Tips for Success

- Practice every example.
- Read error messages carefully.
- Experiment with different values.
- Use `type()` frequently.
- Build small programs on your own.
- Focus on understanding instead of memorizing.

---

# Module Summary

In this module, you learned how Python converts data from one type to another.

You explored:

- Implicit type conversion
- Explicit type conversion
- `int()`
- `float()`
- `str()`
- `bool()`
- `type()`
- User input conversion
- Common mistakes
- Best practices

These skills form an essential foundation for future Python topics such as conditional statements, loops, functions, file handling, and artificial intelligence applications.

---

## Next Module

➡️ **Module 07 – Operators**

In the next module, you will learn how to perform arithmetic, comparison, logical, assignment, and other operations using Python operators.

Happy Coding! 🚀