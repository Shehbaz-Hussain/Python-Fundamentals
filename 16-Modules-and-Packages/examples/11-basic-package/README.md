# Basic Package

This example introduces the basic idea of organizing related Python modules inside a package.

## Files

```text
11-basic-package/
├── README.md
└── basic_package.py
```

## Example

The program imports the `sqrt` function from Python's built-in `math` module:

```text
from math import sqrt
```

It then uses the imported function to calculate the square root of a number.

## Key Concept

A **package** is a way to organize related Python modules into a structured directory.

For example, a larger project might eventually have a structure such as:

```text
my_package/
├── __init__.py
├── calculations.py
├── formatting.py
└── validation.py
```

Each `.py` file can contain related functionality, while the package provides a higher-level organizational structure.

This example uses Python's standard library to keep the focus on importing functionality. The next package examples build on this concept with actual package directories and package-specific imports.

## Example Code

```text
from math import sqrt


number = 144

result = sqrt(number)

print(f"Number: {number}")
print(f"Square root: {result}")
```

## Expected Output

```text
Number: 144
Square root: 12.0
```

## Learning Objective

After completing this example, you should understand:

* The purpose of Python packages
* How packages organize related modules
* The relationship between modules and packages
* How imported functionality can be used inside a Python program
* Why package organization becomes important as projects grow
