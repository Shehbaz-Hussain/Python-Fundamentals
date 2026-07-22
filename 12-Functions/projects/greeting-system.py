"""
Project: Greeting System

Description:
This project demonstrates how to create and use functions with
parameters and default arguments. The program greets users
based on the information they provide.
"""


def greet_user(name, greeting="Hello"):
    """Display a personalized greeting."""
    print(f"{greeting}, {name}!")


def main():
    """Run the greeting system."""
    user_name = input("Enter your name: ")

    print("\nDefault Greeting:")
    greet_user(user_name)

    custom_greeting = input("\nEnter a custom greeting: ")

    print("\nCustom Greeting:")
    greet_user(user_name, custom_greeting)


main()