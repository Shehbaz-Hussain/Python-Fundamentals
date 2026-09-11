"""
Project 02: Banking System

Description:
    Demonstrates instance attributes, instance methods, object
    state, state modification, and basic validation.
"""


class BankAccount:
    """Represent a bank account."""

    def __init__(self, account_number, owner, balance):
        """Initialize a bank account."""
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.balance += amount
        print(f"${amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        """Withdraw money when the amount is valid."""
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        if amount > self.balance:
            print("Insufficient funds.")
            return

        self.balance -= amount
        print(f"${amount:.2f} withdrawn successfully.")

    def display_balance(self):
        """Display account information."""
        print(f"Account Number: {self.account_number}")
        print(f"Owner: {self.owner}")
        print(f"Balance: ${self.balance:.2f}")


account1 = BankAccount(
    "ACC-1001",
    "Ali",
    5000,
)

account2 = BankAccount(
    "ACC-1002",
    "Ayesha",
    3000,
)

print("Banking System")
print("=" * 35)

print("\nInitial Account Information")
print("-" * 35)

account1.display_balance()
print()
account2.display_balance()

print("\nTransactions")
print("-" * 35)

account1.deposit(1000)
account1.withdraw(500)

account2.deposit(500)
account2.withdraw(10000)

print("\nTesting Invalid Transactions")
print("-" * 35)

account1.deposit(0)
account1.withdraw(-100)

print("\nFinal Account Information")
print("-" * 35)

account1.display_balance()
print()
account2.display_balance()