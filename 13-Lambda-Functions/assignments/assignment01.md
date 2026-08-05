# Module 13 - Lambda Functions Assignment 01

## Intermediate Level Assignment

**Python Programming Foundation**

**Module:** 13 - Lambda Functions  
**Difficulty:** Intermediate  
**Python Version:** 3.13+  

---

# Assignment Overview

This assignment is designed to strengthen practical understanding of:

- Lambda functions
- map()
- filter()
- sorted()
- key parameter
- Data transformation
- Data filtering
- Data ranking

You will solve realistic programming problems using functional programming techniques.

---

# Instructions

- Complete all problems using Python 3.13+.
- Use lambda functions wherever appropriate.
- Avoid unnecessary complexity.
- Write clean and readable code.
- Test your program with multiple inputs.
- Do not use external libraries.

---

# Problem 01: Student Score Transformer

Create a program that processes student marks.

Requirements:

- Store student marks in a list.
- Use `map()` with lambda to increase every student's marks by 5%.
- Display updated marks.

Example:

Input:

```python
[70, 80, 90]
```

Expected Output:

```python
[73.5, 84.0, 94.5]
```

---

# Problem 02: Product Price Calculator

A store wants to apply a discount.

Requirements:

- Store product prices.
- Use lambda with `map()`.
- Reduce every price by 10%.
- Display final prices.

Example:

Input:

```python
[1000, 2000, 3000]
```

Expected Output:

```python
[900, 1800, 2700]
```

---

# Problem 03: Employee Salary Filter

Create an employee salary filtering system.

Requirements:

- Store employee salaries.
- Use `filter()` with lambda.
- Display employees earning more than 50000.

Example:

Input:

```python
[30000, 60000, 80000, 45000]
```

Expected Output:

```python
[60000, 80000]
```

---

# Problem 04: Sort Products by Price

Create a product ranking program.

Requirements:

- Store products as dictionaries.
- Use `sorted()`.
- Sort products according to price.
- Use lambda as the key function.

Example:

```python
[
    {"name": "Laptop", "price": 90000},
    {"name": "Phone", "price": 50000}
]
```

Output:

Products sorted from lowest to highest price.

---

# Problem 05: Student Ranking System

Create a student ranking system.

Requirements:

- Store student names and marks.
- Use `sorted()`.
- Sort students by marks.
- Display highest scoring students first.

Example:

```python
[
    {"name": "Ali", "marks": 85},
    {"name": "Sara", "marks": 95}
]
```

---

# Problem 06: Temperature Converter

Create a temperature processing program.

Requirements:

- Store temperatures in Celsius.
- Use `map()` with lambda.
- Convert Celsius into Fahrenheit.

Formula:

```
Fahrenheit = (Celsius * 9/5) + 32
```

Example:

Input:

```python
[0, 25, 100]
```

Output:

```python
[32, 77, 212]
```

---

# Problem 07: Customer Data Filtering

Create a customer filtering system.

Requirements:

- Store customer records.
- Use `filter()`.
- Select customers whose purchases are greater than 10000.

Example:

```python
[
    {"name": "Ali", "purchase": 15000},
    {"name": "Sara", "purchase": 5000}
]
```

---

# Problem 08: Employee Performance Ranking

Create an employee ranking system.

Requirements:

- Store employee performance scores.
- Use `sorted()`.
- Rank employees from highest performance score to lowest.

Use:

- Lambda
- key parameter
- reverse=True

---

# Problem 09: Data Cleaning Pipeline

Create a simple data cleaning program.

Requirements:

Given a list:

```python
["Python", "", "AI", "", "Machine Learning"]
```

Use:

- `filter()`
- lambda

Remove empty values.

Expected output:

```python
["Python", "AI", "Machine Learning"]
```

---

# Problem 10: Sales Report Processor

Create a sales processing system.

Requirements:

- Store sales records.
- Use lambda functions.
- Calculate updated sales values.
- Filter successful sales.
- Sort sales records.

The program should:

- Transform data using map().
- Filter data using filter().
- Rank data using sorted().

---

# Learning Objectives

After completing this assignment, you should be able to:

- Apply lambda functions in practical programs.
- Transform data using map().
- Filter information using filter().
- Sort complex data using sorted().
- Use lambda functions with dictionaries.
- Build simple data processing pipelines.

---

# Submission Requirements

Submit:

- Python source file.
- Proper comments.
- Sample input.
- Sample output.
- Clean formatting.

---

# Challenge Extension

For additional practice:

1. Combine multiple lambda operations.
2. Create a complete mini data analysis workflow.
3. Replace repeated lambda expressions with normal functions where appropriate.

---