# Conditional Statements — Cheat Sheet

> **Module 10 – Python Conditional Statements**  
> **Repository:** Python-Programming-Foundation

---

# What are Conditional Statements?

Conditional statements allow a program to make **decisions**.

The program checks whether a condition is **True** or **False**, then executes different code depending on the result.

Think of them as asking a question.

> **If something is true → do one thing.**  
> **Otherwise → do something else.**

---

# Why Use Conditional Statements?

Conditional statements help programs:

- Make decisions
- Compare values
- Execute different code paths
- Validate user input
- Build interactive applications

Without conditional statements, every program would execute exactly the same instructions every time.

---

# Decision Flow

```text
          Start
            │
            ▼
   Check Condition
            │
     ┌──────┴──────┐
     │             │
   True         False
     │             │
     ▼             ▼
Execute Code   Skip or Execute
   Block       Another Block
     │             │
     └──────┬──────┘
            ▼
           End
```

---

# Python Conditional Statements

Python provides four main conditional structures.

| Statement | Purpose |
|-----------|----------|
| `if` | Execute code when a condition is True |
| `if-else` | Choose between two blocks |
| `if-elif-else` | Choose from multiple conditions |
| Nested `if` | Place one condition inside another |

---

# 1. if Statement

### Syntax

```python
if condition:
    statement
```

### Example

```python
age = 18

if age >= 18:
    print("Adult")
```

---

### Flow

```text
Condition?
    │
 ┌──┴──┐
 │     │
Yes    No
 │      │
 ▼      ▼
Run    Skip
Code
```

---

# 2. if-else Statement

Used when there are **two possible outcomes**.

### Syntax

```python
if condition:
    statement
else:
    statement
```

### Example

```python
marks = 40

if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

---

### Flow

```text
Condition?
    │
 ┌──┴──┐
 │     │
Yes    No
 │      │
 ▼      ▼
if     else
Block  Block
```

---

# 3. if-elif-else Statement

Used when checking **multiple conditions**.

### Syntax

```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

### Example

```python
marks = 82

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("Needs Improvement")
```

---

### Flow

```text
Condition 1?
      │
 ┌────┴────┐
 │         │
Yes       No
 │         │
 ▼         ▼
Run    Condition 2?
            │
      ┌─────┴─────┐
      │           │
     Yes         No
      │           │
      ▼           ▼
    Run      Else Block
```

---

# 4. Nested if Statement

A conditional statement inside another conditional statement.

### Syntax

```python
if condition1:
    if condition2:
        statement
```

### Example

```python
age = 20
citizen = "yes"

if age >= 18:
    if citizen == "yes":
        print("Eligible")
```

---

### Flow

```text
Condition 1?
      │
 ┌────┴────┐
 │         │
Yes       No
 │         │
 ▼         ▼
Condition2 End
      │
 ┌────┴────┐
 │         │
Yes       No
 │         │
 ▼         ▼
Run      Skip
```

---

# Comparison Operators

Conditions commonly use comparison operators.

| Operator | Meaning |
|----------|----------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

---

## Example

```python
age = 18

if age >= 18:
    print("Adult")
```

---

# Logical Operators

Logical operators combine multiple conditions.

| Operator | Meaning |
|-----------|----------|
| `and` | Both conditions must be True |
| `or` | At least one condition must be True |
| `not` | Reverses the result |

---

## and Example

```python
age = 20
citizen = "yes"

if age >= 18 and citizen == "yes":
    print("Eligible")
```

---

## or Example

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

---

## not Example

```python
logged_in = False

if not logged_in:
    print("Please log in")
```

---

# Indentation

Python uses indentation to define code blocks.

Correct:

```python
if True:
    print("Correct")
```

Incorrect:

```python
if True:
print("Wrong")
```

Always use consistent indentation.

---

# Conditional Statement Comparison

| Feature | if | if-else | if-elif-else | Nested if |
|----------|----|----------|---------------|------------|
| One condition | ✅ | ✅ | ✅ | ✅ |
| Two outcomes | ❌ | ✅ | ✅ | ✅ |
| Multiple choices | ❌ | ❌ | ✅ | ✅ |
| Multiple decision levels | ❌ | ❌ | ❌ | ✅ |

---

# Choosing the Right Statement

```text
Need one condition?
        │
        ▼
      Use if

Need two choices?
        │
        ▼
    Use if-else

Need many choices?
        │
        ▼
 Use if-elif-else

Need decisions inside decisions?
        │
        ▼
    Use Nested if
```

---

# Common Applications

Conditional statements are used in:

- Login systems
- Password checking
- ATM machines
- Grade calculators
- Age verification
- Voting eligibility
- Discount calculation
- Menu selection
- Temperature checking
- Game decisions

---

# Best Practices

✅ Write clear conditions.

```python
if age >= 18:
```

---

✅ Keep conditions simple.

---

✅ Use meaningful variable names.

```python
marks = 90
temperature = 35
```

---

✅ Use `elif` for multiple choices.

---

✅ Keep indentation consistent.

---

✅ Test both True and False cases.

---

# Common Mistakes

## Forgetting the Colon

Wrong

```python
if age >= 18
```

Correct

```python
if age >= 18:
```

---

## Incorrect Indentation

Wrong

```python
if age >= 18:
print("Adult")
```

Correct

```python
if age >= 18:
    print("Adult")
```

---

## Using Assignment Instead of Comparison

Wrong

```python
if age = 18:
```

Correct

```python
if age == 18:
```

---

## Writing Impossible Conditions

Wrong

```python
if age > 18 and age < 10:
```

No value can satisfy both conditions at the same time.

---

## Using Multiple if Statements Unnecessarily

Less efficient

```python
if marks >= 90:
    print("A")

if marks >= 80:
    print("B")
```

Better

```python
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
```

---

# Quick Examples

## Check Positive Number

```python
number = 5

if number > 0:
    print("Positive")
```

---

## Even or Odd

```python
number = 8

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## Grade Checker

```python
marks = 75

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("D")
```

---

## Voting Eligibility

```python
age = 20

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

# Operator Summary

## Comparison Operators

| Operator | Example |
|----------|----------|
| `==` | `a == b` |
| `!=` | `a != b` |
| `>` | `a > b` |
| `<` | `a < b` |
| `>=` | `a >= b` |
| `<=` | `a <= b` |

---

## Logical Operators

| Operator | Example |
|-----------|----------|
| `and` | `a > 0 and b > 0` |
| `or` | `a > 0 or b > 0` |
| `not` | `not a > 0` |

---

# Revision Checklist

Before moving to the next module, make sure you can:

- Explain what a conditional statement is.
- Write an `if` statement.
- Write an `if-else` statement.
- Use `if-elif-else`.
- Write a nested `if`.
- Use comparison operators correctly.
- Use logical operators correctly.
- Read program flow from top to bottom.
- Predict program output.
- Identify and fix common mistakes.

---

# Key Takeaways

- Conditional statements allow programs to make decisions.
- Conditions evaluate to either **True** or **False**.
- `if` executes code only when a condition is True.
- `if-else` provides two possible execution paths.
- `if-elif-else` is used for multiple alternatives.
- Nested `if` statements allow more detailed decision-making.
- Comparison operators create conditions.
- Logical operators combine conditions.
- Proper indentation is required in Python.
- Clear, simple conditions make programs easier to read and maintain.

---

## Module Summary

After completing this module, you should be able to:

- Build programs that make decisions.
- Compare values using relational operators.
- Combine conditions using logical operators.
- Select the correct conditional structure for a problem.
- Read, write, and debug beginner-level Python programs that use conditional statements.