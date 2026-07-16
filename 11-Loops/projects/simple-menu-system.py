# ==========================================================
# Project: Simple Menu System
# ==========================================================
# Description:
# This program displays a simple text-based menu that allows
# the user to choose from several options. The menu continues
# to appear until the user selects the Exit option.
#
# Concepts Practiced:
# - Variables
# - Input and Output
# - Type Conversion
# - while Loop
# - Conditional Statements
# - break Statement
# ==========================================================

print("=== Simple Menu System ===")

# Keep displaying the menu until the user chooses to exit
while True:
    print("\nMenu")
    print("1. Say Hello")
    print("2. Display Numbers 1 to 5")
    print("3. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        print("\nHello! Welcome to the program.")

    elif choice == 2:
        print()

        for number in range(1, 6):
            print(number)

    elif choice == 3:
        print("\nExiting the program...")
        break

    else:
        print("\nInvalid choice. Please try again.")

print("Program terminated.")