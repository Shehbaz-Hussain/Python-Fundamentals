# break Statement Syntax

# Introduction

The `break` statement is used to terminate a loop immediately. When Python encounters a `break` statement inside a loop, the loop stops executing, and program control moves to the first statement after the loop.

The `break` statement can be used inside both `while` loops and `for` loops.

---

# Basic Syntax

```python
break
```

The `break` statement is typically placed inside a conditional statement so that the loop stops only when a specific condition is met.

---

# Using `break` in a `while` Loop

```python
count = 1

while count <= 10:
    print(count)

    if count == 5:
        break

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

### Explanation

- The loop starts with `count = 1`.
- Each iteration prints the current value.
- When `count` becomes `5`, the condition is `True`.
- The `break` statement immediately terminates the loop.
- The remaining iterations are skipped.

---

# Using `break` in a `for` Loop

```python
for number in range(1, 11):
    print(number)

    if number == 6:
        break
```

### Output

```text
1
2
3
4
5
6
```

The loop ends as soon as `number` becomes `6`.

---

# Flow of Execution

The following steps describe how `break` works:

1. The loop begins.
2. The loop body executes normally.
3. Python reaches the `break` statement.
4. The current loop ends immediately.
5. Execution continues with the first statement after the loop.

---

# Visual Flow

```text
Loop starts
     │
     ▼
Execute loop body
     │
     ▼
Is break executed?
     │
 ┌───┴────┐
 │        │
No       Yes
 │        │
 ▼        ▼
Next    Exit loop
Iteration
```

---

# Using `break` with an `if` Statement

A `break` statement is usually controlled by a condition.

```python
for number in range(1, 11):

    if number == 4:
        break

    print(number)
```

### Output

```text
1
2
3
```

Since the loop stops before `print(number)` executes for `4`, only the first three numbers are displayed.

---

# Breaking Out of a Nested Loop

The `break` statement only terminates the loop in which it appears.

```python
for row in range(1, 4):
    for column in range(1, 4):

        if column == 2:
            break

        print(row, column)
```

### Output

```text
1 1
2 1
3 1
```

### Explanation

- The inner loop stops when `column` becomes `2`.
- The outer loop continues with the next value of `row`.

---

# Common Use Cases

The `break` statement is useful when:

- A desired value has been found.
- User input satisfies a condition.
- Further iterations are unnecessary.
- An early exit improves efficiency.

---

# Common Mistakes

## Mistake 1: Using `break` Outside a Loop

```python
break
```

This produces an error because `break` can only be used inside a loop.

---

## Mistake 2: Assuming `break` Ends Every Loop

```python
for row in range(2):
    for column in range(3):
        break

    print(row)
```

### Output

```text
0
1
```

Only the inner loop ends. The outer loop continues executing.

---

## Mistake 3: Placing `break` Before Important Statements

```python
for number in range(5):
    break
    print(number)
```

The `print()` statement never executes because the loop ends immediately.

---

# Best Practices

- Use `break` only when an early exit is necessary.
- Place `break` inside a clear condition.
- Write readable conditions that explain why the loop ends.
- Avoid multiple unnecessary `break` statements in the same loop.
- Keep loop logic simple and easy to follow.

---

# Syntax Summary

| Syntax | Purpose |
|--------|---------|
| `break` | Immediately terminates the current loop |
| `if condition:`<br>`    break` | Ends the loop when a condition becomes `True` |

---

# Key Points

- `break` immediately terminates the current loop.
- It can be used in both `while` and `for` loops.
- It is commonly placed inside an `if` statement.
- After `break` executes, control moves to the first statement following the loop.
- In nested loops, `break` only exits the loop in which it appears.