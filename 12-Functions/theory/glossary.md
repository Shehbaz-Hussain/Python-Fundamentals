# Glossary

## Introduction

This glossary contains the important terms introduced in **Module 12 – Functions**.

Understanding these terms will help you read Python documentation, communicate with other programmers, answer interview questions, and write function-based programs with confidence.

The terms are arranged in alphabetical order for quick reference.

---

# A

## Argument

An **argument** is the actual value passed to a function when it is called.

### Example

```python
def greet(name):
    print("Hello,", name)

greet("Ali")
```

Here, `"Ali"` is the **argument**.

---

# C

## Call (Function Call)

A **function call** is the act of executing a function.

### Example

```python
greet()
```

The function begins running when it is called.

---

# D

## Default Argument

A **default argument** is a parameter that already has a predefined value.

If no value is provided during the function call, Python uses the default value.

### Example

```python
def greet(name="Guest"):
    print("Hello,", name)

greet()
```

Output:

```
Hello, Guest
```

---

## Docstring

A **docstring** (documentation string) is a string written as the first statement inside a function.

It explains the purpose of the function.

### Example

```python
def square(number):
    """Return the square of a number."""
    return number * number
```

---

# F

## Function

A **function** is a reusable block of code that performs a specific task.

Functions help organize programs and reduce repeated code.

### Example

```python
def greet():
    print("Hello!")
```

---

## Function Definition

A **function definition** is the process of creating a function using the `def` keyword.

### Example

```python
def welcome():
    print("Welcome!")
```

---

## Function Name

The **function name** is the identifier used to define and call a function.

### Example

```python
def calculate_total():
    pass
```

`calculate_total` is the function name.

---

# G

## Global Variable

A **global variable** is a variable created outside all functions.

It can be accessed throughout the program unless hidden by a local variable with the same name.

### Example

```python
course = "Python"

def show_course():
    print(course)
```

---

# K

## Keyword Argument

A **keyword argument** is an argument passed by specifying the parameter name.

### Example

```python
def student(name, age):
    print(name, age)

student(age=20, name="Ali")
```

---

# L

## Local Variable

A **local variable** is a variable created inside a function.

It exists only while the function is executing and cannot be accessed outside that function.

### Example

```python
def greet():
    message = "Hello"
    print(message)
```

---

# P

## Parameter

A **parameter** is a variable listed in the function definition.

It receives data when the function is called.

### Example

```python
def greet(name):
    print(name)
```

`name` is the parameter.

---

## Positional Argument

A **positional argument** is matched to a parameter based on its position.

### Example

```python
def add(a, b):
    return a + b

add(5, 3)
```

The value `5` is assigned to `a`, and `3` is assigned to `b`.

---

# R

## Reusability

**Reusability** is the ability to use the same function multiple times without rewriting its code.

Functions make programs shorter, cleaner, and easier to maintain.

---

## Return Statement

The **return statement** sends a value back to the place where the function was called.

### Example

```python
def add(a, b):
    return a + b
```

---

## Return Value

A **return value** is the value sent back by a function using the `return` statement.

### Example

```python
result = add(4, 6)
```

The value assigned to `result` is the function's return value.

---

# S

## Scope

**Scope** is the region of a program where a variable can be accessed.

There are two types of scope covered in this module:

- Local scope
- Global scope

---

## Snake Case

**Snake case** is the Python naming convention for functions and variables.

Words are written in lowercase and separated with underscores.

### Examples

```python
calculate_area()
```

```python
print_student_name()
```

---

# V

## Variable

A **variable** is a named location used to store data in a program.

Variables can be:

- Local
- Global

depending on where they are created.

---

# Commonly Confused Terms

| Term | Meaning |
|------|---------|
| Function Definition | Creating a function using `def` |
| Function Call | Executing a function |
| Parameter | Variable in the function definition |
| Argument | Actual value passed during the function call |
| `print()` | Displays output on the screen |
| `return` | Sends a value back to the caller |
| Local Variable | Exists only inside a function |
| Global Variable | Exists throughout the program |

---

# Quick Revision Table

| Term | Short Definition |
|------|------------------|
| Function | A reusable block of code |
| Function Call | Running a function |
| Function Definition | Creating a function |
| Parameter | Variable in a function definition |
| Argument | Value passed to a function |
| Positional Argument | Matched by position |
| Keyword Argument | Matched by parameter name |
| Default Argument | Parameter with a predefined value |
| Return Statement | Sends a value back |
| Return Value | Value returned by a function |
| Local Variable | Variable inside a function |
| Global Variable | Variable outside functions |
| Scope | Area where a variable is accessible |
| Docstring | Documentation inside a function |
| Reusability | Using the same function multiple times |
| Snake Case | Python naming convention using lowercase words separated by underscores |

---

# Tips

> **Tip:** Review this glossary whenever you encounter an unfamiliar term while studying functions.

> **Tip:** Understanding the terminology makes reading Python documentation and discussing code much easier.

> **Tip:** Many interview questions begin by asking for the definition of these terms, so learning them now will help you later.

---

# Key Takeaways

- A function is a reusable block of code that performs a specific task.
- Parameters receive data, while arguments provide data.
- Functions are defined with the `def` keyword and executed through function calls.
- The `return` statement sends a value back to the caller.
- Local variables exist only inside functions, whereas global variables are created outside functions.
- Docstrings document the purpose of functions and improve code readability.
- Following Python's naming conventions, such as using snake_case, helps produce clean and consistent code.
- Understanding these terms provides a strong foundation for writing and reading Python functions.