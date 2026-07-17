"""
Exercise 14: Simple ATM Withdrawal Checker

Problem Statement:
Write a Python program that asks the user to enter their account balance and
the amount they want to withdraw.

Withdrawal Rules:
- The withdrawal amount must be greater than 0.
- The withdrawal amount cannot exceed the available account balance.
- If the withdrawal is successful, display the remaining balance.
- Otherwise, display an appropriate message.

Expected Output Examples:

Example 1:
Enter your account balance: 5000
Enter the withdrawal amount: 1500
Withdrawal successful.
Remaining Balance: 3500.0

Example 2:
Enter your account balance: 2500
Enter the withdrawal amount: 3000
Transaction declined.
Reason: Insufficient balance.

Example 3:
Enter your account balance: 4000
Enter the withdrawal amount: -500
Transaction declined.
Reason: Invalid withdrawal amount.
"""

# Ask the user to enter the account balance
balance = float(input("Enter your account balance: "))

# Ask the user to enter the withdrawal amount
withdraw_amount = float(input("Enter the withdrawal amount: "))

# Check whether the withdrawal amount is valid
if withdraw_amount <= 0:
    print("Transaction declined.")
    print("Reason: Invalid withdrawal amount.")
elif withdraw_amount > balance:
    print("Transaction declined.")
    print("Reason: Insufficient balance.")
else:
    # Calculate the remaining balance
    remaining_balance = balance - withdraw_amount

    print("Withdrawal successful.")
    print("Remaining Balance:", remaining_balance)