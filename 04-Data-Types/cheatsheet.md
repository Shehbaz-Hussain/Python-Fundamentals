# Data Types Cheat Sheet

## 1. Quick Reference

| Type | Example | Mutable | Common Use |
|---|---|---|---|
| `int` | `5` | No | whole numbers |
| `float` | `3.14` | No | decimals |
| `complex` | `2+3j` | No | scientific math |
| `bool` | `True` | No | conditions |
| `str` | `"hello"` | No | text |
| `list` | `[1, 2, 3]` | Yes | dynamic collections |
| `tuple` | `(1, 2, 3)` | No | fixed records |
| `set` | `{1, 2, 3}` | Yes | uniqueness |
| `frozenset` | `frozenset({1, 2})` | No | immutable sets |
| `dict` | `{"a": 1}` | Yes | key-value data |
| `range` | `range(5)` | No | loops |
| `bytes` | `b"abc"` | No | binary data |
| `bytearray` | `bytearray(b"abc")` | Yes | mutable bytes |
| `memoryview` | `memoryview(b"abc")` | Depends | binary access |
| `None` | `None` | No | missing value |

## 2. Common Operations

```python
len([1, 2, 3])         # 3
sum([1, 2, 3])         # 6
"hello".upper()       # HELLO
"a" in ["a", "b"]      # True
```

## 3. Type Conversion

```python
int("10")
float("3.14")
str(42)
bool(0)
list((1, 2, 3))
tuple([1, 2, 3])
set([1, 2, 2])
dict([("a", 1), ("b", 2)])
```

## 4. Mutability Tips

- use `list` when you need to change content
- use `tuple` when you want safety
- use `dict` for structured mappings
- use `set` for membership and uniqueness

## 5. Best Practices

- choose the simplest type that fits the task
- prefer descriptive variable names
- avoid mixing unrelated data in one structure
- keep collections consistent
