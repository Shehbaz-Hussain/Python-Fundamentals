# Import Module

This example demonstrates the basic `import` statement in Python.

## Files

```text
01-import-module/
├── README.md
└── import_module.py
```

## Example

The Python file imports the `math` module:

```text
import math

radius = 5

area = math.pi * radius**2

print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
```

## Key Concept

The statement:

```text
import math
```

imports the `math` module and makes the name `math` available in the current module's namespace.

Members of the imported module are accessed using dot notation:

```text
math.pi
```

For example:

```text
area = math.pi * radius**2
```

The `math` prefix makes it clear that `pi` belongs to the `math` module.

## Expected Output

```text
Radius: 5
Area: 78.54
```

## Learning Objective

After completing this example, you should understand how to:

* Import a Python module
* Access module members using dot notation
* Use functionality provided by the standard library
* Keep imported names organized under a module namespace
