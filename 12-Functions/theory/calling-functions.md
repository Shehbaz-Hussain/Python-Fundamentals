# Calling Functions

## Introduction

In the previous lesson, you learned how to **define** a function using the `def` keyword. However, simply defining a function does not make it run.

To execute the code inside a function, you must **call** the function.

Calling a function tells Python to execute the statements stored inside that function. Every time a function is called, Python runs the code inside the function from top to bottom.

Understanding how to call functions is essential because a function only performs its task when it is invoked.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand what it means to call a function.
- Call a function correctly.
- Explain the difference between defining and calling a function.
- Call a function multiple times.
- Understand the execution flow when a function is called.
- Avoid common mistakes when calling functions.

---

# What Is a Function Call?

A **function call** is the process of telling Python to execute a previously defined function.

A function is called by writing its name followed by a pair of parentheses.

### Syntax

```python
function_name()
```

The parentheses are required, even if the function does not need any information.

---

# Defining vs Calling a Function

These two concepts are different but closely related.

| Defining a Function | Calling a Function |
|----------------------|--------------------|
| Creates the function | Executes the function |
| Uses the `def` keyword | Uses the function name with parentheses |
| Stores the instructions | Runs the stored instructions |
| Usually written once | Can be written many times |

---

# Example 1: Calling a Function

First, define the function.

Then, call it.

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

When Python reaches the function call, it executes that statement and displays the message.

---

# What Happens During a Function Call?

Consider the following example.

```python
def greeting():
    print("Good Morning!")

greeting()
```

Python performs these steps:

1. Reads the function definition.
2. Stores the function in memory.
3. Continues reading the program.
4. Finds the function call.
5. Executes the statements inside the function.
6. Returns to the next line after the function call.

This process happens every time the function is called.

---

# Example 2: Calling a Function Multiple Times

A function can be called as many times as needed.

### Code

```python
# Define the function
def welcome():
    print("Welcome!")

# Call the function multiple times
welcome()
welcome()
welcome()
```

### Expected Output

```text
Welcome!
Welcome!
Welcome!
```

### Explanation of the Output

The function is defined only once.

Each function call executes the same code again.

This is one of the biggest advantages of using functions.

---

# Example 3: Calling Different Functions

A program can contain multiple functions.

### Code

```python
# Define the first function
def morning_message():
    print("Good Morning!")

# Define the second function
def evening_message():
    print("Good Evening!")

# Call both functions
morning_message()
evening_message()
```

### Expected Output

```text
Good Morning!
Good Evening!
```

### Explanation of the Output

Python executes the first function call.

After it finishes, Python executes the second function call.

---

# Example 4: Mixing Normal Statements and Function Calls

Function calls can appear anywhere in your program.

### Code

```python
print("Program Started")

def welcome():
    print("Welcome to Python!")

welcome()

print("Program Finished")
```

### Expected Output

```text
Program Started
Welcome to Python!
Program Finished
```

### Explanation of the Output

Python executes statements in order.

When it reaches the function call, it temporarily enters the function, executes its statements, and then continues with the remaining program.

---

# Calling a Function Before It Is Defined

Python reads programs from top to bottom.

If you call a function before Python has seen its definition, an error occurs.

### Incorrect Code

```python
welcome()

def welcome():
    print("Welcome!")
```

Python cannot execute the function because it has not yet been defined.

---

### Correct Code

```python
def welcome():
    print("Welcome!")

welcome()
```

Always define a function before calling it.

---

# Calling a Function Inside a Loop

Since you have already learned loops, you can use them with functions.

### Code

```python
def greeting():
    print("Hello!")

for number in range(3):
    greeting()
```

### Expected Output

```text
Hello!
Hello!
Hello!
```

### Explanation of the Output

The loop runs three times.

During each iteration, the function is called once.

---

# Calling the Same Function from Different Places

A function can be reused throughout a program.

### Code

```python
def separator():
    print("--------------------")

print("Student Report")
separator()

print("Marks")
separator()

print("End of Report")
```

### Expected Output

```text
Student Report
--------------------
Marks
--------------------
End of Report
```

### Explanation of the Output

Instead of writing the separator multiple times, the function is reused whenever needed.

This makes the program shorter and easier to maintain.

---

# Why Are Function Calls Useful?

Calling functions provides several advantages.

- Reuse existing code.
- Reduce repetition.
- Improve readability.
- Make programs easier to update.
- Keep related statements together.

---

# Common Beginner Mistakes

## Forgetting the Parentheses

Incorrect

```python
welcome
```

Correct

```python
welcome()
```

Without parentheses, the function is not called.

---

## Calling Before Defining

Incorrect

```python
hello()

def hello():
    print("Hello")
```

Correct

```python
def hello():
    print("Hello")

hello()
```

---

## Misspelling the Function Name

Incorrect

```python
def greeting():
    print("Hello")

greting()
```

Correct

```python
def greeting():
    print("Hello")

greeting()
```

The function name must match exactly.

---

## Assuming a Function Runs Automatically

Incorrect assumption:

```python
def message():
    print("Python")
```

Nothing is displayed because the function has not been called.

Correct:

```python
def message():
    print("Python")

message()
```

---

# Best Practices

- Define functions before calling them.
- Use meaningful function names.
- Keep each function focused on one task.
- Call functions whenever the task is needed.
- Avoid writing the same code repeatedly.

---

# Key Points

- A function call executes a function.
- Functions are called using their name followed by parentheses.
- A function can be called many times.
- Python executes function calls in the order they appear.
- The function must be defined before it is called.
- Function calls help make programs reusable and organized.

---

# Summary

In this lesson, you learned how to call functions in Python.

You learned:

- What a function call is.
- How to call a function.
- The difference between defining and calling a function.
- How Python executes function calls.
- How to call a function multiple times.
- Common mistakes beginners should avoid.

In the next lesson, you will learn about **parameters**, which allow functions to receive information when they are called.
```