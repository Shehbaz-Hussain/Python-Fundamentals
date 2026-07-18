# Local Variable Syntax

## Introduction

A local variable is declared inside a function.

It can only be accessed within that function.

After the function finishes executing, the local variable is no longer available.

---

## Syntax

```python
def function_name():
    variable_name = value
```

---

## Example

```python
def calculate():
    total = 50
    print(total)

calculate()
```

### Output

```
50
```

---

## Characteristics

- Created when the function is called.
- Exists only during function execution.
- Cannot be accessed outside the function.

---

## Best Practices

- Use local variables whenever possible.
- Keep their names meaningful.
- Limit their scope to improve maintainability.

---

## Summary

Local variables store temporary data that is needed only while a function is running.