# Parameter Syntax

## Introduction

Functions become much more useful when they can work with different pieces of information. Instead of writing separate functions for every situation, we can create **parameters** that allow a function to receive values when it is called.

Parameters make functions flexible, reusable, and easier to maintain.

This chapter explains the syntax of parameters and demonstrates how to use them correctly in beginner-level Python programs.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the syntax of parameters.
- Define functions with one or more parameters.
- Pass arguments to parameters.
- Recognize the relationship between parameters and arguments.
- Use default parameter values.
- Avoid common parameter-related mistakes.

---

# What Is a Parameter?

A **parameter** is a variable listed inside the parentheses of a function definition.

It acts as a placeholder that receives a value when the function is called.

### General Syntax

```python
def function_name(parameter):
    # Function body
```

---

# Function Without Parameters

A function does not always need parameters.

```python
def welcome():
    print("Welcome to Python!")
```

Calling the function:

```python
welcome()
```

### Expected Output

```
Welcome to Python!
```

### Explanation

This function always performs the same task and therefore does not require any input.

---

# Function with One Parameter

A function can receive one piece of information.

### Syntax

```python
def function_name(parameter):
    # Function body
```

### Example

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

### Explanation

- `name` is the parameter.
- `"Ali"` is the argument.
- The parameter receives the argument during the function call.

---

# Function with Multiple Parameters

A function can receive multiple values.

### Syntax

```python
def function_name(parameter1, parameter2):
    # Function body
```

### Example

```python
def add(number1, number2):
    print(number1 + number2)
```

Calling the function:

```python
add(8, 5)
```

### Expected Output

```
13
```

### Explanation

The function receives two arguments and uses them in the calculation.

---

# Parameter Order

Parameters are listed in the order they should receive values.

```python
def student(name, age):
    print(name)
    print(age)
```

Correct function call:

```python
student("Sara", 20)
```

### Expected Output

```
Sara
20
```

---

# Positional Arguments

When arguments are passed according to their position, they are called **positional arguments**.

```python
def rectangle(length, width):
    print(length * width)

rectangle(8, 5)
```

### Expected Output

```
40
```

The first argument is assigned to `length`, and the second is assigned to `width`.

---

# Keyword Arguments

Arguments can also be passed using parameter names.

```python
def student(name, age):
    print(name)
    print(age)

student(age=19, name="Ali")
```

### Expected Output

```
Ali
19
```

### Explanation

The order of the arguments does not matter because each value is assigned using its parameter name.

---

# Default Parameters

A parameter can have a predefined value.

### Syntax

```python
def function_name(parameter="default_value"):
    # Function body
```

### Example

```python
def greet(name="Guest"):
    print("Hello,", name)
```

Calling the function:

```python
greet()
```

### Expected Output

```
Hello, Guest
```

Calling the function with an argument:

```python
greet("Ayesha")
```

### Expected Output

```
Hello, Ayesha
```

### Explanation

If no argument is provided, Python uses the default value.

---

# Function with Multiple Parameters and a Default Value

```python
def introduce(name, country="Pakistan"):
    print("Name:", name)
    print("Country:", country)
```

Calling the function:

```python
introduce("Ali")
```

### Expected Output

```
Name: Ali
Country: Pakistan
```

Calling the function:

```python
introduce("Sara", "Canada")
```

### Expected Output

```
Name: Sara
Country: Canada
```

---

# General Parameter Template

```python
def function_name(parameter1, parameter2="Default"):
    """
    Optional docstring
    """

    # Statements

    return value
```

Depending on the function, parameters, a docstring, and a return statement may or may not be needed.

---

# Parameter Naming Guidelines

Choose descriptive parameter names.

### Good Examples

```python
def calculate_area(length, width):
```

```python
def greet(student_name):
```

```python
def calculate_salary(monthly_salary):
```

### Poor Examples

```python
def calculate(a, b):
```

```python
def data(x):
```

Meaningful names make programs easier to read and understand.

---

# Common Mistakes

## Forgetting a Required Argument

Incorrect:

```python
def greet(name):
    print("Hello,", name)

greet()
```

Python reports that a required argument is missing.

Correct:

```python
greet("Ali")
```

---

## Passing Arguments in the Wrong Order

Incorrect:

```python
def student(name, age):
    print(name)
    print(age)

student(20, "Ali")
```

### Output

```
20
Ali
```

Correct:

```python
student("Ali", 20)
```

---

## Using Unclear Parameter Names

Poor:

```python
def area(a, b):
```

Better:

```python
def area(length, width):
```

Descriptive parameter names improve readability.

---

# Best Practices

- Use meaningful parameter names.
- Keep the number of parameters reasonable.
- Use default parameters when a value is commonly the same.
- Pass arguments in the correct order when using positional arguments.
- Use keyword arguments when they improve readability.
- Write a docstring describing the function and its parameters.

---

# Summary Table

| Syntax | Purpose |
|--------|---------|
| `def greet(name):` | Function with one parameter |
| `def add(a, b):` | Function with two parameters |
| `def greet(name="Guest"):` | Function with a default parameter |
| `greet("Ali")` | Positional argument |
| `greet(name="Ali")` | Keyword argument |

---

# Tips

> **Tip:** Choose parameter names that clearly describe the information they receive.

> **Tip:** Use default parameter values when a function often receives the same value.

> **Tip:** If you are unsure about the order of arguments, keyword arguments can make your function calls easier to understand.

---

# Warning

Do not confuse **parameters** with **arguments**.

- **Parameters** are written in the function definition.
- **Arguments** are supplied when the function is called.

Understanding this distinction is essential for writing correct function calls.

---

# Key Takeaways

- Parameters allow functions to receive information.
- Parameters are defined inside the parentheses of a function definition.
- Arguments provide values for those parameters when the function is called.
- Functions may have one parameter, multiple parameters, or default parameter values.
- Positional arguments match parameters by order, while keyword arguments match by parameter name.
- Meaningful parameter names and correct argument usage make functions easier to read, understand, and maintain.