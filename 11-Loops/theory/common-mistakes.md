# Common Mistakes When Using Loops

## Introduction

Loops are one of the most frequently used programming constructs in Python. While they are straightforward to learn, beginners often make mistakes that lead to incorrect output, infinite loops, or runtime errors.

Understanding these common mistakes will help you write more reliable and maintainable programs.

---

# 1. Forgetting to Update the Loop Variable

This is one of the most common mistakes when using a `while` loop.

### Incorrect

```python
count = 1

while count <= 5:
    print(count)
```

**Result**

The program enters an **infinite loop** because `count` never changes.

### Correct

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

---

# 2. Writing an Incorrect Loop Condition

If the condition is incorrect, the loop may never execute or may execute more times than intended.

### Incorrect

```python
count = 10

while count < 5:
    print(count)
```

**Result**

The loop body never executes because the condition is `False` before the first iteration.

### Correct

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

---

# 3. Incorrect Indentation

Python uses indentation to define the loop body.

### Incorrect

```python
for number in range(5):
print(number)
```

**Result**

```text
IndentationError
```

### Correct

```python
for number in range(5):
    print(number)
```

---

# 4. Assuming the `stop` Value in `range()` Is Included

### Incorrect Expectation

```python
for number in range(1, 6):
    print(number)
```

Expected output:

```text
1
2
3
4
5
6
```

### Actual Output

```text
1
2
3
4
5
```

The `stop` value is **always excluded**.

---

# 5. Confusing `break` and `continue`

These statements have different purposes.

### `break`

Stops the loop immediately.

```python
for number in range(5):
    if number == 3:
        break

    print(number)
```

Output:

```text
0
1
2
```

---

### `continue`

Skips only the current iteration.

```python
for number in range(5):
    if number == 3:
        continue

    print(number)
```

Output:

```text
0
1
2
4
```

---

# 6. Expecting `pass` to Skip an Iteration

### Incorrect Assumption

```python
for number in range(5):
    if number == 2:
        pass

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

The `pass` statement does nothing.

Use `continue` if the iteration should be skipped.

---

# 7. Forgetting to Reset the Inner Loop Variable

This mistake occurs with nested `while` loops.

### Incorrect

```python
row = 1
column = 1

while row <= 3:
    while column <= 2:
        print(row, column)
        column = column + 1

    row = row + 1
```

The inner loop executes only during the first outer iteration.

### Correct

```python
row = 1

while row <= 3:
    column = 1

    while column <= 2:
        print(row, column)
        column = column + 1

    row = row + 1
```

---

# 8. Forgetting the Colon (`:`)

### Incorrect

```python
for number in range(5)
    print(number)
```

**Result**

```text
SyntaxError
```

### Correct

```python
for number in range(5):
    print(number)
```

---

# 9. Using `break` or `continue` Outside a Loop

### Incorrect

```python
break
```

or

```python
continue
```

**Result**

```text
SyntaxError
```

These statements can only be used inside `for` or `while` loops.

---

# 10. Expecting Loop `else` to Execute After `break`

### Incorrect Assumption

```python
for number in range(5):
    if number == 2:
        break
else:
    print("Completed")
```

Expected:

```text
Completed
```

### Actual Result

Nothing is printed after the loop because `break` prevents the `else` block from executing.

---

# 11. Choosing the Wrong Type of Loop

Using a `while` loop when a `for` loop is simpler can make the code harder to read.

Less suitable:

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

More suitable:

```python
for number in range(1, 6):
    print(number)
```

Choose the loop that best fits the problem.

---

# 12. Using Poor Variable Names

Less descriptive:

```python
for x in range(5):
    print(x)
```

More descriptive:

```python
for student_number in range(5):
    print(student_number)
```

Meaningful names improve readability.

---

# Quick Checklist

Before running your program, verify the following:

- Did you use the correct loop?
- Does a `while` loop eventually terminate?
- Is the indentation correct?
- Did you remember the colon (`:`)?
- Is the loop condition correct?
- Did you update the loop variable?
- Did you choose the correct `range()` arguments?
- Are you using `break`, `continue`, and `pass` correctly?
- Are variable names meaningful?
- Have you tested boundary cases?

---

# Key Points

- Most loop errors result from incorrect conditions or missing updates.
- Proper indentation is essential in Python.
- The `stop` value in `range()` is excluded.
- `break`, `continue`, and `pass` each have distinct purposes.
- Choosing the appropriate loop improves readability and correctness.

---

# Summary

Many beginner loop errors are easy to avoid once you understand how loops execute. Paying attention to loop conditions, variable updates, indentation, and the behavior of loop control statements will help you write correct and maintainable Python programs. Developing the habit of reviewing your loops against a simple checklist can prevent many common programming mistakes.