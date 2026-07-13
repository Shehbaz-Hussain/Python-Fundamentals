# Glossary

## Introduction

This glossary contains the important terms introduced in the **Conditional Statements** module. Understanding these terms will help you read Python documentation, communicate effectively with other programmers, and strengthen your understanding of decision-making in programming.

The terms are listed in alphabetical order for quick reference.

---

# A

## Assignment Operator (`=`)

An operator used to assign a value to a variable.

**Example**

```python
age = 18
```

**Note:** Do not confuse the assignment operator (`=`) with the equality operator (`==`).

---

# B

## Block of Code

A group of one or more statements that belong together.

In Python, a block of code is defined by **indentation**.

**Example**

```python
if age >= 18:
    print("Adult")
```

The indented `print()` statement forms the block of code.

---

## Boolean

A data type that has only two possible values:

- `True`
- `False`

Boolean values are commonly produced by comparison operators and used in conditional statements.

---

## Boolean Expression

An expression that evaluates to either `True` or `False`.

**Example**

```python
marks >= 50
```

---

# C

## Colon (`:`)

A symbol placed at the end of an `if`, `elif`, or `else` statement to indicate that an indented block of code follows.

**Example**

```python
if age >= 18:
```

---

## Comparison Operator

An operator used to compare two values.

Common comparison operators include:

- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`

Comparison operators always return a Boolean value.

---

## Condition

A Boolean expression that determines whether a block of code should execute.

**Example**

```python
age >= 18
```

---

## Conditional Statement

A programming statement that executes different blocks of code depending on whether a condition is `True` or `False`.

Examples include:

- `if`
- `if-else`
- `if-elif-else`

---

## Control Flow

The order in which statements are executed in a program.

Conditional statements change the normal flow of execution by making decisions.

---

# D

## Decision Making

The process of choosing which block of code to execute based on the result of a condition.

Decision making is one of the primary uses of conditional statements.

---

# E

## Equality Operator (`==`)

A comparison operator that checks whether two values are equal.

**Example**

```python
if marks == 100:
    print("Perfect score")
```

---

## `else`

A keyword used to define a block of code that executes when all previous conditions are `False`.

**Example**

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## `elif`

A keyword that stands for **else if**.

It allows additional conditions to be checked after an `if` statement.

**Example**

```python
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
```

---

# F

## False

One of the two Boolean values in Python.

A condition that evaluates to `False` does not execute the corresponding `if` block.

---

# I

## Indentation

The spaces placed at the beginning of a line to define a block of code.

Python uses indentation instead of braces (`{}`).

The standard convention is **4 spaces** for each indentation level.

---

## `if`

A Python keyword used to execute a block of code when a condition is `True`.

**Example**

```python
if number > 0:
    print("Positive")
```

---

## `if-else`

A conditional statement that provides two possible execution paths.

One block executes if the condition is `True`; the other executes if it is `False`.

---

## `if-elif-else`

A conditional statement used to select one action from multiple possible outcomes.

Python evaluates the conditions from top to bottom and executes the first block whose condition is `True`.

---

# L

## Logical Operator

An operator used to combine or modify Boolean expressions.

Python provides three logical operators:

- `and`
- `or`
- `not`

---

# N

## Nested `if`

An `if` statement placed inside another conditional statement.

Nested `if` statements are useful when one decision depends on another.

---

## `not`

A logical operator that reverses the Boolean value of a condition.

**Example**

```python
logged_in = False

if not logged_in:
    print("Please log in.")
```

---

# O

## `or`

A logical operator that returns `True` if at least one condition is `True`.

**Example**

```python
if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

---

# P

## Program Flow

The sequence in which statements are executed in a program.

Conditional statements allow the program flow to change based on conditions.

---

# T

## True

One of the two Boolean values in Python.

When a condition evaluates to `True`, the corresponding block of code is executed.

---

# V

## Variable

A named location used to store data in a program.

Variables are commonly used in conditional statements.

**Example**

```python
temperature = 32
```

---

# Key Terms at a Glance

| Term | Meaning |
|------|---------|
| Assignment Operator (`=`) | Assigns a value to a variable |
| Block of Code | A group of indented statements |
| Boolean | `True` or `False` |
| Boolean Expression | An expression that evaluates to `True` or `False` |
| Comparison Operator | Compares two values |
| Condition | A Boolean expression used for decision making |
| Conditional Statement | Executes code based on a condition |
| Control Flow | The order in which statements execute |
| Decision Making | Choosing actions based on conditions |
| Equality Operator (`==`) | Compares two values for equality |
| `elif` | Checks an additional condition |
| `else` | Executes when previous conditions are `False` |
| `if` | Executes code when a condition is `True` |
| `if-else` | Provides two execution paths |
| `if-elif-else` | Handles multiple possible outcomes |
| Indentation | Defines blocks of code in Python |
| Logical Operator | Combines or modifies conditions |
| Nested `if` | An `if` statement inside another conditional statement |
| Program Flow | The sequence of program execution |

---

# Summary

The terms in this glossary represent the essential vocabulary for understanding conditional statements in Python. Becoming familiar with these concepts will make it easier to read code, understand documentation, solve programming problems, and communicate effectively with other developers. Keep this glossary as a quick reference while working through the examples, exercises, and projects in this module.