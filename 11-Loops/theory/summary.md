# Module Summary — Loops

## Overview

In this module, you learned how to use **loops** to execute a block of code repeatedly. Loops are one of the fundamental control flow mechanisms in Python and are essential for automating repetitive tasks.

Instead of writing the same statements multiple times, loops allow you to write the code once and execute it as many times as needed.

Python provides two primary looping constructs:

- `while` loop
- `for` loop

You also learned how to control loop execution using:

- `break`
- `continue`
- `pass`
- `else` with loops

These concepts form the foundation for solving a wide variety of programming problems efficiently.

---

# Topics Covered

During this module, you studied:

- Introduction to loops
- Why loops are important
- `while` loop
- `for` loop
- The `range()` function
- Nested loops
- `break` statement
- `continue` statement
- `pass` statement
- Loop `else`
- Best practices
- Common mistakes
- Interview questions

---

# Key Concepts

## Loop

A loop repeatedly executes a block of code.

---

## Iteration

One complete execution of the loop body.

---

## `while` Loop

Repeats while a condition remains `True`.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

---

## `for` Loop

Repeats once for each value in a sequence.

Example:

```python
for number in range(1, 6):
    print(number)
```

---

## `range()`

Generates a sequence of integers.

Examples:

```python
range(5)
range(1, 6)
range(2, 11, 2)
```

---

## Nested Loops

A loop inside another loop.

Example:

```python
for row in range(2):
    for column in range(3):
        print(row, column)
```

---

## `break`

Immediately exits the nearest enclosing loop.

Example:

```python
for number in range(10):
    if number == 5:
        break

    print(number)
```

---

## `continue`

Skips the rest of the current iteration and moves to the next iteration.

Example:

```python
for number in range(5):
    if number == 2:
        continue

    print(number)
```

---

## `pass`

Performs no action and is commonly used as a placeholder.

Example:

```python
for number in range(5):
    pass
```

---

## Loop `else`

Executes only if the loop finishes normally without a `break`.

Example:

```python
for number in range(3):
    print(number)
else:
    print("Completed")
```

---

# Comparison Table

| Feature | `while` Loop | `for` Loop |
|---------|--------------|------------|
| Based on | Condition | Sequence |
| Best used when | Number of iterations is unknown | Number of iterations is known |
| Variable update | Manual | Automatic |
| Infinite loop possible | Yes | Rare in normal use |

---

# Loop Control Statements

| Statement | Purpose |
|-----------|---------|
| `break` | Exit the loop immediately |
| `continue` | Skip the current iteration |
| `pass` | Do nothing (placeholder) |
| `else` | Execute after normal loop completion |

---

# Common Mistakes to Avoid

- Forgetting to update the loop variable in a `while` loop.
- Writing incorrect loop conditions.
- Incorrect indentation.
- Forgetting the colon (`:`).
- Assuming the `stop` value in `range()` is included.
- Confusing `break` and `continue`.
- Expecting `pass` to skip an iteration.
- Forgetting to reset variables in nested `while` loops.
- Using the wrong type of loop for the task.

---

# Best Practices

- Choose the appropriate loop.
- Use meaningful variable names.
- Keep loop bodies simple.
- Avoid unnecessary nesting.
- Ensure `while` loops can terminate.
- Use `break`, `continue`, and `pass` only when appropriate.
- Test boundary conditions.
- Write clean and readable code.

---

# Practical Skills Gained

After completing this module, you should be able to:

- Write `while` loops.
- Write `for` loops.
- Use the `range()` function correctly.
- Create nested loops.
- Control loop execution with `break`, `continue`, and `pass`.
- Use loop `else` appropriately.
- Avoid common looping errors.
- Solve beginner-level programming problems involving repetition.

---

# Real-World Applications

Loops are used in many areas of software development, including:

- Login systems
- ATM software
- Menu-driven applications
- Games
- Countdown timers
- Report generation
- Data processing
- Automation scripts
- Artificial intelligence and machine learning workflows

---

# Before Moving to the Next Module

Make sure you can:

- Explain the difference between `for` and `while`.
- Predict the output of simple loop programs.
- Use `range()` correctly.
- Explain when `break`, `continue`, and `pass` should be used.
- Trace the execution of nested loops.
- Understand when the loop `else` clause executes.
- Solve the exercises and projects without assistance.

---

# Final Thoughts

Loops are among the most frequently used programming constructs in Python. They enable efficient repetition, reduce code duplication, and form the basis for many algorithms and real-world applications. A solid understanding of loops will make it significantly easier to learn collections, functions, file handling, algorithms, and other advanced Python topics in the modules that follow.