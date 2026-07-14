# The `continue` Statement

## Introduction

The **`continue`** statement is a loop control statement that **skips the remaining statements in the current iteration** and immediately moves to the next iteration of the loop.

Unlike the `break` statement, which terminates the loop completely, `continue` keeps the loop running and simply skips the rest of the current iteration.

The `continue` statement can be used with both `while` loops and `for` loops.

---

# Why Use `continue`?

Sometimes you want to ignore certain values or situations without stopping the entire loop.

Examples include:

- Skipping negative numbers.
- Ignoring invalid input.
- Processing only even numbers.
- Skipping specific values in a sequence.

The `continue` statement allows the loop to proceed directly to the next iteration.

---

# Syntax

```python
continue
```

The `continue` statement is typically used inside an `if` statement.

Example:

```python
if condition:
    continue
```

---

# Example 1: Using `continue` with a `for` Loop

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

**Output**

```text
1
2
4
5
```

### Explanation

| Iteration | `number` | Action |
|-----------|---------:|--------|
| 1 | 1 | Print 1 |
| 2 | 2 | Print 2 |
| 3 | 3 | `continue` skips `print()` |
| 4 | 4 | Print 4 |
| 5 | 5 | Print 5 |

The value `3` is skipped, but the loop continues.

---

# Example 2: Using `continue` with a `while` Loop

```python
count = 0

while count < 5:
    count = count + 1

    if count == 3:
        continue

    print(count)
```

**Output**

```text
1
2
4
5
```

Notice that the loop variable is updated **before** the `continue` statement.

---

# Example 3: Print Only Even Numbers

```python
for number in range(1, 11):
    if number % 2 != 0:
        continue

    print(number)
```

**Output**

```text
2
4
6
8
10
```

The loop skips all odd numbers.

---

# Example 4: Skip Negative Numbers

```python
for number in range(-2, 4):
    if number < 0:
        continue

    print(number)
```

**Output**

```text
0
1
2
3
```

Only non-negative numbers are printed.

---

# Flow of Execution

```text
Start Loop
     │
     ▼
Execute Loop Body
     │
     ▼
Is continue executed?
     │
 ┌───┴────┐
 │        │
No       Yes
 │        │
 ▼        ▼
Execute   Next
Remaining Iteration
Statements
```

---

# `continue` in Nested Loops

When `continue` is used inside nested loops, it affects only the nearest enclosing loop.

Example:

```python
for row in range(1, 3):
    for column in range(1, 4):
        if column == 2:
            continue

        print(row, column)
```

**Output**

```text
1 1
1 3
2 1
2 3
```

Only the current iteration of the inner loop is skipped.

---

# Common Uses

The `continue` statement is useful for:

- Skipping unwanted values.
- Ignoring invalid data.
- Filtering numbers.
- Simplifying conditional logic.
- Processing only values that meet certain conditions.

---

# Common Mistakes

## 1. Forgetting to Update the Loop Variable in a `while` Loop

Incorrect:

```python
count = 1

while count <= 5:
    if count == 3:
        continue

    count = count + 1
```

This causes an infinite loop because `count` never changes when it is `3`.

Correct:

```python
count = 1

while count <= 5:
    count = count + 1

    if count == 3:
        continue

    print(count)
```

Always ensure the loop variable is updated before executing `continue` when using a `while` loop.

---

## 2. Using `continue` Outside a Loop

Incorrect:

```python
continue
```

Result:

```text
SyntaxError
```

The `continue` statement can only be used inside a loop.

---

## 3. Expecting `continue` to End the Loop

`continue` does **not** terminate the loop.

It skips only the current iteration and then proceeds to the next one.

To terminate a loop completely, use `break`.

---

# `break` vs `continue`

| `break` | `continue` |
|----------|------------|
| Terminates the loop immediately | Skips only the current iteration |
| Remaining iterations are not executed | Remaining iterations continue |
| Execution continues after the loop | Execution continues with the next iteration |

---

# Best Practices

- Use `continue` only when it improves code readability.
- Ensure `while` loop variables are updated correctly.
- Avoid excessive use of `continue`, as it can make program flow harder to follow.
- Use meaningful conditions when deciding to skip an iteration.

---

# Key Points

- `continue` skips the rest of the current iteration.
- The loop itself continues executing.
- It works with both `for` and `while` loops.
- In nested loops, it affects only the nearest enclosing loop.
- Proper loop variable updates are especially important in `while` loops.

---

# Summary

The `continue` statement allows a loop to ignore the remainder of the current iteration without terminating the loop. It is useful when certain values or conditions should be skipped while allowing the rest of the iterations to continue. Understanding the difference between `break` and `continue` is essential for writing clear and efficient loop-based programs.