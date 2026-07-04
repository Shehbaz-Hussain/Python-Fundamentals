# Common Mistakes with Data Types

## 1. Using `==` Instead of `is`

```python
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True
print(x is y)  # False
```

## 2. Confusing Lists and Tuples

```python
numbers_list = [1, 2, 3]
numbers_tuple = (1, 2, 3)
```

A list is mutable; a tuple is not.

## 3. Mutable Default Arguments

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

This can cause unexpected shared state.

## 4. Improper Type Conversion

```python
value = "10"
result = value + 5
```

This raises an error. Convert first:

```python
result = int(value) + 5
```

## 5. Type Confusion

```python
price = "19.99"
print(price + 1)
```

## 6. Forgetting Sets Remove Duplicates

```python
numbers = {1, 2, 2, 3}
print(numbers)  # {1, 2, 3}
```

## 7. Assuming Dictionaries Preserve Order

Dictionaries preserve insertion order in modern Python, but they are conceptually mappings rather than ordered sequences.

## 8. Using Strings Like Lists

```python
word = "hello"
# word[0] = "H"  # invalid
```

## 9. Comparing Booleans to Integers

```python
print(True == 1)  # True
```

This can be surprising for beginners.

## 10. Ignoring `None`

```python
result = None
```

Use `None` intentionally when a value is missing.
