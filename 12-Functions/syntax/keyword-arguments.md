# Keyword Arguments Syntax

## Introduction

In the previous lesson, you learned that **positional arguments** are matched to parameters based on their order.

Python also provides another way to pass values to functions: **keyword arguments**.

With keyword arguments, each argument is assigned to a parameter by **name** instead of by position. This makes function calls easier to read and reduces the chance of passing values in the wrong order.

This chapter explains the syntax and proper use of keyword arguments.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what keyword arguments are.
- Learn the syntax for keyword arguments.
- Pass arguments using parameter names.
- Compare keyword arguments with positional arguments.
- Avoid common mistakes when using keyword arguments.

---

# What Are Keyword Arguments?

**Keyword arguments** are arguments passed to a function by specifying the parameter name followed by an equal sign (`=`) and a value.

General syntax:

```python
function_name(parameter=value)
```

Instead of relying on the order of the arguments, Python matches each value with the parameter name.

---

# Basic Syntax

Function definition:

```python
def function_name(parameter1, parameter2):
    # Function body
```

Function call:

```python
function_name(parameter1=value1, parameter2=value2)
```

---

# Example 1: One Keyword Argument

```python
def greet(name):
    print("Hello,", name)


greet(name="Ali")
```

### Expected Output

```
Hello, Ali
```

### Explanation

The value `"Ali"` is assigned to the parameter `name` by using its name.

---

# Example 2: Multiple Keyword Arguments

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)


student(name="Sara", age=20)
```

### Expected Output

```
Name: Sara
Age: 20
```

---

# Changing the Order

One advantage of keyword arguments is that the order of the arguments does not matter.

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)


student(age=20, name="Sara")
```

### Expected Output

```
Name: Sara
Age: 20
```

### Explanation

Python assigns values using the parameter names rather than their positions.

---

# Comparing Positional and Keyword Arguments

Function definition:

```python
def rectangle(length, width):
    print("Area:", length * width)
```

### Positional Arguments

```python
rectangle(8, 5)
```

### Expected Output

```
Area: 40
```

### Keyword Arguments

```python
rectangle(width=5, length=8)
```

### Expected Output

```
Area: 40
```

Both function calls produce the same result.

---

# Keyword Arguments with Default Parameters

```python
def greet(name="Guest"):
    print("Hello,", name)
```

Using the default value:

```python
greet()
```

### Expected Output

```
Hello, Guest
```

Providing a keyword argument:

```python
greet(name="Ahmed")
```

### Expected Output

```
Hello, Ahmed
```

---

# Using Variables with Keyword Arguments

Variables can also be passed using keyword arguments.

```python
def employee(name, salary):
    print("Employee:", name)
    print("Salary:", salary)


employee_name = "Ali"
employee_salary = 50000

employee(name=employee_name, salary=employee_salary)
```

### Expected Output

```
Employee: Ali
Salary: 50000
```

---

# General Syntax Examples

## One Keyword Argument

```python
function_name(parameter=value)
```

---

## Two Keyword Arguments

```python
function_name(parameter1=value1, parameter2=value2)
```

---

## Three Keyword Arguments

```python
function_name(
    parameter1=value1,
    parameter2=value2,
    parameter3=value3
)
```

---

# Complete Example

```python
def introduce(name, city):
    """Display basic information about a person."""
    print("Name:", name)
    print("City:", city)


introduce(city="Gilgit", name="Ayesha")
```

### Expected Output

```
Name: Ayesha
City: Gilgit
```

### Explanation

Although the arguments are written in a different order, Python matches them using the parameter names.

---

# Common Mistakes

## Misspelling a Parameter Name

Incorrect:

```python
def greet(name):
    print(name)


greet(nam="Ali")
```

Python reports an error because `nam` is not a parameter in the function definition.

Correct:

```python
greet(name="Ali")
```

---

## Forgetting the Equal Sign

Incorrect:

```python
greet(name "Ali")
```

This produces a syntax error.

Correct:

```python
greet(name="Ali")
```

---

## Using a Parameter Name That Does Not Exist

Incorrect:

```python
def add(number1, number2):
    print(number1 + number2)


add(first=5, second=8)
```

The parameter names `first` and `second` do not exist in the function definition.

Correct:

```python
add(number1=5, number2=8)
```

---

# Keyword Arguments vs Positional Arguments

| Feature | Positional Arguments | Keyword Arguments |
|---------|----------------------|-------------------|
| Matching | By position | By parameter name |
| Order | Important | Flexible |
| Readability | Good | Better for many parameters |
| Chance of incorrect assignment | Higher | Lower |

---

# Best Practices

- Use the exact parameter names when writing keyword arguments.
- Choose descriptive parameter names when defining functions.
- Use keyword arguments to improve readability.
- Review the function definition before calling it.
- Keep function calls clear and easy to understand.

---

# Summary Table

| Function Definition | Keyword Function Call |
|---------------------|-----------------------|
| `def greet(name):` | `greet(name="Ali")` |
| `def add(a, b):` | `add(a=5, b=8)` |
| `def student(name, age):` | `student(age=20, name="Sara")` |
| `def rectangle(length, width):` | `rectangle(width=5, length=8)` |

---

# Tips

> **Tip:** Keyword arguments make your code easier to read, especially when a function has several parameters.

> **Tip:** Because keyword arguments identify parameters by name, you can write them in any order.

> **Tip:** Always use the exact parameter names from the function definition.

---

# Warning

Do not invent new parameter names when calling a function.

Python matches keyword arguments only with the parameter names defined in the function. A misspelled or incorrect parameter name will result in an error.

---

# Key Takeaways

- Keyword arguments pass values to functions by specifying parameter names.
- The general syntax is `parameter=value`.
- Keyword arguments improve readability and reduce mistakes caused by incorrect argument order.
- The order of keyword arguments does not affect how values are assigned.
- Parameter names must exactly match those used in the function definition.
- Keyword arguments are especially useful when functions have multiple parameters or when clarity is important.