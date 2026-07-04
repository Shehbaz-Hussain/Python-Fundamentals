# Best Practices for Using Data Types

## 1. Choose the Right Type

Use the simplest data type that fits the purpose.

- use `int` for whole numbers
- use `float` for decimal values
- use `str` for text
- use `list` for ordered, changeable collections
- use `tuple` for fixed data
- use `dict` for structured key-value records
- use `set` for unique values

## 2. Prefer Readable Names

```python
student_age = 19
student_name = "Amina"
```

Avoid vague names like `x` or `data` when possible.

## 3. Keep Collections Consistent

Avoid mixing many unrelated values in one collection.

## 4. Use Immutability When Appropriate

Tuples and strings are safer when values should not change.

## 5. Handle Missing Values Carefully

Use `None` clearly and consistently.

## 6. Follow PEP 8

- use snake_case for variable names
- keep lines reasonably short
- add blank lines between logical sections

## 7. Optimize for Readability First

Performance matters, but clarity comes first.

## 8. Be Careful with Type Conversion

Convert explicitly when needed and validate input.
