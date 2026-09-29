# From Import

This example demonstrates how to import a specific function from a Python module using the `from ... import ...` syntax.

## Files

```text
02-from-import/
├── README.md
└── from_import.py
```

## Example

The Python file imports `sqrt` directly from the `math` module:

```text
from math import sqrt


number = 144

result = sqrt(number)

print(f"Number: {number}")
print(f"Square root: {result}")
```

## Key Concept

The statement:

```text
from math import sqrt
```

imports the `sqrt` name from the `math` module into the current module's namespace.

The function can then be called directly:

```text
sqrt(144)
```

Instead of using:

```text
math.sqrt(144)
```

This is different from:

```text
import math
```

where the module name must be used to access its members.

## Expected Output

```text
Number: 144
Square root: 12.0
```

## Learning Objective

After completing this example, you should understand how to:

* Use `from ... import ...`
* Import a specific function from a module
* Call an imported function directly
* Distinguish `from module import name` from `import module`
