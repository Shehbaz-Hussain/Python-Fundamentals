# The `else` Clause with Loops

## Introduction

In Python, both `for` loops and `while` loops can include an **`else` clause**.

The `else` block is executed **only if the loop finishes normally**.

A loop finishes normally when:

- A `for` loop iterates over all values in its sequence.
- A `while` loop ends because its condition becomes `False`.

If the loop is terminated by a `break` statement, the `else` block is **not** executed.

---

# Syntax

## `for` Loop with `else`

```python
for variable in sequence:
    statement(s)
else:
    statement(s)
```

---

## `while` Loop with `else`

```python
while condition:
    statement(s)
else:
    statement(s)
```

---

# How It Works

The `else` block executes only after the loop completes all of its iterations without encountering a `break` statement.

Flow of execution:

```text
Start Loop
      │
      ▼
Execute Loop Body
      │
      ▼
Was break executed?
      │
 ┌────┴────┐
 │         │
No        Yes
 │         │
 ▼         ▼
Loop      Exit Loop
Ends       Immediately
 │
 ▼
Execute else Block
```

---

# Example 1: `for` Loop with `else`

```python
for number in range(1, 6):
    print(number)
else:
    print("Loop completed successfully.")
```

**Output**

```text
1
2
3
4
5
Loop completed successfully.
```

The `else` block executes because the loop completes normally.

---

# Example 2: `for` Loop with `break`

```python
for number in range(1, 6):
    if number == 3:
        break

    print(number)
else:
    print("Loop completed successfully.")
```

**Output**

```text
1
2
```

The `else` block does **not** execute because the loop ends with a `break`.

---

# Example 3: `while` Loop with `else`

```python
count = 1

while count <= 3:
    print(count)
    count = count + 1
else:
    print("Loop finished.")
```

**Output**

```text
1
2
3
Loop finished.
```

The condition eventually becomes `False`, so the `else` block runs.

---

# Example 4: `while` Loop with `break`

```python
count = 1

while count <= 5:
    if count == 4:
        break

    print(count)
    count = count + 1
else:
    print("Loop finished.")
```

**Output**

```text
1
2
3
```

The `else` block is skipped because the loop is terminated by `break`.

---

# When Should You Use Loop `else`?

The `else` clause is useful when you want to perform an action only if the loop completes normally.

Common situations include:

- Completing a search without finding a match.
- Finishing all iterations successfully.
- Displaying a completion message.
- Confirming that no early termination occurred.

---

# Comparing Normal Completion and `break`

| Loop Behavior | Does `else` Execute? |
|---------------|:--------------------:|
| Loop completes normally | Yes |
| Loop ends with `break` | No |
| `while` condition becomes `False` | Yes |
| `for` processes every value | Yes |

---

# Common Mistakes

## 1. Assuming `else` Belongs to `if`

Example:

```python
for number in range(3):
    print(number)
else:
    print("Done")
```

The `else` is associated with the **`for` loop**, not with an `if` statement.

---

## 2. Expecting `else` to Execute After `break`

Incorrect expectation:

```python
for number in range(5):
    if number == 2:
        break
else:
    print("Done")
```

The `else` block is **not** executed.

---

## 3. Incorrect Indentation

Incorrect:

```python
for number in range(3):
    print(number)
    else:
        print("Done")
```

This produces a `SyntaxError`.

Correct:

```python
for number in range(3):
    print(number)
else:
    print("Done")
```

---

# Best Practices

- Use loop `else` only when it clearly improves readability.
- Remember that `break` prevents the `else` block from executing.
- Keep the `else` block concise and meaningful.
- Do not confuse loop `else` with conditional `else`.

---

# Key Points

- Both `for` and `while` loops can have an `else` clause.
- The `else` block executes only when the loop finishes normally.
- A `break` statement prevents the `else` block from executing.
- Loop `else` is associated with the loop, not with an `if` statement.
- It is commonly used to indicate successful completion without early termination.

---

# Summary

The `else` clause provides a way to execute code after a loop completes normally. It is particularly useful for distinguishing between loops that finish all iterations and loops that terminate early using `break`. Understanding this behavior helps you write clearer and more expressive loop-based programs.