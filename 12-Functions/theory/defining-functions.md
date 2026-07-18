# Defining Functions

## Introduction

In the previous lesson, you learned that a **function** is a reusable block of code that performs a specific task. However, before a function can be used, it must first be **defined**.

Defining a function means creating the function by giving it a name and writing the statements that should execute whenever the function is called.

In Python, functions are defined using the **`def`** keyword.

Learning how to define functions is one of the most important programming skills because functions help organize code into small, manageable, and reusable pieces.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand what it means to define a function.
- Use the `def` keyword correctly.
- Name functions using good programming practices.
- Write simple functions.
- Understand the basic structure of a function.
- Identify the different parts of a function definition.

---

# What Does "Define a Function" Mean?

Defining a function means telling Python:

- The function's name.
- The task it should perform.
- Which statements belong to that function.

Defining a function **does not execute it**.

It simply stores the instructions so they can be used later.

---

# Function Definition Syntax

The basic syntax of a function is:

```python
def function_name():
    # Function body
    # Statements
```

---

# Understanding the Syntax

Let's examine each part of the syntax.

```python
def welcome():
    print("Welcome to Python Programming!")
```

### 1. `def`

The keyword `def` tells Python that you are defining a function.

Every function definition begins with this keyword.

---

### 2. Function Name

```python
welcome
```

This is the name of the function.

Choose names that clearly describe what the function does.

Good examples:

- `welcome`
- `calculate_total`
- `display_menu`
- `check_age`

Poor examples:

- `abc`
- `test`
- `data`
- `function1`

Meaningful names make programs easier to understand.

---

### 3. Parentheses `()`

Parentheses are required after the function name.

At this stage, the parentheses are empty because the function does not need any information to perform its task.

Later in this module, you will learn how to place **parameters** inside the parentheses.

---

### 4. Colon `:`

Every function definition ends with a colon.

The colon tells Python that the function body begins on the next line.

---

### 5. Function Body

The indented statements below the function definition form the function body.

Example:

```python
def welcome():
    print("Welcome to Python Programming!")
    print("Enjoy your learning journey.")
```

Everything that belongs to the function must be indented.

Python commonly uses **four spaces** for indentation.

---

# Example 1: Defining a Simple Function

The following function prints a welcome message.

### Code

```python
# Define the function
def welcome():
    print("Welcome to Python Programming!")

# Call the function
welcome()
```

### Expected Output

```text
Welcome to Python Programming!
```

### Explanation of the Output

The function `welcome()` contains one `print()` statement.

When the function is called, Python executes that statement and displays the welcome message.

---

# Example 2: Function with Multiple Statements

A function can contain more than one statement.

### Code

```python
# Define the function
def course_information():
    print("Course: Python Programming")
    print("Module: Functions")
    print("Level: Beginner")

# Call the function
course_information()
```

### Expected Output

```text
Course: Python Programming
Module: Functions
Level: Beginner
```

### Explanation of the Output

The function contains three `print()` statements.

When the function is called, Python executes each statement in order.

---

# Example 3: Reusing a Function

One of the biggest advantages of functions is code reuse.

### Code

```python
# Define the function
def greeting():
    print("Good Morning!")

# Call the function multiple times
greeting()
greeting()
greeting()
```

### Expected Output

```text
Good Morning!
Good Morning!
Good Morning!
```

### Explanation of the Output

The function is written only once but can be called as many times as needed.

This reduces code duplication and makes programs easier to maintain.

---

# Defining vs Calling a Function

Many beginners confuse these two concepts.

| Defining a Function | Calling a Function |
|---------------------|--------------------|
| Creates the function | Executes the function |
| Uses the `def` keyword | Uses the function name followed by `()` |
| Stores the instructions | Runs the stored instructions |
| Happens once | Can happen many times |

Example:

```python
# Function definition
def hello():
    print("Hello!")

# Function call
hello()
```

---

# Function Naming Rules

Function names follow the same basic rules as variable names.

A function name:

- Must begin with a letter or an underscore (`_`).
- Can contain letters, numbers, and underscores.
- Cannot contain spaces.
- Cannot begin with a number.
- Cannot use Python keywords.

### Valid Names

```python
display_menu
calculate_area
student_information
show_result
```

### Invalid Names

```python
2numbers
student name
for
class
```

---

# Function Naming Best Practices

Use names that describe the task performed by the function.

Good examples:

```python
display_marks()
calculate_salary()
check_age()
print_receipt()
```

Avoid vague names like:

```python
abc()
test()
function()
demo()
```

Meaningful names improve readability.

---

# Common Beginner Mistakes

## Forgetting Parentheses

Incorrect:

```python
def welcome:
    print("Hello")
```

Correct:

```python
def welcome():
    print("Hello")
```

---

## Forgetting the Colon

Incorrect:

```python
def welcome()
    print("Hello")
```

Correct:

```python
def welcome():
    print("Hello")
```

---

## Incorrect Indentation

Incorrect:

```python
def welcome():
print("Hello")
```

Correct:

```python
def welcome():
    print("Hello")
```

Python requires proper indentation.

---

## Expecting the Function to Run Automatically

Incorrect assumption:

```python
def welcome():
    print("Hello")
```

Nothing happens because the function has not been called.

Correct:

```python
def welcome():
    print("Hello")

welcome()
```

---

# Tips

- Use meaningful function names.
- Keep each function focused on one task.
- Always use parentheses after the function name.
- Do not forget the colon.
- Indent the function body correctly.
- Define the function before calling it.

---

# Key Points

- Functions are defined using the `def` keyword.
- A function definition creates a reusable block of code.
- Defining a function does not execute it.
- Every function has a name.
- Parentheses are required after the function name.
- The function body must be indented.
- A function can contain one or many statements.

---

# Summary

In this lesson, you learned how to define functions in Python.

You learned:

- What it means to define a function.
- The syntax of a function definition.
- The purpose of the `def` keyword.
- The importance of indentation.
- How to write meaningful function names.
- The difference between defining and executing a function.

In the next lesson, you will learn how to **call functions** and understand what happens when Python executes a function.