# Local Variables vs Global Variables

## Introduction

In the previous lessons, you learned about **local variables** and **global variables** individually. While both are used to store data, they differ in **where they are created**, **where they can be accessed**, and **how long they exist**.

Understanding the difference between local and global variables is important because it helps you write functions that are predictable, organized, and easy to maintain.

This chapter compares these two types of variables side by side.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Differentiate between local and global variables.
- Identify where each type of variable is created.
- Understand the scope of local and global variables.
- Decide when to use local variables and when to use global variables.
- Avoid common mistakes related to variable scope.

---

# What Is a Local Variable?

A **local variable** is a variable that is created **inside a function**.

It can only be accessed within that function.

Once the function finishes executing, the local variable is no longer available.

### Example

```python
def greet():
    message = "Welcome to Python!"
    print(message)

greet()
```

### Expected Output

```
Welcome to Python!
```

### Explanation

The variable `message` exists only inside the `greet()` function.

---

# What Is a Global Variable?

A **global variable** is a variable that is created **outside all functions**.

It can be accessed from anywhere in the program, including inside functions (as long as it is not hidden by a local variable with the same name).

### Example

```python
course = "Python Programming"

def display_course():
    print(course)

display_course()
```

### Expected Output

```
Python Programming
```

### Explanation

The variable `course` is defined outside the function, making it a global variable.

---

# Comparing Local and Global Variables

| Feature | Local Variable | Global Variable |
|---------|----------------|-----------------|
| Created | Inside a function | Outside all functions |
| Scope | Only inside the function | Throughout the program |
| Lifetime | Exists only while the function runs | Exists until the program ends |
| Accessibility | Cannot be used outside its function | Can be accessed inside and outside functions |
| Purpose | Temporary data for one function | Shared data used by multiple parts of a program |

---

# Example 1: Local Variable

```python
def calculate():
    number = 10
    print(number)

calculate()
```

### Expected Output

```
10
```

### Explanation

The variable `number` belongs only to the `calculate()` function.

---

# Example 2: Trying to Use a Local Variable Outside Its Function

```python
def calculate():
    number = 10

calculate()

print(number)
```

### Expected Result

```
NameError
```

### Explanation

The variable `number` exists only inside the function.

It cannot be accessed after the function has finished.

---

# Example 3: Global Variable

```python
language = "Python"

def show_language():
    print(language)

show_language()

print(language)
```

### Expected Output

```
Python
Python
```

### Explanation

The global variable `language` is available both inside and outside the function.

---

# Example 4: Local and Global Variables with Different Names

```python
country = "Pakistan"

def student_information():
    name = "Ali"

    print(name)
    print(country)

student_information()
```

### Expected Output

```
Ali
Pakistan
```

### Explanation

- `name` is a local variable.
- `country` is a global variable.

The function can access both because the global variable is visible throughout the program.

---

# Example 5: Local Variable Hides a Global Variable

A local variable can have the same name as a global variable.

In that case, the local variable is used inside the function.

```python
message = "Global Message"

def display():
    message = "Local Message"
    print(message)

display()

print(message)
```

### Expected Output

```
Local Message
Global Message
```

### Explanation

Inside the function, Python uses the local variable.

Outside the function, Python uses the global variable.

The two variables are separate, even though they have the same name.

---

# When Should You Use Local Variables?

Local variables are the preferred choice in most situations.

Use local variables when:

- Data is needed only inside one function.
- The value is temporary.
- You want to avoid affecting other parts of the program.
- You want functions to be independent.

---

# When Should You Use Global Variables?

Global variables can be useful when several functions need to access the same information.

Examples include:

- The name of a company.
- A course title.
- A tax rate that remains constant.
- A welcome message used throughout the program.

Use global variables carefully to keep programs organized and easier to understand.

---

# Advantages of Local Variables

- Keep functions independent.
- Reduce accidental changes.
- Make debugging easier.
- Improve code organization.
- Encourage reusable functions.

---

# Advantages of Global Variables

- Store information shared across multiple functions.
- Reduce duplication of common values.
- Useful for values that remain constant throughout the program.

---

# Common Mistakes

## Mistake 1: Using a Local Variable Outside Its Function

```python
def show():
    score = 95

show()

print(score)
```

This produces a `NameError` because `score` is local to the function.

---

## Mistake 2: Assuming Every Variable Is Global

```python
def greet():
    name = "Sara"

print(name)
```

The variable `name` cannot be accessed because it exists only inside the function.

---

## Mistake 3: Giving Local and Global Variables the Same Name Unnecessarily

Although Python allows it, using the same name for both local and global variables can make programs harder to understand.

Choose clear and meaningful names whenever possible.

---

# Best Practices

- Prefer local variables whenever possible.
- Use global variables only when the same information is genuinely shared across the program.
- Give variables descriptive names.
- Avoid unnecessary global variables.
- Keep variable scope as limited as possible.

---

# Tips

> **Tip:** If a variable is used by only one function, make it a local variable.

> **Tip:** Smaller variable scopes generally make programs easier to understand and maintain.

> **Tip:** Read function code carefully to determine whether a variable is local or global.

---

# Warning

Do not assume that a variable created inside a function will still exist after the function finishes.

Always remember:

- **Local variables stay inside the function.**
- **Global variables are created outside functions and can be accessed throughout the program.**

---

# Quick Comparison

| Question | Local Variable | Global Variable |
|----------|----------------|-----------------|
| Where is it created? | Inside a function | Outside all functions |
| Can it be used outside the function? | No | Yes |
| Does it exist after the function finishes? | No | Yes |
| Recommended for temporary data? | Yes | No |
| Recommended for shared data? | No | Yes |

---

# Key Takeaways

- Local variables are created inside functions and are available only within those functions.
- Global variables are created outside functions and can be accessed throughout the program.
- Local variables have a limited scope, while global variables have a broader scope.
- A local variable can have the same name as a global variable, but inside the function the local variable takes precedence.
- Use local variables whenever possible to keep functions independent and easier to maintain.
- Use global variables only when multiple parts of the program need to access the same shared information.
- Understanding variable scope helps you avoid common programming errors and write cleaner, more organized Python code.