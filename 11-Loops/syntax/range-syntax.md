# range() Syntax

# Introduction

The `range()` function generates a sequence of numbers. It is most commonly used with a `for` loop to repeat a block of code a specific number of times.

The numbers produced by `range()` follow a predictable pattern based on the arguments provided.

---

# Basic Syntax

```python
range(stop)
```

```python
range(start, stop)
```

```python
range(start, stop, step)
```

---

# Syntax Forms

| Syntax | Description |
|---------|-------------|
| `range(stop)` | Generates numbers starting from `0` up to, but not including, `stop`. |
| `range(start, stop)` | Generates numbers starting from `start` up to, but not including, `stop`. |
| `range(start, stop, step)` | Generates numbers from `start` to `stop`, changing by `step` each time. |

---

# 1. Using `range(stop)`

This is the simplest form.

```python
for number in range(5):
    print(number)
```

### Output

```text
0
1
2
3
4
```

Notice that the sequence starts at `0` and stops before `5`.

---

# 2. Using `range(start, stop)`

You can specify both the starting and ending values.

```python
for number in range(1, 6):
    print(number)
```

### Output

```text
1
2
3
4
5
```

The sequence starts at `1` and stops before `6`.

---

# 3. Using `range(start, stop, step)`

The third argument controls how much the value changes after each iteration.

```python
for number in range(2, 11, 2):
    print(number)
```

### Output

```text
2
4
6
8
10
```

Here, the numbers increase by `2` each time.

---

# Using a Negative Step

A negative step generates numbers in descending order.

```python
for number in range(5, 0, -1):
    print(number)
```

### Output

```text
5
4
3
2
1
```

The value decreases by `1` during each iteration.

---

# Understanding the Stop Value

One of the most important rules is that the **stop value is never included**.

Example:

```python
for number in range(3):
    print(number)
```

Output:

```text
0
1
2
```

Although the stop value is `3`, it is not printed.

---

# Common Patterns

## Count from 0

```python
for number in range(5):
    print(number)
```

---

## Count from 1

```python
for number in range(1, 6):
    print(number)
```

---

## Count by Twos

```python
for number in range(0, 11, 2):
    print(number)
```

---

## Count Backwards

```python
for number in range(10, 0, -2):
    print(number)
```

---

# How `range()` Works in a Loop

Consider the following code:

```python
for number in range(1, 4):
    print(number)
```

The loop receives the following values one by one:

| Iteration | Value of `number` |
|-----------|-------------------|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |

After the last value, the loop ends.

---

# Common Mistakes

## Mistake 1: Expecting the Stop Value to Be Included

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

The value `5` is **not** included.

---

## Mistake 2: Using a Step of Zero

```python
range(1, 10, 0)
```

A step value of `0` is not allowed because the sequence cannot progress.

---

## Mistake 3: Using the Wrong Step Direction

```python
for number in range(1, 6, -1):
    print(number)
```

This loop produces no output because the sequence cannot move from `1` to `6` using a negative step.

---

# Best Practices

- Use `range()` with a `for` loop when repeating code a fixed number of times.
- Remember that the stop value is excluded.
- Choose meaningful start, stop, and step values.
- Use a positive step for ascending sequences.
- Use a negative step for descending sequences.

---

# Syntax Summary

| Form | Example | Output |
|------|---------|--------|
| `range(stop)` | `range(5)` | `0 1 2 3 4` |
| `range(start, stop)` | `range(2, 6)` | `2 3 4 5` |
| `range(start, stop, step)` | `range(2, 11, 2)` | `2 4 6 8 10` |
| Negative step | `range(5, 0, -1)` | `5 4 3 2 1` |

---

# Key Points

- `range()` generates a sequence of numbers.
- It is commonly used with `for` loops.
- The stop value is **not included** in the sequence.
- The step value determines how much the numbers increase or decrease.
- A positive step counts upward, while a negative step counts downward.
- `range()` makes repetition simple, readable, and efficient.