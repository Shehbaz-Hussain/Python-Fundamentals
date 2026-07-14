# Loop `else` Syntax

# Introduction

In Python, both `for` loops and `while` loops can have an optional `else` clause.

The code inside the `else` block executes **only if the loop finishes normally**. If the loop is terminated using a `break` statement, the `else` block is skipped.

This feature is unique to Python and helps clearly separate code that should run only after a loop completes successfully.

---

# Basic Syntax

## `for` Loop with `else`

```python
for variable in sequence:
    # Loop body
else:
    # Executes if the loop completes normally
```

---

## `while` Loop with `else`

```python
while condition:
    # Loop body
else:
    # Executes if the loop completes normally
```

---

# How It Works

A loop with an `else` clause follows these steps:

1. The loop begins executing.
2. Each iteration runs normally.
3. If the loop completes without encountering a `break` statement, the `else` block executes.
4. If a `break` statement is executed, the `else` block is skipped.

---

# `for` Loop with `else`

```python
for number in range(1, 6):
    print(number)
else:
    print("Loop completed successfully.")
```

### Output

```text
1
2
3
4
5
Loop completed successfully.
```

### Explanation

The loop finishes all five iterations without interruption, so the `else` block executes.

---

# `for` Loop with `break`

```python
for number in range(1, 6):

    if number == 3:
        break

    print(number)
else:
    print("Loop completed successfully.")
```

### Output

```text
1
2
```

### Explanation

The loop stops when `number` becomes `3`.

Because the loop ends with `break`, the `else` block is **not** executed.

---

# `while` Loop with `else`

```python
count = 1

while count <= 3:
    print(count)
    count = count + 1
else:
    print("Loop completed successfully.")
```

### Output

```text
1
2
3
Loop completed successfully.
```

The condition eventually becomes `False`, so the `else` block executes.

---

# `while` Loop with `break`

```python
count = 1

while count <= 5:

    if count == 3:
        break

    print(count)
    count = count + 1
else:
    print("Loop completed successfully.")
```

### Output

```text
1
2
```

The loop is terminated by `break`, so the `else` block is skipped.

---

# Visual Flow

```text
Start Loop
     │
     ▼
Execute Loop Body
     │
     ▼
Was break executed?
     │
 ┌───┴────┐
 │        │
No       Yes
 │        │
 ▼        ▼
Loop     Exit Loop
Ends      │
Normally   │
 │         │
 ▼         ▼
Execute   Skip
else      else
```

---

# `else` Without `break`

```python
for number in range(3):
    print(number)
else:
    print("Finished")
```

### Output

```text
0
1
2
Finished
```

The loop completes normally, so the `else` block runs.

---

# `else` With `continue`

```python
for number in range(1, 6):

    if number == 3:
        continue

    print(number)
else:
    print("Loop completed.")
```

### Output

```text
1
2
4
5
Loop completed.
```

### Explanation

The `continue` statement skips only the current iteration. It does **not** stop the loop.

Since no `break` statement is executed, the `else` block still runs.

---

# `else` with Nested Loops

```python
for row in range(1, 3):

    for column in range(1, 3):
        print(row, column)

    else:
        print("Inner loop completed.")
```

### Output

```text
1 1
1 2
Inner loop completed.
2 1
2 2
Inner loop completed.
```

The `else` clause belongs to the inner loop and executes each time that loop finishes normally.

---

# Common Mistakes

## Mistake 1: Thinking `else` Runs Only When the Loop Never Executes

```python
for number in range(3):
    print(number)
else:
    print("Done")
```

The `else` block runs because the loop completed normally—not because the loop was skipped.

---

## Mistake 2: Expecting `else` to Execute After `break`

```python
for number in range(5):

    if number == 2:
        break
else:
    print("Done")
```

The `else` block does **not** execute because the loop ended with `break`.

---

## Mistake 3: Confusing Loop `else` with Conditional `else`

The `else` attached to a loop is different from the `else` used with an `if` statement.

- An `if...else` chooses between conditions.
- A loop `else` runs after the loop completes normally.

---

# Best Practices

- Use a loop `else` only when it improves readability.
- Remember that `break` prevents the `else` block from executing.
- Keep the `else` block short and focused on actions that should occur after normal loop completion.
- Indent the `else` statement at the same level as the loop it belongs to.

---

# Syntax Summary

| Syntax | Purpose |
|--------|---------|
| `for ... else` | Executes the `else` block if the `for` loop finishes normally |
| `while ... else` | Executes the `else` block if the `while` loop finishes normally |
| `break` | Prevents the loop's `else` block from executing |
| `continue` | Skips the current iteration but does not affect the loop's `else` block |

---

# Key Points

- Both `for` and `while` loops can include an `else` clause.
- The `else` block executes only when the loop completes normally.
- A `break` statement skips the `else` block.
- A `continue` statement does not prevent the `else` block from executing.
- Proper indentation determines which loop the `else` clause belongs to.
- Loop `else` is a Python-specific feature that can make certain looping logic clearer.