# continue Statement Syntax

# Introduction

The `continue` statement is used to skip the remaining statements in the current iteration of a loop and immediately move to the next iteration.

Unlike the `break` statement, which terminates a loop completely, `continue` keeps the loop running. It simply skips the rest of the current iteration.

The `continue` statement can be used in both `while` loops and `for` loops.

---

# Basic Syntax

```python
continue
```

The `continue` statement is usually placed inside an `if` statement so that only certain iterations are skipped.

---

# Using `continue` in a `for` Loop

```python
for number in range(1, 6):

    if number == 3:
        continue

    print(number)
```

### Output

```text
1
2
4
5
```

### Explanation

- The loop starts with `1`.
- When `number` becomes `3`, the `continue` statement executes.
- Python skips the `print()` statement for that iteration.
- The loop immediately proceeds with the next value.

---

# Using `continue` in a `while` Loop

```python
count = 0

while count < 5:
    count = count + 1

    if count == 3:
        continue

    print(count)
```

### Output

```text
1
2
4
5
```

### Explanation

The variable is updated **before** the `continue` statement. This ensures that the loop condition eventually becomes `False` and the loop ends normally.

---

# Flow of Execution

The following steps describe how `continue` works:

1. The loop begins.
2. The loop body starts executing.
3. Python reaches a `continue` statement.
4. The remaining statements in the current iteration are skipped.
5. The next iteration begins.

---

# Visual Flow

```text
Loop starts
     │
     ▼
Execute statements
     │
     ▼
Is continue executed?
     │
 ┌───┴────┐
 │        │
No       Yes
 │        │
 ▼        ▼
Execute   Skip remaining
rest of   statements
loop body │
 │        ▼
 └────────►Next iteration
```

---

# Skipping Even Numbers

```python
for number in range(1, 11):

    if number % 2 == 0:
        continue

    print(number)
```

### Output

```text
1
3
5
7
9
```

Only the odd numbers are printed because every even number is skipped.

---

# Multiple Statements After `continue`

```python
for number in range(1, 5):

    if number == 2:
        continue

    print("Current number:", number)
    print("Square:", number * number)
```

### Output

```text
Current number: 1
Square: 1
Current number: 3
Square: 9
Current number: 4
Square: 16
```

The statements after `continue` are skipped only for the iteration where `number` equals `2`.

---

# Using `continue` in Nested Loops

```python
for row in range(1, 3):
    for column in range(1, 4):

        if column == 2:
            continue

        print(row, column)
```

### Output

```text
1 1
1 3
2 1
2 3
```

The `continue` statement affects only the inner loop where it appears.

---

# `continue` vs `break`

| Feature | `continue` | `break` |
|---------|------------|----------|
| Ends the loop | No | Yes |
| Skips current iteration | Yes | No |
| Continues with next iteration | Yes | No |
| Common purpose | Ignore specific iterations | Exit the loop early |

---

# Common Mistakes

## Mistake 1: Forgetting to Update the Loop Variable

```python
count = 1

while count <= 5:

    if count == 3:
        continue

    print(count)
    count = count + 1
```

This creates an infinite loop because `count` is never updated when it becomes `3`.

---

## Correct Version

```python
count = 1

while count <= 5:

    if count == 3:
        count = count + 1
        continue

    print(count)
    count = count + 1
```

Updating the variable before `continue` allows the loop to finish correctly.

---

## Mistake 2: Using `continue` Outside a Loop

```python
continue
```

This produces an error because `continue` can only be used inside a loop.

---

# Best Practices

- Use `continue` only when skipping an iteration improves clarity.
- Keep the condition easy to understand.
- In `while` loops, update loop variables before reaching `continue` when necessary.
- Avoid excessive use of `continue`, which can make code harder to follow.

---

# Syntax Summary

| Syntax | Purpose |
|--------|---------|
| `continue` | Skips the remaining statements in the current iteration |
| `if condition:`<br>`    continue` | Skips an iteration when a condition is `True` |

---

# Key Points

- `continue` skips the rest of the current iteration.
- The loop itself continues executing.
- It works with both `for` and `while` loops.
- In `while` loops, ensure loop variables are updated correctly to avoid infinite loops.
- In nested loops, `continue` affects only the loop in which it appears.