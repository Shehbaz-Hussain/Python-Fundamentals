# Study Notes: Data Types

## 1. Core Idea

Python data types define how values behave and how much memory they use.

## 2. Remember These Questions

- Is the value numeric, textual, or logical?
- Should the data change later?
- Do I need order, uniqueness, or key-value access?

## 3. Quick Mental Model

- numbers → `int`, `float`, `complex`
- truth → `bool`
- text → `str`
- ordered collections → `list`, `tuple`
- unique collections → `set`, `frozenset`
- mappings → `dict`
- binary → `bytes`, `bytearray`, `memoryview`

## 4. Important Rules

- `list` is mutable, `tuple` is not
- strings are immutable
- sets do not preserve order
- dictionaries map keys to values
- `None` means no value

## 5. Common Patterns

```python
user_name = "Sam"
score = 95
passed = True
```

```python
items = ["pen", "book", "notebook"]
```

```python
config = {"theme": "dark", "font_size": 12}
```

## 6. Study Checklist

- [ ] I know the difference between mutable and immutable types
- [ ] I can explain `==` vs `is`
- [ ] I understand why strings are immutable
- [ ] I can convert between common types
- [ ] I can choose between list, tuple, set, and dict
