# Module Namespace

This example demonstrates how an imported module provides its own namespace.

## Files

```text
04-module-namespace/
├── README.md
└── module_namespace.py
```

## Example

The `math` module is imported:

```text
import math
```

Its members are accessed through the module name:

```text
math.sqrt(number)
math.floor(8.9)
```

The module name acts as a namespace that identifies where these names come from.

## Key Concept

A namespace is a mapping between names and the objects those names refer to.

When you write:

```text
math.sqrt(number)
```

`math` refers to the imported module, and `sqrt` refers to a function provided by that module.

This keeps related names grouped under the module namespace.

For example:

```text
import math

print(math.sqrt(25))
```

The name `sqrt` is not introduced directly into the current namespace by this import.

## Why Namespaces Matter

Namespaces help prevent unrelated names from interfering with one another.

Using:

```text
import math

math.sqrt(25)
```

is different from:

```text
from math import sqrt

sqrt(25)
```

The first approach keeps the module name visible at the call site, which can make the origin of the function clearer.

## Expected Output

```text
Number: 25
Square root: 5.0
Floor value: 8
```

## Learning Objective

After completing this example, you should understand:

* What a module namespace represents
* How imported modules provide access to their members
* How dot notation accesses names within a module
* Why namespaces help organize names in Python
