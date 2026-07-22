# Functions Exercise Solutions

This document contains solutions for all exercises in the **Functions** module.

---

# Exercise 01 Solution

```python
def say_hello():
    print("Hello, Python!")


say_hello()
```

---

# Exercise 02 Solution

```python
def display_message():
    print("Welcome to Python Programming Foundation!")


display_message()
display_message()
display_message()
```

---

# Exercise 03 Solution

```python
def greet_user(name):
    print(f"Hello, {name}!")


user_name = input("Enter your name: ")

greet_user(user_name)
```

---

# Exercise 04 Solution

```python
def add_numbers(first_number, second_number):
    print(first_number + second_number)


number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

add_numbers(number1, number2)
```

---

# Exercise 05 Solution

```python
def display_student(name, age):
    print("Student Information")
    print("-------------------")
    print(f"Name: {name}")
    print(f"Age: {age}")


student_name = input("Enter the student's name: ")
student_age = int(input("Enter the student's age: "))

display_student(student_name, student_age)
```

---

# Exercise 06 Solution

```python
def introduce(name, city="Unknown"):
    print(f"Name: {name}")
    print(f"City: {city}")


user_name = input("Enter your name: ")

introduce(user_name)
introduce(user_name, "Lahore")
```

---

# Exercise 07 Solution

```python
def square(number):
    return number * number


value = float(input("Enter a number: "))

result = square(value)

print(f"Square: {result}")
```

---

# Exercise 08 Solution

```python
def display_line():
    print("-" * 30)


def welcome_message():
    print("Welcome to the Python Programming Foundation course!")


def goodbye_message():
    print("Thank you for practicing Python functions!")


display_line()
welcome_message()
display_line()
print("This is the main part of the program.")
display_line()
goodbye_message()
display_line()
```

---

# Exercise 09 Solution

```python
def multiply(number1, number2):
    return number1 * number2


first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

product = multiply(first, second)

print(f"Product: {product}")
```

---

# Exercise 10 Solution

```python
def welcome():
    """Display a welcome message."""
    print("Welcome to Python Programming Foundation!")


welcome()

print(welcome.__doc__)
```

---

# Exercise 11 Solution

```python
def classify_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


user_number = int(input("Enter an integer: "))

result = classify_number(user_number)

print(result)
```

---

# Exercise 12 Solution

```python
def find_largest(number1, number2, number3):
    if number1 >= number2 and number1 >= number3:
        return number1
    elif number2 >= number1 and number2 >= number3:
        return number2
    else:
        return number3


first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
third = float(input("Enter the third number: "))

largest = find_largest(first, second, third)

print(f"Largest number: {largest}")
```

---

# Exercise 13 Solution

```python
def greet_user(name, message="Welcome to Python!"):
    print(f"Hello, {name}!")
    print(message)


user_name = input("Enter your name: ")

greet_user(user_name)
print()
greet_user(user_name, "Keep practicing every day!")
```

---

# Exercise 14 Solution

```python
course_name = "Python Programming Foundation"


def display_course():
    print(f"Course: {course_name}")

    lesson = "Functions"
    print(f"Lesson: {lesson}")


display_course()

print(f"Course: {course_name}")
```

---

# Exercise 15 Solution

```python
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


student_marks = float(input("Enter your marks: "))

grade = calculate_grade(student_marks)

print(f"Grade: {grade}")
```