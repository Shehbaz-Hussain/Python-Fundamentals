# The `if` Statement

## Introduction

The `if` statement is the simplest form of a conditional statement in Python. It allows a program to execute a block of code **only when a specified condition is `True`**.

Many real-world programs need to perform an action only under certain conditions. For example:

- Display a welcome message after a successful login.
- Allow voting only if a person is old enough.
- Show a warning when the temperature is too high.
- Notify a student if they have passed an exam.

The `if` statement makes these decisions possible.

---

# What is an `if` Statement?

An **`if` statement** checks a condition before executing a block of code.

- If the condition evaluates to `True`, the indented block is executed.
- If the condition evaluates to `False`, the block is skipped, and the program continues with the next statement.

The `if` statement does **not** provide an alternative action when the condition is false. It simply skips the associated block.

---

# Syntax

```python
if condition:
    statement
```

or

```python
if condition:
    statement1
    statement2
    statement3
```

---

# Syntax Breakdown

| Part | Description |
|------|-------------|
| `if` | Python keyword used to start a conditional statement |
| `condition` | A Boolean expression that evaluates to `True` or `False` |
| `:` | Marks the beginning of the code block |
| Indented block | Code executed only if the condition is `True` |

---

# How the `if` Statement Works

The execution process is straightforward:

1. Python evaluates the condition.
2. If the result is `True`, the indented block executes.
3. If the result is `False`, Python skips the block.
4. Program execution continues with the next statement after the `if` block.

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
      ▼             │
 Execute Block      │
      │             │
      └──────┬──────┘
             ▼
      Continue Program
```

---

# Example 1: Positive Number Check

```python
number = 15

if number > 0:
    print("The number is positive.")
```

### Output

```text
The number is positive.
```

### Explanation

- The value of `number` is `15`.
- The condition `number > 0` is `True`.
- Therefore, Python executes the `print()` statement.

---

# Example 2: Voting Eligibility

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

### Output

```text
You are eligible to vote.
```

---

# Example 3: Exam Result

```python
marks = 72

if marks >= 50:
    print("You passed the exam.")
```

### Output

```text
You passed the exam.
```

---

# Example 4: Temperature Check

```python
temperature = 36

if temperature > 30:
    print("It is a hot day.")
```

### Output

```text
It is a hot day.
```

---

# Example 5: Using User Input

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
```

### Sample Output

```text
Enter your age: 21
You are an adult.
```

If the user enters a value less than `18`, nothing is printed because the condition evaluates to `False`.

---

# Multiple Statements Inside an `if` Block

An `if` block can contain more than one statement.

```python
marks = 85

if marks >= 50:
    print("Congratulations!")
    print("You passed the exam.")
    print("Keep learning.")
```

### Output

```text
Congratulations!
You passed the exam.
Keep learning.
```

All three statements execute because the condition is `True`.

---

# When the Condition is False

If the condition is `False`, Python skips the entire indented block.

```python
age = 15

if age >= 18:
    print("Eligible to vote.")

print("Program finished.")
```

### Output

```text
Program finished.
```

The first `print()` statement is skipped because the condition is `False`.

---

# Using Comparison Operators

The `if` statement commonly uses comparison operators.

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `marks == 100` |
| `!=` | Not equal to | `age != 18` |
| `>` | Greater than | `price > 500` |
| `<` | Less than | `temperature < 0` |
| `>=` | Greater than or equal to | `age >= 18` |
| `<=` | Less than or equal to | `marks <= 50` |

---

# Using Logical Operators

Multiple conditions can be combined using logical operators.

```python
age = 22
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote.")
```

Here, both conditions must be `True` for the message to be displayed.

---

# Real-World Applications

The `if` statement is used in many situations, including:

- Checking login credentials
- Validating user age
- Detecting positive or negative numbers
- Checking examination results
- Applying discounts
- Verifying passwords
- Monitoring temperature limits
- Determining eligibility for services

---

# Common Mistakes

## Forgetting the Colon

Incorrect:

```python
if age >= 18
    print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

## Incorrect Indentation

Incorrect:

```python
if age >= 18:
print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

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

## Writing Unclear Conditions

Less readable:

```python
if age >= 18 == True:
```

Better:

```python
if age >= 18:
```

Simple conditions are usually easier to understand and maintain.

---

# Best Practices

- Write clear and meaningful conditions.
- Use descriptive variable names.
- Keep `if` blocks short and focused.
- Maintain consistent indentation (4 spaces).
- Test your program with different input values.
- Add comments when they improve readability.
- Avoid unnecessary complexity in conditions.

---

# Interview Insights

You should be able to answer questions such as:

- What is an `if` statement?
- When does an `if` block execute?
- What happens if the condition is `False`?
- Why is indentation important in Python?
- What is the difference between `=` and `==`?
- Which operators are commonly used in `if` statements?

These are common beginner-level interview questions for Python programming.

---

# Key Points

- The `if` statement is the simplest conditional statement in Python.
- It executes a block of code only when a condition is `True`.
- If the condition is `False`, the block is skipped.
- Conditions are usually created using comparison and logical operators.
- Proper indentation is required for the `if` block.

---

# Summary

The `if` statement is the foundation of decision making in Python. It enables programs to execute code selectively based on Boolean conditions, making software responsive to different inputs and situations. Mastering the `if` statement is essential before learning more advanced conditional structures such as `if-else`, `if-elif-else`, and nested `if` statements.