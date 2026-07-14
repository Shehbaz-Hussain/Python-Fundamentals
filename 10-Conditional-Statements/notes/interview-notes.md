# Conditional Statements — Interview Notes

## Module Overview

Conditional statements are one of the most fundamental programming concepts. They allow a program to make decisions by executing different blocks of code depending on whether a condition evaluates to `True` or `False`.

Interview questions on conditional statements typically focus on:
- Understanding decision-making logic
- Writing correct conditional structures
- Identifying common mistakes
- Explaining how Python evaluates conditions

---

# Interview Questions and Answers

## 1. What is a conditional statement?

**Answer:**

A conditional statement is a control flow statement that executes different blocks of code based on whether a specified condition is `True` or `False`.

Example:

```python
age = 18

if age >= 18:
    print("Eligible to vote")
```

---

## 2. Why are conditional statements used?

**Answer:**

Conditional statements allow programs to make decisions instead of executing every statement sequentially.

They are commonly used for:

- Input validation
- User authentication
- Menu selection
- Decision making
- Business rules
- Grade calculation

---

## 3. What types of conditional statements are available in Python?

**Answer:**

Python provides:

- `if`
- `if-else`
- `if-elif-else`
- Nested `if`

---

## 4. What is the difference between `if` and `if-else`?

**Answer:**

`if` executes a block only when the condition is `True`.

`if-else` provides two execution paths: one when the condition is `True`, and another when it is `False`.

Example:

```python
number = 5

if number > 0:
    print("Positive")
else:
    print("Not Positive")
```

---

## 5. What is an `elif` statement?

**Answer:**

`elif` stands for **else if**. It allows multiple conditions to be checked after the initial `if` statement.

Example:

```python
marks = 75

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("Below C")
```

---

## 6. What is a nested `if` statement?

**Answer:**

A nested `if` is an `if` statement placed inside another `if` or `else` block.

Example:

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Access granted")
```

---

## 7. What are comparison operators?

**Answer:**

Comparison operators compare two values and return either `True` or `False`.

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

---

## 8. What are logical operators?

**Answer:**

Logical operators combine or modify conditions.

| Operator | Description |
|----------|-------------|
| `and` | Returns `True` only if both conditions are `True` |
| `or` | Returns `True` if at least one condition is `True` |
| `not` | Reverses the Boolean value |

---

## 9. Why is indentation important in Python?

**Answer:**

Python uses indentation to define code blocks. Incorrect indentation results in an `IndentationError` or changes the program's logic.

Correct example:

```python
if True:
    print("Hello")
```

---

## 10. What happens when multiple conditions are `True` in an `if-elif-else` chain?

**Answer:**

Python evaluates conditions from top to bottom and executes only the **first** condition that evaluates to `True`. The remaining `elif` and `else` blocks are skipped.

---

## 11. What is the difference between `=` and `==`?

**Answer:**

- `=` is the assignment operator.
- `==` is the equality comparison operator.

Example:

```python
x = 10      # Assignment

if x == 10: # Comparison
    print("Equal")
```

---

## 12. What are common mistakes beginners make with conditional statements?

**Answer:**

Common mistakes include:

- Using `=` instead of `==`
- Forgetting the colon (`:`)
- Incorrect indentation
- Writing `elif` without an `if`
- Using incompatible data types in comparisons
- Writing conditions in the wrong order

---

## 13. How does Python evaluate an `if-elif-else` structure?

**Answer:**

Python checks each condition sequentially:

1. Evaluate the `if` condition.
2. If it is `True`, execute its block and skip the rest.
3. Otherwise, evaluate each `elif` condition in order.
4. If none are `True`, execute the `else` block (if present).

---

# Quick Interview Tips

- Understand the purpose of each conditional statement.
- Know when to use `if`, `if-else`, `if-elif-else`, and nested `if`.
- Be able to explain comparison and logical operators.
- Remember that indentation determines code blocks.
- Distinguish clearly between assignment (`=`) and comparison (`==`).
- Explain the execution flow of an `if-elif-else` chain.
- Write clean, readable, and properly indented code.