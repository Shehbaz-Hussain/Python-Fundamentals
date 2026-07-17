"""
Exercise 09: Body Mass Index (BMI) Category Checker

Problem Statement:
Write a Python program that asks the user to enter their weight (in kilograms)
and height (in meters). Calculate the Body Mass Index (BMI) and display the
appropriate BMI category.

BMI Formula:
BMI = weight / (height × height)

BMI Categories:
- Less than 18.5           -> Underweight
- 18.5 to 24.9             -> Normal Weight
- 25.0 to 29.9             -> Overweight
- 30.0 or above            -> Obese

Expected Output Examples:

Example 1:
Enter your weight (kg): 50
Enter your height (m): 1.70
Your BMI is: 17.30
BMI Category: Underweight

Example 2:
Enter your weight (kg): 68
Enter your height (m): 1.70
Your BMI is: 23.53
BMI Category: Normal Weight

Example 3:
Enter your weight (kg): 85
Enter your height (m): 1.70
Your BMI is: 29.41
BMI Category: Overweight
"""

# Ask the user to enter their weight
weight = float(input("Enter your weight (kg): "))

# Ask the user to enter their height
height = float(input("Enter your height (m): "))

# Calculate the Body Mass Index (BMI)
bmi = weight / (height * height)

# Display the calculated BMI
print("Your BMI is:", round(bmi, 2))

# Determine the BMI category
if bmi < 18.5:
    print("BMI Category: Underweight")
elif bmi < 25:
    print("BMI Category: Normal Weight")
elif bmi < 30:
    print("BMI Category: Overweight")
else:
    print("BMI Category: Obese")