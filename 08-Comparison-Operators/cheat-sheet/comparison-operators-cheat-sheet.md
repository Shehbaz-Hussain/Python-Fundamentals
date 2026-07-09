# Comparison Operators Cheat Sheet

## Comparison Operators

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `==` | Equal to | `10 == 10` | `True` |
| `!=` | Not equal to | `10 != 20` | `True` |
| `>` | Greater than | `20 > 10` | `True` |
| `<` | Less than | `10 < 20` | `True` |
| `>=` | Greater than or equal to | `15 >= 15` | `True` |
| `<=` | Less than or equal to | `15 <= 20` | `True` |

---

## General Syntax

```python
value1 operator value2
```

Example:

```python
number1 > number2
```

---

## Boolean Values

Comparison operators always return one of the following values:

```python
True
False
```

---

## Comparing Variables

```python
age = 18
limit = 16

print(age > limit)
```

---

## Comparing User Input

```python
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print(number1 == number2)
```

---

## Quick Examples

```python
10 == 10
```

```python
True
```

```python
8 != 5
```

```python
True
```

```python
25 > 15
```

```python
True
```

```python
7 < 12
```

```python
True
```

```python
18 >= 18
```

```python
True
```

```python
9 <= 4
```

```python
False
```

---

## Remember

- `==` checks equality.
- `!=` checks inequality.
- `>` checks if the left value is greater.
- `<` checks if the left value is less.
- `>=` checks if the left value is greater than or equal to the right value.
- `<=` checks if the left value is less than or equal to the right value.
- Every comparison returns either `True` or `False`.