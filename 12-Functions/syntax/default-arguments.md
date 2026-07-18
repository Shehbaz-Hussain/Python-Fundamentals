# Default Arguments Syntax

## Introduction

Default arguments allow a function parameter to have a predefined value.

If the caller does not provide a value, Python automatically uses the default.

---

## Syntax

```python
def function_name(parameter=default_value):
    # function body
```

---

## Example

```python
def greet(name="Guest"):
    print("Welcome", name)

greet()
greet("Sara")
```

### Output

```
Welcome Guest
Welcome Sara
```

---

## Rules

- Default values are assigned in the function definition.
- Parameters with default values should appear after required parameters.
- A provided argument always replaces the default value.

---

## Best Practices

- Use defaults for optional parameters.
- Choose sensible default values.
- Keep required parameters before optional ones.

---

## Summary

Default arguments make functions more flexible by allowing parameters to have predefined values when no argument is supplied.