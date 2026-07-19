"""
File: 12-Functions/examples/example16.py
Topic: Greeting Function

Description:
This example demonstrates how a function can generate a personalized
greeting message. The same function is called multiple times with
different arguments, showing how functions eliminate code repetition
and improve reusability.
"""


def greet_user(name):
    """
    Display a personalized greeting message.
    """
    print(f"Hello, {name}!")
    print("Welcome to the Python Programming Foundation course.")
    print("We hope you enjoy learning functions.")
    print()


# Call the function with different names
greet_user("Ali")
greet_user("Sara")
greet_user("Ahmed")