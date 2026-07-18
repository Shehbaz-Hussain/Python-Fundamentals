# Arguments

## Introduction

In the previous lesson, you learned about **parameters**, which are variables defined in a function to receive information.

However, parameters alone are not enough. When we call a function, we need to provide actual values for those parameters. These actual values are called **arguments**.

Understanding arguments is essential because they allow a single function to work with different data without changing its definition.

In this lesson, you will learn what arguments are, why they are important, how they work with parameters, and how to pass different values to a function.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Define an argument.
- Understand the relationship between parameters and arguments.
- Pass arguments to functions correctly.
- Pass one or more arguments.
- Understand how arguments are assigned to parameters.
- Identify common mistakes when passing arguments.

---

# What Are Arguments?

An **argument** is the **actual value** that is passed to a function when it is called.

The function receives this value and stores it in its corresponding parameter.

### Simple Definition

> An **argument** is the value you provide to a function when calling it.

---

# Parameters vs Arguments

Many beginners confuse these two terms.

The difference is simple.

| Parameter | Argument |
|-----------|----------|
| A variable declared in the function definition | The actual value passed during the function call |
| Acts as a placeholder | Provides real data |
| Written when defining a function | Written when calling a function |

Consider the following example:

```python
def greet(name):
    print("Hello,", name)

greet("Ali")
```

In this example:

- `name` is the **parameter**.
- `"Ali"` is the **argument**.

---

# How Arguments Work

When a function is called, Python performs the following steps:

1. Receives the argument.
2. Assigns it to the corresponding parameter.
3. Executes the statements inside the function.
4. Finishes the function.
5. Returns to the next statement in the program.

---

# Example 1: Passing One Argument

This function receives one value.

### Code

```python
# Define the function
def greet(name):
    print("Hello,", name)

# Call the function
greet("Sara")
```

### Expected Output

```text
Hello, Sara
```

### Explanation of the Output

The argument `"Sara"` is assigned to the parameter `name`.

The function then prints the greeting using that value.

---

# Example 2: Calling the Same Function with Different Arguments

A function can receive different arguments every time it is called.

### Code

```python
# Define the function
def greet(name):
    print("Welcome,", name)

# Call the function
greet("Ali")
greet("Ahmed")
greet("Ayesha")
```

### Expected Output

```text
Welcome, Ali
Welcome, Ahmed
Welcome, Ayesha
```

### Explanation of the Output

The function definition does not change.

Only the arguments change, allowing the function to produce different results.

---

# Example 3: Passing Multiple Arguments

A function may require more than one argument.

### Code

```python
# Define the function
def student_information(name, age):
    print("Name:", name)
    print("Age:", age)

# Call the function
student_information("Fatima", 19)
```

### Expected Output

```text
Name: Fatima
Age: 19
```

### Explanation of the Output

The first argument is assigned to the first parameter.

The second argument is assigned to the second parameter.

---

# Example 4: Calculator Function

Arguments are commonly used in calculations.

### Code

```python
# Define the function
def add_numbers(first_number, second_number):
    total = first_number + second_number
    print("Sum:", total)

# Call the function
add_numbers(15, 25)
```

### Expected Output

```text
Sum: 40
```

### Explanation of the Output

The function receives two arguments.

These arguments are assigned to the parameters and added together.

---

# Example 5: Shopping Bill

Arguments can represent prices, quantities, and other values.

### Code

```python
# Define the function
def calculate_bill(price, quantity):
    total = price * quantity
    print("Total Bill:", total)

# Call the function
calculate_bill(350, 3)
```

### Expected Output

```text
Total Bill: 1050
```

### Explanation of the Output

The first argument represents the price.

The second argument represents the quantity.

The function calculates the total bill and displays it.

---

# The Number of Arguments Must Match the Number of Parameters

Every parameter needs a corresponding argument unless a default value is provided (covered in a later lesson).

Example:

```python
def student(name, age):
    print(name)
    print(age)
```

Correct function call:

```python
student("Ali", 20)
```

Here:

- `name` receives `"Ali"`
- `age` receives `20`

---

# Too Few Arguments

Incorrect code:

```python
def student(name, age):
    print(name)
    print(age)

student("Ali")
```

The function expects two arguments but receives only one.

Python will report an error because the second parameter does not receive a value.

---

# Too Many Arguments

Incorrect code:

```python
def student(name):
    print(name)

student("Ali", 20)
```

The function expects one argument but receives two.

Python will report an error because an extra argument was supplied.

---

# Passing Different Types of Arguments

Arguments can be of different data types.

### Example

```python
def display_information(name, age, is_student):
    print("Name:", name)
    print("Age:", age)
    print("Student:", is_student)

display_information("Ali", 20, True)
```

### Expected Output

```text
Name: Ali
Age: 20
Student: True
```

The function receives:

- A string
- An integer
- A Boolean value

---

# Real-World Example

Suppose a school needs to print report cards.

Instead of creating a different function for every student, one function can be used repeatedly.

```python
def report(name, marks):
    print(name)
    print(marks)

report("Ali", 92)
report("Sara", 88)
report("Ahmed", 95)
```

This approach is much more efficient than writing separate functions for every student.

---

# Common Beginner Mistakes

## Confusing Parameters and Arguments

Incorrect understanding:

> Parameters and arguments are the same thing.

Correct understanding:

- Parameters are written in the function definition.
- Arguments are written in the function call.

---

## Passing Too Few Arguments

Incorrect

```python
def greet(name):
    print(name)

greet()
```

Always provide the required argument.

---

## Passing Too Many Arguments

Incorrect

```python
def greet(name):
    print(name)

greet("Ali", "Ahmed")
```

Only pass the required number of arguments.

---

## Passing Arguments in the Wrong Order

Consider this function.

```python
def student(name, age):
    print(name)
    print(age)
```

Correct

```python
student("Ali", 20)
```

Incorrect

```python
student(20, "Ali")
```

Although Python accepts the values, the output will not represent the intended information.

---

# Best Practices

- Pass the correct number of arguments.
- Pass arguments in the correct order.
- Use meaningful parameter names.
- Reuse the same function with different arguments instead of creating multiple similar functions.
- Read the function definition before calling it.

---

# Tips

> **Tip**
>
> A simple way to remember the difference:
>
> - **Parameter = Placeholder**
> - **Argument = Actual Value**

---

> **Remember**
>
> Every time a function is called, its parameters receive new values from the arguments provided.

---

# Key Points

- Arguments are the actual values passed to a function.
- Parameters receive those values.
- The number of arguments should normally match the number of parameters.
- Different function calls can use different arguments.
- Arguments make functions flexible and reusable.

---

# Summary

In this lesson, you learned how arguments work in Python functions.

You learned:

- What arguments are.
- The difference between parameters and arguments.
- How arguments are assigned to parameters.
- How to pass one or more arguments.
- Common mistakes beginners should avoid.
- How arguments make functions reusable for different situations.

In the next lesson, you will learn about **positional and keyword arguments**, two common ways of passing arguments to a function.