# Python Functions Cheat Sheet

## Function Definition

```python
def function_name():
    # Function body
```

---

## Calling a Function

```python
function_name()
```

---

## Function with Parameters

```python
def greet(name):
    print(f"Hello, {name}!")
```

---

## Calling a Function with Arguments

```python
greet("Alice")
```

---

## Function with Multiple Parameters

```python
def add(a, b):
    return a + b
```

---

## Positional Arguments

```python
add(10, 20)
```

---

## Keyword Arguments

```python
add(b=20, a=10)
```

---

## Default Arguments

```python
def greet(name, message="Welcome!"):
    print(message, name)
```

---

## Return Statement

```python
def square(number):
    return number * number
```

---

## Storing a Returned Value

```python
result = square(5)
print(result)
```

---

## Local Variable

```python
def display():
    message = "Hello"
    print(message)
```

---

## Global Variable

```python
course = "Python"


def display():
    print(course)
```

---

## Docstring

```python
def greet():
    """Display a welcome message."""
    print("Hello")
```

---

## Accessing a Docstring

```python
print(greet.__doc__)
```

---

## Best Practices

- Use meaningful function names.
- Keep each function focused on a single task.
- Add docstrings to describe function behavior.
- Use parameters instead of hard-coded values.
- Return values when results need to be reused.
- Follow PEP 8 naming conventions.
- Keep functions short and easy to understand.
- Avoid unnecessary global variables.
- Write reusable and modular code.