# Common Mistakes

## Introduction

Beginners often make mistakes when using logical operators because they misunderstand how conditions are evaluated. Learning these common mistakes will help you write correct and reliable Python programs.

---

# 1. Confusing `=` with `==`

The `=` operator assigns a value to a variable, while `==` compares two values.

### Incorrect

```python
age = 18

print(age = 18)
```

### Correct

```python
age = 18

print(age == 18)
```

---

# 2. Using `and` Instead of `or`

Choose the operator that matches the required logic.

### Incorrect

```python
marks = 45

print(marks >= 50 and marks >= 40)
```

**Output**

```text
False
```

### Correct

```python
marks = 45

print(marks >= 50 or marks >= 40)
```

**Output**

```text
True
```

---

# 3. Forgetting That `not` Reverses the Result

The `not` operator changes `True` to `False` and `False` to `True`.

### Example

```python
is_logged_in = False

print(not is_logged_in)
```

**Output**

```text
True
```

---

# 4. Ignoring Operator Precedence

Python evaluates `not` before `and`, and `and` before `or`.

### Example

```python
print(True or False and False)
```

**Output**

```text
True
```

Use parentheses if the intended order is not obvious.

```python
print((True or False) and False)
```

**Output**

```text
False
```

---

# 5. Writing Overly Complex Conditions

Long logical expressions are difficult to read and understand.

### Avoid

```python
print(age >= 18 and age <= 60 and marks >= 50 and marks <= 100)
```

Prefer keeping expressions as simple as possible while remaining correct.

---

# 6. Forgetting Parentheses for Readability

Parentheses are not always required, but they improve readability.

### Better

```python
print((age >= 18) and (marks >= 50))
```

---

# 7. Assuming Every Condition Is Evaluated

Python uses **short-circuit evaluation**.

### Example

```python
print(False and True)
```

**Output**

```text
False
```

Once the result is known, Python stops evaluating the remaining conditions.

---

# 8. Using Unclear Variable Names

### Avoid

```python
a = 20
b = 90

print(a >= 18 and b >= 50)
```

### Better

```python
age = 20
marks = 90

print(age >= 18 and marks >= 50)
```

---

# 9. Forgetting to Test Different Values

A logical expression should be tested with different inputs, including:

- Valid values
- Invalid values
- Boundary values

Testing helps ensure the expression behaves as expected.

---

# 10. Mixing Too Many Operators Without Parentheses

Expressions with several logical operators can be difficult to understand.

### Better

```python
print((age >= 18 and age <= 60) or marks >= 90)
```

Using parentheses makes the intended logic clear.

---

# Tips to Avoid These Mistakes

- Use `==` for comparisons.
- Select the correct logical operator.
- Remember that `not` reverses a Boolean value.
- Learn the precedence of logical operators.
- Use parentheses to improve readability.
- Write short, clear conditions.
- Use meaningful variable names.
- Test your code with different input values.

---

# Summary

Common mistakes when using logical operators include:

- Confusing `=` with `==`
- Choosing the wrong logical operator
- Misusing the `not` operator
- Ignoring operator precedence
- Writing overly complex expressions
- Omitting parentheses in complex conditions
- Forgetting about short-circuit evaluation
- Using unclear variable names
- Failing to test different input values

Avoiding these mistakes will help you write cleaner, more accurate, and easier-to-maintain Python programs.