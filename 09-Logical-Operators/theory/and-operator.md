# And Operator (`and`)

## Definition

The `and` operator is a logical operator in Python that combines two or more conditions. It returns `True` only when **all** the conditions are `True`.

If **any one** condition is `False`, the entire expression becomes `False`.

---

# Purpose

The `and` operator is used when multiple conditions must all be satisfied before an action can be performed.

---

# Syntax

```python
condition1 and condition2
```

Multiple conditions can also be combined.

```python
condition1 and condition2 and condition3
```

---

# How It Works

The `and` operator checks each condition.

- If every condition is `True`, the result is `True`.
- If at least one condition is `False`, the result is `False`.

---

# Simple Examples

## Example 1

```python
age = 20

print(age >= 18 and age <= 60)
```

**Output**

```text
True
```

Both conditions are `True`.

---

## Example 2

```python
marks = 45

print(marks >= 50 and marks <= 100)
```

**Output**

```text
False
```

The first condition is `False`, so the result is `False`.

---

## Example 3

```python
number = 8

print(number > 0 and number % 2 == 0)
```

**Output**

```text
True
```

The number is positive and even.

---

## Example 4

```python
temperature = 35

print(temperature >= 20 and temperature <= 30)
```

**Output**

```text
False
```

The second condition is `False`.

---

# Truth Table

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

# Common Use Cases

The `and` operator is commonly used for:

- Age validation
- Login verification
- Password checking
- Admission eligibility
- Voting eligibility
- Employee bonus rules
- Security checks
- Range checking

---

# Notes

- Every condition must be `True`.
- One `False` condition makes the entire expression `False`.
- The `and` operator is often used with comparison operators.

---

# Best Practices

- Keep conditions simple and readable.
- Use meaningful variable names.
- Use parentheses when combining complex conditions.
- Test each condition carefully.

---

# Summary

- The `and` operator combines two or more conditions.
- It returns `True` only if **all** conditions are `True`.
- If any condition is `False`, the result is `False`.
- It is widely used in decision-making and validation tasks.