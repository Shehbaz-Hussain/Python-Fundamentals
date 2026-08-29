"""
Exercise 12: Encapsulation

Problem:
Create a Python class named BankAccount that demonstrates
encapsulation by controlling access to an account balance.

Requirements:
1. Define a class named BankAccount.
2. Define an __init__() method that accepts owner and balance.
3. Store owner as a public instance attribute named owner.
4. Store balance as a non-public instance attribute named
   _balance.
5. Define a method named deposit() that accepts an amount.
6. The deposit() method should increase _balance only when
   the amount is greater than zero.
7. Define a method named get_balance() that returns _balance.
8. Create a BankAccount object for "Ali" with a balance of 1000.
9. Deposit 500 into the account.
10. Display the owner's name and updated balance.

Expected Behavior:
The program should display:

Owner: Ali
Balance: $1500.00
"""