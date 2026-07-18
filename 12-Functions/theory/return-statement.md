# Return Statement

## Introduction

In the previous lessons, you learned how to create functions, pass information to them using parameters and arguments, and use default arguments.

So far, most of our functions have used the `print()` function to display information on the screen. While printing is useful, there are many situations where we want a function to **produce a result that can be used later in the program** instead of displaying it immediately.

This is where the **`return` statement** becomes important.

The `return` statement allows a function to send a value back to the place where the function was called. The returned value can then be stored in a variable, used in calculations, displayed on the screen, or passed to another function.

Understanding the `return` statement is one of the most important steps in learning functions because it allows you to write more reusable and flexible programs.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand the purpose of the `return` statement.
- Explain the difference between `print()` and `return`.
- Return values from a function.
- Store returned values in variables.
- Use returned values in expressions.
- Write reusable functions that produce results.
- Avoid common mistakes when using `return`.

---

# What Is the `return` Statement?

The **`return` statement** is used to send a value from a function back to the place where the function was called.

### Simple Definition

> The `return` statement ends a function and sends a value back to the caller.

---

# Why Do We Need the `return` Statement?

Suppose you create a function that adds two numbers.

### Using `print()`

```python
def add_numbers(first_number, second_number):
    total = first_number + second_number
    print(total)

add_numbers(10, 20)
```

Output:

```text
30
```

The function prints the answer.

However, you cannot easily use this result later in your program.

Now look at the same example using `return`.

```python
def add_numbers(first_number, second_number):
    total = first_number + second_number
    return total

result = add_numbers(10, 20)

print(result)
```

Output:

```text
30
```

Although both programs display the same output, the second program is much more useful because the result is stored in the variable `result`.

---

# Syntax

The basic syntax is:

```python
def function_name():
    # Function body
    return value
```

The value after the `return` keyword is sent back to the caller.

---

# Example 1: Returning a Number

### Explanation

This function adds two numbers and returns their sum.

### Code

```python
# Define the function
def add_numbers(first_number, second_number):
    total = first_number + second_number
    return total

# Call the function
answer = add_numbers(15, 25)

print("Sum:", answer)
```

### Expected Output

```text
Sum: 40
```

### Explanation of the Output

The function calculates the sum and returns the value `40`.

That value is stored in the variable `answer`, which is then printed.

---

# Example 2: Returning the Area of a Rectangle

### Explanation

A function can return calculated values.

### Code

```python
# Define the function
def rectangle_area(length, width):
    area = length * width
    return area

# Call the function
result = rectangle_area(8, 6)

print("Area:", result)
```

### Expected Output

```text
Area: 48
```

### Explanation of the Output

The function calculates the area and returns the result instead of printing it directly.

---

# Example 3: Returning a Greeting Message

Functions can also return strings.

### Code

```python
# Define the function
def create_greeting(name):
    return "Hello, " + name + "!"

# Call the function
message = create_greeting("Ali")

print(message)
```

### Expected Output

```text
Hello, Ali!
```

### Explanation of the Output

The function creates a greeting message and returns it.

The returned value is stored in the variable `message`.

---

# Example 4: Using a Returned Value in a Calculation

A returned value can be used in another calculation.

### Code

```python
# Define the function
def multiply(number1, number2):
    return number1 * number2

result = multiply(5, 4)

final_answer = result + 10

print(final_answer)
```

### Expected Output

```text
30
```

### Explanation of the Output

The function returns `20`.

That value is stored in `result`.

The program then adds `10`, producing the final answer `30`.

---

# Example 5: Returning Student Marks

### Code

```python
# Define the function
def total_marks(math, science):
    return math + science

marks = total_marks(85, 90)

print("Total Marks:", marks)
```

### Expected Output

```text
Total Marks: 175
```

### Explanation of the Output

The function returns the total marks.

The returned value is stored in the variable `marks`.

---

# Difference Between `print()` and `return`

Although they may appear similar, they serve different purposes.

| `print()` | `return` |
|-----------|----------|
| Displays information on the screen | Sends a value back to the caller |
| Does not make the value available for later use | Allows the returned value to be stored or reused |
| Mainly used for output | Mainly used for producing results |

---

# Example: `print()` vs `return`

### Using `print()`

```python
def add_numbers(number1, number2):
    total = number1 + number2
    print(total)

result = add_numbers(10, 20)

print(result)
```

### Output

```text
30
None
```

Why?

The function prints `30`, but it does not return anything.

Therefore, `result` does not receive the value `30`.

---

### Using `return`

```python
def add_numbers(number1, number2):
    total = number1 + number2
    return total

result = add_numbers(10, 20)

print(result)
```

### Output

```text
30
```

Now the value is returned and stored correctly.

---

# A Function Stops After `return`

When Python reaches a `return` statement, the function immediately ends.

Example:

```python
def example():
    print("First")
    return
    print("Second")

example()
```

### Output

```text
First
```

The second `print()` statement never executes because the function ends when it reaches `return`.

---

# Real-World Example

Imagine a calculator.

You enter two numbers.

The calculator performs the calculation and gives you the answer.

The calculator does not automatically decide what you should do with the answer.

Similarly, a function returns a result so the rest of your program can decide how to use it.

---

# Common Beginner Mistakes

## Confusing `print()` with `return`

Incorrect understanding:

> Printing a value is the same as returning it.

This is not correct.

Printing only displays the value.

Returning sends the value back to the caller.

---

## Forgetting to Store the Returned Value

Incorrect

```python
def square(number):
    return number * number

square(5)
```

The function returns a value, but it is not stored or displayed.

Correct

```python
result = square(5)

print(result)
```

---

## Expecting Code After `return` to Execute

Incorrect

```python
def message():
    return "Hello"
    print("Python")
```

The `print()` statement never executes.

---

# Best Practices

- Use `return` when a function produces a result.
- Use meaningful variable names to store returned values.
- Keep each function focused on one task.
- Return values instead of printing whenever the result will be reused.
- Write clear and readable functions.

---

# Tips

> **Tip**
>
> If another part of your program needs the result produced by a function, use `return` instead of `print()`.

---

> **Remember**
>
> The `return` statement immediately ends the execution of a function.

---

# Key Points

- The `return` statement sends a value back to the caller.
- A returned value can be stored in a variable.
- Returned values can be used in calculations.
- `print()` displays information, while `return` produces a reusable result.
- A function ends as soon as it reaches a `return` statement.

---

# Summary

In this lesson, you learned about one of the most important features of Python functions—the `return` statement.

You learned:

- What the `return` statement is.
- Why it is useful.
- How to return values from a function.
- How to store and use returned values.
- The difference between `print()` and `return`.
- Common mistakes beginners should avoid.

In the next lesson, you will learn about **variable scope**, which explains where variables can be accessed inside a Python program.
```