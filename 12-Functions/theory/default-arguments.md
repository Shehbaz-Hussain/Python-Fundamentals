# Default Arguments

## Introduction

In the previous lesson, you learned how to pass values to a function using **positional arguments** and **keyword arguments**.

However, there are situations where a function should work even if the caller does not provide every argument.

For example:

- A greeting function could greet a user by name, but if no name is provided, it could greet **"Guest"**.
- A shopping application could use a default tax rate.
- A school program could assume a passing mark if one is not specified.

Python allows us to solve these situations using **default arguments**.

A **default argument** gives a parameter a predefined value. If the caller does not provide a value for that parameter, Python automatically uses the default value.

Default arguments make functions more flexible while reducing the amount of code that users need to write.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand what default arguments are.
- Explain why default arguments are useful.
- Define functions with default arguments.
- Override default values by providing your own arguments.
- Identify common mistakes when using default arguments.
- Apply default arguments in practical examples.

---

# What Are Default Arguments?

A **default argument** is a parameter that already has a value assigned to it in the function definition.

If the function is called without providing a value for that parameter, Python automatically uses the default value.

### Simple Definition

> A **default argument** is a parameter that has a predefined value.

---

# Why Do We Need Default Arguments?

Suppose you want to create a greeting function.

Most of the time, users will provide their names.

Sometimes, they may not.

Instead of creating two separate functions, you can use a default argument.

Without a default argument:

```python
def greet(name):
    print("Hello,", name)
```

The caller **must** provide a name.

With a default argument:

```python
def greet(name="Guest"):
    print("Hello,", name)
```

Now the function works whether a name is provided or not.

---

# Syntax

The basic syntax for a default argument is:

```python
def function_name(parameter=default_value):
    # Function body
```

Example:

```python
def greet(name="Guest"):
    print("Hello,", name)
```

Here:

- `name` is the parameter.
- `"Guest"` is the default value.

---

# Example 1: Using the Default Value

### Explanation

The function has one parameter with a default value.

Since no argument is provided, Python uses the default value.

### Code

```python
# Define the function
def greet(name="Guest"):
    print("Hello,", name)

# Call the function without an argument
greet()
```

### Expected Output

```text
Hello, Guest
```

### Explanation of the Output

The function is called without passing a value.

Python automatically assigns `"Guest"` to the parameter `name`.

---

# Example 2: Overriding the Default Value

### Explanation

You can replace the default value by passing an argument.

### Code

```python
# Define the function
def greet(name="Guest"):
    print("Hello,", name)

# Call the function with an argument
greet("Ali")
```

### Expected Output

```text
Hello, Ali
```

### Explanation of the Output

Although the default value is `"Guest"`, Python uses `"Ali"` because it was provided during the function call.

---

# Example 3: Greeting Multiple Users

### Code

```python
# Define the function
def welcome(name="Guest"):
    print("Welcome,", name)

# Function calls
welcome()
welcome("Sara")
welcome("Ahmed")
```

### Expected Output

```text
Welcome, Guest
Welcome, Sara
Welcome, Ahmed
```

### Explanation of the Output

- The first call uses the default value.
- The second call uses `"Sara"`.
- The third call uses `"Ahmed"`.

The same function behaves differently depending on the arguments provided.

---

# Example 4: Employee Salary

### Explanation

Suppose most employees receive a standard bonus of 5000.

Instead of passing the bonus every time, we can use a default argument.

### Code

```python
# Define the function
def calculate_salary(basic_salary, bonus=5000):
    total_salary = basic_salary + bonus
    print("Total Salary:", total_salary)

# Function calls
calculate_salary(50000)
calculate_salary(50000, 8000)
```

### Expected Output

```text
Total Salary: 55000
Total Salary: 58000
```

### Explanation of the Output

For the first call:

- `basic_salary = 50000`
- `bonus = 5000` (default)

For the second call:

- `basic_salary = 50000`
- `bonus = 8000` (provided by the caller)

---

# Example 5: Rectangle Area

### Code

```python
# Define the function
def rectangle_area(length, width=5):
    area = length * width
    print("Area:", area)

# Function calls
rectangle_area(8)
rectangle_area(8, 10)
```

### Expected Output

```text
Area: 40
Area: 80
```

### Explanation of the Output

In the first function call, Python uses the default width.

In the second function call, the provided width replaces the default value.

---

# Rules for Default Arguments

When using default arguments, remember these rules.

## Rule 1: Default Values Are Optional

The caller does not have to provide a value for a parameter that has a default value.

Example:

```python
def display_city(city="Gilgit"):
    print(city)

display_city()
```

---

## Rule 2: You Can Override the Default Value

Providing an argument replaces the default value.

Example:

```python
display_city("Lahore")
```

---

## Rule 3: Default Parameters Should Come After Required Parameters

Correct:

```python
def student(name, age=18):
    print(name)
    print(age)
```

Incorrect:

```python
def student(age=18, name):
    print(name)
```

Required parameters should appear before parameters with default values.

---

# Real-World Examples

Default arguments are useful in many situations.

| Function | Possible Default Value |
|----------|------------------------|
| Greeting | Guest |
| Employee Bonus | 5000 |
| Passing Marks | 40 |
| Sales Tax | 18 |
| Country | Pakistan |
| Currency | PKR |

Using default values makes functions easier to use.

---

# Common Beginner Mistakes

## Forgetting That the Default Can Be Replaced

Some beginners think the default value is permanent.

This is incorrect.

Example:

```python
def greet(name="Guest"):
    print(name)

greet("Ali")
```

Output:

```text
Ali
```

The provided argument replaces the default value.

---

## Placing Default Parameters Before Required Parameters

Incorrect:

```python
def student(age=18, name):
    print(name)
```

Correct:

```python
def student(name, age=18):
    print(name)
```

---

## Providing Too Many Arguments

Incorrect:

```python
def greet(name="Guest"):
    print(name)

greet("Ali", "Sara")
```

The function accepts only one parameter.

---

# Best Practices

- Use default arguments only when a sensible default value exists.
- Choose meaningful default values.
- Keep default values simple and easy to understand.
- Place required parameters before default parameters.
- Avoid unnecessary default values.

---

# Tips

> **Tip**
>
> Default arguments make functions easier to use because callers only need to provide values when they want to change the default behavior.

---

> **Remember**
>
> If an argument is provided during the function call, it always takes priority over the default value.

---

# Key Points

- A default argument has a predefined value.
- Default values are assigned in the function definition.
- The caller may choose to use the default value or replace it.
- Default arguments make functions more flexible.
- Required parameters should come before default parameters.

---

# Summary

In this lesson, you learned how to use default arguments in Python.

You learned:

- What default arguments are.
- Why they are useful.
- How to define parameters with default values.
- How Python uses default values.
- How to replace default values by providing arguments.
- Best practices and common mistakes.

In the next lesson, you will learn about the **return statement**, which allows a function to send a result back to the part of the program that called it.