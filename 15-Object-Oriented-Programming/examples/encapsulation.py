"""
Topic: Encapsulation

Description:
Demonstrates Python's conventions for non-public attributes
and name mangling using a double underscore.
"""


class BankAccount:
    """Represent a bank account with encapsulated account data."""

    def __init__(self, owner, balance):
        """Initialize the account."""
        self.owner = owner
        self._balance = balance
        self.__account_number = "ACC-1001"

    def deposit(self, amount):
        """Add a valid amount to the account balance."""
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        """Return the current account balance."""
        return self._balance

    def display_account_number(self):
        """Display the account number through a class method."""
        print(f"Account Number: {self.__account_number}")


account = BankAccount("Ali", 1000)

print(f"Owner: {account.owner}")
print(f"Balance: ${account.get_balance():.2f}")

account.deposit(500)

print(f"Updated Balance: ${account.get_balance():.2f}")

account.display_account_number()