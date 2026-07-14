# While Loop

## Introduction

A **`while` loop** repeatedly executes a block of code **as long as a specified condition evaluates to `True`**.

It is most useful when the number of repetitions is **not known in advance**. Before each iteration, Python evaluates the loop condition. If the condition is `True`, the loop body executes. If it is `False`, the loop terminates.

---

# Syntax

```python
while condition:
    statement(s)
```

- `while` is a Python keyword.
- `condition` must evaluate to either `True` or `False`.
- The indented statements form the **loop body**.

---

# Flow of Execution

The execution of a `while` loop follows these steps:

1. Evaluate the condition.
2. If the condition is `True`, execute the loop body.
3. Return to the condition.
4. Repeat the process.
5. When the condition becomes `False`, exit the loop.

Flow diagram:

```text
           Start
             │
             ▼
    Evaluate Condition
             │
      ┌──────┴──────┐
      │             │
   True          False
      │             │
      ▼             ▼
 Execute Body      End
      │
      └─────────────┘
```

---

# Example 1: Print Numbers from 1 to 5

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

**Output**

```text
1
2
3
4
5
```

### How It Works

| Iteration | `count` Before | Condition (`count <= 5`) | Output | `count` After |
|-----------|---------------:|:-------------------------:|--------|--------------:|
| 1 | 1 | True | 1 | 2 |
| 2 | 2 | True | 2 | 3 |
| 3 | 3 | True | 3 | 4 |
| 4 | 4 | True | 4 | 5 |
| 5 | 5 | True | 5 | 6 |
| 6 | 6 | False | — | Loop ends |

---

# Example 2: Print a Message Three Times

```python
count = 1

while count <= 3:
    print("Welcome to Python!")
    count = count + 1
```

**Output**

```text
Welcome to Python!
Welcome to Python!
Welcome to Python!
```

---

# Example 3: Countdown

```python
number = 5

while number >= 1:
    print(number)
    number = number - 1

print("Done!")
```

**Output**

```text
5
4
3
2
1
Done!
```

---

# Importance of Updating the Loop Variable

A `while` loop usually depends on a variable whose value changes during each iteration.

Correct:

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

If the update statement is omitted:

```python
count = 1

while count <= 5:
    print(count)
```

the condition never changes, so the loop never ends.

---

# Infinite Loops

An **infinite loop** is a loop whose condition never becomes `False`.

Example:

```python
while True:
    print("Running...")
```

This loop continues indefinitely unless interrupted or terminated by another mechanism.

Infinite loops are useful in some applications (such as servers or interactive programs), but they are often caused by programming errors.

---

# Common Uses of `while` Loops

Use a `while` loop when:

- The number of repetitions is unknown.
- Repetition depends on a condition.
- The program must continue until the user chooses to stop.
- A value must be validated before proceeding.
- A task continues until a specific event occurs.

Examples include:

- Login systems
- Menu-driven programs
- Input validation
- Number guessing games
- Countdown timers

---

# Common Mistakes

## 1. Forgetting to Update the Loop Variable

```python
count = 1

while count <= 5:
    print(count)
```

Result: Infinite loop.

---

## 2. Incorrect Loop Condition

```python
count = 1

while count >= 5:
    print(count)
    count = count + 1
```

Result: The loop never executes because the condition is `False` initially.

---

## 3. Incorrect Indentation

```python
count = 1

while count <= 5:
print(count)
```

Result: `IndentationError`

---

# Best Practices

- Ensure the loop condition can eventually become `False`.
- Update the loop variable correctly.
- Keep the loop body simple and readable.
- Use meaningful variable names.
- Test boundary cases to verify the loop starts and stops correctly.

---

# Key Points

- A `while` loop repeats **while** its condition is `True`.
- The condition is checked **before** every iteration.
- The loop body executes only if the condition is `True`.
- A `while` loop may execute **zero or more times**.
- Failing to update the loop state can cause an infinite loop.

---

# Summary

The `while` loop is ideal for situations where repetition depends on a condition rather than a predetermined number of iterations. Understanding how the condition, loop body, and loop variable work together is essential for writing correct and efficient Python programs.