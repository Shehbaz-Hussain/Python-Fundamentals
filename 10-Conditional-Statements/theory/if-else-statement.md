# The `if-else` Statement

## Introduction

In the previous lesson, you learned that an `if` statement executes a block of code only when its condition is `True`. However, many real-world problems require a program to perform one action when a condition is true and a different action when it is false.

This is where the **`if-else` statement** becomes useful.

The `if-else` statement allows a program to choose between **exactly two execution paths** based on the result of a condition.

---

# What is an `if-else` Statement?

An **`if-else` statement** is a conditional statement that executes one block of code if a condition is `True` and another block of code if the condition is `False`.

Unlike a simple `if` statement, an `if-else` statement guarantees that **one of the two code blocks will always execute**.

---

# Why Use an `if-else` Statement?

The `if-else` statement is useful whenever a program needs to make a decision with two possible outcomes.

Examples include:

- Pass or fail
- Login successful or login failed
- Adult or minor
- Positive or non-positive number
- Even or odd number
- Eligible or not eligible

---

# Syntax

```python
if condition:
    # Code executed when the condition is True
else:
    # Code executed when the condition is False
```

---

# Syntax Breakdown

| Part | Description |
|------|-------------|
| `if` | Begins the conditional statement. |
| `condition` | A Boolean expression that evaluates to `True` or `False`. |
| `:` | Marks the beginning of a code block. |
| `if` block | Executes only when the condition is `True`. |
| `else` | Defines the alternative block. |
| `else` block | Executes only when the condition is `False`. |

---

# How the `if-else` Statement Works

The execution process is simple:

1. Python evaluates the condition.
2. If the condition is `True`, the `if` block executes.
3. If the condition is `False`, the `else` block executes.
4. Only **one** of the two blocks is executed.
5. The program then continues with the next statement after the `if-else` statement.

---

# Flow Diagram

```text
            Start
              │
              ▼
      Evaluate Condition
              │
       ┌──────┴──────┐
       │             │
     True          False
       │             │
       ▼             ▼
 Execute if     Execute else
    Block          Block
       │             │
       └──────┬──────┘
              ▼
      Continue Program
```

---

# Example 1: Voting Eligibility

```python
age = 16

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

### Output

```text
You are not eligible to vote.
```

### Explanation

- The condition `age >= 18` is evaluated.
- Since `16 >= 18` is `False`, Python skips the `if` block.
- The `else` block is executed.

---

# Example 2: Pass or Fail

```python
marks = 72

if marks >= 50:
    print("You passed the exam.")
else:
    print("You failed the exam.")
```

### Output

```text
You passed the exam.
```

---

# Example 3: Positive or Negative Number

```python
number = -8

if number >= 0:
    print("The number is positive.")
else:
    print("The number is negative.")
```

### Output

```text
The number is negative.
```

> **Note:** In this example, `0` is treated as a non-negative number for simplicity.

---

# Example 4: Even or Odd Number

```python
number = 15

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```

### Output

```text
The number is odd.
```

---

# Example 5: Using User Input

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

### Sample Output

```text
Enter your age: 14
You are a minor.
```

---

# Multiple Statements in Each Block

Each block can contain more than one statement.

```python
marks = 82

if marks >= 50:
    print("Congratulations!")
    print("You passed the exam.")
    print("Keep up the good work.")
else:
    print("You did not pass the exam.")
    print("Practice more and try again.")
```

Only one block is executed.

---

# Using Comparison Operators

Comparison operators are commonly used in `if-else` statements.

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `age == 18` |
| `!=` | Not equal to | `marks != 50` |
| `>` | Greater than | `price > 100` |
| `<` | Less than | `temperature < 0` |
| `>=` | Greater than or equal to | `age >= 18` |
| `<=` | Less than or equal to | `marks <= 100` |

---

# Using Logical Operators

Conditions can also combine multiple comparisons.

```python
age = 25
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")
```

Here, both conditions must be `True` for the `if` block to execute.

---

# Real-World Applications

The `if-else` statement is widely used in software development.

Examples include:

- Login authentication
- Password verification
- ATM withdrawal approval
- Online payment validation
- Grade calculation
- Age verification
- Temperature monitoring
- Access control systems

---

# Common Mistakes

## Forgetting the Colon

Incorrect:

```python
if age >= 18
    print("Adult")
else
    print("Minor")
```

Correct:

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## Incorrect Indentation

Incorrect:

```python
if age >= 18:
print("Adult")
else:
print("Minor")
```

Correct:

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## Writing `else` Without an `if`

Incorrect:

```python
else:
    print("Invalid")
```

An `else` statement must always follow a corresponding `if`.

---

## Using Assignment Instead of Comparison

Incorrect:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

Remember:

- `=` assigns a value.
- `==` compares two values.

---

# Best Practices

- Write clear and meaningful conditions.
- Keep each block focused on a single task.
- Use descriptive variable names.
- Maintain consistent indentation.
- Test both the `True` and `False` paths.
- Keep conditions simple and easy to read.
- Add comments only when they improve understanding.

---

# Interview Insights

Be prepared to answer questions such as:

- What is an `if-else` statement?
- How is it different from an `if` statement?
- Can both the `if` and `else` blocks execute?
- What happens when the condition is `False`?
- Why is indentation important?

These questions are commonly asked in beginner Python interviews and programming assessments.

---

# Key Points

- An `if-else` statement provides two possible execution paths.
- Exactly one block is executed.
- The `if` block runs when the condition is `True`.
- The `else` block runs when the condition is `False`.
- Proper indentation and correct comparison operators are essential.

---

# Summary

The `if-else` statement extends the basic `if` statement by providing an alternative block of code when a condition is not satisfied. It is one of the most frequently used control structures in Python because many real-world decisions involve exactly two possible outcomes. Mastering the `if-else` statement prepares you for more advanced decision-making structures such as the `if-elif-else` ladder and nested conditional statements.