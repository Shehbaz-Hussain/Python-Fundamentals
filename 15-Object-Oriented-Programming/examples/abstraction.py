"""
Topic: Abstraction

Description:
Demonstrates abstraction by defining a common interface
for different payment methods.
"""


from abc import ABC, abstractmethod


class Payment(ABC):
    """Define the interface for a payment method."""

    @abstractmethod
    def pay(self, amount):
        """Process a payment amount."""
        pass


class CashPayment(Payment):
    """Represent a cash payment."""

    def pay(self, amount):
        """Process a cash payment."""
        print(f"Paid ${amount:.2f} with cash.")


class CardPayment(Payment):
    """Represent a card payment."""

    def pay(self, amount):
        """Process a card payment."""
        print(f"Paid ${amount:.2f} with a card.")


cash_payment = CashPayment()
card_payment = CardPayment()

cash_payment.pay(50)
card_payment.pay(75)