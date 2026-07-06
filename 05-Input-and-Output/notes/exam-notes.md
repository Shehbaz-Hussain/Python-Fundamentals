# 📝 Exam Notes — Input and Output in Python

> **Module:** 05 - Input and Output  
> **Repository:** Python-Programming-Foundation  
> **Purpose:** University exam revision notes for Python Input and Output.

---

# Table of Contents

1. Topic Overview
2. Key Concepts
3. Important Syntax
4. Frequently Asked Exam Questions
5. Important Programming Questions
6. Common Mistakes
7. Memory Tricks
8. One-Page Revision Table
9. Last-Minute Exam Checklist

---

# 1. Topic Overview

## What is Input?

**Input** is the process of receiving data from the user or another source so that a program can process it.

Python primarily receives user input using:

```python
input()
```

Example:

```python
name = input("Enter your name: ")
```

---

## What is Output?

**Output** is the information produced by a program after processing data.

Python primarily displays output using:

```python
print()
```

Example:

```python
print("Welcome!")
```

---

## Importance of Input and Output

Input and Output allow programs to:

- Communicate with users
- Accept user data
- Display results
- Build interactive applications
- Perform calculations using user-provided values

Without Input and Output, programs would execute fixed instructions without interacting with users.

---

## Real-World Applications

| Application | Input | Output |
|------------|-------|--------|
| ATM | PIN, Amount | Balance, Receipt |
| Calculator | Numbers | Result |
| Login System | Username, Password | Success/Failure |
| Online Shopping | Product Details | Total Bill |
| Student Portal | Roll Number | Student Record |
| Banking | Account Number | Transaction Details |
| BMI Calculator | Height, Weight | BMI Value |
| Weather App | City Name | Weather Forecast |

---

# 2. Key Concepts

## print()

Displays information on the screen.

Example:

```python
print("Hello")
```

Output

```
Hello
```

---

## input()

Reads input from the keyboard.

Example

```python
name = input("Enter name: ")
```

---

## sep Parameter

Separates multiple values printed using `print()`.

Default separator:

```
space
```

Example

```python
print("Python", "Java", "C++", sep=", ")
```

Output

```
Python, Java, C++
```

---

## end Parameter

Controls what is printed after the output.

Default value:

```
newline (\n)
```

Example

```python
print("Hello", end=" ")
print("World")
```

Output

```
Hello World
```

---

## Escape Characters

Escape characters begin with a backslash (`\`).

| Escape Character | Meaning |
|-----------------|----------|
| `\n` | New Line |
| `\t` | Tab |
| `\\` | Backslash |
| `\"` | Double Quote |
| `\'` | Single Quote |

Example

```python
print("Python\nProgramming")
```

Output

```
Python
Programming
```

---

## f-Strings

A modern and readable way to insert variables into strings.

Example

```python
name = "Ali"
age = 20

print(f"{name} is {age} years old.")
```

Output

```
Ali is 20 years old.
```

Advantages

- Easy to read
- Fast
- Recommended in modern Python
- Supports expressions

Example

```python
x = 10

print(f"Square = {x*x}")
```

---

## str.format()

Formats strings using placeholders.

Example

```python
name = "Sara"

print("Hello {}".format(name))
```

Output

```
Hello Sara
```

Multiple placeholders

```python
print("{} scored {}".format("Ali", 95))
```

---

## Multiple Arguments in print()

```python
name = "Ali"
age = 20

print(name, age)
```

Output

```
Ali 20
```

---

## String Concatenation

Joining strings using `+`.

Example

```python
first = "Hello"
second = "World"

print(first + " " + second)
```

Output

```
Hello World
```

---

## Type Conversion with input()

`input()` always returns a string.

Convert input before mathematical operations.

Example

```python
age = int(input("Age: "))
```

Floating-point input

```python
height = float(input("Height: "))
```

---

## Interactive Console Programs

Interactive programs continuously communicate with users.

Example

```python
name = input("Name: ")
age = int(input("Age: "))

print(f"{name} is {age} years old.")
```

---

# 3. Important Syntax

## print()

```python
print(object1, object2, ..., sep=" ", end="\n")
```

---

## input()

```python
variable = input("Prompt")
```

---

## f-string

```python
name = "Ali"

print(f"Hello {name}")
```

---

## format()

```python
print("Hello {}".format(name))
```

---

## sep

```python
print("A", "B", "C", sep="-")
```

---

## end

```python
print("Hello", end=" ")
print("World")
```

---

# 4. Frequently Asked Exam Questions

## 1. What is Input?

Input is data supplied to a program for processing.

---

## 2. What is Output?

Output is information produced after processing.

---

## 3. What does print() do?

Displays information on the screen.

---

## 4. What does input() do?

Accepts data from the keyboard.

---

## 5. What data type does input() return?

It always returns a string (`str`).

---

## 6. Why is type conversion necessary?

Because mathematical operations require numeric data types.

---

## 7. What is string concatenation?

Joining strings using the `+` operator.

---

## 8. What are escape characters?

Special characters beginning with `\` that control formatting.

---

## 9. What is an f-string?

A formatted string literal that allows variable interpolation using `{}`.

---

## 10. What is `str.format()`?

A method used to insert values into strings using placeholders.

---

## 11. What is the purpose of `sep`?

It changes the separator between printed values.

---

## 12. What is the default value of `sep`?

A single space.

---

## 13. What is the purpose of `end`?

It changes what is printed after the output.

---

## 14. What is the default value of `end`?

A newline (`\n`).

---

## 15. What is interactive programming?

Programming where users provide input while the program is running.

---

## 16. What is the difference between input and output?

Input receives data; output displays data.

---

## 17. Why are prompts used in input()?

To guide the user about what information to enter.

---

## 18. Name two numeric conversion functions.

- `int()`
- `float()`

---

## 19. Which formatting method is recommended in modern Python?

f-strings.

---

## 20. Why is Input and Output important?

Because they enable communication between users and programs.

---

# 5. Important Programming Questions

Students should practice writing programs for:

1. Print "Hello, World!"
2. Display personal information.
3. Take user name and greet the user.
4. Add two numbers entered by the user.
5. Calculate area of a rectangle.
6. Calculate BMI.
7. Convert temperature (Celsius ↔ Fahrenheit).
8. Find average of three numbers.
9. Swap two variables.
10. Display a formatted student report.
11. Calculate simple interest.
12. Calculate age from birth year.
13. Build a basic calculator.
14. Convert kilometers to miles.
15. Generate a multiplication table.
16. Print values using custom separators.
17. Print values on the same line using `end`.
18. Demonstrate escape characters.
19. Use `str.format()` for formatted output.
20. Use f-strings to display calculated results.

---

# 6. Common Mistakes

| Mistake | Why It Happens | Correct Approach |
|----------|----------------|------------------|
| Adding two inputs directly | `input()` returns strings | Convert using `int()` or `float()` |
| Forgetting parentheses | Syntax error | Always use `print()` and `input()` with parentheses |
| Missing quotation marks | Invalid string | Enclose text in quotes |
| Incorrect indentation | Python uses indentation | Maintain consistent indentation |
| Mixing strings and integers | TypeError | Convert values or use formatting |
| Using `=` instead of `==` in conditions | Assignment vs comparison | Use the correct operator |
| Forgetting prompts | Poor user experience | Always provide meaningful prompts |
| Misusing escape characters | Incorrect output | Learn common escape sequences |

> **⚠️ Warning:** Never assume that numeric input is automatically converted to an integer or float. `input()` always returns a string.

---

# 7. Memory Tricks

## Remember Input vs Output

**Input → In**

Data comes **into** the program.

---

**Output → Out**

Information goes **out** of the program.

---

## Remember print()

> **P = Present**

`print()` presents information.

---

## Remember input()

> **I = Intake**

`input()` takes data into the program.

---

## Remember sep

> **SEP = Separate**

Changes the separator.

---

## Remember end

> **END = Ending**

Controls what appears after printing.

---

## Remember f-string

> **f = formatted**

Used for readable and modern string formatting.

---

# 8. One-Page Revision Table

| Concept | Purpose | Example |
|---------|---------|----------|
| `print()` | Display output | `print("Hi")` |
| `input()` | Receive input | `input("Age: ")` |
| `int()` | Convert to integer | `int(input())` |
| `float()` | Convert to decimal | `float(input())` |
| `str()` | Convert to string | `str(10)` |
| `sep` | Separator | `sep="-"` |
| `end` | Ending character | `end=""` |
| `\n` | New line | `"A\nB"` |
| `\t` | Tab | `"A\tB"` |
| Concatenation | Join strings | `"A" + "B"` |
| `format()` | Format strings | `"{}".format(x)` |
| f-string | Modern formatting | `f"{x}"` |

---

# 9. Last-Minute Exam Checklist

Before your exam, make sure you can:

- ✅ Define Input and Output.
- ✅ Explain the purpose of `print()`.
- ✅ Explain the purpose of `input()`.
- ✅ State that `input()` always returns a string.
- ✅ Convert input using `int()` and `float()`.
- ✅ Use `sep` correctly.
- ✅ Use `end` correctly.
- ✅ Write and explain escape characters.
- ✅ Use string concatenation.
- ✅ Use `str.format()`.
- ✅ Use f-strings.
- ✅ Explain the difference between formatting methods.
- ✅ Write interactive console programs.
- ✅ Solve basic input/output programming questions.
- ✅ Identify common beginner mistakes.
- ✅ Read and trace simple Input/Output code.
- ✅ Predict program output.
- ✅ Explain syntax accurately.
- ✅ Follow Python formatting conventions.

---

# Quick Reference

| Function | Purpose |
|----------|----------|
| `print()` | Display output |
| `input()` | Read user input |
| `int()` | Convert to integer |
| `float()` | Convert to float |
| `str()` | Convert to string |
| `sep` | Change separator |
| `end` | Change line ending |
| `f""` | Format strings |
| `format()` | Insert values into strings |

---

## Key Takeaways

- `print()` displays output to the console.
- `input()` reads user input and always returns a string.
- Convert numeric input using `int()` or `float()` before calculations.
- Use **f-strings** for clean, modern formatting.
- `sep` customizes separators between printed values.
- `end` controls what is printed after a `print()` call.
- Escape characters improve the formatting of output.
- Practice interactive programs to strengthen Input and Output skills.