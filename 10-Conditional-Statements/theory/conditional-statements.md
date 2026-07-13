# Conditional Statements

## Introduction

Programs often need to make decisions based on different situations. For example, a program may need to determine whether a student has passed an exam, whether a user is old enough to vote, or whether a password is correct. If every statement in a program were executed one after another without making decisions, the program would not be able to respond differently to different inputs.

Conditional statements solve this problem by allowing a program to choose which block of code to execute based on whether a condition is `True` or `False`.

In Python, conditional statements are one of the most important control flow mechanisms. They enable programs to behave intelligently by executing different instructions under different circumstances.

---

# What is a Conditional Statement?

A **conditional statement** is a programming construct that executes a block of code only when a specified condition is satisfied.

The condition is a **Boolean expression**, meaning it evaluates to either:

- `True`
- `False`

If the condition is `True`, Python executes the associated block of code.

If the condition is `False`, Python skips that block or executes an alternative block if one is provided.

---

# Why Do We Need Conditional Statements?

Without conditional statements, every line of code would execute in the same order regardless of the situation.

Conditional statements allow programs to:

- Make decisions
- Respond to user input
- Compare values
- Validate data
- Execute different actions for different conditions
- Control the flow of execution

They are essential for creating interactive and intelligent applications.

---

# Real-World Examples

Conditional statements are used in many everyday applications.

| Situation | Decision |
|-----------|----------|
| ATM Machine | Allow withdrawal only if sufficient balance is available |
| Online Shopping | Apply a discount if the purchase amount meets the requirement |
| Login System | Grant access if the username and password are correct |
| Weather App | Display different messages depending on the weather |
| School System | Determine whether a student has passed or failed |
| Traffic Signal | Stop, wait, or move based on the signal color |

---

# Decision Making in Programming

Programming often follows this simple pattern:

1. Check a condition.
2. Determine whether the condition is `True` or `False`.
3. Execute the appropriate block of code.

This process is known as **decision making**.

For example:

- Is the user at least 18 years old?
- Is the entered password correct?
- Is the number positive?
- Did the student score enough marks to pass?

Each of these questions can be answered using conditional statements.

---

# Boolean Evaluation

Conditional statements depend on **Boolean values**.

A Boolean value has only two possible results:

| Expression | Result |
|------------|--------|
| `10 > 5` | `True` |
| `7 == 3` | `False` |
| `20 != 15` | `True` |
| `8 < 2` | `False` |

Python evaluates these expressions before deciding which block of code to execute.

---

# Basic Syntax

The simplest conditional statement is the `if` statement.

```python
if condition:
    # Code to execute if the condition is True
```

### Explanation

- `if` is a Python keyword.
- `condition` is a Boolean expression.
- A colon (`:`) marks the beginning of the code block.
- Indentation tells Python which statements belong to the `if` block.

---

# Example 1: Check Age

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

### Output

```text
You are eligible to vote.
```

### Flow Explanation

1. Store `20` in the variable `age`.
2. Evaluate the condition `age >= 18`.
3. The condition is `True`.
4. Python executes the indented `print()` statement.

---

# Example 2: Check Temperature

```python
temperature = 35

if temperature > 30:
    print("It is a hot day.")
```

### Output

```text
It is a hot day.
```

---

# Example 3: Check Password Length

```python
password_length = 8

if password_length >= 8:
    print("Password length is acceptable.")
```

### Output

```text
Password length is acceptable.
```

---

# Flow of a Conditional Statement

The execution of a conditional statement can be understood as follows:

```text
Start
   │
   ▼
Evaluate Condition
   │
 ┌─┴─────────┐
 │           │
True      False
 │           │
 ▼           ▼
Execute     Skip
Code        Code
 │
 ▼
Continue Program
```

---

# Indentation in Conditional Statements

Python uses indentation to define code blocks.

Correct example:

```python
age = 18

if age >= 18:
    print("Adult")
```

Incorrect example:

```python
age = 18

if age >= 18:
print("Adult")
```

The second example produces an `IndentationError` because the `print()` statement is not indented.

> **Important:** By convention, Python uses **4 spaces** for each indentation level.

---

# Real-World Analogy

Imagine a security guard at the entrance of a building.

The guard asks:

> "Is this person carrying a valid ID?"

- If the answer is **Yes**, the person is allowed to enter.
- If the answer is **No**, entry is denied.

A conditional statement works in the same way by checking a condition before deciding what to do.

---

# Common Mistakes

Beginners often make the following mistakes:

- Forgetting the colon (`:`) after the condition.
- Using incorrect indentation.
- Writing conditions that always evaluate to the same result.
- Confusing comparison operators with assignment.
- Making conditional logic unnecessarily complex.

---

# Best Practices

- Write clear and meaningful conditions.
- Use descriptive variable names.
- Keep conditional statements simple and readable.
- Test your program with different input values.
- Follow consistent indentation throughout your code.
- Add comments when they improve understanding.

---

# Key Points

- Conditional statements control the flow of a program.
- They execute code based on whether a condition is `True` or `False`.
- Conditions are Boolean expressions.
- Proper indentation is required in Python.
- Conditional statements are used in almost every real-world software application.

---

# Summary

Conditional statements are the foundation of decision making in Python. They allow programs to respond differently depending on the values of variables or user input. By evaluating Boolean expressions, a program can choose which code to execute, making it interactive, flexible, and capable of solving real-world problems.

Understanding conditional statements is essential before learning more advanced programming concepts, as they are used throughout almost every Python application.