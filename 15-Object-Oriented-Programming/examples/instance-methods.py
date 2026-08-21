"""
Topic: Instance Methods

Description:
Demonstrates how an instance method operates on the data belonging
to a particular object.
"""


class BankAccount:
    """Represent a simple bank account."""

    def set_details(self, owner, balance):
        """Set the account owner's name and initial balance."""
        self.owner = owner
        self.balance = balance

    def display_balance(self):
        """Display the current account balance."""
        print(f"{self.owner}'s balance: ${self.balance:.2f}")


account = BankAccount()
account.set_details("Ali", 1500.00)

account.display_balance()