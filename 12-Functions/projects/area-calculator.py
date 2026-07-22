"""
Project: Area Calculator

Description:
This project demonstrates how functions can be used to calculate
the areas of different geometric shapes.
"""


def calculate_rectangle_area(length, width):
    """Return the area of a rectangle."""
    return length * width


def calculate_square_area(side):
    """Return the area of a square."""
    return side * side


def calculate_circle_area(radius):
    """Return the area of a circle."""
    return 3.14159 * radius * radius


def main():
    """Run the area calculator."""
    print("Area Calculator")
    print("---------------")

    length = float(input("Enter the rectangle length: "))
    width = float(input("Enter the rectangle width: "))
    rectangle_area = calculate_rectangle_area(length, width)

    side = float(input("\nEnter the square side length: "))
    square_area = calculate_square_area(side)

    radius = float(input("\nEnter the circle radius: "))
    circle_area = calculate_circle_area(radius)

    print("\nAreas")
    print("-----")
    print(f"Rectangle Area: {rectangle_area:.2f}")
    print(f"Square Area: {square_area:.2f}")
    print(f"Circle Area: {circle_area:.2f}")


main()