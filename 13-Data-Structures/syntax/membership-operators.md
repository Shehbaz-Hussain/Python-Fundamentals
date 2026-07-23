# Membership Operators

## Overview

Membership operators are used to determine whether a value exists within a collection. Python provides two membership operators:

- `in`
- `not in`

These operators return a Boolean value (`True` or `False`).

Membership operators work with many built-in data structures, including:

- Lists
- Tuples
- Sets
- Dictionaries
- Strings

They are commonly used in conditional statements, loops, and data validation.

---

# Basic Syntax

## The `in` Operator

The `in` operator checks whether a value exists in a collection.

General syntax:

```python
value in collection
```

Example:

```python
languages = ["Python", "Java", "C++"]

print("Python" in languages)
```

Output:

```text
True
```

Explanation:

Since `"Python"` is present in the list, the expression evaluates to `True`.

---

## The `not in` Operator

The `not in` operator checks whether a value does **not** exist in a collection.

General syntax:

```python
value not in collection
```

Example:

```python
languages = ["Python", "Java", "C++"]

print("JavaScript" not in languages)
```

Output:

```text
True
```

Explanation:

`"JavaScript"` is not present in the list, so the expression evaluates to `True`.

---

# Syntax Variations

## Membership in a List

```python
numbers = [10, 20, 30, 40]

print(20 in numbers)
```

Output:

```text
True
```

---

## Membership in a Tuple

```python
days = ("Saturday", "Sunday")

print("Sunday" in days)
```

Output:

```text
True
```

---

## Membership in a Set

```python
colors = {"Red", "Green", "Blue"}

print("Green" in colors)
```

Output:

```text
True
```

Sets are commonly used when membership testing is required because they are optimized for this operation.

---

## Membership in a String

```python
word = "Python"

print("th" in word)
```

Output:

```text
True
```

Strings support checking for both characters and substrings.

---

## Membership in a Dictionary

For dictionaries, membership operators check **keys**, not values.

```python
student = {
    "name": "Ali",
    "age": 20
}

print("name" in student)
```

Output:

```text
True
```

Checking a value:

```python
print("Ali" in student)
```

Output:

```text
False
```

Because `"Ali"` is a value rather than a key.

---

# Parameters

Membership operators require two parts:

- A value to search for.
- A collection to search within.

General syntax:

```python
value in collection
```

or

```python
value not in collection
```

---

# Return Values

Membership operators always return a Boolean value.

Example:

```python
numbers = [1, 2, 3]

result = 2 in numbers

print(result)
```

Output:

```text
True
```

---

# Common Patterns

## Using `in` with an `if` Statement

```python
subjects = ["Python", "AI", "Statistics"]

if "Python" in subjects:
    print("Subject found.")
```

Output:

```text
Subject found.
```

---

## Using `not in`

```python
cities = ["Gilgit", "Islamabad", "Lahore"]

if "Karachi" not in cities:
    print("City not found.")
```

Output:

```text
City not found.
```

---

## Membership in a String

```python
text = "Artificial Intelligence"

print("Intelligence" in text)
```

Output:

```text
True
```

---

## Membership in a Tuple

```python
months = (
    "January",
    "February",
    "March"
)

print("April" in months)
```

Output:

```text
False
```

---

## Membership in a Dictionary

```python
employee = {
    "name": "Sara",
    "department": "IT"
}

print("department" in employee)
```

Output:

```text
True
```

---

## Membership in a Set

```python
skills = {
    "Python",
    "Machine Learning",
    "SQL"
}

print("SQL" in skills)
```

Output:

```text
True
```

---

# Common Mistakes

## Assuming Dictionaries Search Values

Incorrect expectation:

```python
student = {
    "name": "Ali"
}

print("Ali" in student)
```

Output:

```text
False
```

Membership checks dictionary keys.

To check values:

```python
print("Ali" in student.values())
```

Output:

```text
True
```

---

## Confusing Uppercase and Lowercase Letters

```python
word = "Python"

print("python" in word)
```

Output:

```text
False
```

Membership testing is case-sensitive.

---

## Assuming Partial Numeric Matches

```python
numbers = [10, 20, 30]

print(2 in numbers)
```

Output:

```text
False
```

The value `2` is not the same as `20`.

---

## Forgetting That Strings Search Substrings

```python
word = "Programming"

print("gram" in word)
```

Output:

```text
True
```

Python searches for substrings in strings.

---

## Using Membership on the Wrong Data Structure

If you need to test for dictionary values rather than keys, remember to use:

```python
value in dictionary.values()
```

instead of:

```python
value in dictionary
```

---

# Best Practices

- Use `in` and `not in` instead of writing unnecessary loops for simple membership tests.
- Use descriptive variable names.
- Remember that dictionary membership checks keys.
- Be aware that string membership is case-sensitive.
- Choose a set when frequent membership testing is required.
- Follow PEP 8 naming and formatting conventions.

---

# Examples

## Example 1

```python
languages = [
    "Python",
    "Java",
    "C++"
]

print("Python" in languages)
```

Output:

```text
True
```

---

## Example 2

```python
numbers = [5, 10, 15]

print(20 not in numbers)
```

Output:

```text
True
```

---

## Example 3

```python
text = "Data Science"

print("Science" in text)
```

Output:

```text
True
```

---

## Example 4

```python
student = {
    "name": "Fatima",
    "semester": 4
}

print("semester" in student)
```

Output:

```text
True
```

---

# Summary

Membership operators provide a simple and readable way to determine whether a value exists in a collection. The `in` operator returns `True` if the value is found, while `not in` returns `True` if the value is absent. These operators work with lists, tuples, sets, strings, and dictionaries, although dictionary membership checks keys rather than values. Using membership operators correctly results in cleaner, more expressive Python code.