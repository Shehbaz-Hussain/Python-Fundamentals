# While Loop Syntax

## Introduction

A `while` loop repeatedly executes a block of code as long as a specified condition evaluates to `True`. It is useful when the number of iterations is not known in advance and depends on a condition.

The condition is checked **before** each iteration. If the condition is `False` from the beginning, the loop body will not execute.

---

# Basic Syntax

```python
while condition:
    # Code to execute repeatedly
```

### Syntax Breakdown

| Part | Description |
|------|-------------|
| `while` | Keyword used to start a while loop |
| `condition` | A Boolean expression evaluated before every iteration |
| `:` | Indicates the beginning of the loop block |
| Indented block | Statements that execute while the condition remains `True` |

---

# Flow of Execution

1. The condition is evaluated.
2. If the condition is `True`, the loop body executes.
3. The condition is evaluated again.
4. The process repeats until the condition becomes `False`.
5. The program continues with the next statement after the loop.

---

# Simple Example

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

### Output

```text
1
2
3
4
5
```

---

# Understanding the Condition

The condition controls whether the loop continues.

Example:

```python
number = 3

while number > 0:
    print(number)
    number = number - 1
```

Output:

```text
3
2
1
```

When `number` becomes `0`, the condition `number > 0` becomes `False`, so the loop stops.

---

# Updating the Loop Variable

Most `while` loops require updating a variable inside the loop.

Example:

```python
counter = 1

while counter <= 3:
    print(counter)
    counter = counter + 1
```

Without updating `counter`, the condition would always remain `True`.

---

# Infinite Loop

An infinite loop occurs when the loop condition never becomes `False`.

Example:

```python
count = 1

while count <= 5:
    print(count)
```

Since `count` is never updated, the condition is always `True`, causing the loop to run forever.

---

# Avoiding Infinite Loops

Always ensure that something inside the loop eventually changes the condition.

Correct example:

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

---

# Using Boolean Values

A Boolean variable can directly control a loop.

```python
running = True

while running:
    print("Program is running.")
    running = False
```

Output:

```text
Program is running.
```

---

# Common Pattern

```python
variable = starting_value

while condition:
    # Perform work
    variable = updated_value
```

Example:

```python
score = 0

while score < 5:
    print("Current score:", score)
    score = score + 1
```

---

# Indentation Rules

Python uses indentation to determine which statements belong to the loop.

Correct:

```python
count = 1

while count <= 3:
    print(count)
    count = count + 1

print("Done")
```

Incorrect:

```python
count = 1

while count <= 3:
print(count)
count = count + 1
```

The incorrect example produces an `IndentationError`.

---

# Syntax Summary

| Syntax Element | Purpose |
|---------------|---------|
| `while` | Starts the loop |
| Condition | Controls repetition |
| Colon (`:`) | Begins the loop block |
| Indentation | Defines the loop body |
| Variable update | Prevents infinite loops |

---

# Best Practices

- Write clear and meaningful loop conditions.
- Update loop variables correctly.
- Keep the loop body easy to read.
- Avoid unnecessary complexity.
- Test the loop with small values first.
- Ensure the condition can eventually become `False`.

---

# Common Mistakes

| Mistake | Result |
|---------|--------|
| Forgetting to update the loop variable | Infinite loop |
| Incorrect indentation | `IndentationError` |
| Using the wrong condition | Loop executes too many or too few times |
| Changing the wrong variable | Unexpected behavior |

---

# Key Points

- A `while` loop repeats as long as its condition is `True`.
- The condition is checked before every iteration.
- The loop may execute zero or more times.
- Loop variables should usually be updated inside the loop.
- Proper indentation is required for correct execution.
```