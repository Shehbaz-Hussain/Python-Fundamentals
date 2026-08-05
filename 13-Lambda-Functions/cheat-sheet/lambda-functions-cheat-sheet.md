# Lambda Functions Cheat Sheet

## Python Programming Foundation

**Module:** 13 - Lambda Functions  
**Python Version:** 3.13+

---

# Lambda Function Syntax Summary

## Basic Syntax

```python
lambda arguments: expression
```

Example:

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```

---

# Lambda Function Examples

## One Parameter

```python
double = lambda x: x * 2

print(double(10))
```

Output:

```text
20
```

---

## Multiple Parameters

```python
add = lambda a, b: a + b

print(add(5, 3))
```

Output:

```text
8
```

---

## Lambda with Conditional Expression

```python
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(7))
```

Output:

```text
Odd
```

---

# Lambda vs Normal Function

| Feature | Normal Function | Lambda Function |
|---|---|---|
| Keyword | def | lambda |
| Name | Required | Optional |
| Statements | Multiple | Single expression |
| Return | return keyword | Automatic |
| Best Use | Complex logic | Small operations |

---

# map() Function

## Purpose

`map()` transforms every element of an iterable.

---

## Syntax

```python
map(function, iterable)
```

---

## Example

```python
numbers = [1, 2, 3, 4]

result = list(
    map(lambda x: x * 2, numbers)
)

print(result)
```

Output:

```text
[2, 4, 6, 8]
```

---

## map() Workflow

| Input | Operation | Output |
|---|---|---|
| Data | Apply function | Transformed data |

---

## Real-World Uses

- Salary calculations
- Data conversion
- Feature transformation
- Price updates

---

# filter() Function

## Purpose

`filter()` selects items based on a condition.

---

## Syntax

```python
filter(function, iterable)
```

---

## Example

```python
numbers = [10, 15, 20, 25]

result = list(
    filter(lambda x: x > 15, numbers)
)

print(result)
```

Output:

```text
[20, 25]
```

---

## filter() Workflow

| Input | Condition | Output |
|---|---|---|
| Data | True/False check | Selected items |

---

## Real-World Uses

- Finding active users
- Removing invalid data
- Selecting qualified records

---

# reduce() Function

## Purpose

`reduce()` combines multiple values into one result.

---

## Import

```python
from functools import reduce
```

---

## Syntax

```python
reduce(function, iterable)
```

---

## Example

```python
from functools import reduce

numbers = [1, 2, 3, 4]

total = reduce(
    lambda x, y: x + y,
    numbers
)

print(total)
```

Output:

```text
10
```

---

## reduce() Uses

| Task | Example |
|---|---|
| Sum values | Total sales |
| Multiply values | Product calculation |
| Combine data | Aggregation |

---

# sorted() Function

## Purpose

`sorted()` creates a sorted list.

---

## Syntax

```python
sorted(iterable, key=function)
```

---

## Basic Example

```python
numbers = [5, 2, 8, 1]

result = sorted(numbers)

print(result)
```

Output:

```text
[1, 2, 5, 8]
```

---

# sorted() with Lambda

Example:

```python
students = [
    {"name": "Ali", "marks": 80},
    {"name": "Sara", "marks": 95}
]

result = sorted(
    students,
    key=lambda student: student["marks"]
)
```

---

# key Parameter

## Purpose

The `key` parameter defines the sorting rule.

---

## Syntax

```python
sorted(
    data,
    key=lambda item: value
)
```

---

## Examples

### Sort by Length

```python
names = ["Python", "AI", "Machine"]

result = sorted(
    names,
    key=lambda x: len(x)
)
```

---

### Sort Dictionary Data

```python
products = [
    {"name": "Laptop", "price": 90000},
    {"name": "Phone", "price": 50000}
]

result = sorted(
    products,
    key=lambda product: product["price"]
)
```

---

# Comparison Table

| Function | Purpose | Returns |
|---|---|---|
| lambda | Create function | Function object |
| map() | Transform data | Iterator |
| filter() | Select data | Iterator |
| reduce() | Combine data | Single value |
| sorted() | Sort data | List |

---

# Decision Table

| Requirement | Use |
|---|---|
| Change every item | map() |
| Remove unwanted items | filter() |
| Combine many values | reduce() |
| Arrange records | sorted() |
| Create short function | lambda |

---

# Common Patterns

## Data Transformation

```python
list(
    map(lambda x: operation, data)
)
```

---

## Data Filtering

```python
list(
    filter(lambda x: condition, data)
)
```

---

## Custom Sorting

```python
sorted(
    data,
    key=lambda x: value
)
```

---

# Best Practices

| Practice | Reason |
|---|---|
| Keep lambdas short | Improves readability |
| Use meaningful variables | Easier maintenance |
| Use functions for complex logic | Better structure |
| Combine operations carefully | Avoid confusion |

---

# Common Mistakes

## Mistake 1: Large Lambda Expressions

Avoid:

```python
lambda x: very_complex_calculation
```

Use:

```python
def calculate():
    pass
```

---

## Mistake 2: Forgetting list()

Example:

```python
map(lambda x: x * 2, numbers)
```

Convert when required:

```python
list(map(lambda x: x * 2, numbers))
```

---

## Mistake 3: Incorrect key Function

Incorrect:

```python
sorted(products)
```

Correct:

```python
sorted(
    products,
    key=lambda x: x["price"]
)
```

---

# Performance Considerations

| Technique | Consideration |
|---|---|
| lambda | Small overhead, good for short operations |
| map() | Efficient transformation |
| filter() | Efficient selection |
| reduce() | Useful for aggregation |
| sorted() | Requires sorting time |

---

# Interview Tips

## What is lambda?

A lambda is an anonymous function used for short expressions.

---

## Difference between map() and filter()?

| map() | filter() |
|---|---|
| Changes values | Selects values |
| Transformation | Condition checking |

---

## Why use key in sorted()?

The key parameter allows custom sorting rules.

---

# Real-World Examples

## AI Data Processing

```python
normalized = list(
    map(lambda x: x / 100, data)
)
```

---

## Customer Filtering

```python
active = list(
    filter(lambda customer: customer["active"], customers)
)
```

---

## Ranking Systems

```python
ranking = sorted(
    users,
    key=lambda user: user["score"],
    reverse=True
)
```

---

# Quick Revision

| Concept | Remember |
|---|---|
| Lambda | Small anonymous function |
| map | Modify |
| filter | Find |
| reduce | Combine |
| sorted | Arrange |
| key | Sorting rule |

---

# Final Checklist

Before moving forward, you should know:

- [ ] Lambda syntax
- [ ] Lambda limitations
- [ ] Lambda with map()
- [ ] Lambda with filter()
- [ ] Lambda with reduce()
- [ ] Lambda with sorted()
- [ ] key parameter usage
- [ ] Functional programming concepts
- [ ] Real-world applications
- [ ] Best practices

---