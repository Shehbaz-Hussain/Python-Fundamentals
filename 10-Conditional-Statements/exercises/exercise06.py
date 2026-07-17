"""
Exercise 06: Leap Year Checker

Problem Statement:
Write a Python program that asks the user to enter a year and determines
whether it is a leap year or not.

Leap Year Rules:
1. A year is a leap year if it is divisible by 400.
2. If it is divisible by 100 but not by 400, it is NOT a leap year.
3. Otherwise, if it is divisible by 4, it is a leap year.
4. All other years are not leap years.

Example Output:

Example 1:
Enter a year: 2024
2024 is a leap year.

Example 2:
Enter a year: 1900
1900 is not a leap year.

Example 3:
Enter a year: 2000
2000 is a leap year.
"""

# Ask the user to enter a year
year = int(input("Enter a year: "))

# Check whether the year is a leap year
if year % 400 == 0:
    print(year, "is a leap year.")
elif year % 100 == 0:
    print(year, "is not a leap year.")
elif year % 4 == 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")