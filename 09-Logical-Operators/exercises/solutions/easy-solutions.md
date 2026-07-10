# Easy Exercise Solutions

## Exercise 01: AND Operator Practice

### Problem

Check whether the user's age is between **18** and **60** (inclusive).

### Solution

```python
age = int(input("Enter your age: "))

is_valid_age = age >= 18 and age <= 60

print("Age is between 18 and 60:", is_valid_age)
```

### Explanation

1. Read the user's age.
2. Check whether the age is greater than or equal to **18**.
3. Check whether the age is less than or equal to **60**.
4. Use the `and` operator to combine both conditions.
5. Display the result.

---

## Exercise 02: OR Operator Practice

### Problem

Check whether the temperature is below **0°C** or above **35°C**.

### Solution

```python
temperature = float(input("Enter the temperature: "))

is_outside_range = temperature < 0 or temperature > 35

print("Temperature is outside the normal range:", is_outside_range)
```

### Explanation

1. Read the temperature.
2. Check whether it is below **0°C**.
3. Check whether it is above **35°C**.
4. Use the `or` operator because either condition is sufficient.
5. Display the result.

---

## Exercise 03: NOT Operator Practice

### Problem

Check whether the entered password is incorrect.

### Solution

```python
correct_password = "python123"

entered_password = input("Enter your password: ")

is_incorrect = not (entered_password == correct_password)

print("Password is incorrect:", is_incorrect)
```

### Explanation

1. Store the correct password.
2. Read the user's password.
3. Compare the entered password with the correct password.
4. Use the `not` operator to reverse the comparison result.
5. Display whether the password is incorrect.

---

## Exercise 04: Positive and Even Number

### Problem

Check whether a number is both positive and even.

### Solution

```python
number = int(input("Enter a number: "))

is_positive_and_even = number > 0 and number % 2 == 0

print("Positive and even:", is_positive_and_even)
```

### Explanation

1. Read an integer.
2. Check whether the number is positive.
3. Check whether the number is even.
4. Use the `and` operator because both conditions must be true.
5. Display the result.

---

## Exercise 05: Exam Eligibility

### Problem

Check whether a student is eligible for the examination.

### Solution

```python
attendance = float(input("Enter attendance percentage: "))
fee_paid = input("Have you paid the examination fee? (yes/no): ")

is_eligible = attendance >= 75 and fee_paid == "yes"

print("Eligible for exam:", is_eligible)
```

### Explanation

1. Read the attendance percentage.
2. Read whether the examination fee has been paid.
3. Check whether attendance is at least **75%**.
4. Check whether the fee has been paid.
5. Use the `and` operator because both conditions must be satisfied.
6. Display the result.

---

# Summary

These exercises reinforce the following concepts:

- Using the `and` operator
- Using the `or` operator
- Using the `not` operator
- Combining comparison operators with logical operators
- Solving simple real-world decision-making problems