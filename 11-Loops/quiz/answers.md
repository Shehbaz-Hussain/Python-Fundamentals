# Module 10 Quiz – Answer Key

## Overview

This document contains the correct answers and explanations for the **Module 10 – Conditional Statements** quiz.

Use this answer key **after** attempting the quiz to evaluate your understanding of decision-making in Python.

---

# Part A – Multiple Choice Questions

## Question 1

**Correct Answer:** C. `if`

**Explanation:**

The `if` statement is used to make decisions in Python. It executes a block of code only when its condition evaluates to `True`.

---

## Question 2

**Correct Answer:** A. `if`

**Explanation:**

The code inside an `if` statement runs only when its condition is `True`.

---

## Question 3

**Correct Answer:** B. `else`

**Explanation:**

The `else` block executes when the `if` condition (and any preceding `elif` conditions) evaluates to `False`.

---

## Question 4

**Correct Answer:** B. `elif`

**Explanation:**

The `elif` keyword allows Python to check another condition if the previous condition was `False`.

---

## Question 5

**Correct Answer:** C.

```python
if
elif
else
```

**Explanation:**

The correct order is:

1. `if`
2. Zero or more `elif`
3. Optional `else`

---

## Question 6

```python
number = 15

if number > 10:
    print("Large")
```

**Correct Answer:** A. Large

**Explanation:**

Since `15 > 10` is `True`, the message `"Large"` is printed.

---

## Question 7

```python
age = 12

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

**Correct Answer:** B. Minor

**Explanation:**

The condition is `False`, so the `else` block executes.

---

## Question 8

**Correct Answer:** C. `>`

**Explanation:**

The `>` operator checks whether the value on the left is greater than the value on the right.

---

## Question 9

**Correct Answer:** B. `==`

**Explanation:**

`==` compares two values for equality.

Remember:

- `=` assigns a value.
- `==` compares two values.

---

## Question 10

**Correct Answer:** B. `and`

**Explanation:**

The `and` operator returns `True` only when **both** conditions are `True`.

---

# Part B – Predict the Output

## Question 11

```python
number = 8

if number < 10:
    print("A")
else:
    print("B")
```

**Correct Output**

```
A
```

**Explanation:**

Since `8 < 10` is `True`, the `if` block executes.

---

## Question 12

```python
marks = 85

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
else:
    print("C")
```

**Correct Output**

```
B
```

**Explanation:**

The first condition is `False`, but the second condition is `True`.

---

## Question 13

```python
age = 20

if age >= 18 and age <= 60:
    print("Eligible")
else:
    print("Not Eligible")
```

**Correct Output**

```
Eligible
```

**Explanation:**

Both conditions are `True`, so the `if` block executes.

---

## Question 14

```python
temperature = 35

if temperature < 20:
    print("Cold")
elif temperature < 30:
    print("Warm")
else:
    print("Hot")
```

**Correct Output**

```
Hot
```

**Explanation:**

Both previous conditions are `False`, so the `else` block runs.

---

## Question 15

```python
number = 5

if number > 10:
    print("A")
elif number > 7:
    print("B")
else:
    print("C")
```

**Correct Output**

```
C
```

**Explanation:**

Neither condition is `True`, so the `else` block executes.

---

# Part C – True or False

## Question 16

**Statement**

An `if` statement always executes.

**Answer:** False

**Explanation:**

The `if` block executes only when its condition is `True`.

---

## Question 17

**Statement**

An `else` block is optional.

**Answer:** True

**Explanation:**

You can write an `if` statement without an `else` block.

---

## Question 18

**Statement**

Only one branch of an `if-elif-else` structure executes.

**Answer:** True

**Explanation:**

Python executes the first matching condition and skips the remaining branches.

---

## Question 19

**Statement**

Nested `if` statements are allowed in Python.

**Answer:** True

**Explanation:**

An `if` statement can be placed inside another `if` statement.

---

## Question 20

**Statement**

Indentation is optional in Python.

**Answer:** False

**Explanation:**

Indentation is required in Python. Incorrect indentation results in a syntax error.

---

# Part D – Short Answer

## Question 21

**Question**

What is the purpose of an `if` statement?

**Sample Answer**

An `if` statement allows a program to make decisions by executing code only when a specified condition is `True`.

---

## Question 22

**Question**

When should you use `elif`?

**Sample Answer**

Use `elif` when you need to check another condition after a previous condition evaluates to `False`.

---

## Question 23

**Question**

What happens if every condition in an `if-elif-else` structure is `False` and there is no `else` block?

**Sample Answer**

No block of code is executed, and the program continues with the next statement.

---

## Question 24

**Question**

Why is proper indentation important in conditional statements?

**Sample Answer**

Indentation tells Python which statements belong to each conditional block. Without correct indentation, the program will produce an error or behave incorrectly.

---

## Question 25

**Question**

Name two logical operators used with conditional statements.

**Sample Answer**

- `and`
- `or`

(`not` is also a logical operator.)

---

# Scoring Guide

| Score | Performance |
|--------|-------------|
| 23–25 | Excellent – You have a strong understanding of conditional statements. |
| 20–22 | Very Good – You understand the concepts well with only minor mistakes. |
| 18–19 | Good – You passed, but review the topics you missed. |
| 15–17 | Fair – Practice more before moving to the next module. |
| Below 15 | Needs Improvement – Revisit the theory, examples, and exercises before continuing. |

---

# Key Takeaways

After completing this quiz, you should be able to:

- Explain the purpose of conditional statements.
- Write `if`, `if-else`, and `if-elif-else` statements correctly.
- Use comparison and logical operators in conditions.
- Read and predict the output of simple decision-making programs.
- Avoid common syntax and indentation mistakes.
- Choose the appropriate conditional structure for different situations.

---

**Recommended Next Step**

If you scored below the passing score, revisit:

- Theory
- Examples
- Exercises
- Projects

Then attempt the quiz again without looking at the answer key.