# Lambda Functions Revision Notes

## Python Programming Foundation

**Module:** 13 - Lambda Functions  
**Python Version:** 3.13+

---

# Core Concepts

A **lambda function** is a small anonymous function in Python created using the `lambda` keyword.

Unlike normal functions created using `def`, lambda functions:

- Do not require a function name.
- Contain only one expression.
- Automatically return the expression result.
- Are commonly used for short operations.

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

# Lambda Syntax

General syntax:

```python
lambda arguments: expression
```

Example:

```python
add = lambda a, b: a + b

print(add(10, 5))
```

Output:

```text
15
```

## Components

| Component | Description |
|---|---|
| lambda | Keyword used to create anonymous functions |
| arguments | Input values |
| expression | Operation performed and returned |

---

# Lambda Rules and Limitations

## Rules

- Lambda functions use the `lambda` keyword.
- They can accept zero or more arguments.
- They contain only one expression.
- The result is returned automatically.

Example:

```python
multiply = lambda x, y: x * y
```

---

## Limitations

Lambda functions cannot contain:

| Not Allowed | Example |
|---|---|
| Multiple statements | Multiple lines of logic |
| Assignment statements | `x = 5` |
| Complex workflows | Large algorithms |

---

# Lambda vs Normal Function

| Feature | Normal Function | Lambda Function |
|---|---|---|
| Keyword | def | lambda |
| Name | Required | Optional |
| Statements | Multiple | Single expression |
| Best use | Large logic | Small operations |
| Readability | Better for complex code | Better for simple code |

---

# Lambda with map()

## Concept

The `map()` function applies a function to every item in an iterable.

Syntax:

```python
map(function, iterable)
```

Example:

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

## Common Uses

- Data transformation
- Calculations
- Data conversion
- Feature preparation

Example:

```python
prices = [100, 200, 300]

discounted = list(
    map(lambda price: price * 0.9, prices)
)
```

---

# Lambda with filter()

## Concept

The `filter()` function selects elements that satisfy a condition.

Syntax:

```python
filter(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

even = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(even)
```

Output:

```text
[2, 4, 6]
```

---

## Common Uses

- Removing unwanted data
- Selecting records
- Data cleaning

Example:

```python
scores = [45, 80, 90, 30]

passed = list(
    filter(lambda x: x >= 50, scores)
)
```

---

# Lambda with reduce()

## Concept

`reduce()` combines multiple values into a single result.

It is available from the `functools` module.

Syntax:

```python
reduce(function, iterable)
```

Example:

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

## Common Uses

- Total calculations
- Aggregation
- Combining results

Examples:

- Total sales
- Average calculation
- Maximum value calculation

---

# Lambda with sorted()

## Concept

The `sorted()` function creates a sorted list.

Syntax:

```python
sorted(iterable, key=function)
```

Lambda functions are commonly used with the `key` parameter.

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

The `key` parameter defines the sorting rule.

Example:

```python
names = ["python", "AI", "machine"]

sorted_names = sorted(
    names,
    key=lambda x: len(x)
)
```

The list is sorted according to string length.

---

# Common Lambda Patterns

## Pattern 1: Transformation

```python
map(
    lambda x: operation,
    data
)
```

Example:

```python
map(lambda x: x * 2, numbers)
```

---

## Pattern 2: Filtering

```python
filter(
    lambda x: condition,
    data
)
```

Example:

```python
filter(lambda x: x > 50, scores)
```

---

## Pattern 3: Sorting

```python
sorted(
    data,
    key=lambda x: value
)
```

Example:

```python
sorted(
    students,
    key=lambda x: x["marks"]
)
```

---

# Best Practices

## Keep Lambda Functions Simple

Good:

```python
lambda x: x * 2
```

Bad:

```python
lambda x: complicated_large_operation
```

---

## Use Normal Functions for Complex Logic

Use:

```python
def calculate_score():
    ...
```

instead of a large lambda expression.

---

## Use Meaningful Data

Example:

Good:

```python
lambda student: student["marks"]
```

Avoid:

```python
lambda x: x[1]
```

---

# Common Mistakes

## Mistake 1: Using Lambda Everywhere

Lambda functions are not replacements for all functions.

---

## Mistake 2: Writing Complex Expressions

Large lambda expressions reduce readability.

---

## Mistake 3: Forgetting map() Returns an Iterator

Example:

```python
result = map(lambda x: x * 2, numbers)
```

Convert when needed:

```python
list(result)
```

---

## Mistake 4: Incorrect Sorting Logic

Incorrect:

```python
sorted(data)
```

when custom sorting is required.

Correct:

```python
sorted(
    data,
    key=lambda x: x["value"]
)
```

---

# Interview Tips

## Question:
What is a lambda function?

Answer:

A lambda function is an anonymous function that contains a single expression and returns its result automatically.

---

## Question:
Why use lambda functions?

Answer:

They provide a concise way to create small temporary functions.

---

## Question:
Can lambda functions contain multiple statements?

Answer:

No. Lambda functions support only one expression.

---

## Question:
Where are lambda functions commonly used?

Answer:

They are commonly used with map(), filter(), sorted(), and reduce().

---

# Exam Tips

Remember:

- Lambda = Anonymous function
- map() = Transform data
- filter() = Select data
- reduce() = Combine data
- sorted() = Arrange data
- key = Custom sorting rule

---

# Practical Reminders

| Function | Purpose |
|---|---|
| lambda | Create small functions |
| map() | Transform every item |
| filter() | Select matching items |
| reduce() | Combine values |
| sorted() | Sort data |
| key | Define sorting logic |

---

# Memory Tricks

## Remember:

**Map = Modify**

Changes every item.

---

**Filter = Find**

Keeps matching items.

---

**Reduce = Reduce**

Combines many values into one.

---

**Sorted = Arrange**

Organizes data.

---

**Key = Criteria**

Defines sorting rule.

---

# Quick Revision Checklist

Before completing this module, make sure you can:

- [ ] Create lambda functions.
- [ ] Explain lambda limitations.
- [ ] Use lambda with map().
- [ ] Use lambda with filter().
- [ ] Use lambda with sorted().
- [ ] Understand reduce().
- [ ] Use key parameter correctly.
- [ ] Choose between lambda and normal functions.
- [ ] Apply lambda functions in real-world data processing.
- [ ] Write clean functional programming solutions.

---