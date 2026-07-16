# ==========================================================
# Project: Pattern Printer
# ==========================================================
# Description:
# This program asks the user to enter the number of rows and
# prints different star patterns using nested loops.
#
# Concepts Practiced:
# - Variables
# - Input and Output
# - Type Conversion
# - for Loop
# - Nested Loops
# - range() Function
# ==========================================================

print("=== Pattern Printer ===")

# Ask the user to enter the number of rows
rows = int(input("Enter the number of rows: "))

print("\nRight-Angled Triangle:\n")

# Print a right-angled triangle
for row in range(1, rows + 1):
    for column in range(row):
        print("*", end="")
    print()

print("\nInverted Right-Angled Triangle:\n")

# Print an inverted right-angled triangle
for row in range(rows, 0, -1):
    for column in range(row):
        print("*", end="")
    print()

print("\nPattern printing completed.")