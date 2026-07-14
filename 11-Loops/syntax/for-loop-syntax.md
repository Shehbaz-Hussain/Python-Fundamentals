# For Loop Syntax

## Introduction

A `for` loop is used to repeat a block of code for each value in a sequence. In this module, the sequence will be generated using the `range()` function, which is the standard way to control the number of iterations.

Unlike a `while` loop, a `for` loop automatically moves to the next value in the sequence. You do not need to manually update a loop variable.

---

# Basic Syntax

```python
for variable in sequence:
    # Code to execute repeatedly
```

### Syntax Breakdown

| Part | Description |
|------|-------------|
| `for` | Keyword used to start a for loop |
| `variable` | Stores the current value during each iteration |
| `in` | Connects the loop variable with the sequence |
| `sequence` | Collection of values to iterate over (in this module, created using `range()`) |
| `:` | Indicates the beginning of the loop body |
| Indented block | Statements that execute once for each value |

---

# Basic Example

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

In each iteration, `number` receives the next value produced by `range(1, 6)`.

---

# How a For Loop Works

The loop follows these steps:

1. Generate the sequence.
2. Assign the first value to the loop variable.
3. Execute the loop body.
4. Assign the next value to the loop variable.
5. Repeat until there are no more values.
6. Continue with the next statement after the loop.

---

# Loop Variable

The loop variable changes automatically during each iteration.

Example:

```python
for count in range(3):
    print("Current value:", count)
```

Output:

```text
Current value: 0
Current value: 1
Current value: 2
```

---

# Using the Loop Variable

The loop variable can be used in calculations, conditions, and output.

Example:

```python
for number in range(1, 6):
    square = number * number
    print("Square of", number, "is", square)
```

Output:

```text
Square of 1 is 1
Square of 2 is 4
Square of 3 is 9
Square of 4 is 16
Square of 5 is 25
```

---

# Multiple Statements Inside a Loop

A loop body may contain more than one statement.

```python
for number in range(1, 4):
    print("Number:", number)
    print("Double:", number * 2)
    print()
```

Output:

```text
Number: 1
Double: 2

Number: 2
Double: 4

Number: 3
Double: 6
```

---

# Nested For Loop

A `for` loop can be placed inside another `for` loop.

```python
for row in range(1, 3):
    for column in range(1, 4):
        print(row, column)
```

Output:

```text
1 1
1 2
1 3
2 1
2 2
2 3
```

---

# Indentation Rules

Python uses indentation to determine which statements belong to the loop.

Correct:

```python
for number in range(3):
    print(number)

print("Loop finished")
```

Incorrect:

```python
for number in range(3):
print(number)
```

The incorrect example produces an `IndentationError`.

---

# Comparing `for` and `while`

| Feature | `for` Loop | `while` Loop |
|---------|------------|--------------|
| Number of iterations | Usually known | Often unknown |
| Variable update | Automatic | Manual |
| Common use | Repeating a fixed number of times | Repeating until a condition changes |

---

# Common Pattern

```python
for variable in range(start, stop):
    # Statements
```

Example:

```python
for value in range(1, 6):
    print(value)
```

---

# Best Practices

- Use meaningful loop variable names.
- Choose a `for` loop when the number of iterations is known.
- Keep the loop body simple and readable.
- Follow consistent indentation.
- Avoid unnecessary nested loops when a single loop is sufficient.

---

# Common Mistakes

| Mistake | Result |
|---------|--------|
| Missing indentation | `IndentationError` |
| Forgetting the colon (`:`) | `SyntaxError` |
| Using unclear variable names | Reduced readability |
| Assuming the loop variable keeps its initial value | Unexpected output |

---

# Syntax Summary

| Syntax Element | Purpose |
|---------------|---------|
| `for` | Starts the loop |
| Loop variable | Holds the current value |
| `in` | Connects the variable to the sequence |
| `range()` | Generates values for iteration |
| Colon (`:`) | Begins the loop block |
| Indentation | Defines the loop body |

---

# Key Points

- A `for` loop repeats a block of code for each value in a sequence.
- In this module, the sequence is generated using `range()`.
- The loop variable is updated automatically.
- Proper indentation is required.
- A `for` loop is the preferred choice when the number of iterations is known in advance.