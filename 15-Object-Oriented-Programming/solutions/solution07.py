"""
Solution 07: Update Object State

Implements exercise07 by creating a BankAccount class and
updating its balance through an instance method.
"""


class BankAccount:
    """Represent a bank account."""

    def __init__(self, owner, balance):
        """Initialize a bank account."""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add an amount to the account balance."""
        self.balance += amount

    def display_balance(self):
        """Display the account owner and current balance."""
        print(f"Owner: {self.owner}")
        print(f"Balance: ${self.balance:.2f}")


account = BankAccount("Ali", 1000)

account.deposit(500)
account.display_balance()