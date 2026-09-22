# Import Syntax

## Overview

The `import` statement loads a module and binds it to a name in the current namespace.

Basic syntax:

```python
import module_name
```

The imported module can then be accessed through its module name.

---

## Basic Import

```python
import math

result = math.sqrt(25)

print(result)
```

Output:

```text
5.0
```

The module name `math` becomes available in the current namespace.

---

## Import Multiple Modules

Multiple modules can be imported with separate statements:

```python
import math
import json
import pathlib
```

This is generally clearer than combining unrelated modules into one statement.

---

## Import Multiple Modules in One Statement

Python also allows:

```python
import math, json
```

However, separate import statements are usually preferred for readability:

```python
import math
import json
```

---

## Import a Custom Module

Suppose the project contains:

```text
project/
├── main.py
└── calculator.py
```

`calculator.py`:

```python
def add(first: int, second: int) -> int:
    return first + second
```

`main.py`:

```python
import calculator

result = calculator.add(10, 5)

print(result)
```

The module is accessed through:

```python
calculator.add()
```

---

## Import a Package

A package can also be imported:

```python
import utilities
```

If a submodule is required:

```python
import utilities.formatting
```

It can then be accessed using the package hierarchy:

```python
utilities.formatting.format_name()
```

---

## Import a Nested Module

For a package structure such as:

```text
project/
└── application/
    ├── __init__.py
    └── utilities/
        ├── __init__.py
        └── formatting.py
```

the nested module can be imported with:

```python
import application.utilities.formatting
```

---

## Accessing Imported Names

After:

```python
import math
```

use:

```python
math.sqrt(16)
math.pi
```

The module namespace keeps the imported names grouped under `math`.

---

## Importing a Module with an Alias

The `as` keyword assigns an alternate local name:

```python
import math as mathematics
```

Then:

```python
result = mathematics.sqrt(25)

print(result)
```

Aliases are useful when a module has a long name or when a project follows an established naming convention.

---

## Syntax Pattern

```python
import module_name as alias
```

Example:

```python
import statistics as stats

average = stats.mean([10, 20, 30])

print(average)
```

---

## Importing Multiple Aliased Modules

```python
import numpy as np
import pandas as pd
```

This style is common in data-science and AI projects when it follows the conventions of the libraries being used.

---

## Importing Without an Alias

The normal form is:

```python
import module_name
```

Example:

```python
import json

data = json.loads('{"name": "Aisha"}')

print(data)
```

---

## Important Rule

`import` imports the module, not individual names from that module.

For example:

```python
import math
```

requires:

```python
math.sqrt(25)
```

If you want `sqrt` directly in the current namespace, use:

```python
from math import sqrt
```

That is covered in the `from-import` syntax reference.

---

## Common Mistakes

### Incorrect Module Name

```python
import maths
```

If no module named `maths` exists, Python raises an import error.

### Incorrect Alias Usage

```python
import math as mathematics

print(math.sqrt(25))
```

The local name is `mathematics`, so the correct code is:

```python
print(mathematics.sqrt(25))
```

### Importing a File with an Invalid Module Name

Avoid module names containing characters that do not follow Python identifier conventions.

Prefer:

```text
data_loader.py
```

instead of:

```text
data-loader.py
```

---

## Best Practices

* Use one clear import statement per module.
* Use aliases only when they improve readability or follow established conventions.
* Access imported functionality through the module namespace.
* Prefer meaningful module names.
* Avoid unnecessary aliases.
* Keep imports near the beginning of the file.
* Avoid wildcard imports.

---

## Quick Reference

```python
import module
```

```python
import module as alias
```

```python
import package.module
```

```python
import package.subpackage.module
```

### Example

```python
import math

radius = 5
area = math.pi * radius**2

print(area)
```
