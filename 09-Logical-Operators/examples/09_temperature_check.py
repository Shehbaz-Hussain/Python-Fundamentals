# Example 09: Temperature Check
# This program checks whether the temperature
# is below the minimum limit or above the maximum limit.

temperature = float(input("Enter the temperature: "))

print()

print("Temperature:", temperature)

# Check whether the temperature is outside the normal range.
is_outside_range = temperature < 0 or temperature > 35

print("Temperature is outside the normal range:", is_outside_range)

# Display individual condition results.
print("Below 0°C:", temperature < 0)
print("Above 35°C:", temperature > 35)


# Sample Output 1:

# Enter the temperature: -5

# Temperature: -5.0
# Temperature is outside the normal range: True
# Below 0°C: True
# Above 35°C: False 

# Sample Output 2:

# Enter the temperature: 25

# Temperature: 25.0
# Temperature is outside the normal range: False
# Below 0°C: False
# Above 35°C: False

# Sample Output 3:

# Enter the temperature: 40

# Temperature: 40.0
# Temperature is outside the normal range: True
# Below 0°C: False
# Above 35°C: True