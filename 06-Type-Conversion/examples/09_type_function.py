"""
File: example09_type_function.py

Topic:
Using the type() Function

Description:
This program demonstrates how to use the type() function
to determine the data type of different values and variables.

Concepts Used:
- Variables
- type()
- print()
- int()
- float()
- str()
- bool()
"""

print("=== Python type() Function Example ===")
print()

# Create variables of different data types
student_name = "Ali"
student_age = 20
student_height = 1.75
is_student = True

# Display values and their data types
print("Student Name:", student_name)
print("Data Type:", type(student_name))

print()

print("Student Age:", student_age)
print("Data Type:", type(student_age))

print()

print("Student Height:", student_height)
print("Data Type:", type(student_height))

print()

print("Is Student:", is_student)
print("Data Type:", type(is_student))

print()

# Demonstrate type changes after conversion
number = "100"

print("Before Conversion:")
print("Value:", number)
print("Type:", type(number))

print()

number = int(number)

print("After Conversion:")
print("Value:", number)
print("Type:", type(number))

"""
Expected Output:

=== Python type() Function Example ===

Student Name: Ali
Data Type: <class 'str'>

Student Age: 20
Data Type: <class 'int'>

Student Height: 1.75
Data Type: <class 'float'>

Is Student: True
Data Type: <class 'bool'>

Before Conversion:
Value: 100
Type: <class 'str'>

After Conversion:
Value: 100
Type: <class 'int'>
"""