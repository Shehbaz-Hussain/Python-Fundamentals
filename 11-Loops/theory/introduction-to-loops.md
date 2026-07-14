# Introduction to Loops

## What Is a Loop?

A **loop** is a control flow structure that repeatedly executes a block of code as long as a specified condition is satisfied or for each item in a sequence.

Instead of writing the same statements multiple times, a loop allows you to write the code once and execute it repeatedly.

Loops make programs:

- Shorter
- Easier to read
- Easier to maintain
- More efficient

---

# Why Do We Need Loops?

Imagine you want to display the message **"Welcome to Python!"** five times.

Without loops:

```python
print("Welcome to Python!")
print("Welcome to Python!")
print("Welcome to Python!")
print("Welcome to Python!")
print("Welcome to Python!")
```

This approach has several problems:

- Repetitive code
- Difficult to maintain
- Easy to make mistakes
- Not practical for a large number of repetitions

Using a loop:

```python
for count in range(5):
    print("Welcome to Python!")
```

The loop performs the repetition automatically, making the code cleaner and easier to modify.

---

# What Can Loops Do?

Loops are used whenever a task needs to be repeated.

Common uses include:

- Displaying messages multiple times
- Counting numbers
- Processing user input repeatedly
- Performing calculations repeatedly
- Generating tables
- Drawing patterns
- Validating input
- Building interactive programs

---

# Types of Loops in Python

Python provides two primary loop statements.

## 1. `while` Loop

A `while` loop repeats a block of code **while a condition remains `True`**.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

---

## 2. `for` Loop

A `for` loop repeats a block of code for each value in a sequence.

Example:

```python
for number in range(1, 6):
    print(number)
```

---

# How a Loop Works

A loop generally follows these steps:

1. Start.
2. Check the loop condition or retrieve the next value.
3. Execute the loop body.
4. Update the loop state (if required).
5. Repeat until the loop finishes.

For a `while` loop, the condition is checked before each iteration.

For a `for` loop, Python automatically retrieves the next value from the sequence.

---

# Loop Terminology

## Iteration

One complete execution of the loop body.

Example:

```python
for number in range(3):
    print(number)
```

This loop performs **three iterations**.

---

## Loop Body

The indented block of code that is executed repeatedly.

Example:

```python
for number in range(3):
    print(number)
```

The statement

```python
print(number)
```

is the loop body.

---

## Loop Condition

A Boolean expression that determines whether a `while` loop continues executing.

Example:

```python
while count <= 5:
```

The condition is:

```python
count <= 5
```

---

## Counter Variable

A variable used to track the progress of a loop.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

Here, `count` is the counter variable.

---

# Advantages of Loops

Using loops provides several benefits:

- Reduces duplicated code.
- Improves readability.
- Simplifies repetitive tasks.
- Makes programs easier to update.
- Supports automation.
- Enables scalable solutions.

---

# Real-World Examples

Loops are commonly used in:

- ATM systems
- Login systems
- Online quizzes
- Games
- Scientific calculations
- Data processing
- AI and machine learning workflows
- Automation scripts

---

# Key Points

- A loop repeats a block of code.
- Python provides `while` and `for` loops.
- Each repetition is called an **iteration**.
- A `while` loop depends on a condition.
- A `for` loop iterates over a sequence.
- Loops reduce repetitive code and improve program structure.
- Proper loop design is essential to avoid infinite loops and logic errors.

---

# Summary

Loops are a fundamental programming concept that allows repetitive tasks to be performed efficiently. By replacing duplicated code with structured repetition, loops make programs cleaner, more maintainable, and more powerful. Understanding loops is essential before learning more advanced programming techniques.