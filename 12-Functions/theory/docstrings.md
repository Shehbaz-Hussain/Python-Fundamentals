# Docstrings in Python Functions

## Introduction

As your programs become larger, it becomes increasingly important to explain what your code does. While comments help explain parts of the code, Python also provides a special way to document functions using **docstrings**.

A well-written docstring helps both you and other programmers understand the purpose of a function without reading every line of its implementation.

Docstrings are considered a standard part of writing professional Python code.

---

# Learning Objectives

After studying this topic, you will be able to:

- Understand what a docstring is.
- Know why docstrings are useful.
- Write docstrings for your own functions.
- Read documentation written as docstrings.
- Follow the basic recommendations of **PEP 257**, Python's official docstring convention.

---

# What Is a Docstring?

A **docstring** (documentation string) is a string placed as the **first statement inside a function**.

It explains:

- What the function does
- What information the function expects (if any)
- What the function returns (if applicable)

A docstring is enclosed in triple quotation marks.

```python
def function_name():
    """This is a docstring."""
```

Although triple single quotes also work, the Python style guide recommends using **triple double quotes**.

---

# Why Do We Use Docstrings?

Imagine opening a project that contains dozens or even hundreds of functions.

Without documentation, understanding each function would require reading its code line by line.

Docstrings solve this problem by describing the function immediately.

Benefits include:

- Makes code easier to understand.
- Improves readability.
- Helps future maintenance.
- Assists team collaboration.
- Encourages good programming habits.
- Acts as built-in documentation.

---

# How Does a Docstring Work?

The docstring is written immediately after the function definition.

Example:

```python
def greet():
    """Display a welcome message."""
    print("Welcome!")
```

The first statement inside the function is the docstring.

Everything after it is the function's actual implementation.

---

# Simple Example

```python
def say_hello():
    """Print a greeting message."""
    print("Hello!")
```

### Expected Output

```
Hello!
```

### Explanation

The function contains a short description explaining its purpose before the executable code.

---

# Example with Parameters

A docstring can mention the purpose of parameters.

```python
def greet(name):
    """
    Display a personalized greeting.

    Parameter:
        name: The person's name.
    """
    print("Hello,", name)
```

### Expected Output

```
Hello, Ali
```

if called as:

```python
greet("Ali")
```

---

# Example with a Return Value

When a function returns a value, the docstring should mention it.

```python
def add(number1, number2):
    """
    Return the sum of two numbers.
    """
    return number1 + number2
```

---

# Multi-Line Docstrings

Short functions often use a one-line docstring.

More detailed functions may use multiple lines.

Example:

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
        length: Length of the rectangle.
        width: Width of the rectangle.

    Returns:
        The area of the rectangle.
    """
    return length * width
```

This format becomes especially useful as programs grow larger.

---

# One-Line vs Multi-Line Docstrings

| One-Line | Multi-Line |
|----------|------------|
| Short description | Detailed explanation |
| Used for simple functions | Used for larger functions |
| Easy to read | Includes additional information |
| Best for obvious behavior | Best for complex behavior |

---

# Docstrings vs Comments

Many beginners confuse comments with docstrings.

| Comments | Docstrings |
|----------|------------|
| Explain specific code | Explain an entire function |
| Start with `#` | Use triple quotation marks |
| Can appear anywhere | Must be the first statement inside a function |
| Not formal documentation | Official documentation style |

Example:

```python
def square(number):
    """Return the square of a number."""

    # Multiply the number by itself.
    return number * number
```

Here:

- The docstring explains the function.
- The comment explains one line of code.

---

# Writing Good Docstrings

Good docstrings should be:

- Clear
- Short
- Accurate
- Easy to understand
- Grammatically correct

Good example:

```python
"""Return the larger of two numbers."""
```

Poor example:

```python
"""This function does something."""
```

The second example gives almost no useful information.

---

# Best Practices

When writing docstrings:

- Write them immediately after the function definition.
- Use triple double quotation marks.
- Start with a short summary.
- Keep the language simple.
- Describe the function's purpose.
- Mention parameters when helpful.
- Mention return values when appropriate.
- Update the docstring whenever the function changes.

---

# Common Beginner Mistakes

## 1. Forgetting the Docstring

```python
def greet():
    print("Hello")
```

Adding a docstring makes the function easier to understand.

---

## 2. Writing the Docstring in the Wrong Place

Incorrect:

```python
def greet():
    print("Hello")
    """Greeting"""
```

The docstring must be the **first statement** inside the function.

Correct:

```python
def greet():
    """Print a greeting."""
    print("Hello")
```

---

## 3. Making the Docstring Too Vague

Poor:

```python
"""Function"""
```

Better:

```python
"""Display a welcome message to the user."""
```

---

# Practical Example

```python
def calculate_total(price, quantity):
    """
    Calculate the total cost of purchased items.

    Parameters:
        price: Price of one item.
        quantity: Number of items.

    Returns:
        Total purchase cost.
    """
    return price * quantity
```

### Expected Output

If called as:

```python
print(calculate_total(50, 4))
```

Output:

```
200
```

### Explanation

The docstring immediately explains:

- What the function does
- What inputs it expects
- What it returns

The code becomes easier to understand without reading every statement.

---

# Real-World Importance

Professional software projects often contain:

- Hundreds of files
- Thousands of functions
- Multiple developers

Docstrings help developers:

- Understand unfamiliar code
- Maintain existing software
- Reduce confusion
- Improve collaboration

Many documentation tools also use docstrings to generate project documentation automatically.

---

# Tips

> **Tip:** Write the docstring before writing the function body. This encourages you to think about the function's purpose first.

> **Tip:** Keep your docstrings updated whenever you modify a function.

> **Tip:** A clear docstring is often more valuable than many unnecessary comments.

---

# Warning

A docstring should describe **what** a function does, not explain every line of code inside it.

Keep implementation details in comments only when necessary.

---

# Key Takeaways

- A **docstring** is a documentation string placed as the first statement inside a function.
- Docstrings use **triple double quotation marks (`"""`)**.
- They explain the purpose of a function.
- They improve readability and maintainability.
- They are recommended by **PEP 257**.
- Good docstrings are clear, concise, and accurate.
- Comments explain individual code, while docstrings describe an entire function.
- Writing docstrings is a professional programming practice that makes code easier to understand and maintain.