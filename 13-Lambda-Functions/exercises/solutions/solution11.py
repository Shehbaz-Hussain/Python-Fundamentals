"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 11
Exercise Title: Applying map() with Lambda Functions
Difficulty: Intermediate

Objective:
    Practice using the built-in map() function together with a lambda function
    to convert a list of temperatures from Celsius to Fahrenheit. Store the
    converted values in a new list and display both the original and converted
    temperatures.

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create a list of temperatures in Celsius.
celsius_temperatures = [0, 15, 25, 30, 40]

# Convert Celsius temperatures to Fahrenheit using map() and a lambda function.
fahrenheit_temperatures = list(
    map(
        lambda temperature: (temperature * 9 / 5) + 32,
        celsius_temperatures,
    )
)

# Challenge: Round each Fahrenheit temperature to one decimal place.
rounded_fahrenheit = list(
    map(
        lambda temperature: round(temperature, 1),
        fahrenheit_temperatures,
    )
)

# Display the results.
print("Original Celsius:")
print(celsius_temperatures)

print("\nConverted Fahrenheit:")
print(rounded_fahrenheit)


"""
===============================================================================
Expected Output
===============================================================================

Original Celsius:
[0, 15, 25, 30, 40]

Converted Fahrenheit:
[32.0, 59.0, 77.0, 86.0, 104.0]

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A list of Celsius temperatures is created.
2. The map() function processes each temperature in the list.
3. A lambda function applies the Fahrenheit conversion formula:

       (temperature * 9 / 5) + 32

4. The map object is converted into a list using the list() constructor.
5. As an additional challenge, another map() function with a lambda expression
   rounds each Fahrenheit value to one decimal place.
6. The original Celsius list and the converted Fahrenheit list are displayed.

How the Lambda Expressions Work
-------------------------------

First lambda expression:

    lambda temperature: (temperature * 9 / 5) + 32

- Accepts one Celsius temperature.
- Applies the Fahrenheit conversion formula.
- Returns the converted value.

Second lambda expression:

    lambda temperature: round(temperature, 1)

- Accepts one Fahrenheit temperature.
- Rounds it to one decimal place.
- Returns the rounded value.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- map()
- Lists
- Return values
- Arithmetic operations
- Function invocation

===============================================================================
Time Complexity
===============================================================================

O(n)

Explanation:
Each call to map() processes every element in the list once. Since two map()
operations are performed sequentially, the overall time complexity remains O(n).

===============================================================================
Space Complexity
===============================================================================

O(n)

Explanation:
A new list is created to store the converted temperatures, and another list is
created for the rounded values.

===============================================================================
Best Practices
===============================================================================

- Use map() when applying the same transformation to every element.
- Keep lambda expressions short and focused on a single operation.
- Convert the map object to a list when the results need to be stored or
  displayed.
- Use descriptive variable names to improve code readability.

===============================================================================
Common Mistakes
===============================================================================

- Forgetting to convert the map object into a list.
- Using an incorrect Fahrenheit conversion formula.
- Omitting the lambda function when using map().
- Using a traditional for loop instead of map() for the conversion.
- Forgetting to round the values for the challenge.

===============================================================================
Alternative Approach
===============================================================================

Another valid implementation is to combine the conversion and rounding into a
single lambda expression:

    rounded_fahrenheit = list(
        map(
            lambda temperature: round((temperature * 9 / 5) + 32, 1),
            celsius_temperatures,
        )
    )

This produces the same output while performing both operations in one step.

===============================================================================
Real-World Relevance
===============================================================================

Using map() with lambda functions is common in:

- Data preprocessing
- Sensor data conversion
- Data transformation pipelines
- Scientific computing
- Machine learning data preparation

===============================================================================
Key Takeaways
===============================================================================

- map() applies a function to every element of an iterable.
- Lambda functions provide a concise way to define simple transformations.
- Converting a map object to a list makes the results easy to use and display.
- Combining map() with lambda functions is an efficient way to transform data.
===============================================================================
"""