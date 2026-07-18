# Parameters

## Introduction

In the previous lessons, you learned how to define and call functions. The functions you created performed the same task every time they were called because they did not receive any information from outside the function.

However, many real-world problems require functions to work with different values.

For example:

- A greeting function should greet different people.
- A calculator should work with different numbers.
- An area calculator should work with different dimensions.
- A student's report should display information for different students.

Instead of creating a separate function for every possible value, Python allows us to pass information into a function using **parameters**.

Parameters make functions more flexible, reusable, and practical.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand what parameters are.
- Explain why parameters are important.
- Define functions with one or more parameters.
- Use parameter values inside a function.
- Recognize the difference between parameters and arguments.
- Write reusable functions using parameters.

---

# What Are Parameters?

A **parameter** is a variable that is declared inside the parentheses of a function definition.

It acts as a placeholder for the value that will be provided when the function is called.

### Simple Definition

> A **parameter** is a variable that allows a function to receive information.

---

# Why Do We Need Parameters?

Suppose you want a function that greets different people.

Without parameters, you would need to create a separate function for every person.

### Example

```python
def greet_ali():
    print("Hello, Ali!")

def greet_sara():
    print("Hello, Sara!")

def greet_ahmed():
    print("Hello, Ahmed!")
```

This approach is inefficient because the only difference is the person's name.

Instead, you can create one reusable function using a parameter.

---

# Function Syntax with Parameters

The basic syntax is:

```python
def function_name(parameter_name):
    # Function body
```

Example:

```python
def greet(name):
    print("Hello,", name)
```

Here:

- `greet` is the function name.
- `name` is the parameter.
- The function uses the value stored in `name`.

---

# Understanding Parameters

Consider the following function:

```python
def greet(student_name):
    print("Welcome,", student_name)
```

In this example:

- `student_name` is the parameter.
- It does not have a fixed value.
- It receives a value whenever the function is called.

Think of a parameter as an empty container waiting to store information.

---

# Example 1: Function with One Parameter

This function greets a student.

### Code

```python
# Define the function
def greet(name):
    print("Hello,", name)

# Call the function
greet("Ali")
```

### Expected Output

```text
Hello, Ali
```

### Explanation of the Output

When the function is called, the value `"Ali"` is assigned to the parameter `name`.

The `print()` statement then displays the greeting using that value.

---

# Example 2: Calling the Same Function with Different Values

One function can work with many different values.

### Code

```python
# Define the function
def greet(name):
    print("Hello,", name)

# Call the function multiple times
greet("Ali")
greet("Sara")
greet("Ahmed")
```

### Expected Output

```text
Hello, Ali
Hello, Sara
Hello, Ahmed
```

### Explanation of the Output

The function is defined only once.

Each function call provides a different value for the parameter `name`.

This makes the function reusable.

---

# Example 3: Function with Two Parameters

A function can have more than one parameter.

### Code

```python
# Define the function
def student_information(name, age):
    print("Name:", name)
    print("Age:", age)

# Call the function
student_information("Ayesha", 20)
```

### Expected Output

```text
Name: Ayesha
Age: 20
```

### Explanation of the Output

The function has two parameters:

- `name`
- `age`

Each parameter receives a corresponding value when the function is called.

---

# Example 4: Area of a Rectangle

Parameters are useful for calculations.

### Code

```python
# Define the function
def rectangle_area(length, width):
    area = length * width
    print("Area:", area)

# Call the function
rectangle_area(8, 5)
```

### Expected Output

```text
Area: 40
```

### Explanation of the Output

The function receives two numbers.

It multiplies them and prints the calculated area.

---

# Example 5: Shopping Bill

Parameters can also represent prices and quantities.

### Code

```python
# Define the function
def calculate_total(price, quantity):
    total = price * quantity
    print("Total Bill:", total)

# Call the function
calculate_total(250, 4)
```

### Expected Output

```text
Total Bill: 1000
```

### Explanation of the Output

The function receives:

- Price = 250
- Quantity = 4

It calculates and displays the total bill.

---

# Multiple Parameters

A function can receive multiple pieces of information.

General syntax:

```python
def function_name(parameter1, parameter2, parameter3):
    # Function body
```

Example:

```python
def employee_information(name, department, salary):
    print(name)
    print(department)
    print(salary)
```

Each parameter stores one value.

---

# Choosing Good Parameter Names

Choose names that clearly describe the information they store.

Good examples:

```python
student_name
employee_salary
length
width
temperature
marks
quantity
price
```

Avoid unclear names such as:

```python
a
b
x
y
data
value
```

Meaningful names improve readability.

---

# Parameters vs Variables

Parameters are a special type of variable.

| Variable | Parameter |
|----------|-----------|
| Created inside the program | Created in a function definition |
| Stores information | Receives information from a function call |
| Can be used anywhere in its scope | Used inside the function |

Example:

```python
def greet(name):
    print(name)
```

Here, `name` is a parameter because it is declared in the function definition.

---

# Common Beginner Mistakes

## Forgetting the Parameter

Incorrect

```python
def greet():
    print("Hello,", name)
```

The variable `name` does not exist.

Correct

```python
def greet(name):
    print("Hello,", name)
```

---

## Using Different Parameter Names

Incorrect

```python
def greet(student_name):
    print(name)
```

Correct

```python
def greet(student_name):
    print(student_name)
```

Always use the correct parameter name inside the function.

---

## Missing Commas Between Parameters

Incorrect

```python
def student(name age):
    print(name)
```

Correct

```python
def student(name, age):
    print(name)
```

Separate multiple parameters with commas.

---

# Best Practices

- Give parameters meaningful names.
- Keep parameter names short but descriptive.
- Only include the parameters the function actually needs.
- Avoid unnecessary parameters.
- Make each function perform one specific task.

---

# Tips

> **Tip**
>
> Think of parameters as empty containers that receive values when a function is called.

---

> **Remember**
>
> Parameters are written when defining a function, not when calling it.

---

# Key Points

- Parameters allow functions to receive information.
- Parameters are declared inside the parentheses of a function definition.
- A function can have one, two, or many parameters.
- Parameters make functions flexible and reusable.
- Meaningful parameter names improve code readability.

---

# Summary

In this lesson, you learned that parameters allow functions to receive information from the outside.

You learned:

- What parameters are.
- Why parameters are useful.
- How to define functions with parameters.
- How to use one or more parameters.
- How parameters make functions reusable.
- Common mistakes to avoid.

In the next lesson, you will learn about **arguments**, which are the actual values passed to parameters when a function is called.