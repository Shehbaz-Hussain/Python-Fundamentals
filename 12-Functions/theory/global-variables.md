# Global Variables

## Introduction

In the previous lesson, you learned about **local variables**, which are created inside a function and can only be accessed within that function.

Sometimes, however, a program needs a variable that can be accessed by multiple functions or by both the main program and its functions. In such situations, Python allows us to create **global variables**.

A global variable is created **outside** all functions. Since it belongs to the entire program, it can be accessed from different parts of the program.

Understanding global variables helps you decide where a variable should be created and how it should be used effectively.

> **Note**
>
> Although global variables are useful in some situations, beginner programs should primarily rely on **parameters**, **arguments**, and **return values** to exchange information between functions. Excessive use of global variables can make programs harder to understand and maintain.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Define a global variable.
- Explain how global variables differ from local variables.
- Access global variables inside functions.
- Understand when global variables are useful.
- Identify situations where global variables should be avoided.
- Avoid common mistakes related to global variables.

---

# What Is a Global Variable?

A **global variable** is a variable that is created **outside all functions**.

It belongs to the entire program and can be accessed from different parts of the program, including functions.

### Simple Definition

> A **global variable** is a variable that is defined outside a function and is available throughout the program.

---

# Where Is a Global Variable Created?

Global variables are written outside any function definition.

Example:

```python
course = "Python Programming"

def display_course():
    print(course)

display_course()
```

In this example:

- `course` is created outside the function.
- The function accesses the value stored in `course`.

---

# Visual Representation

```text
Python Program
│
├── Global Variable
│       │
│       ├── Accessible in Function A
│       ├── Accessible in Function B
│       └── Accessible in Function C
│
└── End of Program
```

The global variable exists independently of any specific function.

---

# Example 1: Accessing a Global Variable

### Explanation

The following program creates a global variable and accesses it inside a function.

### Code

```python
# Global variable
course_name = "Python Programming"

# Define a function
def display_course():
    print("Course:", course_name)

# Call the function
display_course()
```

### Expected Output

```text
Course: Python Programming
```

### Explanation of the Output

The variable `course_name` is created outside the function.

Since it is global, the function can access and display its value.

---

# Example 2: Using a Global Variable in Multiple Functions

### Explanation

A single global variable can be accessed by multiple functions.

### Code

```python
# Global variable
school_name = "ABC School"

# First function
def display_student():
    print("Student School:", school_name)

# Second function
def display_teacher():
    print("Teacher School:", school_name)

# Function calls
display_student()
display_teacher()
```

### Expected Output

```text
Student School: ABC School
Teacher School: ABC School
```

### Explanation of the Output

Both functions access the same global variable.

There is only one copy of `school_name`, and both functions use it.

---

# Example 3: Accessing a Global Variable in the Main Program

Global variables can also be used outside functions.

### Code

```python
# Global variable
country = "Pakistan"

print("Country:", country)

def display_country():
    print("Country:", country)

display_country()
```

### Expected Output

```text
Country: Pakistan
Country: Pakistan
```

### Explanation of the Output

The variable `country` is available:

- In the main program.
- Inside the function.

---

# Global Variables vs Local Variables

The following table compares the two types of variables.

| Global Variable | Local Variable |
|-----------------|----------------|
| Created outside a function | Created inside a function |
| Can be accessed throughout the program | Can only be accessed inside its function |
| Exists independently of functions | Exists only while its function is executing |
| Can be shared by multiple functions | Belongs to one function only |

---

# Local and Global Variables Together

A program may contain both local and global variables.

### Code

```python
# Global variable
course = "Python"

def display_information():
    # Local variable
    level = "Beginner"

    print("Course:", course)
    print("Level:", level)

display_information()
```

### Expected Output

```text
Course: Python
Level: Beginner
```

### Explanation of the Output

The function uses:

- A global variable (`course`).
- A local variable (`level`).

Both variables are available inside the function because:

- Global variables can be accessed throughout the program.
- Local variables can be accessed within their own function.

---

# When Should You Use Global Variables?

Global variables are useful when the same information is needed throughout a program.

Examples include:

- School name
- Company name
- Country
- Currency
- Application title

These values usually remain the same while the program is running.

---

# When Should You Avoid Global Variables?

Avoid global variables when the information:

- Is only needed inside one function.
- Can be passed as a parameter.
- Can be returned from a function.
- Does not need to be shared throughout the program.

Using unnecessary global variables makes programs harder to understand and maintain.

---

# Real-World Example

Suppose every report generated by a school application should display the school name.

Instead of writing the school name inside every function, one global variable can be created.

```python
school_name = "Bright Future School"

def display_heading():
    print(school_name)
    print("----------------------")

display_heading()
```

This makes it easy to update the school name later.

---

# Common Beginner Mistakes

## Creating Too Many Global Variables

Incorrect approach:

```python
student_name = "Ali"
student_marks = 90
student_age = 20
student_class = "BSAI"
```

If these variables are only used inside one function, they should be local variables instead.

---

## Confusing Local and Global Variables

Some beginners believe every variable is global.

This is incorrect.

Only variables created outside functions are global.

---

## Depending Too Much on Global Variables

Although global variables are convenient, using them everywhere can make a program difficult to understand.

Whenever possible:

- Pass information using parameters.
- Return results using the `return` statement.

These techniques make functions more reusable.

---

# Best Practices

- Use global variables only for shared information.
- Keep the number of global variables small.
- Use meaningful variable names.
- Prefer local variables whenever possible.
- Use parameters and return values for most function communication.

---

# Tips

> **Tip**
>
> Ask yourself:
>
> "Does this value need to be shared by the entire program?"
>
> If the answer is **yes**, a global variable may be appropriate.

---

> **Remember**
>
> A global variable belongs to the entire program, while a local variable belongs to a single function.

---

# Key Points

- A global variable is created outside all functions.
- Global variables can be accessed inside functions.
- Multiple functions can use the same global variable.
- Local variables exist only inside their own function.
- Use global variables only when information needs to be shared throughout the program.

---

# Summary

In this lesson, you learned about **global variables**.

You learned:

- What a global variable is.
- Where global variables are created.
- How global variables are accessed inside functions.
- The differences between global and local variables.
- When global variables should be used.
- When they should be avoided.
- Best practices for writing clear and maintainable programs.

In the next lesson, you will learn about **docstrings**, which are used to document functions and make your code easier to understand.
```