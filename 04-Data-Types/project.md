# Mini Project: Student Record Manager

## Problem Statement

Create a beginner-friendly program that stores student records using Python data types.

## Folder Structure

```text
student-record-manager/
├── main.py
└── README.md
```

## Implementation

```python
students = [
    {"name": "Amina", "age": 20, "courses": ["Math", "Science"], "active": True},
    {"name": "Bilal", "age": 21, "courses": ["English", "Art"], "active": False},
]

for student in students:
    print(student["name"], student["age"], student["courses"], student["active"])
```

## Explanation

This project uses:

- `list` to store multiple students
- `dict` to store each student's profile
- `str` for names
- `int` for ages
- `list` for courses
- `bool` for active status

## Possible Improvements

- add search by name
- add average GPA support
- save data to a file
- add sorting
