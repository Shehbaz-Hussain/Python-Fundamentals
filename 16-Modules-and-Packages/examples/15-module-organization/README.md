# Module Organization

This example demonstrates how related functionality can be grouped into a module using focused functions and a clear namespace.

## Files

```text
15-module-organization/
├── README.md
└── module_organization.py
```

## Key Concept

A well-organized module should group related functionality together.

Instead of placing every function in one large Python file, a project can separate functionality by responsibility.

For example:

```text
geometry/
├── __init__.py
├── circles.py
├── rectangles.py
└── triangles.py
```

The `circles.py` module could contain functions related specifically to circles.

## Example

This example contains two related functions:

```text
def calculate_circle_area(radius):
    ...


def calculate_circle_circumference(radius):
    ...
```

Both functions are responsible for circle calculations, making them appropriate candidates for the same module.

The program also imports the `math` module:

```text
import math
```

and uses `math.pi` for accurate calculations.

## Example Code

```text
"""
Topic: Module Organization

Description:
Demonstrates how related functionality can be grouped
inside a module and accessed through a clear module namespace.
"""


import math


def calculate_circle_area(radius):
    """Return the area of a circle."""
    return math.pi * radius**2


def calculate_circle_circumference(radius):
    """Return the circumference of a circle."""
    return 2 * math.pi * radius


radius = 5

area = calculate_circle_area(radius)
circumference = calculate_circle_circumference(radius)

print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
```

## Expected Output

```text
Radius: 5
Area: 78.54
Circumference: 31.42
```

## Organization Principles

When designing modules:

* Keep related functionality together.
* Give modules a clear responsibility.
* Avoid unnecessarily large modules.
* Use descriptive function and variable names.
* Minimize unrelated dependencies.
* Keep module-level side effects to a minimum.
* Design modules so their functionality can be reused.

## Learning Objective

After completing this example, you should understand how module organization can improve:

* Code readability
* Reusability
* Maintainability
* Separation of responsibilities
* Project scalability
