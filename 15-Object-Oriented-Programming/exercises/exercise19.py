"""
Exercise 19: Abstraction

Problem:
Create an abstract Payment class that defines a common
interface for different payment methods.

Requirements:
1. Import ABC and abstractmethod from the abc module.
2. Define an abstract class named Payment that inherits from ABC.
3. Define an abstract method named pay() that accepts amount.
4. Define a class named CashPayment that inherits from Payment.
5. Implement pay() in CashPayment.
6. Define a class named CardPayment that inherits from Payment.
7. Implement pay() in CardPayment.
8. Each implementation should display how the payment was made.
9. Create one CashPayment object and one CardPayment object.
10. Call pay() on both objects with an amount of 50.

Expected Behavior:
The program should display information similar to:

Paid $50.00 with cash.
Paid $50.00 with a card.

Important:
The Payment class should define the required interface but
should not provide a concrete implementation of pay().
"""