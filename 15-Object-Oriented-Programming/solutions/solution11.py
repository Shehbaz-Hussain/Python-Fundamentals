"""
Solution 11: Static Method

Implements exercise11 by defining a static method that checks
whether a Celsius temperature is at or below freezing.
"""


class Temperature:
    """Provide temperature-related utility behavior."""

    @staticmethod
    def is_freezing(celsius):
        """Return True when the temperature is at or below 0°C."""
        return celsius <= 0


temperatures = [-5, 10]

for temperature in temperatures:
    if Temperature.is_freezing(temperature):
        print(f"{temperature}°C is freezing.")
    else:
        print(f"{temperature}°C is not freezing.")