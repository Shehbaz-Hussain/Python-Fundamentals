# Medium Exercise Solutions

## Exercise 01: Admission Eligibility

### Problem

Check whether a student is eligible for admission based on age and marks.

### Solution

```python
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))

is_eligible = age >= 18 and marks >= 80

print("Eligible for admission:", is_eligible)
```

### Explanation

1. Read the student's age.
2. Read the student's marks.
3. Check whether the age is at least **18**.
4. Check whether the marks are at least **80**.
5. Use the `and` operator because both conditions must be satisfied.
6. Display the result.

---

## Exercise 02: Login Validation

### Problem

Check whether both the username and password are correct.

### Solution

```python
correct_username = "admin"
correct_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

login_successful = (
    username == correct_username and
    password == correct_password
)

print("Login successful:", login_successful)
```

### Explanation

1. Store the correct username and password.
2. Read the username and password entered by the user.
3. Compare the entered username with the correct username.
4. Compare the entered password with the correct password.
5. Use the `and` operator because both credentials must match.
6. Display the result.

---

## Exercise 03: Employee Bonus Eligibility

### Problem

Check whether an employee is eligible for a bonus.

### Solution

```python
years_of_service = int(input("Enter years of service: "))
performance_score = int(input("Enter performance score: "))

bonus_eligible = (
    years_of_service >= 5 and
    performance_score >= 85
)

print("Bonus eligible:", bonus_eligible)
```

### Explanation

1. Read the years of service.
2. Read the performance score.
3. Check whether the employee has at least **5 years** of service.
4. Check whether the performance score is at least **85**.
5. Use the `and` operator because both conditions must be true.
6. Display the result.

---

## Exercise 04: Security Access Check

### Problem

Determine whether access should be granted.

### Solution

```python
has_id_card = input("Do you have an ID card? (yes/no): ")
has_access_card = input("Do you have an access card? (yes/no): ")

access_granted = (
    has_id_card == "yes" or
    has_access_card == "yes"
)

print("Access granted:", access_granted)
```

### Explanation

1. Read whether the user has an ID card.
2. Read whether the user has an access card.
3. Check whether either answer is `"yes"`.
4. Use the `or` operator because either condition is sufficient.
5. Display the result.

---

## Exercise 05: Scholarship Eligibility

### Problem

Check whether a student is eligible for a scholarship.

### Solution

```python
marks = int(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))

scholarship_eligible = (
    marks >= 90 and
    attendance >= 85
)

print("Scholarship eligible:", scholarship_eligible)
```

### Explanation

1. Read the student's marks.
2. Read the attendance percentage.
3. Check whether the marks are at least **90**.
4. Check whether the attendance is at least **85%**.
5. Use the `and` operator because both requirements must be satisfied.
6. Display the result.

---

# Key Concepts Practiced

By completing these exercises, you practiced:

- Combining multiple comparison expressions.
- Using the `and` operator for mandatory conditions.
- Using the `or` operator for alternative conditions.
- Applying logical operators to real-world scenarios.
- Creating simple decision-making programs.
- Writing beginner-friendly, readable Python code using only concepts covered through **Module 09**.

---

# Summary

These medium-level exercises build on the fundamentals introduced in this module and prepare you for the next topic: **Conditional Statements (`if`, `elif`, and `else`)**, where logical expressions will be used to control the flow of program execution.