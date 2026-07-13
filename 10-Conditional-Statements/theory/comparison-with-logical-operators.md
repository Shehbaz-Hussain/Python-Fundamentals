# Combining Comparison and Logical Operators

## Introduction

In previous modules, you learned about:

- **Comparison operators**, which compare two values.
- **Logical operators**, which combine multiple conditions.

When writing conditional statements, these two types of operators are often used together to create more meaningful and practical decision-making logic.

For example, instead of checking only whether a person's age is greater than or equal to 18, you might also need to verify that the person is a citizen before allowing them to vote.

This lesson explains how comparison operators and logical operators work together inside conditional statements.

---

# Review: Comparison Operators

Comparison operators compare two values and produce a Boolean result.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `10 > 4` | `True` |
| `<` | Less than | `2 < 8` | `True` |
| `>=` | Greater than or equal to | `18 >= 18` | `True` |
| `<=` | Less than or equal to | `6 <= 5` | `False` |

These operators return either `True` or `False`.

---

# Review: Logical Operators

Logical operators combine one or more Boolean expressions.

| Operator | Meaning |
|----------|---------|
| `and` | Returns `True` only if **all** conditions are `True`. |
| `or` | Returns `True` if **at least one** condition is `True`. |
| `not` | Reverses the Boolean value of a condition. |

Logical operators are most useful when a decision depends on multiple conditions.

---

# Why Combine Them?

Comparison operators answer individual questions.

Examples:

- Is the age at least 18?
- Is the password correct?
- Are the marks greater than 50?

Logical operators combine those answers into a single decision.

Examples:

- Is the user at least 18 **and** a citizen?
- Is the number less than 0 **or** greater than 100?
- Is the password **not** empty?

Combining both types of operators allows programs to solve more realistic problems.

---

# General Syntax

```python
if condition1 and condition2:
    # Code
```

```python
if condition1 or condition2:
    # Code
```

```python
if not condition:
    # Code
```

Each condition is usually created using comparison operators.

---

# Using the `and` Operator

The `and` operator requires **every condition** to be `True`.

## Example 1: Voting Eligibility

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote.")
```

### Output

```text
Eligible to vote.
```

### Explanation

Python checks:

- `age >= 18`
- `citizen`

Both conditions are `True`, so the message is displayed.

---

## Example 2: Exam Qualification

```python
marks = 75
attendance = 90

if marks >= 50 and attendance >= 75:
    print("Course completed successfully.")
```

### Output

```text
Course completed successfully.
```

The student satisfies both requirements.

---

# Using the `or` Operator

The `or` operator requires **at least one condition** to be `True`.

## Example 3: Weekend Check

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

### Output

```text
Weekend
```

Only one comparison needs to be `True`.

---

## Example 4: Discount Eligibility

```python
member = True
purchase_amount = 1200

if member or purchase_amount >= 1000:
    print("Discount applied.")
```

### Output

```text
Discount applied.
```

The customer qualifies because at least one condition is satisfied.

---

# Using the `not` Operator

The `not` operator reverses the result of a condition.

## Example 5: Account Status

```python
account_blocked = False

if not account_blocked:
    print("Login allowed.")
```

### Output

```text
Login allowed.
```

### Explanation

- `account_blocked` is `False`.
- `not False` becomes `True`.
- The `if` block executes.

---

# Combining Multiple Conditions

A conditional statement may contain several comparison expressions.

```python
age = 22
marks = 80
citizen = True

if age >= 18 and marks >= 50 and citizen:
    print("All requirements are satisfied.")
```

Every comparison must evaluate to `True`.

---

# Mixing `and` and `or`

Logical operators can be combined.

```python
age = 20
student = True
employee = False

if age >= 18 and (student or employee):
    print("Eligible")
```

### Explanation

The person must:

- Be at least 18 years old.
- Be either a student or an employee.

> **Note:** Parentheses improve readability by making the intended grouping of conditions clear.

---

# Using Comparison and Logical Operators with User Input

```python
age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ")

if age >= 18 and citizen == "yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

### Sample Output

```text
Enter your age: 21
Are you a citizen? (yes/no): yes
You are eligible to vote.
```

---

# Real-World Applications

Comparison and logical operators are used together in many applications, including:

- Login systems
- ATM machines
- Voting eligibility
- Student grading systems
- Product discounts
- Security checks
- Traffic management
- Age verification
- Membership validation

---

# Common Mistakes

## Confusing `=` with `==`

Incorrect:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

---

## Using the Wrong Logical Operator

Incorrect:

```python
if marks >= 50 or attendance >= 75:
```

This allows students to pass even if only one requirement is met.

Correct:

```python
if marks >= 50 and attendance >= 75:
```

---

## Writing Conditions That Are Difficult to Read

Less readable:

```python
if age >= 18 and citizen == True:
```

Better:

```python
if age >= 18 and citizen:
```

---

## Forgetting Parentheses in Complex Conditions

Although not always required, parentheses make complex conditions easier to understand.

Better example:

```python
if age >= 18 and (student or employee):
    print("Eligible")
```

---

# Best Practices

- Keep conditions simple and readable.
- Use meaningful variable names.
- Group related conditions logically.
- Use parentheses to improve clarity in complex expressions.
- Test every possible outcome.
- Avoid writing unnecessarily long conditional expressions.

---

# Interview Insights

You should be able to answer questions such as:

- What is the difference between comparison and logical operators?
- Why are logical operators used with comparison operators?
- When should you use `and` instead of `or`?
- What does the `not` operator do?
- Why can parentheses improve readability?

These are common beginner-level Python interview questions.

---

# Key Points

- Comparison operators compare values and return Boolean results.
- Logical operators combine one or more Boolean expressions.
- The `and` operator requires every condition to be `True`.
- The `or` operator requires at least one condition to be `True`.
- The `not` operator reverses the result of a condition.
- Combining these operators enables more powerful and realistic decision making.

---

# Summary

Comparison operators and logical operators work together to create meaningful conditions in Python programs. Comparison operators evaluate individual expressions, while logical operators combine those expressions into a single decision. Mastering this combination allows you to write flexible, readable, and practical conditional statements for real-world applications.