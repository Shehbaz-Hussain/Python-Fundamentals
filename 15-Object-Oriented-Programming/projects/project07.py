"""
Project 07: Shopping Cart System

Description:
    Demonstrates composition by allowing a ShoppingCart object
    to contain and collaborate with Product objects.
"""


class Product:
    """Represent a product."""

    def __init__(self, name, price):
        """Initialize a product."""
        self.name = name
        self.price = price

    def display_info(self):
        """Display product information."""
        print(f"{self.name}: ${self.price:.2f}")


class ShoppingCart:
    """Represent a shopping cart containing products."""

    def __init__(self):
        """Initialize an empty shopping cart."""
        self.products = []

    def add_product(self, product):
        """Add a product to the cart."""
        self.products.append(product)
        print(f"{product.name} added to the cart.")

    def remove_product(self, product):
        """Remove a product from the cart."""
        if product in self.products:
            self.products.remove(product)
            print(f"{product.name} removed from the cart.")
        else:
            print(f"{product.name} is not in the cart.")

    def display_cart(self):
        """Display all products in the cart."""
        if not self.products:
            print("The shopping cart is empty.")
            return

        print("Shopping Cart")

        for product in self.products:
            product.display_info()

    def calculate_total(self):
        """Calculate the total price of all products."""
        total = 0

        for product in self.products:
            total += product.price

        return total


product1 = Product("Laptop", 1200)
product2 = Product("Keyboard", 80)
product3 = Product("Mouse", 40)

cart = ShoppingCart()

print("Shopping Cart System")
print("=" * 40)

cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

print()

cart.display_cart()

print("=" * 40)
print(f"Total: ${cart.calculate_total():.2f}")

print("\nRemoving Mouse")
print("=" * 40)

cart.remove_product(product3)

cart.display_cart()

print("=" * 40)
print(f"Updated Total: ${cart.calculate_total():.2f}")