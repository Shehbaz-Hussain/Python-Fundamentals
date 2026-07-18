# Function Definition Syntax

## Introduction

Before a function can be used, it must first be **defined**. Defining a function means creating a reusable block of code and giving it a name so that it can be executed whenever needed.

In Python, every function definition follows a specific syntax. Understanding this syntax is essential because even a small mistake, such as forgetting a colon or using incorrect indentation, will result in a syntax error.

This chapter explains the syntax of function definitions step by step.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what a function definition is.
- Learn the syntax for defining a function.
- Identify the parts of a function definition.
- Write correctly formatted function definitions.
- Avoid common syntax mistakes.

---

# What Is a Function Definition?

A **function definition** is the process of creating a function.

When Python encounters a function definition, it stores the function in memory. The function is **not executed immediately**. It executes only when it is called.

---

# Basic Syntax

```python
def function_name():
    # Function body
```

This is the simplest form of a function definition.

---

# Parts of a Function Definition

Consider the following example:

```python
def greet():
    print("Hello!")
```

Each part has a specific purpose.

| Part | Purpose |
|------|---------|
| `def` | Keyword used to define a function |
| `greet` | Function name |
| `()` | Parentheses that hold parameters (empty in this example) |
| `:` | Indicates the beginning of the function body |
| Indented block | Statements that belong to the function |

---

# Step 1: Use the `def` Keyword

Every function definition begins with the `def` keyword.

```python
def
```

This tells Python that a new function is being created.

---

# Step 2: Choose a Meaningful Function Name

The function name should clearly describe what the function does.

### Good Examples

```python
def display_menu():
```

```python
def calculate_total():
```

```python
def print_report():
```

### Poor Examples

```python
def abc():
```

```python
def test():
```

Choose names that make the purpose of the function obvious.

---

# Step 3: Add Parentheses

Parentheses are required after the function name.

```python
def greet():
```

Even if the function does not receive any information, the parentheses cannot be omitted.

---

# Step 4: End the Definition Line with a Colon

Every function definition ends with a colon.

```python
def greet():
```

The colon tells Python that the function body follows.

---

# Step 5: Write the Function Body

The function body contains the statements that will execute when the function is called.

```python
def greet():
    print("Hello!")
```

All statements inside the function must have the same indentation.

---

# Example 1: Simple Function Definition

```python
def welcome():
    print("Welcome to Python!")
```

### Expected Output

```
No output
```

### Explanation

The function has only been **defined**.

It has not been called yet.

---

# Example 2: Function Definition and Function Call

```python
def welcome():
    print("Welcome to Python!")

welcome()
```

### Expected Output

```
Welcome to Python!
```

### Explanation

After defining the function, the statement `welcome()` calls it.

Python then executes the function body.

---

# Function Definition with Parameters

Functions can be defined with parameters.

```python
def greet(name):
    print("Hello,", name)
```

Calling the function:

```python
greet("Ali")
```

### Expected Output

```
Hello, Ali
```

---

# Function Definition with Multiple Parameters

```python
def add(number1, number2):
    print(number1 + number2)
```

Calling the function:

```python
add(5, 7)
```

### Expected Output

```
12
```

---

# Function Definition with a Return Statement

```python
def square(number):
    return number * number
```

Calling the function:

```python
result = square(6)

print(result)
```

### Expected Output

```
36
```

---

# General Template

```python
def function_name(parameter1, parameter2):
    """
    Optional docstring
    """

    # Function body

    return value
```

Depending on the function, parameters, a docstring, and a return statement may or may not be required.

---

# Naming Rules

Function names should:

- Begin with a letter or underscore.
- Contain only letters, numbers, and underscores.
- Be descriptive.
- Use lowercase letters.
- Separate words with underscores.

Examples:

```python
calculate_average()
```

```python
display_student_information()
```

---

# Common Mistakes

## Missing Parentheses

Incorrect:

```python
def greet:
    print("Hello")
```

Correct:

```python
def greet():
    print("Hello")
```

---

## Missing Colon

Incorrect:

```python
def greet()
    print("Hello")
```

Correct:

```python
def greet():
    print("Hello")
```

---

## Incorrect Indentation

Incorrect:

```python
def greet():
print("Hello")
```

Correct:

```python
def greet():
    print("Hello")
```

---

## Forgetting to Call the Function

```python
def welcome():
    print("Welcome!")
```

### Expected Output

```
No output
```

The function has been defined but not executed.

---

# Best Practices

- Use meaningful function names.
- Follow the `snake_case` naming convention.
- Keep functions focused on one task.
- Write a docstring for important functions.
- Maintain consistent indentation.
- Test every function after defining it.

---

# Summary Table

| Syntax Element | Purpose |
|---------------|---------|
| `def` | Starts a function definition |
| Function name | Identifies the function |
| `()` | Holds parameters |
| `:` | Begins the function body |
| Indentation | Defines the function body |
| `return` | Sends a value back to the caller |

---

# Tips

> **Tip:** Think about what your function should do before writing it.

> **Tip:** Choose function names that describe the action being performed.

> **Tip:** Keep function definitions simple and easy to understand.

---

# Warning

Defining a function does **not** execute it.

A function only runs when it is explicitly called elsewhere in the program.

---

# Key Takeaways

- A function definition creates a reusable block of code.
- Every function definition starts with the `def` keyword.
- A function definition includes a name, parentheses, a colon, and an indented body.
- Functions may include parameters and a `return` statement.
- Correct syntax and indentation are essential for Python to interpret the function correctly.
- Well-defined functions improve code organization, readability, and reusability.