# Function Syntax

## Introduction

Before writing functions, it is important to understand their syntax. **Syntax** refers to the rules that define how code must be written so that Python can understand and execute it.

A function definition follows a fixed structure. Learning this structure will help you create functions correctly and avoid common syntax errors.

This chapter explains the syntax of Python functions step by step using beginner-friendly examples.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the basic syntax of a function.
- Identify the different parts of a function definition.
- Write simple functions using correct syntax.
- Call functions correctly.
- Recognize common syntax mistakes.

---

# Basic Function Syntax

A function is defined using the `def` keyword.

```python
def function_name():
    # Function body
```

This is the simplest form of a Python function.

---

# Parts of a Function Definition

Consider the following example:

```python
def greet():
    print("Hello!")
```

The function consists of the following parts:

| Part | Description |
|------|-------------|
| `def` | Keyword used to define a function |
| `greet` | Function name |
| `()` | Parentheses used for parameters (empty in this example) |
| `:` | Colon indicating the start of the function body |
| Indented block | Statements that belong to the function |

---

# Step-by-Step Breakdown

## Step 1: Use the `def` Keyword

Every function begins with the `def` keyword.

```python
def
```

This tells Python that you are defining a function.

---

## Step 2: Choose a Function Name

Give the function a meaningful name.

Example:

```python
def display_message():
```

Good names describe the task performed by the function.

Examples:

- `calculate_area()`
- `print_result()`
- `show_menu()`
- `find_average()`

---

## Step 3: Add Parentheses

Parentheses follow the function name.

```python
def greet():
```

Even if the function does not require any information, the parentheses must still be included.

---

## Step 4: End with a Colon

A colon (`:`) marks the beginning of the function body.

```python
def greet():
```

Forgetting the colon results in a syntax error.

---

## Step 5: Write the Function Body

The statements inside the function must be indented.

```python
def greet():
    print("Hello!")
```

Everything with the same indentation belongs to the function.

---

# Calling a Function

Defining a function does **not** execute it.

To run the function, call it using its name followed by parentheses.

```python
def greet():
    print("Hello!")

greet()
```

### Expected Output

```
Hello!
```

### Explanation

- The function is first defined.
- The statement `greet()` calls the function.
- Python executes the statements inside the function.

---

# Function with Parameters

Functions can receive information through parameters.

```python
def greet(name):
    print("Hello,", name)
```

Call the function by providing an argument.

```python
greet("Ali")
```

### Expected Output

```
Hello, Ali
```

### Explanation

The parameter `name` receives the argument `"Ali"`.

---

# Function with Multiple Parameters

A function can have more than one parameter.

```python
def add(number1, number2):
    print(number1 + number2)
```

Calling the function:

```python
add(5, 3)
```

### Expected Output

```
8
```

---

# Function with a Return Statement

A function may return a value.

```python
def square(number):
    return number * number
```

Calling the function:

```python
result = square(4)

print(result)
```

### Expected Output

```
16
```

### Explanation

The function returns the calculated value, which is stored in the variable `result`.

---

# General Function Template

The following template shows the structure of a typical function.

```python
def function_name(parameter1, parameter2):
    """
    Optional docstring
    """

    # Statements

    return value
```

Not every function requires parameters, a docstring, or a `return` statement. Include only the parts that are needed.

---

# Syntax Rules

When defining a function:

1. Start with the `def` keyword.
2. Choose a meaningful function name.
3. Write parentheses after the function name.
4. Add a colon (`:`).
5. Indent the function body consistently.
6. Call the function when you want it to execute.

---

# Naming Guidelines

Function names should:

- Use lowercase letters.
- Separate words with underscores.
- Clearly describe the function's purpose.

### Good Examples

```python
calculate_total()
```

```python
display_menu()
```

```python
print_report()
```

### Poor Examples

```python
abc()
```

```python
test()
```

```python
data()
```

---

# Common Syntax Mistakes

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
def greet():
    print("Hello")
```

### Expected Output

```
No output
```

The function has been defined but not executed.

Correct:

```python
greet()
```

---

# Complete Example

```python
def welcome_student(student_name):
    """Display a welcome message for a student."""
    print("Welcome,", student_name)


welcome_student("Sara")
```

### Expected Output

```
Welcome, Sara
```

### Explanation

This example demonstrates:

- Function definition
- Meaningful function name
- Parameter
- Argument
- Docstring
- Function call

---

# Summary Table

| Syntax Element | Purpose |
|---------------|---------|
| `def` | Defines a function |
| Function name | Identifies the function |
| `()` | Holds parameters |
| `:` | Begins the function body |
| Indentation | Groups statements inside the function |
| `return` | Sends a value back to the caller |
| Function call | Executes the function |

---

# Tips

> **Tip:** Always give functions descriptive names that explain their purpose.

> **Tip:** Use consistent indentation, typically four spaces, to define the function body.

> **Tip:** Remember that defining a function does not execute it. You must call the function explicitly.

---

# Warning

Python is sensitive to syntax and indentation.

A missing colon, incorrect indentation, or forgotten parentheses can prevent your program from running.

Always review the structure of your function carefully.

---

# Key Takeaways

- A function is defined using the `def` keyword.
- Every function definition includes a name, parentheses, a colon, and an indented body.
- Parentheses are required even when a function has no parameters.
- A function executes only when it is called.
- Parameters allow functions to receive information.
- The `return` statement sends values back to the caller when needed.
- Following Python's syntax rules and naming conventions helps you write clear, correct, and maintainable functions.