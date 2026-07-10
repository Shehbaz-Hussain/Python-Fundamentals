# Example 12: Short-Circuit Evaluation
# This program demonstrates how Python performs
# short-circuit evaluation with logical operators.

print("Short-Circuit Evaluation Demonstration")

print()

# Example 1
print("Example 1: AND Operator")
print("Expression: False and True")
print("Result:", False and True)

print()

# Example 2
print("Example 2: OR Operator")
print("Expression: True or False")
print("Result:", True or False)

print()

# Example 3
number = 10

print("Example 3")
print("Number:", number)
print("Expression: number > 0 and number < 100")
print("Result:", number > 0 and number < 100)

print()

# Example 4
temperature = 40

print("Example 4")
print("Temperature:", temperature)
print("Expression: temperature < 0 or temperature > 35")
print("Result:", temperature < 0 or temperature > 35)

print()

print("Note:")
print("Python stops evaluating a logical expression")
print("as soon as the final result is determined.")


# Expected Output:

# Short-Circuit Evaluation Demonstration

# Example 1: AND Operator
# Expression: False and True
# Result: False

# Example 2: OR Operator
# Expression: True or False
# Result: True

# Example 3
# Number: 10
# Expression: number > 0 and number < 100
# Result: True

# Example 4
# Temperature: 40
# Expression: temperature < 0 or temperature > 35
# Result: True

# Note:
# Python stops evaluating a logical expression
# as soon as the final result is determined.