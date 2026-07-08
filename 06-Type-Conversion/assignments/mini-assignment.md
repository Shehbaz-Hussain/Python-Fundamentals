# Mini Assignment: Personal Expense Calculator

## Module Information

- **Module:** 06 – Type Conversion
- **Assignment Type:** Mini Project
- **Difficulty:** Beginner
- **Total Marks:** 30

---

# Objective

The objective of this mini assignment is to combine all type conversion
concepts learned in Module 06 and apply them in a practical real-world
scenario.

Students will create a simple expense calculator that accepts user input,
converts values into appropriate data types, performs calculations, and
displays formatted output.

---

# Background

Most real-world software applications collect information from users.

Examples:

- Banking applications collect transaction amounts.
- Shopping applications collect product prices.
- Finance applications calculate expenses.

Since user input is received as text, programs must convert this data into
appropriate types before processing.

---

# Project Title

## Personal Expense Calculator

---

# Tasks

Create a Python program that calculates a user's daily expenses.

The program should ask the user for:

1. User name
2. Food expense
3. Transport expense
4. Education expense
5. Other expense

---

# Program Requirements

Your program must:

## 1. Take User Input

Use:

```python
input()
```

to collect all required information.

---

## 2. Perform Type Conversion

Convert:

- Expense values into floating-point numbers using:

```python
float()
```

---

## 3. Calculate Total Expense

Use the formula:

```
Total Expense =
Food + Transport + Education + Other
```

---

## 4. Display Output

Display:

- User name
- Individual expenses
- Total expense
- Data type of each converted value

---

# Example Output

```
=================================
PERSONAL EXPENSE CALCULATOR
=================================

Enter your name: Ali

Enter food expense: 500
Enter transport expense: 200
Enter education expense: 300
Enter other expense: 100

========== EXPENSE REPORT ==========

Name: Ali

Food Expense: 500.0
Transport Expense: 200.0
Education Expense: 300.0
Other Expense: 100.0

Total Expense: 1100.0

Total Expense Type:
<class 'float'>
```

---

# Submission Requirements

Submit:

- Python source file:

```
personal-expense-calculator.py
```

The program should include:

- Comments explaining important steps.
- Meaningful variable names.
- Proper indentation.
- Clear output formatting.

---

# Expected Learning Outcomes

After completing this mini assignment, students should be able to:

- Understand why type conversion is required.
- Convert user input into numeric values.
- Use arithmetic operations with converted data.
- Apply `int()`, `float()`, `str()`, `bool()`, and `type()`.
- Build a small practical Python application.

---

# Marking Criteria

| Criteria | Marks |
|----------|------:|
| Correct use of input and conversion | 10 |
| Correct calculations | 8 |
| Code readability | 5 |
| Comments and documentation | 3 |
| Output formatting | 4 |
| **Total** | **30** |

---

# Practice Questions

1. Why must expense values be converted before addition?
2. What happens if strings are added using the `+` operator?
3. Why is `float()` better than `int()` for money values?
4. How can you verify the data type of total expense?
5. What type of data does `input()` return?
6. Explain the difference between `int()` and `float()`.
7. What happens when an empty string is converted using `bool()`?
8. Why is type conversion important in software development?

---

# Challenge Extension (Optional)

Without using advanced concepts, try to:

- Display a welcome message using the user's name.
- Display the total number of expense categories.
- Convert the user's name explicitly using `str()`.

---

# End of Mini Assignment