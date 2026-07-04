# Examples: Data Types in Action

## 1. Simple Examples

### Numeric types

```python
age = 20
height = 1.75
complex_number = 3 + 4j
```

### Boolean example

```python
is_student = True
is_active = False
```

### String example

```python
name = "Ada"
message = "Python is fun"
```

## 2. Collection Examples

### List

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
```

### Tuple

```python
point = (10, 20)
```

### Set

```python
numbers = {1, 2, 2, 3}
print(numbers)  # {1, 2, 3}
```

### Dictionary

```python
student = {"name": "Mina", "age": 21, "active": True}
```

## 3. Intermediate Examples

### Comparing values

```python
x = 10
y = 10.0
print(x == y)  # True
print(x is y)  # False
```

### Mutable vs immutable

```python
numbers = [1, 2, 3]
numbers.append(4)

text = "hello"
# text[0] = "H"  # This would raise an error
```

## 4. Real-World Examples

### Student record

```python
student_record = {
    "name": "Lina",
    "courses": ["Math", "Science"],
    "age": 19,
    "active": True,
}
```

### Shopping basket

```python
basket = ["milk", "bread", "eggs"]
```

### Product inventory

```python
product = {
    "sku": "A100",
    "price": 19.99,
    "in_stock": True,
}
```

## 5. AI-Related Examples

### Text preprocessing

```python
text = "AI and Python are powerful"
words = text.split()
print(words)
```

### Feature list

```python
features = [0.5, 0.8, 0.2, 0.9]
```

### Label encoding

```python
labels = {"cat": 0, "dog": 1}
```

## 6. Business Examples

### Sales summary

```python
sales = {
    "January": 1500.50,
    "February": 2200.75,
    "March": 1800.00,
}
```

### Inventory flags

```python
low_stock = True
```

## 7. Student Examples

```python
scores = [88, 92, 77]
average = sum(scores) / len(scores)
```

## 8. Type Conversion Examples

```python
value = "42"
number = int(value)
print(number + 8)
```

```python
price = 10
text_price = str(price)
print("Price is " + text_price)
```

## 9. Practical Notes

- use `list` when you need to add or remove elements
- use `tuple` when the data should not change
- use `dict` for labeled data
- use `set` when you need uniqueness
- use `str` for human-readable text
