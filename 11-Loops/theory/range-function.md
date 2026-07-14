# The `range()` Function

## Introduction

The **`range()`** function is a built-in Python function that generates a sequence of integers. It is most commonly used with a `for` loop to repeat a block of code a specific number of times.

The `range()` function **does not print numbers by itself**. Instead, it provides a sequence of values that a `for` loop iterates over.

---

# Why Use `range()`?

Without `range()`, printing the numbers from 1 to 5 would require writing each value manually.

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

Using `range()` with a `for` loop:

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

The code is shorter, easier to read, and easier to modify.

---

# Forms of `range()`

The `range()` function can be used in three different ways.

## 1. `range(stop)`

Generates numbers starting from `0` up to, but **not including**, `stop`.

### Syntax

```python
range(stop)
```

### Example

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

Notice that `5` is **not** included.

---

## 2. `range(start, stop)`

Generates numbers starting from `start` up to, but **not including**, `stop`.

### Syntax

```python
range(start, stop)
```

### Example

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

---

## 3. `range(start, stop, step)`

Generates numbers from `start` to `stop` (exclusive), increasing or decreasing by `step`.

### Syntax

```python
range(start, stop, step)
```

### Example: Counting by Twos

```python
for number in range(2, 11, 2):
    print(number)
```

Output:

```text
2
4
6
8
10
```

---

### Example: Counting Backwards

```python
for number in range(5, 0, -1):
    print(number)
```

Output:

```text
5
4
3
2
1
```

A negative step counts in reverse.

---

# Understanding the Stop Value

A common beginner mistake is assuming the `stop` value is included.

Example:

```python
for number in range(1, 5):
    print(number)
```

Output:

```text
1
2
3
4
```

The value `5` is **not** printed because the `stop` value is always excluded.

---

# Visualizing `range(1, 6)`

```text
Start                     Stop
  │                         │
  ▼                         ▼
1 → 2 → 3 → 4 → 5     6 (excluded)
```

---

# Common Uses of `range()`

The `range()` function is useful for:

- Counting numbers
- Printing multiplication tables
- Repeating an action a fixed number of times
- Creating countdowns
- Generating even or odd numbers
- Building simple patterns

---

# Examples

## Print Numbers from 1 to 10

```python
for number in range(1, 11):
    print(number)
```

---

## Print Even Numbers

```python
for number in range(2, 21, 2):
    print(number)
```

Output:

```text
2
4
6
8
10
12
14
16
18
20
```

---

## Print Odd Numbers

```python
for number in range(1, 20, 2):
    print(number)
```

Output:

```text
1
3
5
7
9
11
13
15
17
19
```

---

## Countdown

```python
for number in range(10, 0, -1):
    print(number)

print("Blast off!")
```

Output:

```text
10
9
8
7
6
5
4
3
2
1
Blast off!
```

---

# Common Mistakes

## 1. Assuming the Stop Value Is Included

Incorrect expectation:

```python
range(1, 6)
```

Expected:

```text
1 2 3 4 5 6
```

Actual:

```text
1 2 3 4 5
```

---

## 2. Using the Wrong Step

Example:

```python
range(1, 10, 3)
```

Output:

```text
1
4
7
```

The values increase by `3` each time.

---

## 3. Using a Step of Zero

Incorrect:

```python
range(1, 10, 0)
```

This raises a `ValueError` because the step cannot be zero.

---

# Best Practices

- Remember that the `stop` value is excluded.
- Use meaningful loop variable names.
- Choose an appropriate step value.
- Use a negative step when counting backwards.
- Select the simplest form of `range()` that meets your needs.

---

# Quick Reference

| Form | Description |
|------|-------------|
| `range(stop)` | Start at `0`, stop before `stop` |
| `range(start, stop)` | Start at `start`, stop before `stop` |
| `range(start, stop, step)` | Count by `step` from `start` to `stop` (exclusive) |

---

# Key Points

- `range()` generates a sequence of integers.
- It is most commonly used with `for` loops.
- The `stop` value is **never included**.
- The `step` determines how much the value changes after each iteration.
- A negative `step` counts backwards.
- `range()` simplifies repetitive counting tasks.

---

# Summary

The `range()` function is an essential tool for controlling `for` loops in Python. By generating sequences of integers, it allows programs to repeat actions efficiently without manually writing repeated values. Understanding its three forms and the fact that the `stop` value is excluded is fundamental to writing correct and predictable loop-based programs.