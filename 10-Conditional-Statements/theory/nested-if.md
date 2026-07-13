# Nested `if` Statements

## Introduction

As programs become more complex, a single condition is sometimes not enough to make a decision. In many situations, one decision depends on the result of another.

For example:

- A student must first pass an examination before receiving a grade classification.
- A user must first enter the correct username before the password is checked.
- A customer must first be a member before receiving a membership discount.

These situations require **one conditional statement inside another**, which is known as a **nested `if` statement**.

---

# What is a Nested `if` Statement?

A **nested `if` statement** is an `if` statement placed inside another `if`, `elif`, or `else` block.

The inner `if` statement is evaluated **only if the outer block containing it is executed**.

This allows a program to make decisions in multiple stages.

---

# Why Use Nested `if` Statements?

Nested `if` statements are useful when:

- One condition depends on another.
- Multiple levels of validation are required.
- A decision must be made step by step.
- A program needs hierarchical decision making.

---

# Syntax

```python
if condition1:
    if condition2:
        # Code to execute
```

A nested `if` can also include an `else` statement.

```python
if condition1:
    if condition2:
        # Code
    else:
        # Code
else:
    # Code
```

---

# Syntax Breakdown

| Part | Description |
|------|-------------|
| Outer `if` | Evaluates the first condition. |
| Inner `if` | Executes only if the outer condition is `True`. |
| `else` | Handles the alternative path when needed. |
| Indentation | Indicates the level of nesting. |

---

# How a Nested `if` Statement Works

Python follows these steps:

1. Evaluate the outer condition.
2. If the outer condition is `False`, the inner condition is skipped.
3. If the outer condition is `True`, evaluate the inner condition.
4. Execute the appropriate block based on the result of the inner condition.
5. Continue with the remaining program.

---

# Flow Diagram

```text
             Start
               │
               ▼
     Evaluate Outer Condition
               │
        ┌──────┴──────┐
        │             │
      True          False
        │             │
        ▼             ▼
 Evaluate Inner     Skip Inner
   Condition        Condition
        │
   ┌────┴────┐
   │         │
 True      False
   │         │
   ▼         ▼
Execute   Execute
 Block     Block
   │
   ▼
Continue Program
```

---

# Example 1: Voting Eligibility

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("You are eligible to vote.")
```

### Output

```text
You are eligible to vote.
```

### Explanation

- The outer condition checks whether the person is at least 18 years old.
- Since it is `True`, Python evaluates the inner condition.
- The inner condition is also `True`, so the message is displayed.

---

# Example 2: Login Verification

```python
username = "admin"
password = "python123"

if username == "admin":
    if password == "python123":
        print("Login successful.")
```

### Output

```text
Login successful.
```

The password is checked only after the username is verified.

---

# Example 3: Exam Qualification

```python
marks = 78
attendance = 85

if marks >= 50:
    if attendance >= 75:
        print("You passed the course.")
```

### Output

```text
You passed the course.
```

---

# Example 4: Nested `if` with `else`

```python
age = 16

if age >= 18:
    print("Adult")
    if age >= 60:
        print("Senior Citizen")
    else:
        print("Adult but not a senior citizen")
else:
    print("Minor")
```

### Output

```text
Minor
```

Since the outer condition is `False`, Python skips the inner `if` statement completely.

---

# Example 5: Using User Input

```python
username = input("Enter username: ")
password = input("Enter password: ")

if username == "student":
    if password == "python":
        print("Access granted.")
    else:
        print("Incorrect password.")
else:
    print("Invalid username.")
```

### Sample Output

```text
Enter username: student
Enter password: python
Access granted.
```

---

# Understanding Indentation

Indentation becomes even more important when using nested `if` statements.

Correct example:

```python
age = 20

if age >= 18:
    print("Adult")

    if age >= 60:
        print("Senior Citizen")
```

Notice that the inner `if` statement is indented one level further than the outer `if`.

---

# Levels of Nesting

A nested `if` statement can contain another nested `if`.

Example:

```python
if condition1:
    if condition2:
        if condition3:
            print("All conditions are True.")
```

Although Python allows multiple levels of nesting, excessive nesting makes programs difficult to read and maintain.

For beginner programs, keep nesting as simple as possible.

---

# Real-World Applications

Nested `if` statements are commonly used in:

- Login systems
- ATM transactions
- Banking applications
- Student management systems
- Access control systems
- Online registration forms
- Membership validation
- Multi-step verification processes

---

# Common Mistakes

## Incorrect Indentation

Incorrect:

```python
if age >= 18:
if citizen:
    print("Eligible")
```

Correct:

```python
if age >= 18:
    if citizen:
        print("Eligible")
```

---

## Unnecessary Nesting

Less readable:

```python
if marks >= 50:
    if marks >= 60:
        print("Good")
```

Consider whether a simpler condition can achieve the same result.

---

## Forgetting the Colon

Incorrect:

```python
if age >= 18
```

Correct:

```python
if age >= 18:
```

---

## Assuming the Inner `if` Always Executes

The inner `if` is evaluated **only if** the outer condition is `True`.

---

# Best Practices

- Keep nesting to the minimum necessary.
- Use meaningful variable names.
- Maintain consistent indentation.
- Test every possible execution path.
- Add comments when the decision-making process is not obvious.
- Prefer clear logic over deeply nested structures.

---

# Interview Insights

You should be able to answer questions such as:

- What is a nested `if` statement?
- When is a nested `if` useful?
- Does the inner `if` execute if the outer condition is `False`?
- Why is indentation important in nested `if` statements?
- What are the disadvantages of excessive nesting?

These are common beginner-level interview and examination questions.

---

# Key Points

- A nested `if` is an `if` statement inside another conditional block.
- The inner condition is evaluated only if the outer block executes.
- Proper indentation defines the nesting level.
- Nested `if` statements support multi-stage decision making.
- Excessive nesting should be avoided to keep code readable.

---

# Summary

Nested `if` statements allow Python programs to make decisions in multiple stages by placing one conditional statement inside another. They are useful when one condition depends on the result of a previous condition, such as login verification, eligibility checks, and access control. While nested `if` statements are powerful, they should be used carefully to maintain clear, readable, and maintainable code.