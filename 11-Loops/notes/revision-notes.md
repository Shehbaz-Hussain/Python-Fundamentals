# Revision Notes: Loops in Python

## Overview

Loops allow a program to execute the same block of code multiple times without writing duplicate code. They are one of the most important programming constructs and are widely used in software development for automation, repetition, and data processing.

Python provides two primary types of loops:

- `for` loop
- `while` loop

---

# Why Use Loops?

Without loops, repetitive tasks require writing the same statements multiple times.

Instead of writing:

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

A loop makes the code shorter and easier to maintain.

```python
for count in range(5):
    print("Hello")
```

---

# Types of Loops

| Loop | Purpose |
|------|---------|
| `for` | Repeat a known number of times |
| `while` | Repeat while a condition remains True |

---

# for Loop

A `for` loop repeats code for every value produced by `range()`.

### Syntax

```python
for variable in range(start, stop, step):
    # code
```

### Example

```python
for number in range(1, 6):
    print(number)
```

Output

```
1
2
3
4
5
```

---

# while Loop

A `while` loop continues executing as long as its condition evaluates to `True`.

### Syntax

```python
while condition:
    # code
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# The range() Function

The `range()` function generates a sequence of numbers.

### One Argument

```python
range(5)
```

Produces

```
0 1 2 3 4
```

---

### Two Arguments

```python
range(1, 6)
```

Produces

```
1 2 3 4 5
```

---

### Three Arguments

```python
range(2, 11, 2)
```

Produces

```
2 4 6 8 10
```

---

# Nested Loops

A loop placed inside another loop is called a nested loop.

Example

```python
for row in range(3):
    for column in range(3):
        print("*", end="")
    print()
```

Output

```
***
***
***
```

---

# break Statement

The `break` statement immediately terminates the nearest loop.

Example

```python
for number in range(1, 11):
    if number == 6:
        break

    print(number)
```

Output

```
1
2
3
4
5
```

---

# continue Statement

The `continue` statement skips the remaining code in the current iteration and moves to the next iteration.

Example

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

Output

```
1
2
4
5
```

---

# pass Statement

The `pass` statement performs no action.

It acts as a placeholder for code that will be added later.

Example

```python
for number in range(5):
    pass
```

---

# Loop else

The `else` block executes only if the loop finishes normally.

If the loop is terminated using `break`, the `else` block is skipped.

Example

```python
for number in range(1, 6):
    print(number)
else:
    print("Loop completed.")
```

---

# Common Applications of Loops

Loops are commonly used for:

- Printing patterns
- Multiplication tables
- Counting
- Repeating user input
- Searching
- Menu-driven programs
- Password validation
- Number processing
- Simple games
- Automation of repetitive tasks

---

# Common Mistakes

### Forgetting to update the loop variable

```python
count = 1

while count <= 5:
    print(count)
```

This creates an infinite loop.

Correct version

```python
count += 1
```

---

### Incorrect range()

Incorrect

```python
range(1, 5)
```

Expected output

```
1 2 3 4 5
```

Actual output

```
1 2 3 4
```

Remember:

The stop value is **not included**.

---

### Misusing break

Using `break` ends the entire loop immediately.

Use it only when the loop should stop completely.

---

### Misusing continue

`continue` skips only the current iteration.

It does **not** stop the loop.

---

# Best Practices

- Choose `for` loops when the number of iterations is known.
- Choose `while` loops when repetition depends on a condition.
- Use meaningful variable names.
- Keep loop bodies simple and readable.
- Avoid unnecessary nested loops.
- Update loop variables correctly.
- Use `break` only when early termination is required.
- Use `continue` only when skipping specific iterations improves readability.
- Maintain proper indentation.

---

# Summary

After completing this module, you should be able to:

- Explain why loops are used.
- Write `for` loops.
- Write `while` loops.
- Use the `range()` function effectively.
- Create nested loops.
- Control loop execution using `break`.
- Skip iterations using `continue`.
- Use `pass` as a placeholder.
- Understand the purpose of loop `else`.
- Build beginner-friendly programs using loops.