# Nested Loops

## Introduction

A **nested loop** is a loop placed inside another loop.

The outer loop executes first. For **each iteration** of the outer loop, the inner loop executes **completely** before the outer loop continues to its next iteration.

Nested loops are useful for solving problems that require multiple levels of repetition, such as printing patterns, generating tables, or processing rows and columns.

---

# General Syntax

## Nested `for` Loops

```python
for outer_variable in range(...):
    for inner_variable in range(...):
        statement
```

---

## Nested `while` Loops

```python
outer = 1

while outer <= 3:
    inner = 1

    while inner <= 2:
        statement
        inner = inner + 1

    outer = outer + 1
```

---

# How Nested Loops Work

Suppose we have:

```python
for row in range(1, 4):
    for column in range(1, 3):
        print(row, column)
```

Execution order:

```text
Outer Loop: row = 1
    Inner Loop:
        column = 1
        column = 2

Outer Loop: row = 2
    Inner Loop:
        column = 1
        column = 2

Outer Loop: row = 3
    Inner Loop:
        column = 1
        column = 2
```

The inner loop starts from the beginning every time the outer loop advances.

---

# Example 1: Print Coordinates

```python
for row in range(1, 4):
    for column in range(1, 3):
        print("Row:", row, "Column:", column)
```

**Output**

```text
Row: 1 Column: 1
Row: 1 Column: 2
Row: 2 Column: 1
Row: 2 Column: 2
Row: 3 Column: 1
Row: 3 Column: 2
```

---

# Example 2: Multiplication Table (1 to 3)

```python
for row in range(1, 4):
    for column in range(1, 4):
        print(row * column)
```

**Output**

```text
1
2
3
2
4
6
3
6
9
```

Each value is printed on a separate line because `print()` automatically moves to the next line.

---

# Example 3: Print a Square Pattern

```python
for row in range(3):
    for column in range(3):
        print("*", end="")
    print()
```

**Output**

```text
***
***
***
```

### Explanation

- The inner loop prints three asterisks on the same line.
- `print()` with no arguments moves to the next line after each row.

---

# Example 4: Number Pattern

```python
for row in range(1, 4):
    for column in range(3):
        print(row, end=" ")
    print()
```

**Output**

```text
1 1 1
2 2 2
3 3 3
```

---

# Nested `while` Loop Example

```python
row = 1

while row <= 3:
    column = 1

    while column <= 2:
        print(row, column)
        column = column + 1

    row = row + 1
```

**Output**

```text
1 1
1 2
2 1
2 2
3 1
3 2
```

Notice that `column` is reset to `1` each time the outer loop starts a new iteration.

---

# Real-World Applications

Nested loops are commonly used for:

- Printing patterns
- Multiplication tables
- Processing rows and columns
- Grid-based games
- Matrix operations (introduced later)
- Image processing concepts
- Data analysis tasks

---

# Common Mistakes

## 1. Forgetting to Reset the Inner Loop Variable

Incorrect:

```python
row = 1
column = 1

while row <= 3:
    while column <= 2:
        print(row, column)
        column = column + 1

    row = row + 1
```

The inner loop runs only during the first outer iteration because `column` is never reset.

Correct:

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

## 2. Incorrect Indentation

```python
for row in range(3):
print(row)
```

Result:

```text
IndentationError
```

---

## 3. Confusing the Roles of the Loops

Use meaningful variable names such as `row` and `column` instead of generic names like `i` and `j` when they improve readability.

---

# Best Practices

- Use descriptive variable names.
- Keep nesting levels as shallow as possible.
- Reset inner loop variables when using nested `while` loops.
- Maintain consistent indentation.
- Add comments when nested logic becomes complex.

---

# Key Points

- A nested loop is a loop inside another loop.
- The inner loop executes completely for each iteration of the outer loop.
- Nested loops can be created using `for` loops, `while` loops, or a combination of both.
- They are useful for solving problems involving rows, columns, tables, and patterns.
- Proper indentation and variable management are essential for correct behavior.

---

# Summary

Nested loops extend the power of basic loops by allowing repeated execution within repeated execution. They are fundamental for tasks such as generating multiplication tables, printing patterns, and processing two-dimensional structures. Understanding the execution order of nested loops is essential before progressing to more advanced programming topics.