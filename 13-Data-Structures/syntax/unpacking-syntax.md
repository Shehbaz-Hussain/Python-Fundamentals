# Unpacking Syntax

## Overview

**Unpacking** is the process of assigning the elements of an iterable (such as a list or tuple) to multiple variables in a single statement.

Instead of accessing each element individually using indexing, unpacking allows you to retrieve multiple values at once.

Python supports unpacking for several iterable data structures, including:

- Lists
- Tuples
- Strings
- Sets (although the order is not guaranteed)
- Dictionaries (keys are unpacked by default)

Unpacking makes code shorter, easier to read, and less error-prone.

---

# Basic Syntax

The general syntax for unpacking is:

```python
variable1, variable2, variable3 = iterable
```

The number of variables must match the number of elements in the iterable unless extended unpacking is used.

---

## Unpacking a List

```python
numbers = [10, 20, 30]

first, second, third = numbers

print(first)
print(second)
print(third)
```

Output:

```text
10
20
30
```

Explanation:

Each list element is assigned to the corresponding variable.

---

## Unpacking a Tuple

```python
coordinates = (35.90, 74.34)

latitude, longitude = coordinates

print(latitude)
print(longitude)
```

Output:

```text
35.9
74.34
```

---

## Unpacking a String

```python
word = "CAT"

first, second, third = word

print(first)
print(second)
print(third)
```

Output:

```text
C
A
T
```

Each character is assigned to a separate variable.

---

# Syntax Variations

## Extended Unpacking

Use the `*` operator to collect multiple elements into a list.

```python
numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

Output:

```text
10
[20, 30, 40]
50
```

Explanation:

- `first` receives the first element.
- `middle` receives the remaining middle elements as a list.
- `last` receives the final element.

---

## Ignoring Values

Use `_` for values you do not need.

```python
numbers = [10, 20, 30]

first, _, third = numbers

print(first)
print(third)
```

Output:

```text
10
30
```

By convention, `_` indicates that the value is intentionally ignored.

---

## Swapping Variables

Python allows variables to be swapped without a temporary variable.

```python
x = 10
y = 20

x, y = y, x

print(x)
print(y)
```

Output:

```text
20
10
```

This is a common and Pythonic programming technique.

---

## Unpacking Dictionary Keys

By default, unpacking a dictionary returns its keys.

```python
student = {
    "name": "Ali",
    "age": 20
}

key1, key2 = student

print(key1)
print(key2)
```

Output:

```text
name
age
```

---

# Parameters

Unpacking itself does not use parameters.

However, it requires:

- An iterable.
- A matching number of variables, unless extended unpacking (`*`) is used.

Example:

```python
a, b = [10, 20]
```

---

# Return Values

Unpacking does not return a value.

Instead, it assigns values to variables.

Example:

```python
values = (100, 200)

x, y = values

print(x)
print(y)
```

Output:

```text
100
200
```

---

# Common Patterns

## Assign Multiple Values

```python
name, age = ("Sara", 21)

print(name)
print(age)
```

Output:

```text
Sara
21
```

---

## Extended Unpacking

```python
letters = ["A", "B", "C", "D"]

first, *remaining = letters

print(first)
print(remaining)
```

Output:

```text
A
['B', 'C', 'D']
```

---

## Ignore Unwanted Values

```python
data = [100, 200, 300]

first, _, third = data

print(first)
print(third)
```

Output:

```text
100
300
```

---

## Swap Two Variables

```python
city1 = "Gilgit"
city2 = "Islamabad"

city1, city2 = city2, city1

print(city1)
print(city2)
```

Output:

```text
Islamabad
Gilgit
```

---

## Unpacking Characters

```python
text = "AI"

first, second = text

print(first)
print(second)
```

Output:

```text
A
I
```

---

# Common Mistakes

## Number of Variables Does Not Match

Incorrect:

```python
numbers = [10, 20]

a, b, c = numbers
```

This raises a `ValueError` because there are more variables than values.

---

## Too Many Values Without Extended Unpacking

Incorrect:

```python
numbers = [10, 20, 30]

a, b = numbers
```

This also raises a `ValueError`.

Use:

```python
a, *b = numbers
```

---

## Assuming Set Order

```python
colors = {"Red", "Green", "Blue"}

a, b, c = colors
```

The unpacking succeeds if there are exactly three elements, but the assignment order is not guaranteed because sets are unordered.

---

## Expecting Dictionary Values

```python
student = {
    "name": "Ali",
    "age": 20
}

a, b = student
```

This assigns the dictionary's **keys**, not its values.

---

## Forgetting the Asterisk

Incorrect:

```python
numbers = [1, 2, 3, 4]

first, middle, last = numbers
```

This raises a `ValueError`.

Correct:

```python
first, *middle, last = numbers
```

---

# Best Practices

- Use unpacking to improve readability.
- Use descriptive variable names.
- Use extended unpacking when the number of elements may vary.
- Use `_` for values you intentionally ignore.
- Avoid unpacking sets when the order of values matters.
- Follow PEP 8 naming and formatting guidelines.

---

# Examples

## Example 1

```python
student = ["Ali", 20]

name, age = student

print(name)
print(age)
```

Output:

```text
Ali
20
```

---

## Example 2

```python
scores = [80, 85, 90, 95]

first, *others = scores

print(first)
print(others)
```

Output:

```text
80
[85, 90, 95]
```

---

## Example 3

```python
x = 5
y = 10

x, y = y, x

print(x)
print(y)
```

Output:

```text
10
5
```

---

## Example 4

```python
country = "PK"

first, second = country

print(first)
print(second)
```

Output:

```text
P
K
```

---

# Summary

Unpacking is a convenient Python feature that assigns elements from an iterable to multiple variables in a single statement. It works with lists, tuples, strings, sets, and dictionaries, although dictionaries unpack keys by default and sets do not guarantee order. Extended unpacking using the `*` operator provides additional flexibility when the number of elements varies. Proper use of unpacking results in cleaner, more readable, and more maintainable Python code.