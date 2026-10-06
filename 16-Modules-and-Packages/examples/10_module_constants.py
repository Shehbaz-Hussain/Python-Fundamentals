"""Define and use module-level constants."""

TAX_RATE = 0.08
CURRENCY = "USD"

subtotal = 125.00
total = subtotal * (1 + TAX_RATE)

print(f"Total: {CURRENCY} {total:.2f}")
