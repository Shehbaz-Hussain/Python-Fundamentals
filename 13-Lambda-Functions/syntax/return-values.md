# Return Values in Lambda Functions

## Introduction

Every function in Python can return a value. Lambda functions are no exception.

One of the defining characteristics of a lambda function is that it automatically returns the result of its single expression. Unlike regular functions created with the `def` keyword, a lambda function does **not** use the `return` keyword.

Understanding how return values work is essential because the returned value is often used in calculations, comparisons, sorting, filtering, data transformation, and functional programming.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand what a return value is.
- Explain how lambda functions return values.
- Distinguish between `return` in regular functions and automatic returns in lambda functions.
- Use returned values in expressions and function calls.
- Return different data types from lambda functions.
- Apply best practices when working with lambda return values.

---

# What Is a Return Value?

A **return value** is the result produced by a function after it completes its execution.

The calling code receives this value and can:

- Display it
- Store it in a variable
- Use it in another calculation
- Pass it to another function

Example using a regular function:

```python
def square(number):
    return number ** 2

result = square(5)

print(result)
```

Output

```text
25
```

Here, the function returns the value `25`.

---

# Automatic Return in Lambda Functions

Unlike regular functions, lambda functions automatically return the value of their expression.

Syntax:

```python
lambda parameters: expression
```

The expression itself becomes the return value.

Example:

```python
square = lambda number: number ** 2

print(square(5))
```

Output

```text
25
```

Internally, Python behaves as though the lambda function were written like this:

```python
def square(number):
    return number ** 2
```

---

# No Explicit `return` Statement

The following is **not** valid:

```python
lambda x:
    return x * 2
```

This produces a syntax error because lambda functions cannot contain statements such as `return`.

Correct:

```python
lambda x: x * 2
```

Python automatically returns the result.

---

# Returning Numeric Values

Example:

```python
multiply = lambda a, b: a * b

print(multiply(6, 4))
```

Output

```text
24
```

The expression evaluates to `24`, which becomes the return value.

---

# Returning Strings

Lambda functions can return strings.

Example:

```python
greet = lambda name: f"Hello, {name}!"

print(greet("Alice"))
```

Output

```text
Hello, Alice!
```

---

# Returning Boolean Values

A lambda function may return `True` or `False`.

Example:

```python
is_even = lambda number: number % 2 == 0

print(is_even(8))
print(is_even(5))
```

Output

```text
True
False
```

Boolean return values are commonly used with `filter()` and conditional expressions.

---

# Returning Lists

The returned value can be a list.

Example:

```python
duplicate = lambda value: [value, value]

print(duplicate(7))
```

Output

```text
[7, 7]
```

---

# Returning Tuples

Example:

```python
coordinates = lambda x, y: (x, y)

print(coordinates(10, 20))
```

Output

```text
(10, 20)
```

---

# Returning Dictionaries

Example:

```python
student = lambda name, marks: {
    "name": name,
    "marks": marks
}

print(student("Ali", 92))
```

Output

```text
{'name': 'Ali', 'marks': 92}
```

---

# Returning Expressions

A lambda function always returns the result of evaluating its expression.

Example:

```python
calculate = lambda x: (x + 5) * 2

print(calculate(10))
```

Output

```text
30
```

Python first evaluates:

```python
(10 + 5) * 2
```

The result (`30`) becomes the returned value.

---

# Returning Conditional Results

Lambda functions often return values using conditional expressions.

Example:

```python
status = lambda marks: "Pass" if marks >= 50 else "Fail"

print(status(75))
print(status(42))
```

Output

```text
Pass
Fail
```

---

# Storing Returned Values

Returned values can be assigned to variables.

Example:

```python
cube = lambda number: number ** 3

result = cube(4)

print(result)
```

Output

```text
64
```

---

# Using Returned Values in Expressions

The returned value can immediately participate in another expression.

Example:

```python
square = lambda number: number ** 2

answer = square(6) + 10

print(answer)
```

Output

```text
46
```

---

# Passing Returned Values to Another Function

Example:

```python
double = lambda value: value * 2

print(abs(double(-8)))
```

Output

```text
16
```

The lambda function returns `-16`.

The `abs()` function then converts it to `16`.

---

# Returning Values with `map()`

Lambda return values are frequently used with `map()`.

Example:

```python
numbers = [1, 2, 3, 4]

squares = list(map(lambda number: number ** 2, numbers))

print(squares)
```

Output

```text
[1, 4, 9, 16]
```

Each lambda call returns one squared value.

---

# Returning Values with `filter()`

Example:

```python
numbers = [2, 5, 8, 11, 14]

even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

print(even_numbers)
```

Output

```text
[2, 8, 14]
```

The lambda function returns either:

- `True`
- `False`

Only elements producing `True` are kept.

---

# Returning Values with `sorted()`

Example:

```python
words = ["banana", "kiwi", "apple", "grape"]

sorted_words = sorted(words, key=lambda word: len(word))

print(sorted_words)
```

Output

```text
['kiwi', 'apple', 'grape', 'banana']
```

The lambda function returns the length of each word, which `sorted()` uses as the sorting key.

---

# Rules for Lambda Return Values

- A lambda function always returns the result of its expression.
- The `return` keyword is never written explicitly.
- Only one expression is allowed.
- Any valid Python object can be returned.
- The returned value can be stored, displayed, or passed to another function.

---

# Common Mistakes

## Writing the `return` Keyword

Incorrect:

```python
lambda x: return x * 2
```

Correct:

```python
lambda x: x * 2
```

---

## Expecting Multiple Statements

Incorrect:

```python
lambda x:
    y = x * 2
    y
```

Lambda functions cannot contain assignment statements or multiple lines.

Use a regular function instead.

---

## Forgetting That Every Lambda Returns Something

Even this lambda returns a value:

```python
lambda: None
```

The returned value is simply `None`.

---

## Returning Complex Logic

Avoid squeezing complicated logic into a single expression.

Instead of:

```python
lambda x: ...
```

Use:

```python
def process(x):
    ...
    return result
```

Complex logic is easier to read and maintain in a regular function.

---

# Best Practices

- Keep return expressions short and readable.
- Return one clear result.
- Use lambda functions only for simple operations.
- Use regular functions for complex calculations.
- Give meaningful names when assigning lambda functions to variables.
- Use lambda return values with functions such as `map()`, `filter()`, and `sorted()`.

---

# Lambda Return Values vs Regular Function Return Values

| Feature | Lambda Function | Regular Function |
|--------|-----------------|------------------|
| Uses `return` keyword | ✘ | ✔ |
| Automatic return | ✔ | ✘ |
| Returns one expression | ✔ | ✘ |
| Multiple return statements | ✘ | ✔ |
| Complex return logic | ✘ | ✔ |
| Readability for simple operations | Excellent | Good |

---

# Real-World Applications

Lambda return values are commonly used for:

- Data transformation
- Sorting collections
- Filtering data
- Mathematical calculations
- Event callbacks
- Functional programming
- Processing datasets
- Automation scripts

Example:

```python
prices = [120, 350, 500]

discounted = list(map(lambda price: price * 0.9, prices))

print(discounted)
```

Output

```text
[108.0, 315.0, 450.0]
```

Each lambda call returns the discounted price.

---

# Summary

A lambda function automatically returns the result of its single expression. Unlike regular functions, no `return` keyword is used. The returned value can be of any Python data type and is frequently used with functions such as `map()`, `filter()`, and `sorted()`. Lambda functions are best suited for short, simple return expressions.

---

# Key Takeaways

- Every lambda function returns a value automatically.
- The `return` keyword is never used inside a lambda function.
- Only one expression can be evaluated and returned.
- Lambda functions can return numbers, strings, booleans, lists, tuples, dictionaries, or any other Python object.
- Returned values can be stored, displayed, or passed to other functions.
- Keep lambda return expressions simple and readable.
- Use regular functions when multiple statements or complex return logic are required.