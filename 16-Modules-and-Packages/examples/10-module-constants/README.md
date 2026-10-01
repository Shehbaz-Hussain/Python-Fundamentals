# Module Constants

This example demonstrates how constants provided by Python's built-in `math` module can be accessed through a module namespace.

## Files

```text
10-module-constants/
├── README.md
└── module_constants.py
```

## Example

The program imports the `math` module:

```text
import math
```

It then accesses constants through the module namespace:

```text
math.pi
math.tau
```

`math.pi` represents the mathematical constant π, while `math.tau` represents τ, which is equal to `2π`.

## Key Concept

Modules can provide values in addition to functions and classes.

When using:

```text
import math
```

the constants remain associated with the `math` namespace. They are accessed using dot notation:

```text
math.pi
math.tau
```

This makes it clear where the values originate.

## Example Code

```text
import math


radius = 5

area = math.pi * radius**2
circle_ratio = math.tau

print(f"Radius: {radius}")
print(f"Pi: {math.pi}")
print(f"Circle area: {area:.2f}")
print(f"Tau: {circle_ratio}")
```

## Expected Output

```text
Radius: 5
Pi: 3.141592653589793
Circle area: 78.54
Tau: 6.283185307179586
```

## Learning Objective

After completing this example, you should understand how to:

* Import a standard-library module
* Access module-level constants
* Use dot notation with module namespaces
* Distinguish module-provided values from locally defined variables
* Use constants from Python's `math` module in calculations
