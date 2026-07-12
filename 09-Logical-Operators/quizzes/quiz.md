# Logical Operators Quiz

## Introduction

This quiz is designed to assess your understanding of Python logical operators covered in Module 09. The questions range from basic concepts to code analysis and debugging. Attempt all questions without referring to notes. After completing the quiz, review your answers to identify areas that need improvement.

---

# Instructions

- Answer all questions.
- Read each question carefully.
- Predict the output before running any code.
- Do not use an IDE or Python interpreter unless instructed.
- For debugging questions, identify the mistake and explain how to fix it.
- This quiz covers only the concepts learned up to Module 09.

---

# Part A — Conceptual Questions (20 Questions)

### 1. What is a logical operator in Python?

---

### 2. Name the three logical operators available in Python.

---

### 3. What does the `and` operator do?

---

### 4. What does the `or` operator do?

---

### 5. What does the `not` operator do?

---

### 6. Which logical operator returns `True` only when both conditions are `True`?

---

### 7. Which logical operator returns `True` if at least one condition is `True`?

---

### 8. Which logical operator reverses a Boolean value?

---

### 9. What is a Boolean value?

---

### 10. Which comparison operators are commonly used together with logical operators?

---

### 11. What is meant by a logical expression?

---

### 12. What is short-circuit evaluation?

---

### 13. Which operator has higher precedence: `and` or `or`?

---

### 14. What is operator precedence?

---

### 15. Why are parentheses useful in logical expressions?

---

### 16. Can logical operators be used inside `if` statements?

---

### 17. What is the result of `not True`?

---

### 18. What is the result of `not False`?

---

### 19. Why is readability important when writing logical expressions?

---

### 20. Name one real-world application of logical operators.

---

# Part B — Code Prediction (10 Questions)

Predict the output of each program without executing it.

---

### 1.

```python
a = 10
b = 20

print(a < b and b > 15)
```

Output:

______________

---

### 2.

```python
age = 15

print(age >= 18 or age == 15)
```

Output:

______________

---

### 3.

```python
x = 8

print(not x > 10)
```

Output:

______________

---

### 4.

```python
marks = 70

print(marks >= 50 and marks <= 100)
```

Output:

______________

---

### 5.

```python
temperature = 40

print(temperature < 35 or temperature == 40)
```

Output:

______________

---

### 6.

```python
a = 5
b = 8

print(a > b and b > a)
```

Output:

______________

---

### 7.

```python
number = 12

print(not(number < 10))
```

Output:

______________

---

### 8.

```python
x = 7
y = 7

print(x == y and x >= y)
```

Output:

______________

---

### 9.

```python
a = 3
b = 9

print(a == 3 or b == 5)
```

Output:

______________

---

### 10.

```python
value = 25

print(value > 10 and not(value > 30))
```

Output:

______________

---

# Part C — Debugging Questions (5 Questions)

Each program contains one or more mistakes. Identify the mistake(s) and write the corrected code.

---

### 1.

```python
age = 20

if age >= 18 AND age <= 60:
    print("Eligible")
```

Identify the mistake(s):

____________________________________________________

Corrected code:

____________________________________________________

---

### 2.

```python
marks = 80

print(not marks >= 50 and)
```

Identify the mistake(s):

____________________________________________________

Corrected code:

____________________________________________________

---

### 3.

```python
a = 5
b = 8

print(a > b or or b > a)
```

Identify the mistake(s):

____________________________________________________

Corrected code:

____________________________________________________

---

### 4.

```python
number = 10

print(notnot(number == 10))
```

Identify the mistake(s):

____________________________________________________

Corrected code:

____________________________________________________

---

### 5.

```python
x = 5
y = 10

print(x < y and x)
```

Identify the mistake(s):

____________________________________________________

Corrected code:

____________________________________________________

---

# Tips

- Read each expression from left to right.
- Remember the difference between comparison operators and logical operators.
- Use parentheses when expressions become complex.
- Predict the Boolean value of each comparison before evaluating the logical operator.
- Review operator precedence before attempting code prediction questions.

---

# Best Practices

- Keep logical expressions simple and readable.
- Use meaningful variable names.
- Group related conditions using parentheses.
- Test one condition at a time when debugging.
- Review truth tables to understand operator behavior.

---

# Common Mistakes

- Writing `AND`, `OR`, or `NOT` instead of lowercase `and`, `or`, and `not`.
- Forgetting that `not` reverses a Boolean value.
- Confusing comparison operators with logical operators.
- Ignoring operator precedence.
- Writing unnecessarily complex logical expressions.

---

# Summary

This quiz helps reinforce your understanding of Python logical operators by testing conceptual knowledge, code analysis, and debugging skills. Completing these exercises will improve your ability to write correct logical expressions, predict program behavior, and identify common errors before moving on to more advanced Python topics.