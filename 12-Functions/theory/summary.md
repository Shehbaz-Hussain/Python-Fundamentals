# Module Summary

## Introduction

Congratulations! You have completed **Module 12 – Functions**.

This module introduced one of the most important concepts in Python programming. Functions allow you to organize your programs into small, reusable pieces of code. Instead of writing the same statements multiple times, you can write them once inside a function and call them whenever needed.

Functions are a fundamental building block of Python and are widely used in real-world software development, data science, artificial intelligence, automation, and many other fields.

---

# Learning Outcomes

After completing this module, you should be able to:

- Define your own functions using the `def` keyword.
- Call functions correctly.
- Pass information to functions using parameters and arguments.
- Understand positional arguments and keyword arguments.
- Use default arguments when appropriate.
- Return values from functions using the `return` statement.
- Understand the difference between `print()` and `return`.
- Recognize the difference between local and global variables.
- Write simple and meaningful docstrings.
- Apply basic best practices when writing functions.
- Identify and avoid common beginner mistakes.

---

# Topics Covered

The following topics were studied in this module:

| Topic | Description |
|--------|-------------|
| Introduction to Functions | Learned what functions are and why they are useful. |
| Defining Functions | Created functions using the `def` keyword. |
| Calling Functions | Executed functions by calling them. |
| Parameters | Learned how functions receive information. |
| Arguments | Passed values to functions. |
| Positional Arguments | Passed arguments according to their position. |
| Keyword Arguments | Passed arguments using parameter names. |
| Default Arguments | Used default values for parameters. |
| Return Statement | Returned values from functions. |
| Variable Scope | Learned where variables can be accessed. |
| Local Variables | Used variables that exist only inside a function. |
| Global Variables | Used variables defined outside functions. |
| Docstrings | Documented functions using triple-quoted strings. |
| Best Practices | Wrote cleaner and more maintainable functions. |
| Common Mistakes | Learned how to avoid frequent beginner errors. |
| Interview Questions | Reviewed important concepts through questions and answers. |

---

# Important Keywords

Become familiar with the following terms:

- Function
- Function Definition
- Function Call
- Parameter
- Argument
- Positional Argument
- Keyword Argument
- Default Argument
- Return Statement
- Return Value
- Local Variable
- Global Variable
- Variable Scope
- Docstring
- Code Reusability
- Code Organization

---

# Syntax Review

## Defining a Function

```python
def greet():
    print("Hello!")
```

---

## Calling a Function

```python
greet()
```

---

## Function with Parameters

```python
def greet(name):
    print("Hello,", name)
```

---

## Function with Multiple Parameters

```python
def add(number1, number2):
    return number1 + number2
```

---

## Calling a Function with Positional Arguments

```python
add(5, 3)
```

---

## Calling a Function with Keyword Arguments

```python
add(number2=3, number1=5)
```

---

## Function with a Default Argument

```python
def greet(name="Guest"):
    print("Hello,", name)
```

---

## Function with a Return Statement

```python
def square(number):
    return number * number
```

---

# Key Differences

## Function Definition vs Function Call

| Function Definition | Function Call |
|---------------------|---------------|
| Creates a function | Executes a function |
| Uses `def` | Uses the function name followed by `()` |
| Written once | Can be used many times |

---

## Parameter vs Argument

| Parameter | Argument |
|-----------|----------|
| Variable in the function definition | Actual value passed to the function |
| Receives data | Provides data |

---

## `print()` vs `return`

| `print()` | `return` |
|-----------|----------|
| Displays output | Sends a value back to the caller |
| Used for showing information | Used for producing reusable results |
| Does not return the displayed value | Returns a value that can be stored or used later |

---

## Local Variable vs Global Variable

| Local Variable | Global Variable |
|----------------|-----------------|
| Created inside a function | Created outside all functions |
| Accessible only within that function | Accessible throughout the program unless restricted |
| Exists only while the function runs | Exists for the lifetime of the program |

---

# Best Practices Checklist

When writing functions, remember to:

- Choose meaningful function names.
- Follow the `snake_case` naming convention.
- Keep each function focused on one task.
- Use parameters instead of hard-coded values whenever appropriate.
- Return values when the result should be reused.
- Write clear docstrings for important functions.
- Use descriptive variable and parameter names.
- Keep indentation consistent.
- Avoid repeating code.
- Test your functions after writing them.

---

# Common Mistakes to Avoid

Avoid these common errors:

- Defining a function but forgetting to call it.
- Missing parentheses when calling a function.
- Incorrect indentation.
- Forgetting required arguments.
- Passing arguments in the wrong order.
- Confusing `print()` with `return`.
- Forgetting the `return` statement when a result is needed.
- Using local variables outside their function.
- Writing unclear function names.
- Forgetting to update docstrings after changing a function.

---

# Real-World Importance

Functions are used in nearly every Python program, regardless of its size.

They help developers:

- Organize large programs.
- Reuse existing code.
- Reduce duplication.
- Improve readability.
- Simplify debugging.
- Maintain software more easily.

Whether you build a calculator, a game, a website, or an artificial intelligence application, functions will play a central role in structuring your code.

---

# Revision Questions

Test your understanding by answering the following questions:

1. What is a function?
2. Why are functions useful?
3. Which keyword is used to define a function?
4. How do you call a function?
5. What is the difference between a parameter and an argument?
6. What is a positional argument?
7. What is a keyword argument?
8. What is a default argument?
9. What does the `return` statement do?
10. What is the difference between `print()` and `return`?
11. What is a local variable?
12. What is a global variable?
13. What is a docstring?
14. Why are meaningful function names important?
15. How do functions help reduce code duplication?

---

# What's Next?

In the next module, you will continue building your Python programming skills by learning a new core language feature.

The knowledge gained in this module will be used frequently in future topics. Most Python programs rely on functions to organize logic, improve readability, and make code reusable.

---

# Final Takeaways

- Functions are reusable blocks of code designed to perform specific tasks.
- They help reduce repetition and improve program organization.
- Functions are defined with the `def` keyword and executed by calling them.
- Parameters receive information, while arguments provide information.
- Positional, keyword, and default arguments allow flexible function calls.
- The `return` statement sends values back to the caller.
- `print()` displays information, while `return` produces reusable results.
- Local variables exist only within their function, whereas global variables are defined outside functions.
- Docstrings document the purpose of functions and improve code readability.
- Following best practices from the beginning will help you write clean, maintainable, and professional Python programs.