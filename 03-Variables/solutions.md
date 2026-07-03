# solutions.md

# Python Variables Solutions

This file contains complete solutions for all exercises in the variables module.

---

## Beginner Exercises

### Solution 1
**Exercise:** Create a variable named `name` and assign your name to it.

```python
name = "Alice"
print(name)
```

**Expected Output**
```python
Alice
```

**Explanation**
A variable named `name` is created and assigned the string value `"Alice"`.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

### Solution 2
**Exercise:** Print the value of a variable named `city`.

```python
city = "London"
print(city)
```

**Expected Output**
```python
London
```

**Explanation**
The variable `city` is assigned a value and printed.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

### Solution 3
**Exercise:** Create a variable `age` and store your age.

```python
age = 20
print(age)
```

**Expected Output**
```python
20
```

**Explanation**
The integer value `20` is stored in the variable `age`.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

### Solution 4
**Exercise:** Assign the value `100` to a variable named `score`.

```python
score = 100
print(score)
```

**Expected Output**
```python
100
```

**Explanation**
The variable `score` stores the integer value `100`.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

### Solution 5
**Exercise:** Print a variable containing a string value.

```python
message = "Hello"
print(message)
```

**Expected Output**
```python
Hello
```

**Explanation**
A string value is assigned to `message` and printed.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

### Solution 6
**Exercise:** Create two variables, `first_name` and `last_name`, and print both.

```python
first_name = "John"
last_name = "Doe"
print(first_name)
print(last_name)
```

**Expected Output**
```python
John
Doe
```

**Explanation**
Two separate variables are created and printed.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

### Solution 7
**Exercise:** Store `True` in a variable named `is_student`.

```python
is_student = True
print(is_student)
```

**Expected Output**
```python
True
```

**Explanation**
A boolean value is stored in a variable.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

### Solution 8
**Exercise:** Create a variable called `price` and assign `19.99`.

```python
price = 19.99
print(price)
```

**Expected Output**
```python
19.99
```

**Explanation**
A floating-point number is assigned to `price`.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

### Solution 9
**Exercise:** Assign `10` to `a` and `20` to `b`, then print both.

```python
a = 10
b = 20
print(a)
print(b)
```

**Expected Output**
```python
10
20
```

**Explanation**
Two variables are created and displayed separately.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

### Solution 10
**Exercise:** Create a variable called `message` and print it.

```python
message = "Welcome"
print(message)
```

**Expected Output**
```python
Welcome
```

**Explanation**
The variable `message` stores a string and prints it.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

## Intermediate Exercises

### Solution 1
**Exercise:** Store price and quantity and calculate total cost.

```python
price = 50
quantity = 3
total_cost = price * quantity
print(total_cost)
```

**Expected Output**
```python
150
```

**Explanation**
Variables hold the values needed for the calculation.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

### Solution 2
**Exercise:** Use multiple assignment.

```python
x, y, z = 1, 2, 3
print(x, y, z)
```

**Expected Output**
```python
1 2 3
```

**Explanation**
Multiple values are assigned to multiple variables in one line.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

### Solution 3
**Exercise:** Swap two variables.

```python
a = 5
b = 8
a, b = b, a
print(a, b)
```

**Expected Output**
```python
8 5
```

**Explanation**
The values are swapped using tuple unpacking.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

### Solution 4
**Exercise:** Calculate the area of a rectangle.

```python
length = 10
width = 5
area = length * width
print(area)
```

**Expected Output**
```python
50
```

**Explanation**
The area is computed using variable values.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

### Solution 5
**Exercise:** Print a sentence with name, age, and city.

```python
name = "Ava"
age = 22
city = "Berlin"
print(f"{name} is {age} years old and lives in {city}.")
```

**Expected Output**
```python
Ava is 22 years old and lives in Berlin.
```

**Explanation**
Variables are inserted into a formatted string.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

## Advanced Exercises

### Solution 1
**Exercise:** Build a small student information report.

```python
student_name = "Mina"
student_age = 20
student_grade = "A"
print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"Grade: {student_grade}")
```

**Expected Output**
```python
Name: Mina
Age: 20
Grade: A
```

**Explanation**
Variables store student-related information and print it in a structured format.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

### Solution 2
**Exercise:** Calculate final grade from subject scores.

```python
math = 90
science = 85
english = 88
final_grade = (math + science + english) / 3
print(final_grade)
```

**Expected Output**
```python
87.66666666666667
```

**Explanation**
The average of three variables is calculated.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

### Solution 3
**Exercise:** Simulate bank balance update.

```python
balance = 1000
deposit = 250
balance = balance + deposit
print(balance)
```

**Expected Output**
```python
1250
```

**Explanation**
The balance variable is updated after a deposit.

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

## Notes

- These solutions are simple and beginner-friendly.
- They demonstrate the core use of variables clearly.
- Additional improvements can be made for production-grade programs.
