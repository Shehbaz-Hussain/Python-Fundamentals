# From Import Syntax

## Overview

The `from ... import ...` statement imports specific names from a module or package.

Basic syntax:

```python
from module_name import name
```

Unlike:

```python
import module_name
```

the imported name can be accessed directly without using the module name.

---

## Basic Syntax

```python
from math import sqrt

result = sqrt(25)

print(result)
```

Output:

```text
5.0
```

Here, only `sqrt` is imported into the current namespace.

---

## Import Multiple Names

Multiple names can be imported from the same module:

```python
from math import sqrt, floor, ceil

print(sqrt(25))
print(floor(4.8))
print(ceil(4.2))
```

This can be useful when several specific functions are required.

---

## Separate Imports

For readability, imports can also be written separately:

```python
from math import sqrt
from math import floor
from math import ceil
```

Both forms are valid.

When several names come from the same module, grouping them is often more concise:

```python
from math import sqrt, floor, ceil
```

---

## Importing a Constant

Names imported with `from ... import ...` are not limited to functions.

For example:

```python
from math import pi

radius = 5
area = pi * radius**2

print(area)
```

---

## Importing a Class

A class can be imported directly:

```python
from pathlib import Path

path = Path("data.txt")

print(path)
```

The class can then be used directly:

```python
Path("data.txt")
```

instead of:

```python
pathlib.Path("data.txt")
```

---

## Importing a Custom Function

Suppose:

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
from calculator import add

result = add(10, 5)

print(result)
```

Output:

```text
15
```

---

## Importing Multiple Custom Names

If a module contains:

```python
def add(first: int, second: int) -> int:
    return first + second


def subtract(first: int, second: int) -> int:
    return first - second
```

another module can import both:

```python
from calculator import add, subtract

print(add(10, 5))
print(subtract(10, 5))
```

---

## Importing with an Alias

The `as` keyword can assign an alternate local name:

```python
from math import sqrt as square_root

print(square_root(36))
```

The imported name is now:

```python
square_root
```

rather than:

```python
sqrt
```

---

## Syntax Pattern

```python
from module_name import name as alias
```

Example:

```python
from statistics import mean as average

values = [10, 20, 30]

print(average(values))
```

---

## Importing from a Package

For a package:

```text
project/
└── utilities/
    ├── __init__.py
    └── formatting.py
```

you can import a name from the submodule:

```python
from utilities.formatting import format_name
```

Then use:

```python
format_name("Aisha")
```

---

## Importing from a Nested Package

For example:

```text
project/
└── application/
    ├── __init__.py
    └── utilities/
        ├── __init__.py
        └── formatting.py
```

A function can be imported with:

```python
from application.utilities.formatting import format_name
```

---

## Importing Several Names from a Nested Module

```python
from application.utilities.formatting import format_name, normalize_name
```

This allows both functions to be used directly.

---

## Difference from `import`

Using:

```python
import math

result = math.sqrt(25)
```

keeps the name grouped under the `math` namespace.

Using:

```python
from math import sqrt

result = sqrt(25)
```

places `sqrt` directly in the current namespace.

The two forms therefore provide different namespace behavior.

---

## Namespace Considerations

Consider:

```python
from math import sqrt
```

Now:

```python
sqrt(25)
```

works directly.

However, if another imported module also provides a name called `sqrt`, the names can conflict.

Using:

```python
import math

math.sqrt(25)
```

makes the source of the function explicit.

This is one reason module-qualified imports can improve readability in larger applications.

---

## Avoiding Name Conflicts with Aliases

If two modules provide functions with the same name, aliases can prevent conflicts.

For example:

```python
from module_a import process as process_data
from module_b import process as process_text
```

Now both functions can be used clearly:

```python
process_data()
process_text()
```

---

## Importing a Module's Class

Example:

```python
from datetime import datetime

current_time = datetime.now()

print(current_time)
```

The imported class is used directly.

---

## Importing from `__init__.py`

A package can expose selected names through its `__init__.py`.

For example:

```text
utilities/
├── __init__.py
└── formatting.py
```

`__init__.py`:

```python
from .formatting import format_name
```

Another module may then use:

```python
from utilities import format_name
```

This allows a package to define a simpler public interface.

---

## Wildcard Imports

Python allows:

```python
from math import *
```

This imports names according to the module's export rules.

However, wildcard imports are generally discouraged in application code because they make it difficult to determine where names came from.

Prefer:

```python
from math import sqrt, pi
```

or:

```python
import math
```

---

## Importing a Name That Does Not Exist

If the requested name is unavailable:

```python
from math import calculate_average
```

Python raises an `ImportError`.

The module itself may exist, but the requested name does not exist in the expected location.

---

## Circular Import Considerations

`from ... import ...` does not eliminate circular-import problems.

For example:

```python
# module_a.py
from module_b import function_b
```

and:

```python
# module_b.py
from module_a import function_a
```

can still create a circular dependency.

Good package design should avoid unnecessary circular dependencies.

---

## Common Mistakes

### 1. Using the Module Name After a Direct Import

If you write:

```python
from math import sqrt
```

then this is unnecessary:

```python
math.sqrt(25)
```

because `math` was not imported by that statement.

Use:

```python
sqrt(25)
```

instead.

---

### 2. Importing a Nonexistent Name

```python
from math import average
```

will fail because `math` does not provide a name called `average`.

---

### 3. Creating Name Conflicts

Avoid importing many similarly named functions from unrelated modules unless aliases make their roles clear.

---

### 4. Using Wildcard Imports

Avoid:

```python
from module import *
```

because it hides the origin of names.

---

## Best Practices

* Use `from ... import ...` when a specific name is needed directly.
* Use aliases when they improve clarity or prevent conflicts.
* Import only the names the module actually needs.
* Avoid wildcard imports.
* Keep imports explicit and readable.
* Prefer module-qualified imports when namespace clarity is more important.
* Check package documentation before importing names from a third-party package.
* Keep imports consistent throughout a project.

---

## Quick Reference

### Import One Name

```python
from math import sqrt
```

### Import Multiple Names

```python
from math import sqrt, floor, ceil
```

### Import with Alias

```python
from math import sqrt as square_root
```

### Import from a Package

```python
from utilities.formatting import format_name
```

### Import from a Nested Package

```python
from application.utilities.formatting import format_name
```

### Avoid

```python
from module import *
```

### Main Principle

```python
from module import name
```

makes `name` directly available in the current namespace.
