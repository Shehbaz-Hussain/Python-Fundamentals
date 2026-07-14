# The `pass` Statement

## Introduction

The **`pass`** statement is a special Python statement that **does nothing**.

It is called a **null statement** because when Python executes it, no action is performed.

The `pass` statement is commonly used as a **placeholder** where Python requires a statement syntactically, but no code needs to be executed yet.

Although `pass` can be used in many Python constructs, in this module we focus on its use with loops.

---

# Why Use `pass`?

Python requires every loop and conditional statement to contain at least one executable statement.

Sometimes you may be:

- Planning to write the code later.
- Creating the program structure first.
- Temporarily leaving a loop body empty.

In these situations, `pass` prevents a syntax error while allowing the program to run.

---

# Syntax

```python
pass
```

---

# Example 1: Empty `for` Loop

```python
for number in range(5):
    pass

print("Loop completed.")
```

**Output**

```text
Loop completed.
```

The loop executes five times, but nothing happens during each iteration.

---

# Example 2: Empty `while` Loop

```python
count = 1

while count <= 3:
    count = count + 1
    pass

print("Done")
```

**Output**

```text
Done
```

The loop repeats until the condition becomes `False`, but `pass` performs no action.

---

# Example 3: Using `pass` Inside a Condition

```python
for number in range(1, 6):
    if number == 3:
        pass
    else:
        print(number)
```

**Output**

```text
1
2
4
5
```

When `number` is `3`, the `pass` statement executes and nothing is printed.

---

# What Happens Without `pass`?

Suppose you write:

```python
for number in range(5):
```

Python raises an error because the loop body is missing.

Correct:

```python
for number in range(5):
    pass
```

---

# Flow of Execution

```text
Loop Starts
     │
     ▼
Execute pass
     │
     ▼
Nothing Happens
     │
     ▼
Next Iteration
```

The `pass` statement has no effect on the execution of the loop other than satisfying Python's syntax requirements.

---

# `pass` vs `continue` vs `break`

| Statement | Effect |
|-----------|--------|
| `pass` | Does nothing |
| `continue` | Skips the rest of the current iteration and moves to the next iteration |
| `break` | Immediately terminates the loop |

Example:

```python
for number in range(5):
    if number == 2:
        pass

    print(number)
```

**Output**

```text
0
1
2
3
4
```

The `pass` statement does not change the program's flow.

---

# Common Uses

The `pass` statement is useful for:

- Creating placeholder loop bodies.
- Building program structure before implementation.
- Writing incomplete programs during development.
- Satisfying Python's syntax rules for empty blocks.

---

# Common Mistakes

## 1. Expecting `pass` to Skip an Iteration

Incorrect expectation:

```python
for number in range(5):
    if number == 2:
        pass

    print(number)
```

Actual output:

```text
0
1
2
3
4
```

`pass` does **not** skip the iteration.

To skip an iteration, use `continue`.

---

## 2. Expecting `pass` to End a Loop

Incorrect expectation:

```python
for number in range(5):
    if number == 2:
        pass
```

The loop still completes all iterations.

To terminate a loop early, use `break`.

---

## 3. Using `pass` Unnecessarily

If code is already present inside a block, `pass` is unnecessary.

Example:

```python
for number in range(5):
    print(number)
    pass
```

The `pass` statement has no effect and can be removed.

---

# Best Practices

- Use `pass` only as a temporary placeholder.
- Replace `pass` with meaningful code when implementation is complete.
- Do not confuse `pass` with `break` or `continue`.
- Remove unnecessary `pass` statements from finished code.

---

# Key Points

- `pass` is a null statement.
- It performs no action when executed.
- It is commonly used as a placeholder.
- It satisfies Python's requirement that blocks contain at least one statement.
- It does not affect loop execution.

---

# Summary

The `pass` statement allows you to create syntactically valid but intentionally empty code blocks. It is useful during development when the program structure is being designed but the implementation is not yet complete. Unlike `break` and `continue`, `pass` does not change the flow of loop execution—it simply does nothing.