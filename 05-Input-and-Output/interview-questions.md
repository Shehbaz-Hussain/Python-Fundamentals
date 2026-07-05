# Interview Questions: Input and Output in Python

This section is designed to help you prepare for interviews, viva questions, and technical discussions.

---

## 1. Beginner-Level Questions

### 1. What is the difference between `input()` and `print()`?

`input()` is used to receive user data, while `print()` is used to display output to the screen.

### 2. What does `input()` return in Python?

It returns a string.

### 3. Why do we need type conversion with `input()`?

Because `input()` returns a string and numbers are often needed for arithmetic or comparisons.

### 4. What is the purpose of the `sep` parameter?

It changes the separator used when printing multiple values.

### 5. What is the purpose of the `end` parameter?

It changes the character or string printed at the end of the `print()` statement.

---

## 2. Intermediate-Level Questions

### 6. Why is `f-string` preferred over older formatting techniques?

Because it is easier to read, write, and maintain.

### 7. What happens if you use `print("Hello", end=" ")`?

The next output will appear on the same line, separated by a space.

### 8. How does `print("A", "B", sep="|")` behave?

It prints `A|B`.

### 9. What is the output of the following code?

```python
name = "Sara"
print(f"Hello, {name}")
```

Output:

```text
Hello, Sara
```

### 10. Why should user input be validated?

To ensure the program behaves correctly when the user enters unexpected data.

---

## 3. Scenario-Based Questions

### 11. Suppose a user enters age as text. How would you handle it?

You would convert it using `int()` after checking that it is a valid number.

```python
age_input = input("Enter your age: ")
if age_input.isdigit():
    age = int(age_input)
    print(age)
else:
    print("Please enter a valid age")
```

### 12. How would you create a menu-based console program?

You would use `input()` to receive the user choice and `print()` to display options and results.

### 13. How would you display data in a neat table format?

You can use `print()` with formatting and alignment, such as `f-strings` and spacing.

---

## 4. Coding Interview Questions

### 14. Write a program that asks the user for their name and prints a welcome message.

```python
name = input("Enter your name: ")
print(f"Welcome, {name}!")
```

### 15. Write a program that asks for two numbers and prints their sum.

```python
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
print(first_number + second_number)
```

### 16. Write a program that prints values using a custom separator.

```python
print("Python", "Java", "C++", sep=" | ")
```

---

## 5. Detailed Answers

### Answer to Question 1

`input()` reads data from the user, while `print()` sends data to the console for display.

### Answer to Question 6

`f-string` is preferred because it is concise and easy to understand. It reduces clutter and makes code more modern.

### Answer to Question 10

User input should be validated to prevent errors and make programs more robust.

---

## 6. Interview Tips

- Practice writing small interactive programs.
- Be comfortable explaining `input()` and `print()`.
- Understand the difference between strings and numbers.
- Know how `sep` and `end` work.
- Practice formatting output clearly.

---

## 7. Final Summary

Interviewers often ask about input and output because they are fundamental programming concepts. A strong answer should show that you understand how programs receive information and communicate results clearly.
