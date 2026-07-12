# Answers — Logical Operators Quiz and MCQs

## Introduction

This document contains the complete answers for:

- `quiz.md`
- `mcqs.md`

Use this answer key **after attempting all questions**. Reading the explanations will help reinforce important concepts and identify common mistakes.

---

# Part 1 — Answers to `quiz.md`

## Conceptual Questions

### 1. What is a logical operator?

**Answer:**  
A logical operator combines or modifies Boolean expressions and produces a Boolean (`True` or `False`) result.

---

### 2. Name the three logical operators in Python.

**Answer:**

- `and`
- `or`
- `not`

---

### 3. What does the `and` operator do?

**Answer:**  
It returns `True` only if **both** conditions are `True`.

---

### 4. What does the `or` operator do?

**Answer:**  
It returns `True` if **at least one** condition is `True`.

---

### 5. What does the `not` operator do?

**Answer:**  
It reverses a Boolean value.

- `not True` → `False`
- `not False` → `True`

---

### 6. Which logical operator returns `True` only when both conditions are `True`?

**Answer:** `and`

---

### 7. Which logical operator returns `True` if at least one condition is `True`?

**Answer:** `or`

---

### 8. Which logical operator reverses a Boolean value?

**Answer:** `not`

---

### 9. What is a Boolean value?

**Answer:**  
A Boolean value is either `True` or `False`.

---

### 10. Which comparison operators are commonly used with logical operators?

**Answer:**

- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`

---

### 11. What is a logical expression?

**Answer:**  
A logical expression combines one or more conditions using logical operators.

---

### 12. What is short-circuit evaluation?

**Answer:**  
Python may stop evaluating an expression as soon as the final result is already known.

---

### 13. Which operator has higher precedence: `and` or `or`?

**Answer:**  
`and`

---

### 14. What is operator precedence?

**Answer:**  
Operator precedence determines the order in which operators are evaluated.

---

### 15. Why are parentheses useful?

**Answer:**  
They improve readability and control the order of evaluation.

---

### 16. Can logical operators be used inside `if` statements?

**Answer:**  
Yes.

---

### 17. What is the result of `not True`?

**Answer:** `False`

---

### 18. What is the result of `not False`?

**Answer:** `True`

---

### 19. Why is readability important?

**Answer:**  
Readable code is easier to understand, debug, and maintain.

---

### 20. Name one real-world application.

**Sample Answers:**

- Login validation
- Age verification
- Student grading
- Eligibility checking
- Admission systems

---

# Code Prediction Answers

### 1.

```python
a = 10
b = 20

print(a < b and b > 15)
```

**Answer:**

```text
True
```

**Explanation:** Both conditions are `True`.

---

### 2.

```python
age = 15

print(age >= 18 or age == 15)
```

**Answer:**

```text
True
```

**Explanation:** The second condition is `True`.

---

### 3.

```python
x = 8

print(not x > 10)
```

**Answer:**

```text
True
```

**Explanation:** `x > 10` is `False`; `not False` is `True`.

---

### 4.

```python
marks = 70

print(marks >= 50 and marks <= 100)
```

**Answer:**

```text
True
```

---

### 5.

```python
temperature = 40

print(temperature < 35 or temperature == 40)
```

**Answer:**

```text
True
```

---

### 6.

```python
a = 5
b = 8

print(a > b and b > a)
```

**Answer:**

```text
False
```

---

### 7.

```python
number = 12

print(not(number < 10))
```

**Answer:**

```text
True
```

---

### 8.

```python
x = 7
y = 7

print(x == y and x >= y)
```

**Answer:**

```text
True
```

---

### 9.

```python
a = 3
b = 9

print(a == 3 or b == 5)
```

**Answer:**

```text
True
```

---

### 10.

```python
value = 25

print(value > 10 and not(value > 30))
```

**Answer:**

```text
True
```

---

# Debugging Answers

### 1.

**Problem:**

```python
AND
```

is invalid.

**Correct Code:**

```python
age = 20

if age >= 18 and age <= 60:
    print("Eligible")
```

---

### 2.

**Problem:**

The expression is incomplete.

**Correct Code:**

```python
marks = 80

print(not (marks >= 50))
```

---

### 3.

**Problem:**

`or or` is invalid syntax.

**Correct Code:**

```python
a = 5
b = 8

print(a > b or b > a)
```

---

### 4.

**Problem:**

`notnot` is not a Python keyword.

**Correct Code:**

```python
number = 10

print(not (number == 10))
```

---

### 5.

**Problem:**

The second operand is not a Boolean expression.

**Correct Code:**

```python
x = 5
y = 10

print(x < y and y > x)
```

---

# Part 2 — Answers to `mcqs.md`

| Question | Answer |
|----------:|:------:|
| 1 | C |
| 2 | B |
| 3 | D |
| 4 | C |
| 5 | B |
| 6 | C |
| 7 | B |
| 8 | A |
| 9 | C |
| 10 | C |
| 11 | B |
| 12 | B |
| 13 | C |
| 14 | D |
| 15 | B |
| 16 | A |
| 17 | C |
| 18 | A |
| 19 | B |
| 20 | B |
| 21 | B |
| 22 | C |
| 23 | B |
| 24 | D |
| 25 | B |
| 26 | B |
| 27 | C |
| 28 | C |
| 29 | B |
| 30 | B |
| 31 | A |
| 32 | B |
| 33 | B |
| 34 | B |
| 35 | A |
| 36 | B |
| 37 | B |
| 38 | B |
| 39 | B |
| 40 | C |
| 41 | A |
| 42 | B |
| 43 | A |
| 44 | B |
| 45 | A |
| 46 | B |
| 47 | C |
| 48 | D |
| 49 | B |
| 50 | B |

---

# Explanations for Selected MCQs

### Question 22

**Correct Answer:** C (`not`)

`not` has the highest precedence among the logical operators.

---

### Question 23

**Correct Answer:** B (`and`)

Without parentheses, `and` is evaluated before `or`.

---

### Question 36

```python
print(True or False and False)
```

**Answer:** `True`

`False and False` is evaluated first because `and` has higher precedence.

---

### Question 39

**Correct Answer:** B

Short-circuit evaluation avoids evaluating unnecessary conditions once the final result is already determined.

---

### Question 47

**Correct Answer:** C (`or`)

Among the logical operators:

1. `not`
2. `and`
3. `or`

`or` has the lowest precedence and is evaluated last when parentheses are not used.

---

# Summary

This answer key provides complete solutions for the conceptual questions, code prediction exercises, debugging tasks, and all 50 MCQs. Review the explanations carefully to strengthen your understanding of logical operators, Boolean expressions, operator precedence, truth tables, and short-circuit evaluation. Mastering these concepts will help you write clearer, more reliable Python programs and prepare you for exams, coding assessments, and technical interviews.