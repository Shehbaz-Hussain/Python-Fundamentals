# Positional Arguments Syntax

## Introduction

When calling a function, Python must know which value belongs to which parameter.

The most common way to pass values to a function is by using **positional arguments**.

With positional arguments, Python matches each argument to a parameter **based on its position** in the function call.

Understanding positional arguments is essential because they are the default method of passing data to functions.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what positional arguments are.
- Learn the syntax of positional arguments.
- Match arguments with parameters correctly.
- Recognize the importance of argument order.
- Avoid common mistakes when using positional arguments.

---

# What Are Positional Arguments?

**Positional arguments** are arguments that are assigned to parameters according to their position.

Python reads the arguments from **left to right**.

The first argument is assigned to the first parameter, the second argument to the second parameter, and so on.

---

# Basic Syntax

```python
function_name(argument1, argument2, argument3)
```

Each argument is matched with the parameter in the same position.

---

# Example 1: One Positional Argument

```python
def greet(name):
    print("Hello,", name)


greet("Ali")
```

### Expected Output

```
Hello, Ali
```

### Explanation

| Parameter | Argument |
|-----------|----------|
| `name` | `"Ali"` |

The first argument is assigned to the first parameter.

---

# Example 2: Two Positional Arguments

```python
def add(number1, number2):
    print(number1 + number2)


add(5, 8)
```

### Expected Output

```
13
```

### Explanation

| Parameter | Argument |
|-----------|----------|
| `number1` | `5` |
| `number2` | `8` |

Python assigns the arguments in order.

---

# Example 3: Three Positional Arguments

```python
def student_information(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)


student_information("Sara", 20, "Gilgit")
```

### Expected Output

```
Name: Sara
Age: 20
City: Gilgit
```

### Explanation

Each argument is matched with the parameter in the same position.

---

# How Python Matches Positional Arguments

Consider the following function:

```python
def rectangle(length, width):
    print(length * width)


rectangle(8, 5)
```

Python performs the following assignments:

| Parameter | Receives |
|-----------|----------|
| `length` | `8` |
| `width` | `5` |

The multiplication becomes:

```python
8 * 5
```

Output:

```
40
```

---

# Why Order Matters

With positional arguments, **order is extremely important**.

Correct:

```python
def student(name, age):
    print(name)
    print(age)


student("Ali", 19)
```

Output:

```
Ali
19
```

Incorrect:

```python
student(19, "Ali")
```

Output:

```
19
Ali
```

Although Python does not report an error, the information is assigned incorrectly.

---

# Using Variables as Positional Arguments

Arguments can come from variables.

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

---

# Positional Arguments with Default Parameters

```python
def greet(name="Guest"):
    print("Hello,", name)
```

Calling with a positional argument:

```python
greet("Sara")
```

### Expected Output

```
Hello, Sara
```

Calling without an argument:

```python
greet()
```

### Expected Output

```
Hello, Guest
```

---

# General Syntax Examples

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

# Complete Example

```python
def calculate_total(price, quantity):
    """Calculate the total cost."""
    total = price * quantity
    print("Total:", total)


calculate_total(250, 4)
```

### Expected Output

```
Total: 1000
```

### Explanation

The first argument (`250`) is assigned to `price`, and the second argument (`4`) is assigned to `quantity`.

---

# Common Mistakes

## Passing Arguments in the Wrong Order

Incorrect:

```python
def employee(name, salary):
    print(name)
    print(salary)


employee(50000, "Ali")
```

Output:

```
50000
Ali
```

Correct:

```python
employee("Ali", 50000)
```

---

## Missing an Argument

Incorrect:

```python
def add(a, b):
    print(a + b)


add(5)
```

Python reports that one required argument is missing.

---

## Providing Too Many Arguments

Incorrect:

```python
def greet(name):
    print(name)


greet("Ali", "Sara")
```

Python reports that too many arguments were supplied.

---

# Best Practices

- Pass arguments in the same order as the parameters.
- Use meaningful values while testing your functions.
- Review the function definition before calling it.
- Use keyword arguments if the parameter order is difficult to remember.
- Keep function calls clear and readable.

---

# Summary Table

| Function Definition | Function Call |
|---------------------|---------------|
| `def greet(name):` | `greet("Ali")` |
| `def add(a, b):` | `add(5, 8)` |
| `def rectangle(length, width):` | `rectangle(10, 4)` |
| `def student(name, age, city):` | `student("Sara", 20, "Gilgit")` |

---

# Tips

> **Tip:** Read positional arguments from left to right.

> **Tip:** Match the first argument with the first parameter, the second with the second parameter, and so on.

> **Tip:** If the order is confusing, consider using keyword arguments instead.

---

# Warning

Positional arguments depend entirely on **order**.

Even if the values have the correct data types, changing their order may produce incorrect results.

Always verify that each argument corresponds to the intended parameter.

---

# Key Takeaways

- Positional arguments are matched with parameters according to their position.
- Python assigns arguments from left to right.
- The order of positional arguments is important.
- Functions may receive one or more positional arguments.
- Missing or extra positional arguments result in errors.
- Using positional arguments correctly helps functions receive the intended values and produce accurate results.