# Custom Module

This example demonstrates how to create a custom Python module and import reusable functions into another Python file.

## Files

```text
07-custom-module/
├── README.md
├── calculator.py
└── main.py
```

## `calculator.py`

The `calculator.py` file contains reusable functions:

```text
"""
Topic: Custom Module

Description:
Demonstrates how to create a custom Python module
and import it into another Python file.
"""


def add(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


def subtract(first_number, second_number):
    """Return the difference between two numbers."""
    return first_number - second_number
```

## `main.py`

Create a separate `main.py` file to import and use the custom module:

```text
"""
Topic: Using a Custom Module

Description:
Demonstrates how to import functions from a
custom Python module.
"""


import calculator


first_number = 20
second_number = 8

sum_result = calculator.add(first_number, second_number)
difference_result = calculator.subtract(first_number, second_number)

print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
```

## How It Works

Python files can be used as modules.

Here:

```text
calculator.py
```

is the custom module.

The statement:

```text
import calculator
```

imports that module into `main.py`.

Its functions are then accessed through the module namespace:

```text
calculator.add(first_number, second_number)
calculator.subtract(first_number, second_number)
```

The module does not need to be part of Python's standard library. A Python file in the appropriate import context can be imported as a module.

## Expected Output

```text
Sum: 28
Difference: 12
```

## Key Concept

A custom module is useful when related functionality should be separated from the main program.

Instead of placing every function in one large file, related functionality can be organized into focused modules.

In this example:

* `calculator.py` contains calculation functions.
* `main.py` uses those functions.
* `import calculator` makes the custom module available.

## Learning Objective

After completing this example, you should understand how to:

* Create a custom Python module
* Import a custom module
* Access functions through a module namespace
* Separate reusable functionality from program execution
