# Best Practices for Writing Python Functions

## Introduction

Learning how to write functions is only the first step. Writing **good** functions is what makes your programs easier to understand, maintain, and improve.

Professional programmers follow a set of recommended practices when creating functions. These practices make code cleaner, more readable, and easier to reuse.

This chapter introduces beginner-friendly best practices that you should start following from the beginning of your Python journey.

---

# Learning Objectives

After studying this chapter, you will be able to:

- Write clear and readable functions.
- Choose meaningful function names.
- Keep functions focused on one task.
- Use parameters effectively.
- Return values when appropriate.
- Write useful docstrings.
- Avoid common beginner mistakes.
- Develop good programming habits.

---

# What Are Best Practices?

**Best practices** are recommended techniques and habits that help programmers write high-quality code.

They are not strict language rules, but following them makes your programs:

- Easier to read
- Easier to test
- Easier to reuse
- Easier to maintain
- Easier for other programmers to understand

---

# Why Are Best Practices Important?

Imagine two programs that produce exactly the same output.

One program:

- Uses clear names
- Is well organized
- Has helpful documentation

The other:

- Uses confusing names
- Repeats code
- Has no documentation

Although both programs work, the first program is much easier to understand and maintain.

That is why professional developers value code quality as much as correct output.

---

# Best Practice 1: Give Functions Meaningful Names

A function name should clearly describe what the function does.

## Good Example

```python
def calculate_total():
    pass
```

```python
def print_welcome_message():
    pass
```

```python
def find_largest_number():
    pass
```

These names immediately explain the function's purpose.

---

## Poor Example

```python
def abc():
    pass
```

```python
def data():
    pass
```

```python
def test():
    pass
```

These names do not describe the function.

---

# Best Practice 2: Use Lowercase Letters and Underscores

According to **PEP 8**, function names should use **snake_case**.

Correct:

```python
def calculate_area():
    pass
```

```python
def display_result():
    pass
```

Incorrect:

```python
def CalculateArea():
    pass
```

```python
def calculateArea():
    pass
```

Using snake_case keeps your code consistent with the Python community.

---

# Best Practice 3: Keep Functions Small

A function should perform **one specific task**.

Good example:

```python
def greet():
    print("Welcome!")
```

Poor example:

```python
def everything():
    # Reads input
    # Performs calculations
    # Prints reports
    # Displays menus
    # Handles many unrelated tasks
```

Small functions are easier to understand, test, and reuse.

---

# Best Practice 4: Avoid Repeating Code

One of the main purposes of functions is to eliminate repeated code.

Instead of writing the same statements multiple times, place them inside a function.

Without a function:

```python
print("Welcome!")
print("Please log in.")

print("Welcome!")
print("Please log in.")
```

Using a function:

```python
def welcome():
    print("Welcome!")
    print("Please log in.")

welcome()
welcome()
```

The function can be called whenever needed.

---

# Best Practice 5: Use Parameters Instead of Hard-Coding Values

Avoid placing fixed values directly inside a function if they may change.

Less flexible:

```python
def greet():
    print("Hello, Ali")
```

More flexible:

```python
def greet(name):
    print("Hello,", name)
```

Now the same function can greet different people.

---

# Best Practice 6: Return Values When Appropriate

If a function calculates a result, return it instead of printing it.

Good example:

```python
def add(a, b):
    return a + b
```

Then you can decide how to use the result.

```python
answer = add(5, 3)
print(answer)
```

Returning values makes functions more reusable.

---

# Best Practice 7: Write a Docstring

Every important function should include a docstring.

Example:

```python
def square(number):
    """Return the square of a number."""
    return number * number
```

A docstring explains the purpose of the function.

---

# Best Practice 8: Use Meaningful Parameter Names

Choose parameter names that describe the information they store.

Good:

```python
def calculate_area(length, width):
    return length * width
```

Poor:

```python
def calculate_area(a, b):
    return a * b
```

Meaningful names improve readability.

---

# Best Practice 9: Keep Indentation Consistent

Python uses indentation to define blocks of code.

Correct:

```python
def greet():
    print("Hello")
```

Incorrect:

```python
def greet():
print("Hello")
```

Always use consistent indentation throughout your program.

---

# Best Practice 10: Keep Functions Focused

A function should solve **one problem**.

For example:

```python
def calculate_average():
    pass
```

should only calculate an average.

It should not also:

- Print a menu
- Read multiple unrelated inputs
- Display reports

Keeping functions focused makes programs easier to improve later.

---

# Best Practice 11: Call Functions Only When Needed

Defining a function does not execute it.

```python
def greet():
    print("Hello")
```

Nothing happens until you call it.

```python
greet()
```

Always remember to call the function when you want it to run.

---

# Best Practice 12: Keep Comments Helpful

Comments should explain **why** something is done, not repeat obvious code.

Helpful:

```python
# Calculate the final bill including tax.
```

Not helpful:

```python
# Print Hello.
print("Hello")
```

Write comments only when they add useful information.

---

# Example Program

```python
def calculate_rectangle_area(length, width):
    """Return the area of a rectangle."""
    return length * width


length = 8
width = 5

area = calculate_rectangle_area(length, width)

print("Area:", area)
```

### Expected Output

```
Area: 40
```

### Explanation

This program demonstrates several best practices:

- Meaningful function name
- Meaningful parameter names
- Docstring
- Return statement
- Clear variable names
- Simple structure
- Reusable function

---

# Summary Table

| Best Practice | Benefit |
|---------------|---------|
| Use meaningful names | Improves readability |
| Use snake_case | Follows Python standards |
| Keep functions small | Easier to understand |
| Avoid repeated code | Saves time and effort |
| Use parameters | Makes functions reusable |
| Return values | Makes results reusable |
| Write docstrings | Documents the function |
| Use descriptive parameters | Makes code clearer |
| Keep indentation consistent | Prevents syntax errors |
| Focus on one task | Improves organization |
| Call functions when needed | Executes the function |
| Write useful comments | Improves understanding |

---

# Tips

> **Tip:** Before writing a function, ask yourself, *"What single task should this function perform?"*

> **Tip:** A descriptive function name often removes the need for extra comments.

> **Tip:** If you find yourself copying and pasting the same code, consider creating a function.

---

# Warning

Avoid making one function responsible for many unrelated tasks.

Large, complicated functions are difficult to understand, debug, and maintain.

---

# Key Takeaways

- Best practices improve code quality and readability.
- Choose clear, descriptive function names.
- Use **snake_case** for naming functions.
- Keep each function focused on one task.
- Avoid repeating code by using reusable functions.
- Use parameters instead of hard-coded values whenever appropriate.
- Return values when a function performs a calculation.
- Write meaningful docstrings for documentation.
- Use descriptive variable and parameter names.
- Follow consistent indentation and formatting to produce clean, professional Python code.