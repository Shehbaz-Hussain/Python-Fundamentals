"""
Topic: Static Methods

Description:
Demonstrates how a static method works independently of
instance and class state.
"""


class Temperature:
    """Provide temperature-related utility behavior."""

    @staticmethod
    def is_freezing(celsius):
        """Return True if the temperature is at or below freezing."""
        return celsius <= 0


temperatures = [-5, 10, 0, 25]

for temperature in temperatures:
    result = Temperature.is_freezing(temperature)

    if result:
        print(f"{temperature}°C is freezing.")
    else:
        print(f"{temperature}°C is not freezing.")