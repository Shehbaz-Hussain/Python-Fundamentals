# Common Mistakes

## 1. Using `=` Instead of `==`

Incorrect:

```python
print(number1 = number2)
```

Correct:

```python
print(number1 == number2)
```

---

## 2. Confusing `>` and `>=`

Incorrect expectation:

```python
10 > 10
```

Result:

```python
False
```

Correct:

```python
10 >= 10
```

Result:

```python
True
```

---

## 3. Confusing `<` and `<=`

Incorrect expectation:

```python
15 < 15
```

Result:

```python
False
```

Correct:

```python
15 <= 15
```

Result:

```python
True
```

---

## 4. Comparing Different Data Types

Incorrect:

```python
number = 10

print(number == "10")
```

Result:

```python
False
```

Compare values of the same data type whenever possible.

---

## 5. Forgetting Type Conversion

Incorrect:

```python
number = input("Enter a number: ")

print(number > 10)
```

Correct:

```python
number = int(input("Enter a number: "))

print(number > 10)
```

---

## 6. Expecting Comparison Operators to Change Values

Comparison operators only compare values. They do not modify variables.

```python
number1 = 20
number2 = 10

print(number1 > number2)
```

The values of `number1` and `number2` remain unchanged.

---

## Summary

Avoid these common mistakes to write correct comparison expressions and obtain the expected Boolean results.