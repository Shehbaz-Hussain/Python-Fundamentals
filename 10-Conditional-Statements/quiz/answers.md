# Conditional Statements — Quiz Answers

## Part A — Multiple Choice Questions (MCQs)

| Question | Answer |
|----------|:------:|
| 1 | C |
| 2 | B |
| 3 | B |
| 4 | C |
| 5 | B |
| 6 | C |
| 7 | C |
| 8 | B |
| 9 | A |
| 10 | C |

---

# Part B — Short Answer Questions

## 1. What is a conditional statement?

A conditional statement is a control flow statement that executes different blocks of code depending on whether a condition evaluates to `True` or `False`.

---

## 2. What is the difference between an `if` statement and an `if-else` statement?

- An `if` statement executes code only when its condition is `True`.
- An `if-else` statement provides two possible execution paths: one when the condition is `True` and another when it is `False`.

---

## 3. Why is the `elif` statement useful?

The `elif` statement allows multiple conditions to be checked sequentially without writing separate independent `if` statements. It is useful when there are several possible outcomes but only one should execute.

---

## 4. What is the purpose of comparison operators?

Comparison operators compare two values and return either `True` or `False`. They are commonly used to create conditions in conditional statements.

---

## 5. What is the purpose of logical operators?

Logical operators combine or modify conditions:

- `and` returns `True` only if both conditions are `True`.
- `or` returns `True` if at least one condition is `True`.
- `not` reverses a Boolean value.

---

## 6. Explain the difference between `=` and `==`.

- `=` is the assignment operator used to assign a value to a variable.
- `==` is the equality operator used to compare two values.

Example:

```python
x = 10      # Assignment

if x == 10: # Comparison
    print("Equal")
```

---

## 7. What is a nested `if` statement?

A nested `if` statement is an `if` statement placed inside another `if` or `else` block to perform additional decision-making after an initial condition is satisfied.

---

## 8. Why is indentation important in Python?

Indentation defines code blocks in Python. Incorrect indentation can produce an `IndentationError` or change the program's logic.

---

## 9. Can an `if` statement exist without an `else` statement?

Yes. The `else` block is optional. If the condition is `False` and there is no `else` block, the program simply continues with the next statement.

---

## 10. What happens if none of the conditions in an `if-elif-else` statement evaluate to `True` and there is no `else` block?

No conditional block is executed. Control passes directly to the next statement after the conditional structure.

---

# Part C — Predict the Output

## 1.

```python
x = 8

if x > 5:
    print("Yes")
else:
    print("No")
```

**Output**

```text
Yes
```

---

## 2.

```python
number = 3

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Output**

```text
Odd
```

---

## 3.

```python
marks = 72

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("F")
```

**Output**

```text
C
```

---

## 4.

```python
age = 20

if age >= 18:
    if age >= 60:
        print("Senior")
    else:
        print("Adult")
```

**Output**

```text
Adult
```

---

## 5.

```python
value = -5

if value > 0:
    print("Positive")
elif value < 0:
    print("Negative")
else:
    print("Zero")
```

**Output**

```text
Negative
```

---

# Part D — Programming Solutions

## 1. Check Whether a Number Is Positive, Negative, or Zero

```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

---

## 2. Check Voting Eligibility

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

---

## 3. Grade Calculator

```python
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")
```

---

## 4. Find the Largest of Three Numbers

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
```

---

## 5. Simple Login Verification

```python
correct_username = "admin"
correct_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid username or password")
```

---

# Final Revision Points

- Conditional statements control program flow based on conditions.
- Python provides `if`, `if-else`, `if-elif-else`, and nested `if` statements.
- Comparison operators return Boolean values (`True` or `False`).
- Logical operators combine or modify conditions.
- In an `if-elif-else` chain, only the first matching condition executes.
- Indentation is mandatory because it defines code blocks.
- `=` performs assignment, while `==` compares values.
- Test boundary cases and arrange conditions carefully to avoid logic errors.