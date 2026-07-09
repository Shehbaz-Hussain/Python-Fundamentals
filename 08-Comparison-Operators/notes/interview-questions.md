# Interview Questions

## Basic Questions

### 1. What are comparison operators in Python?

Comparison operators are operators used to compare two values or expressions. They return either `True` or `False`.

---

### 2. What is the result of a comparison operation?

A comparison operation returns a Boolean value:

- `True`
- `False`

---

### 3. Name all comparison operators in Python.

- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`

---

### 4. What is the difference between `=` and `==`?

- `=` is the assignment operator used to assign a value to a variable.
- `==` is the equality operator used to compare two values.

---

### 5. What does the `!=` operator do?

It checks whether two values are not equal.

---

### 6. What is the difference between `>` and `>=`?

- `>` returns `True` only if the left value is greater than the right value.
- `>=` returns `True` if the left value is greater than or equal to the right value.

---

### 7. What is the difference between `<` and `<=`?

- `<` returns `True` only if the left value is less than the right value.
- `<=` returns `True` if the left value is less than or equal to the right value.

---

### 8. Can comparison operators be used with variables?

Yes.

Example:

```python
age = 18
limit = 16

print(age > limit)
```

---

### 9. Can comparison operators be used with user input?

Yes. Convert the input to the appropriate data type before comparing it.

Example:

```python
number = int(input("Enter a number: "))

print(number >= 100)
```

---

### 10. Why are comparison operators important?

Comparison operators are used to compare values and produce Boolean results. They are the foundation for making decisions in Python programs.