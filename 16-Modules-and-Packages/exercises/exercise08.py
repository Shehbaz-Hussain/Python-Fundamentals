"""Define a module constant for a 5% discount and apply it to 80."""

DISCOUNT_RATE = 0.05
price = 80
discounted_price = price * (1 - DISCOUNT_RATE)

print(f"Discounted price: {discounted_price:.2f}")
