# Interview Questions — Loops

## Introduction

This document contains beginner-friendly interview questions covering Python loops. The questions reinforce the concepts learned in this module and are suitable for technical interviews, coding assessments, classroom discussions, and revision.

---

# Basic Questions

### 1. What is a loop?

**Answer:**

A loop is a control flow structure that repeatedly executes a block of code until a specified condition becomes `False` or until all values in a sequence have been processed.

---

### 2. Why are loops used?

**Answer:**

Loops reduce code duplication and automate repetitive tasks, making programs shorter, easier to read, and easier to maintain.

---

### 3. What are the two main loops in Python?

**Answer:**

- `while` loop
- `for` loop

---

### 4. What is the difference between a `while` loop and a `for` loop?

**Answer:**

| `while` Loop | `for` Loop |
|--------------|------------|
| Repeats while a condition is `True` | Iterates over a sequence |
| Suitable when the number of iterations is unknown | Suitable when the number of iterations is known |
| Requires manual updates to the loop variable | Automatically retrieves the next value from the sequence |

---

### 5. What is an iteration?

**Answer:**

An iteration is one complete execution of the loop body.

---

### 6. What is the loop body?

**Answer:**

The loop body is the indented block of code that is executed repeatedly during each iteration.

---

### 7. What is an infinite loop?

**Answer:**

An infinite loop is a loop whose terminating condition never becomes `False`, causing it to run indefinitely.

Example:

```python
while True:
    print("Running...")
```

---

### 8. How can an infinite loop be avoided?

**Answer:**

Ensure that the loop condition can eventually become `False` by updating the variables involved in the condition correctly.

---

# Questions About `for` Loops

### 9. What is the purpose of the `for` loop?

**Answer:**

A `for` loop executes a block of code once for each value in a sequence.

---

### 10. What is the `range()` function?

**Answer:**

`range()` is a built-in Python function that generates a sequence of integers, commonly used with `for` loops.

---

### 11. Does `range(5)` include the value `5`?

**Answer:**

No.

`range(5)` generates:

```text
0 1 2 3 4
```

The `stop` value is always excluded.

---

### 12. What are the three forms of `range()`?

**Answer:**

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

---

### 13. How do you count backwards using `range()`?

**Answer:**

Use a negative step.

Example:

```python
for number in range(5, 0, -1):
    print(number)
```

---

# Questions About `while` Loops

### 14. When should a `while` loop be used?

**Answer:**

A `while` loop should be used when the number of repetitions depends on a condition and is not known in advance.

---

### 15. What happens if the condition of a `while` loop is initially `False`?

**Answer:**

The loop body is never executed.

---

### 16. Why is updating the loop variable important?

**Answer:**

Without updating the loop variable, the loop condition may never change, resulting in an infinite loop.

---

# Questions About Loop Control Statements

### 17. What does the `break` statement do?

**Answer:**

It immediately terminates the nearest enclosing loop.

---

### 18. What does the `continue` statement do?

**Answer:**

It skips the remaining statements in the current iteration and continues with the next iteration.

---

### 19. What does the `pass` statement do?

**Answer:**

`pass` is a null statement. It performs no action and is commonly used as a placeholder.

---

### 20. What is the difference between `break` and `continue`?

**Answer:**

| `break` | `continue` |
|----------|------------|
| Terminates the loop | Skips the current iteration |
| Remaining iterations are not executed | Remaining iterations continue |

---

# Questions About Nested Loops

### 21. What is a nested loop?

**Answer:**

A nested loop is a loop placed inside another loop.

---

### 22. How many times does the inner loop execute?

**Answer:**

The inner loop executes completely for every iteration of the outer loop.

---

# Questions About Loop `else`

### 23. Can both `for` and `while` loops have an `else` clause?

**Answer:**

Yes.

Both `for` and `while` loops support an `else` clause.

---

### 24. When does the `else` block execute?

**Answer:**

It executes only when the loop finishes normally without encountering a `break` statement.

---

### 25. Does the `else` block execute after a `break` statement?

**Answer:**

No.

If the loop terminates because of `break`, the `else` block is skipped.

---

# Practical Questions

### 26. Write a loop to print the numbers from 1 to 10.

```python
for number in range(1, 11):
    print(number)
```

---

### 27. Write a loop to print the even numbers from 2 to 20.

```python
for number in range(2, 21, 2):
    print(number)
```

---

### 28. Write a countdown from 5 to 1.

```python
for number in range(5, 0, -1):
    print(number)
```

---

### 29. Write a `while` loop that prints numbers from 1 to 5.

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

---

### 30. Write a loop that stops when the value becomes `4`.

```python
for number in range(1, 10):
    if number == 4:
        break

    print(number)
```

---

# Rapid-Fire Questions

- What keyword starts a `for` loop?
- What keyword starts a `while` loop?
- What keyword immediately exits a loop?
- Which statement skips the current iteration?
- Which statement performs no action?
- Which function is commonly used with `for` loops?
- Is the `stop` value included in `range()`?
- Can loops be nested?
- Can a loop execute zero times?
- Can a `while` loop become infinite?

---

# Expected Answers

| Question | Answer |
|----------|--------|
| `for` loop keyword | `for` |
| `while` loop keyword | `while` |
| Exit a loop | `break` |
| Skip an iteration | `continue` |
| Do nothing | `pass` |
| Sequence generator | `range()` |
| Is stop included? | No |
| Nested loops allowed? | Yes |
| Zero iterations possible? | Yes |
| Infinite loops possible? | Yes |

---

# Interview Tips

- Explain concepts before writing code.
- Use proper Python terminology.
- Distinguish clearly between `for` and `while` loops.
- Remember that `range()` excludes the `stop` value.
- Understand the difference between `break`, `continue`, and `pass`.
- Be able to explain why an infinite loop occurs and how to prevent it.
- Practice tracing loop execution step by step.

---

# Summary

Loops are a fundamental interview topic because they demonstrate your understanding of control flow, repetition, and problem-solving. A solid grasp of loop behavior, `range()`, nested loops, and loop control statements will prepare you for beginner-level Python interviews and programming assessments.