# Function Call Syntax

## Introduction

Defining a function creates it, but **does not execute it**. To make a function perform its task, you must **call** it.

A **function call** tells Python to execute the statements inside a previously defined function.

Understanding how to call functions correctly is essential because every function you define must eventually be called if you want it to perform its intended task.

This chapter explains the syntax of function calls using simple, beginner-friendly examples.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what a function call is.
- Learn the syntax for calling functions.
- Call functions with and without arguments.
- Store returned values from function calls.
- Identify and avoid common function call mistakes.

---

# What Is a Function Call?

A **function call** is the process of executing a function.

When Python reaches a function call, it:

1. Finds the function definition.
2. Executes the statements inside the function.
3. Returns to the next line after the function call.

---

# Basic Function Call Syntax

```python
function_name()
```

This syntax is used to call a function that does not require any arguments.

---

# Defining and Calling a Function

```python
def greet():
    print("Hello!")
```

The function has been defined, but nothing happens yet.

To execute it:

```python
greet()
```

### Expected Output

```
Hello!
```

### Explanation

The statement `greet()` tells Python to execute the code inside the `greet` function.

---

# Calling a Function Multiple Times

One of the main advantages of functions is that they can be called repeatedly.

```python
def welcome():
    print("Welcome!")
```

Function calls:

```python
welcome()
welcome()
welcome()
```

### Expected Output

```
Welcome!
Welcome!
Welcome!
```

### Explanation

The same function definition is reused three times without rewriting the code.

---

# Calling a Function with One Argument

If a function has one parameter, provide one argument.

Function definition:

```python
def greet(name):
    print("Hello,", name)
```

Function call:

```python
greet("Ali")
```

### Expected Output

```
Hello, Ali
```

---

# Calling a Function with Multiple Arguments

```python
def add(number1, number2):
    print(number1 + number2)
```

Function call:

```python
add(8, 5)
```

### Expected Output

```
13
```

---

# Calling a Function Using Keyword Arguments

Arguments can also be supplied using parameter names.

Function definition:

```python
def student(name, age):
    print(name)
    print(age)
```

Function call:

```python
student(age=20, name="Sara")
```

### Expected Output

```
Sara
20
```

### Explanation

Keyword arguments make it clear which value belongs to which parameter.

---

# Calling a Function with Default Arguments

```python
def greet(name="Guest"):
    print("Hello,", name)
```

Function call:

```python
greet()
```

### Expected Output

```
Hello, Guest
```

Calling with a custom value:

```python
greet("Ahmed")
```

### Expected Output

```
Hello, Ahmed
```

---

# Calling a Function That Returns a Value

```python
def square(number):
    return number * number
```

Function call:

```python
result = square(6)

print(result)
```

### Expected Output

```
36
```

### Explanation

The returned value is stored in the variable `result`.

---

# General Function Call Syntax

## Function Without Parameters

```python
function_name()
```

---

## Function with One Argument

```python
function_name(argument)
```

---

## Function with Multiple Arguments

```python
function_name(argument1, argument2)
```

---

## Function with Keyword Arguments

```python
function_name(parameter=value)
```

---

## Function Returning a Value

```python
variable = function_name(arguments)
```

---

# Order of Execution

Consider the following program:

```python
def message():
    print("Learning Functions")

print("Program Started")

message()

print("Program Finished")
```

### Expected Output

```
Program Started
Learning Functions
Program Finished
```

### Explanation

Python executes the program from top to bottom.

When it reaches `message()`, it temporarily moves into the function, executes its statements, and then returns to continue with the next statement.

---

# Common Mistakes

## Forgetting Parentheses

Incorrect:

```python
greet
```

### Expected Output

```
No output
```

The function is referenced but not executed.

Correct:

```python
greet()
```

---

## Calling a Function Before It Is Defined

Incorrect:

```python
greet()

def greet():
    print("Hello")
```

This produces a `NameError` because Python has not yet encountered the function definition.

Correct:

```python
def greet():
    print("Hello")

greet()
```

---

## Forgetting Required Arguments

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

# Best Practices

- Define the function before calling it.
- Always include parentheses when calling a function.
- Pass the correct number of arguments.
- Use meaningful argument values.
- Use keyword arguments when they improve readability.
- Store returned values when they will be used later.

---

# Summary Table

| Function Type | Example Function Call |
|--------------|-----------------------|
| No parameters | `greet()` |
| One parameter | `greet("Ali")` |
| Multiple parameters | `add(5, 3)` |
| Keyword arguments | `student(name="Ali", age=20)` |
| Default argument | `greet()` |
| Returning a value | `result = square(4)` |

---

# Tips

> **Tip:** Defining a function creates it; calling a function runs it.

> **Tip:** Always check that the number of arguments matches the number of required parameters.

> **Tip:** If a function returns a value, store it in a variable when you need to use it later.

---

# Warning

Do not confuse a **function definition** with a **function call**.

- A function definition **creates** the function.
- A function call **executes** the function.

Writing only the function name without parentheses does **not** call the function.

---

# Key Takeaways

- A function call executes a previously defined function.
- Functions without parameters are called using empty parentheses.
- Functions with parameters require appropriate arguments.
- Keyword arguments allow values to be passed by parameter name.
- Functions that return values can have their results stored in variables.
- Correct function calls are essential for writing reusable and well-structured Python programs.