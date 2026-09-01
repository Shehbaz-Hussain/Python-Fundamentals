"""
Solution 12: Encapsulation

Implements exercise12 by using a public owner attribute and
a non-public _balance attribute with methods that control
access to the account balance.
"""


class BankAccount:
    """Represent a bank account."""

    def __init__(self, owner, balance):
        """Initialize a bank account."""
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        """Add a positive amount to the account balance."""
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        """Return the current account balance."""
        return self._balance


account = BankAccount("Ali", 1000)

account.deposit(500)

print(f"Owner: {account.owner}")
print(f"Balance: ${account.get_balance():.2f}")