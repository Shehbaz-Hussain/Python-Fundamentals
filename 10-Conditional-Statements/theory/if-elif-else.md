# The `if-elif-else` Statement

## Introduction

Many programming problems involve more than two possible outcomes. For example, a student can receive different grades based on marks, or a traffic signal can display different colors that require different actions.

Using multiple separate `if` statements for such situations can make a program less efficient and harder to understand. Python provides the **`if-elif-else` statement** to handle multiple conditions in a clear and organized way.

The `if-elif-else` statement allows a program to evaluate several conditions and execute the block of code associated with the **first condition that evaluates to `True`**.

---

# What is an `if-elif-else` Statement?

An **`if-elif-else` statement** is a multi-way decision structure.

It consists of:

- One `if` statement
- Zero or more `elif` statements
- An optional `else` statement

Python evaluates the conditions from top to bottom. As soon as it finds a condition that is `True`, it executes the corresponding block and skips the remaining conditions.

---

# Why Use an `if-elif-else` Statement?

This statement is useful when there are multiple possible outcomes.

Common examples include:

- Assigning grades
- Identifying age groups
- Traffic light systems
- Product discounts
- Salary ranges
- Performance evaluations
- Menu selection
- Number classification

---

# Syntax

```python
if condition1:
    # Code block
elif condition2:
    # Code block
elif condition3:
    # Code block
else:
    # Code block
```

---

# Syntax Breakdown

| Part | Description |
|------|-------------|
| `if` | Checks the first condition. |
| `elif` | Checks another condition if all previous conditions are `False`. |
| `else` | Executes if none of the previous conditions are `True`. |
| `:` | Marks the beginning of a code block. |
| Indentation | Defines the statements belonging to each block. |

---

# How the `if-elif-else` Statement Works

Python follows these steps:

1. Evaluate the `if` condition.
2. If it is `True`, execute its block and skip the remaining conditions.
3. If it is `False`, evaluate the first `elif` condition.
4. Continue checking each `elif` until one condition is `True`.
5. If none of the conditions are `True`, execute the `else` block (if present).
6. Continue with the rest of the program.

Only **one** block executes.

---

# Flow Diagram

```text
                Start
                  │
                  ▼
          Check first condition
                  │
          ┌───────┴────────┐
          │                │
        True             False
          │                │
          ▼                ▼
   Execute if        Check next elif
                          │
                  ┌───────┴────────┐
                  │                │
                True             False
                  │                │
                  ▼                ▼
          Execute elif      Check next elif
                                   │
                              ...
                                   │
                                   ▼
                          Execute else
                                   │
                                   ▼
                           Continue Program
```

---

# Example 1: Student Grades

```python
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade D")
```

### Output

```text
Grade B
```

### Explanation

- `marks >= 90` → `False`
- `marks >= 80` → `True`
- Python prints **Grade B**.
- The remaining conditions are skipped.

---

# Example 2: Age Categories

```python
age = 16

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")
```

### Output

```text
Teenager
```

---

# Example 3: Traffic Signal

```python
signal = "yellow"

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Wait")
elif signal == "green":
    print("Go")
else:
    print("Invalid signal")
```

### Output

```text
Wait
```

---

# Example 4: Positive, Negative, or Zero

```python
number = 0

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

### Output

```text
Zero
```

---

# Example 5: Using User Input

```python
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Very Good")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")
```

### Sample Output

```text
Enter your marks: 78
Very Good
```

---

# Order of Conditions Matters

Python evaluates conditions **from top to bottom**.

Consider the following example:

```python
marks = 95

if marks >= 50:
    print("Pass")
elif marks >= 90:
    print("Excellent")
```

### Output

```text
Pass
```

Although `95` is greater than `90`, the first condition is already `True`, so Python never checks the second condition.

A better approach is:

```python
if marks >= 90:
    print("Excellent")
elif marks >= 50:
    print("Pass")
```

Now the output is:

```text
Excellent
```

Always place **more specific conditions before more general conditions**.

---

# Using Logical Operators

Logical operators can be used inside conditions.

```python
age = 25
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")
elif age >= 18:
    print("Adult but not eligible to vote")
else:
    print("Minor")
```

---

# Real-World Applications

The `if-elif-else` statement is commonly used for:

- Grade calculation
- Tax calculation
- ATM menu systems
- Login validation
- Traffic signal control
- Product discounts
- Salary classification
- Weather reports
- Age categorization

---

# Common Mistakes

## Writing Conditions in the Wrong Order

Incorrect:

```python
if marks >= 50:
    print("Pass")
elif marks >= 90:
    print("Excellent")
```

The second condition is never reached for marks greater than or equal to `90`.

---

## Forgetting the Colon

Incorrect:

```python
elif marks >= 80
```

Correct:

```python
elif marks >= 80:
```

---

## Incorrect Indentation

Every block must be indented consistently.

Correct:

```python
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
else:
    print("C")
```

---

## Using `elif` Without an `if`

Incorrect:

```python
elif marks >= 80:
    print("Grade B")
```

An `elif` statement must always follow an `if` or another `elif`.

---

# Best Practices

- Arrange conditions from most specific to most general.
- Keep conditions simple and readable.
- Use descriptive variable names.
- Avoid unnecessary `elif` statements.
- Test every possible outcome.
- Maintain consistent indentation.
- Include an `else` block when appropriate to handle unexpected cases.

---

# Interview Insights

You should be able to answer questions such as:

- What is the purpose of the `elif` keyword?
- How many `elif` statements can an `if` statement have?
- Does Python evaluate every `elif` condition?
- Why is the order of conditions important?
- Can an `if-elif-else` statement exist without an `else` block?

These are common interview and examination questions for beginners.

---

# Key Points

- The `if-elif-else` statement handles multiple conditions.
- Python checks conditions from top to bottom.
- Only the first `True` condition is executed.
- Remaining conditions are skipped after a match is found.
- The order of conditions is critical for correct program behavior.

---

# Summary

The `if-elif-else` statement allows a Python program to choose one action from multiple possible alternatives. It improves readability, reduces unnecessary comparisons, and provides a structured way to handle complex decision-making. Understanding how Python evaluates conditions in sequence is essential for writing correct and efficient conditional logic.