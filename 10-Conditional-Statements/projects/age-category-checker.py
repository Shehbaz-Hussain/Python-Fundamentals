"""
Project: Age Category Checker

Description:
This program asks the user to enter their age and determines
which age category they belong to using conditional statements.

Concepts Used:
- input()
- int()
- if
- elif
- else
- Comparison operators
- Logical flow

Categories:
0–12   : Child
13–19  : Teenager
20–59  : Adult
60+    : Senior Citizen
Negative age : Invalid
"""

print("===== Age Category Checker =====")

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age. Age cannot be negative.")

elif age <= 12:
    print("Category: Child")

elif age <= 19:
    print("Category: Teenager")

elif age <= 59:
    print("Category: Adult")

else:
    print("Category: Senior Citizen")