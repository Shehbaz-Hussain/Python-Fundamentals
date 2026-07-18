# Interview Questions on Python Functions

## Introduction

Functions are one of the most important topics in Python. They are frequently discussed in technical interviews because they demonstrate a programmer's understanding of code organization, reusability, and problem-solving.

This chapter contains beginner-friendly interview questions covering only the concepts learned in **Module 12 – Functions**.

The questions progress from basic concepts to slightly more practical scenarios, making them suitable for revision before quizzes, examinations, and entry-level technical interviews.

---

# Learning Objectives

After completing this chapter, you should be able to:

- Explain what a function is.
- Describe why functions are useful.
- Differentiate between related function concepts.
- Read and understand simple function-based code.
- Predict the output of function examples.
- Answer common beginner interview questions confidently.

---

# Section 1 — Basic Conceptual Questions

## Question 1

### What is a function in Python?

**Answer**

A function is a reusable block of code that performs a specific task. Functions help organize programs, reduce code duplication, and improve readability.

---

## Question 2

### Why do we use functions?

**Answer**

Functions are used to:

- Reuse code
- Reduce repetition
- Improve readability
- Make programs easier to maintain
- Divide large programs into smaller tasks

---

## Question 3

### How do you define a function?

**Answer**

A function is defined using the `def` keyword.

Example:

```python
def greet():
    print("Hello")
```

---

## Question 4

### How do you call a function?

**Answer**

A function is called by writing its name followed by parentheses.

Example:

```python
greet()
```

---

## Question 5

### What happens if a function is defined but never called?

**Answer**

The function is stored in memory, but its code is never executed.

---

# Section 2 — Parameters and Arguments

## Question 6

### What is a parameter?

**Answer**

A parameter is a variable listed in the function definition that receives data when the function is called.

Example:

```python
def greet(name):
    print("Hello,", name)
```

Here, `name` is a parameter.

---

## Question 7

### What is an argument?

**Answer**

An argument is the actual value passed to a function during a function call.

Example:

```python
greet("Ali")
```

`"Ali"` is an argument.

---

## Question 8

### What is the difference between a parameter and an argument?

**Answer**

| Parameter | Argument |
|-----------|----------|
| Declared in the function definition | Supplied when calling the function |
| Receives data | Provides data |
| Variable | Actual value |

---

## Question 9

### What are positional arguments?

**Answer**

Positional arguments are matched with parameters according to their position.

Example:

```python
def student(name, age):
    print(name, age)

student("Ali", 20)
```

---

## Question 10

### What are keyword arguments?

**Answer**

Keyword arguments specify the parameter name when calling a function.

Example:

```python
student(age=20, name="Ali")
```

---

## Question 11

### What are default arguments?

**Answer**

Default arguments are parameter values that Python uses automatically when no value is provided.

Example:

```python
def greet(name="Guest"):
    print("Hello,", name)
```

---

# Section 3 — Return Statement

## Question 12

### What does the `return` statement do?

**Answer**

The `return` statement sends a value back to the place where the function was called.

Example:

```python
def add(a, b):
    return a + b
```

---

## Question 13

### What is the difference between `print()` and `return`?

**Answer**

| `print()` | `return` |
|-----------|-----------|
| Displays output on the screen | Sends a value back to the caller |
| Does not return the printed value | Returns a value that can be stored or used |
| Mainly used for displaying information | Mainly used for producing results |

---

## Question 14

### Can a function exist without a `return` statement?

**Answer**

Yes.

A function can simply perform an action, such as printing a message.

Example:

```python
def welcome():
    print("Welcome!")
```

---

# Section 4 — Variable Scope

## Question 15

### What is a local variable?

**Answer**

A local variable is created inside a function and can only be used within that function.

---

## Question 16

### What is a global variable?

**Answer**

A global variable is created outside all functions and can be accessed throughout the program unless restricted.

---

## Question 17

### Which variable has a smaller scope?

**Answer**

A local variable has a smaller scope because it exists only inside its function.

---

# Section 5 — Docstrings

## Question 18

### What is a docstring?

**Answer**

A docstring is a documentation string written as the first statement inside a function. It explains the purpose of the function.

Example:

```python
def square(number):
    """Return the square of a number."""
    return number * number
```

---

## Question 19

### Why are docstrings important?

**Answer**

Docstrings:

- Explain what a function does
- Improve readability
- Help other programmers
- Make programs easier to maintain
- Follow professional Python standards

---

# Section 6 — Best Practices

## Question 20

### How should function names be written in Python?

**Answer**

Function names should:

- Be descriptive
- Use lowercase letters
- Separate words with underscores (`snake_case`)
- Clearly describe the function's purpose

Example:

```python
calculate_area()
```

---

## Question 21

### Why should a function perform only one task?

**Answer**

A function that performs one task is:

- Easier to understand
- Easier to test
- Easier to reuse
- Easier to maintain

---

## Question 22

### Why should hard-coded values be avoided?

**Answer**

Using parameters instead of fixed values makes functions more flexible and reusable.

---

# Section 7 — Code Reading Questions

## Question 23

What is the output?

```python
def hello():
    print("Hello")

hello()
```

### Answer

```
Hello
```

---

## Question 24

What is the output?

```python
def add(a, b):
    return a + b

print(add(4, 6))
```

### Answer

```
10
```

---

## Question 25

What is the output?

```python
def greet(name="Guest"):
    print("Hello,", name)

greet()
```

### Answer

```
Hello, Guest
```

---

## Question 26

What is the output?

```python
def greet(name):
    print("Hello,", name)

greet("Sara")
```

### Answer

```
Hello, Sara
```

---

## Question 27

What is the output?

```python
def square(number):
    return number * number

result = square(5)

print(result)
```

### Answer

```
25
```

---

## Question 28

What is the output?

```python
def display():
    print("Python")

display
```

### Answer

There is **no output** because the function is not called.

---

## Question 29

What is the output?

```python
def message():
    print("Learning Functions")

message()
message()
```

### Answer

```
Learning Functions
Learning Functions
```

---

## Question 30

What is the output?

```python
def multiply(a, b):
    return a * b

print(multiply(3, 4))
```

### Answer

```
12
```

---

# Quick Revision Questions

Try answering these without looking at the answers.

1. What keyword is used to define a function?
2. Why are functions useful?
3. What is a parameter?
4. What is an argument?
5. What is a default argument?
6. What does the `return` statement do?
7. What is the difference between `print()` and `return`?
8. What is a local variable?
9. What is a global variable?
10. What is a docstring?
11. Why should functions have meaningful names?
12. Why should functions avoid repeated code?

---

# Tips for Interviews

- Define technical terms using simple, precise language.
- Use small code examples to support your explanations when appropriate.
- Distinguish clearly between similar concepts such as **parameter vs argument** and **print() vs return**.
- When asked about best practices, mention descriptive names, docstrings, code reuse, and keeping functions focused on a single task.
- If asked to predict the output of a function, read the code carefully before answering.

---

# Key Takeaways

- Interview questions on functions usually focus on understanding rather than memorization.
- You should be able to explain what functions are, why they are useful, and how they improve code organization.
- Understand the differences between parameters and arguments, as well as between `print()` and `return`.
- Be comfortable with positional arguments, keyword arguments, default arguments, local variables, global variables, and docstrings.
- Practice reading simple function-based programs and predicting their output.
- Following Python best practices demonstrates professionalism and strong programming fundamentals.