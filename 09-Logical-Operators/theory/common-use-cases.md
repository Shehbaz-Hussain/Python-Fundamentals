# Common Use Cases of Logical Operators

## Introduction

Logical operators are widely used in Python programs that need to make decisions based on one or more conditions.

They help combine conditions, check alternative conditions, and reverse Boolean values to solve real-world problems.

---

# 1. Age Validation

Logical operators can check whether a person's age falls within a required range.

### Example

```python
age = 22

print(age >= 18 and age <= 60)
```

**Output**

```text
True
```

---

# 2. Voting Eligibility

A person can vote only if they meet the minimum age requirement.

### Example

```python
age = 20

print(age >= 18)
```

**Output**

```text
True
```

---

# 3. Student Admission

A student may qualify for admission if they satisfy multiple requirements.

### Example

```python
marks = 85
age = 19

print(marks >= 80 and age >= 18)
```

**Output**

```text
True
```

---

# 4. Login Validation

A user can log in only if both the username and password are correct.

### Example

```python
username = "admin"
password = "python123"

print(username == "admin" and password == "python123")
```

**Output**

```text
True
```

---

# 5. Temperature Check

A temperature warning can be displayed when the temperature is outside the normal range.

### Example

```python
temperature = 38

print(temperature < 0 or temperature > 35)
```

**Output**

```text
True
```

---

# 6. Positive Even Number Check

Logical operators can verify whether a number satisfies multiple conditions.

### Example

```python
number = 14

print(number > 0 and number % 2 == 0)
```

**Output**

```text
True
```

---

# 7. Password Validation

A simple password check compares the entered password with the expected password.

### Example

```python
entered_password = "python123"

print(entered_password == "python123")
```

**Output**

```text
True
```

---

# 8. Employee Bonus Eligibility

An employee may receive a bonus only if multiple conditions are satisfied.

### Example

```python
years_of_service = 6
performance_score = 90

print(years_of_service >= 5 and performance_score >= 85)
```

**Output**

```text
True
```

---

# 9. Security Check

Access can be granted when one or more security conditions are satisfied.

### Example

```python
has_id_card = True
has_access_code = False

print(has_id_card or has_access_code)
```

**Output**

```text
True
```

---

# 10. Business Hours Check

A business may accept customers only during specific hours.

### Example

```python
current_hour = 14

print(current_hour >= 9 and current_hour <= 17)
```

**Output**

```text
True
```

---

# Why Logical Operators Are Important

Logical operators are used in many types of programs, including:

- Login systems
- Registration forms
- School management systems
- Banking applications
- Security systems
- Admission systems
- Employee management systems
- Online shopping websites
- Mobile applications
- Decision-making programs

---

# Notes

- Logical operators make conditions more flexible.
- Combine conditions with `and` when all conditions must be true.
- Use `or` when any one condition is enough.
- Use `not` to reverse the result of a condition.

---

# Best Practices

- Use meaningful variable names.
- Keep logical expressions short and readable.
- Use parentheses when they improve clarity.
- Test conditions with different input values.

---

# Summary

- Logical operators are used in many real-world programming tasks.
- They allow programs to make decisions based on one or more conditions.
- The `and` operator requires all conditions to be `True`.
- The `or` operator requires at least one condition to be `True`.
- The `not` operator reverses the Boolean value of a condition.
- Understanding these common use cases prepares you to build practical Python programs.