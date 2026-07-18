# Argument Syntax

## Introduction

Functions become useful when they can work with different values. These values are provided through **arguments**.

An **argument** is the actual value passed to a function when it is called. The function receives these values through its parameters and uses them to perform its task.

This chapter explains the syntax of arguments and demonstrates how they are passed to functions.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what an argument is.
- Learn the syntax for passing arguments.
- Distinguish between parameters and arguments.
- Pass one or more arguments to functions.
- Use positional and keyword arguments correctly.
- Avoid common argument-related mistakes.

---

# What Is an Argument?

An **argument** is the actual value supplied to a function during a function call.

Arguments provide the information that a function needs to perform its work.

Example:

```python
def greet(name):
    print("Hello,", name)

greet("Ali")
```

Here:

- `name` is the **parameter**.
- `"Ali"` is the **argument**.

---

# Basic Argument Syntax

The general syntax is:

```python
function_name(argument)
```

Example:

```python
greet("Sara")
```

The value `"Sara"` is passed as an argument.

---

# Relationship Between Parameters and Arguments

Consider the following function:

```python
def add(number1, number2):
    print(number1 + number2)
```

Calling the function:

```python
add(5, 8)
```

### Explanation

| Parameter | Argument |
|-----------|----------|
| `number1` | `5` |
| `number2` | `8` |

The arguments are assigned to the parameters in the same order.

---

# Passing One Argument

```python
def display_city(city):
    print("City:", city)

display_city("Gilgit")
```

### Expected Output

```
City: Gilgit
```

### Explanation

The argument `"Gilgit"` is assigned to the parameter `city`.

---

# Passing Multiple Arguments

```python
def multiply(number1, number2):
    print(number1 * number2)

multiply(4, 6)
```

### Expected Output

```
24
```

### Explanation

The function receives two arguments and multiplies them.

---

# Passing String Arguments

```python
def welcome(name):
    print("Welcome,", name)

welcome("Ayesha")
```

### Expected Output

```
Welcome, Ayesha
```

---

# Passing Number Arguments

```python
def square(number):
    print(number * number)

square(9)
```

### Expected Output

```
81
```

---

# Passing Variable Values as Arguments

Arguments do not have to be written directly.

Variables can also be passed.

```python
def greet(name):
    print("Hello,", name)


student_name = "Ahmed"

greet(student_name)
```

### Expected Output

```
Hello, Ahmed
```

### Explanation

The value stored in `student_name` is passed as the argument.

---

# Passing Keyword Arguments

Arguments can be supplied using parameter names.

```python
def student(name, age):
    print(name)
    print(age)

student(age=20, name="Ali")
```

### Expected Output

```
Ali
20
```

---

# Using Default Arguments

```python
def greet(name="Guest"):
    print("Hello,", name)

greet()
```

### Expected Output

```
Hello, Guest
```

Providing an argument:

```python
greet("Sara")
```

### Expected Output

```
Hello, Sara
```

---

# General Argument Syntax

## One Argument

```python
function_name(argument)
```

---

## Two Arguments

```python
function_name(argument1, argument2)
```

---

## Three Arguments

```python
function_name(argument1, argument2, argument3)
```

---

## Keyword Arguments

```python
function_name(parameter=value)
```

---

# Complete Example

```python
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    print("Area:", area)


calculate_area(8, 5)
```

### Expected Output

```
Area: 40
```

### Explanation

The arguments `8` and `5` are assigned to the parameters `length` and `width`.

---

# Common Mistakes

## Forgetting an Argument

Incorrect:

```python
def greet(name):
    print(name)

greet()
```

Python reports that a required argument is missing.

Correct:

```python
greet("Ali")
```

---

## Passing Too Many Arguments

Incorrect:

```python
def greet(name):
    print(name)

greet("Ali", "Sara")
```

Python reports that too many arguments were provided.

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

## Confusing Parameters with Arguments

Incorrect understanding:

- Parameter = value
- Argument = variable

Correct understanding:

- **Parameter** → Variable in the function definition.
- **Argument** → Actual value supplied during the function call.

---

# Best Practices

- Pass the correct number of arguments.
- Match the order of positional arguments with the parameter list.
- Use keyword arguments when they improve readability.
- Choose meaningful values while testing functions.
- Review the function definition before calling it.

---

# Summary Table

| Syntax | Description |
|--------|-------------|
| `greet("Ali")` | One argument |
| `add(5, 3)` | Two positional arguments |
| `student(name="Ali", age=20)` | Keyword arguments |
| `greet()` | Uses the default argument value |

---

# Tips

> **Tip:** Read the function definition first to determine how many arguments are required.

> **Tip:** Keyword arguments can make function calls easier to understand, especially when there are several parameters.

> **Tip:** Practice identifying parameters and arguments in every function you write.

---

# Warning

Arguments must match the function definition.

Providing too few arguments, too many arguments, or arguments in the wrong order may cause errors or produce incorrect results.

---

# Key Takeaways

- Arguments are the actual values passed to a function when it is called.
- Parameters receive those values inside the function.
- Functions can receive one or more arguments.
- Arguments may be numbers, strings, or values stored in variables.
- Keyword arguments identify parameters by name and improve readability.
- Correct argument usage ensures that functions behave as intended.