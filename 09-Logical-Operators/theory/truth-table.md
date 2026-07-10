# Truth Table

## Definition

A **truth table** is a table that shows the result of a logical expression for every possible combination of Boolean values.

Since logical operators work with Boolean values (`True` and `False`), truth tables help us understand exactly how each operator behaves.

---

# Purpose

Truth tables are used to:

- Understand how logical operators work.
- Predict the result of logical expressions.
- Verify logical conditions.
- Reduce logical errors in programs.

---

# Boolean Values

Logical operators work with only two Boolean values.

| Boolean Value | Meaning |
|--------------|---------|
| `True` | The condition is true. |
| `False` | The condition is false. |

---

# Truth Table for `and`

The `and` operator returns `True` only when **both** conditions are `True`.

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### Example

```python
print(True and True)
print(True and False)
print(False and True)
print(False and False)
```

**Output**

```text
True
False
False
False
```

---

# Truth Table for `or`

The `or` operator returns `True` if **at least one** condition is `True`.

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### Example

```python
print(True or True)
print(True or False)
print(False or True)
print(False or False)
```

**Output**

```text
True
True
True
False
```

---

# Truth Table for `not`

The `not` operator reverses the Boolean value.

| Condition | Result |
|-----------|--------|
| True | False |
| False | True |

### Example

```python
print(not True)
print(not False)
```

**Output**

```text
False
True
```

---

# Comparing the Operators

| Operator | Returns `True` When |
|----------|----------------------|
| `and` | All conditions are `True`. |
| `or` | At least one condition is `True`. |
| `not` | The original condition is `False`. |

---

# Why Truth Tables Are Important

Truth tables help you:

- Understand logical expressions.
- Predict program behavior.
- Write correct conditions.
- Debug logical errors.
- Learn Boolean logic more effectively.

---

# Notes

- Every logical expression evaluates to either `True` or `False`.
- Truth tables describe every possible result.
- They are especially useful when combining multiple conditions.

---

# Best Practices

- Refer to truth tables when learning logical operators.
- Test your conditions with both `True` and `False` values.
- Use truth tables to verify complex logical expressions.

---

# Summary

- A truth table shows the result of a logical expression for every possible combination of Boolean values.
- The `and` operator returns `True` only if all conditions are `True`.
- The `or` operator returns `True` if at least one condition is `True`.
- The `not` operator reverses a Boolean value.
- Truth tables are an essential tool for understanding and verifying logical expressions.