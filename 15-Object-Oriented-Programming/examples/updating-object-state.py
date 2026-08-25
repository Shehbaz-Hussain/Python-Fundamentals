"""
Topic: Updating Object State

Description:
Demonstrates how instance methods can update the state of
an object by modifying its instance attributes.
"""


class BankAccount:
    """Represent a simple bank account."""

    def __init__(self, owner, balance):
        """Initialize an account with an owner and balance."""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add an amount to the account balance."""
        self.balance += amount

    def withdraw(self, amount):
        """Subtract an amount from the account balance."""
        self.balance -= amount

    def display_balance(self):
        """Display the current account balance."""
        print(f"Owner: {self.owner}")
        print(f"Balance: ${self.balance:.2f}")


account = BankAccount("Ali", 1000)

account.display_balance()

account.deposit(500)
account.withdraw(200)

print("\nAfter updating account state:")
account.display_balance()