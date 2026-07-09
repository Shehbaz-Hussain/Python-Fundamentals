# Best Practices

## 1. Compare Compatible Data Types

Compare values of the same data type whenever possible.

```python
age = 18
limit = 18

print(age == limit)
```

---

## 2. Use Meaningful Variable Names

Choose variable names that clearly describe the data.

```python
student_marks = 85
passing_marks = 50

print(student_marks > passing_marks)
```

---

## 3. Use Spaces Around Operators

Adding spaces around comparison operators improves readability.

```python
print(number1 >= number2)
```

Avoid:

```python
print(number1>=number2)
```

---

## 4. Store User Input in Variables

Read input once and compare the variables.

```python
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print(number1 < number2)
```

---

## 5. Understand Boolean Results

Comparison operators always return:

- `True`
- `False`

```python
print(25 > 10)
```

---

## 6. Use the Correct Operator

Use the operator that matches the comparison you want to perform.

| Operator | Purpose |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

---

## Summary

Following these practices makes comparison expressions easier to read, understand, and maintain.