# Positional vs Keyword Arguments

## Introduction

In the previous lesson, you learned that **arguments** are the actual values passed to a function when it is called.

When calling a function, Python allows you to pass arguments in different ways. The two most common methods are:

- **Positional Arguments**
- **Keyword Arguments**

Understanding these two methods is important because they determine **how values are assigned to parameters**.

For beginner-level programs, both approaches are useful, and choosing the appropriate one can make your code easier to read and understand.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand positional arguments.
- Understand keyword arguments.
- Explain the differences between them.
- Call functions using both methods.
- Identify situations where each method is useful.
- Avoid common mistakes when passing arguments.

---

# What Are Positional Arguments?

**Positional arguments** are arguments that are assigned to parameters based on their **position**.

The first argument is assigned to the first parameter.

The second argument is assigned to the second parameter.

The third argument is assigned to the third parameter, and so on.

### Syntax

```python
function_name(value1, value2, value3)
```

Python matches each value with its parameter according to its position.

---

# Example 1: Positional Arguments

### Explanation

This function displays a student's name and age.

The first argument is assigned to the first parameter, and the second argument is assigned to the second parameter.

### Code

```python
# Define the function
def student_information(name, age):
    print("Name:", name)
    print("Age:", age)

# Call the function using positional arguments
student_information("Ali", 20)
```

### Expected Output

```text
Name: Ali
Age: 20
```

### Explanation of the Output

Python assigns:

- `"Ali"` to `name`
- `20` to `age`

because the arguments are matched according to their positions.

---

# Example 2: Another Positional Argument Example

### Explanation

This function calculates the area of a rectangle.

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

Python assigns:

- `8` to `length`
- `5` to `width`

The function multiplies these values to calculate the area.

---

# Why Is the Order Important?

When using positional arguments, **order matters**.

Changing the order changes which parameter receives each value.

### Correct Example

```python
def student_information(name, age):
    print("Name:", name)
    print("Age:", age)

student_information("Sara", 19)
```

### Output

```text
Name: Sara
Age: 19
```

---

### Incorrect Order

```python
def student_information(name, age):
    print("Name:", name)
    print("Age:", age)

student_information(19, "Sara")
```

### Output

```text
Name: 19
Age: Sara
```

Although Python executes the program, the information is incorrect because the arguments were passed in the wrong order.

---

# What Are Keyword Arguments?

**Keyword arguments** allow you to specify the parameter name when passing a value.

Instead of relying on position, Python matches the value with the parameter name.

### Syntax

```python
function_name(parameter=value)
```

---

# Example 3: Keyword Arguments

### Explanation

The following function receives a student's name and age.

Instead of relying on position, each value is assigned using the parameter name.

### Code

```python
# Define the function
def student_information(name, age):
    print("Name:", name)
    print("Age:", age)

# Call the function using keyword arguments
student_information(name="Ali", age=20)
```

### Expected Output

```text
Name: Ali
Age: 20
```

### Explanation of the Output

Python assigns the values using the parameter names:

- `name="Ali"`
- `age=20`

The order is not important because the parameter names are provided.

---

# Example 4: Changing the Order with Keyword Arguments

One advantage of keyword arguments is that the order does not matter.

### Code

```python
# Define the function
def employee_information(name, salary):
    print("Name:", name)
    print("Salary:", salary)

# Call the function
employee_information(salary=50000, name="Ahmed")
```

### Expected Output

```text
Name: Ahmed
Salary: 50000
```

### Explanation of the Output

Although `salary` is written first, Python assigns each value to the correct parameter because the parameter names are specified.

---

# Comparing Positional and Keyword Arguments

| Positional Arguments | Keyword Arguments |
|-----------------------|-------------------|
| Matched by position | Matched by parameter name |
| Order is important | Order is not important |
| Shorter to write | Easier to read |
| Common for simple function calls | Useful when functions have multiple parameters |

---

# When Should You Use Positional Arguments?

Positional arguments are a good choice when:

- The function has only a few parameters.
- The order of the values is clear.
- The function call is simple.

### Example

```python
rectangle_area(10, 6)
```

---

# When Should You Use Keyword Arguments?

Keyword arguments are useful when:

- A function has many parameters.
- You want to improve readability.
- You want to avoid mistakes caused by incorrect argument order.

### Example

```python
student_information(name="Fatima", age=21)
```

---

# Real-World Example

Suppose you create a function to display employee details.

```python
def employee(name, department, salary):
    print("Name:", name)
    print("Department:", department)
    print("Salary:", salary)
```

### Positional Arguments

```python
employee("Ali", "Accounts", 60000)
```

### Keyword Arguments

```python
employee(
    name="Ali",
    department="Accounts",
    salary=60000
)
```

Both function calls produce the same output.

The keyword version is often easier to understand because each value clearly identifies its purpose.

---

# Common Beginner Mistakes

## Passing Positional Arguments in the Wrong Order

Incorrect

```python
student_information(20, "Ali")
```

Correct

```python
student_information("Ali", 20)
```

---

## Misspelling Parameter Names

Incorrect

```python
student_information(nam="Ali", age=20)
```

The parameter name does not match the function definition.

Correct

```python
student_information(name="Ali", age=20)
```

---

## Forgetting the Equal Sign

Incorrect

```python
student_information(name "Ali")
```

Correct

```python
student_information(name="Ali")
```

Keyword arguments always use the assignment operator (`=`).

---

# Best Practices

- Use positional arguments for short and simple function calls.
- Use keyword arguments when readability is important.
- Choose meaningful parameter names.
- Double-check the order when using positional arguments.
- Double-check the spelling when using keyword arguments.

---

# Tips

> **Tip**
>
> If you find it difficult to remember the correct order of arguments, use keyword arguments to make your code easier to read.

---

> **Remember**
>
> Positional arguments depend on **position**, while keyword arguments depend on **parameter names**.

---

# Key Points

- Positional arguments are matched according to their position.
- Keyword arguments are matched according to parameter names.
- The order matters for positional arguments.
- The order does not matter for keyword arguments.
- Both methods produce the same result when used correctly.
- Keyword arguments often improve readability.

---

# Summary

In this lesson, you learned two common ways to pass arguments to a function.

You learned:

- What positional arguments are.
- What keyword arguments are.
- The differences between the two methods.
- When to use each approach.
- Common mistakes to avoid.

In the next lesson, you will learn about **default arguments**, which allow functions to use predefined values when an argument is not provided.