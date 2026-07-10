# Exam Notes

## Logical Operators

Logical operators are used to combine or modify Boolean expressions.

Python has **three** logical operators:

- `and`
- `or`
- `not`

Logical operators always return either:

- `True`
- `False`

---

# `and` Operator

## Definition

Returns `True` only if **all** conditions are `True`.

## Syntax

```python
condition1 and condition2
```

## Truth Table

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

# `or` Operator

## Definition

Returns `True` if **at least one** condition is `True`.

## Syntax

```python
condition1 or condition2
```

## Truth Table

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

# `not` Operator

## Definition

Reverses the Boolean value of a condition.

## Syntax

```python
not condition
```

## Truth Table

| Condition | Result |
|-----------|--------|
| True | False |
| False | True |

---

# Operator Precedence

Logical operators are evaluated in the following order:

| Order | Operator |
|------:|----------|
| 1 | `not` |
| 2 | `and` |
| 3 | `or` |

Parentheses `()` have higher precedence than logical operators.

---

# Short-Circuit Evaluation

### `and`

If the first condition is `False`, Python stops evaluating the remaining conditions.

Example:

```python
print(False and True)
```

**Output**

```text
False
```

---

### `or`

If the first condition is `True`, Python stops evaluating the remaining conditions.

Example:

```python
print(True or False)
```

**Output**

```text
True
```

---

# Common Applications

Logical operators are commonly used in:

- Login validation
- Password checking
- Voting eligibility
- Admission systems
- Employee bonus calculation
- Security checks
- Age verification
- Temperature monitoring
- Input validation

---

# Common Mistakes

- Using `=` instead of `==`
- Confusing `and` with `or`
- Forgetting that `not` reverses a Boolean value
- Ignoring operator precedence
- Writing complex conditions without parentheses

---

# Important Points for Exams

- Python has exactly **three** logical operators.
- Logical operators work with Boolean values.
- `and` requires all conditions to be `True`.
- `or` requires at least one condition to be `True`.
- `not` reverses a Boolean value.
- Parentheses improve readability and control evaluation order.
- Python uses short-circuit evaluation for `and` and `or`.

---

# Quick Revision Table

| Operator | Meaning | Returns `True` When |
|----------|---------|---------------------|
| `and` | Combines conditions | All conditions are `True` |
| `or` | Combines alternative conditions | At least one condition is `True` |
| `not` | Reverses a condition | The original condition is `False` |

---

# Exam Tips

- Memorize the truth tables.
- Remember the precedence: `not` → `and` → `or`.
- Practice evaluating logical expressions by hand.
- Use parentheses in complex expressions.
- Test your answers with different Boolean values.
- Read each condition carefully before determining the final result.