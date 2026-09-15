# Importing Modules

## Overview

Python programs are commonly divided into modules so that functionality can be reused across different parts of an application.

The `import` statement provides access to a module's functionality.

For example:

```python
import math
```

After importing `math`, its functions, constants, and other available names can be accessed through the module namespace:

```python
print(math.sqrt(25))
print(math.pi)
```

Understanding how imports work is essential for writing organized Python programs.

---

## Basic Import Syntax

The simplest form of importing a module is:

```python
import module_name
```

For example:

```python
import math
```

The module can then be accessed using its name:

```python
result = math.sqrt(49)

print(result)
```

Output:

```text
7.0
```

The `math` name is available in the current namespace after the import.

---

## Importing Multiple Modules

Multiple modules can be imported with separate import statements:

```python
import math
import statistics
import json
```

This style is generally clear because each dependency is immediately visible.

It is also possible to write:

```python
import math, statistics, json
```

However, separate import statements are generally preferred because they are easier to read and maintain.

---

## Accessing Names Through a Module

When using:

```python
import math
```

the names provided by the `math` module are accessed through `math`.

For example:

```python
import math

print(math.sqrt(64))
print(math.ceil(4.2))
print(math.floor(4.8))
```

The module name acts as a namespace boundary.

This makes the origin of each name clear.

For example:

```python
math.sqrt()
```

clearly indicates that `sqrt()` comes from the `math` module.

---

## Importing a Custom Module

Modules do not have to come from Python's standard library.

Suppose a project contains:

```text
project/
├── main.py
└── calculations.py
```

The `calculations.py` module contains:

```python
def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b
```

The `main.py` file can import the module:

```python
import calculations

print(calculations.add(10, 5))
print(calculations.multiply(4, 3))
```

The importing file accesses the functions through the `calculations` namespace.

---

## What Happens During an Import?

An import involves more than making a filename available.

When Python processes an import, it uses its import system to locate the requested module.

Conceptually, the process involves:

1. Resolving the module name.
2. Finding the corresponding module.
3. Creating and initializing the module when necessary.
4. Executing the module's top-level code.
5. Making the module available to the importing code.
6. Caching the loaded module in `sys.modules`.

For example:

```python
import settings
```

can cause top-level statements in `settings.py` to execute during the first import.

This behavior is important when designing modules because unnecessary side effects at module level can make imports unpredictable.

---

## Imports Create Namespace Bindings

Consider:

```python
import math
```

The name `math` becomes bound in the current namespace to the imported module.

The function is then accessed as:

```python
math.sqrt(25)
```

This differs from:

```python
from math import sqrt
```

which binds `sqrt` directly in the current namespace.

Therefore:

```python
import math

math.sqrt(25)
```

and:

```python
from math import sqrt

sqrt(25)
```

use different namespace arrangements.

The details of `from ... import ...` are covered separately.

---

## Importing the Same Module More Than Once

Python normally caches successfully imported modules in `sys.modules`.

For example:

```python
import math
import math
```

does not normally initialize the module twice.

The second import generally reuses the existing module object from the import system's cache.

This behavior is useful for both performance and consistency within a Python process.

---

## Import Order

Imports are normally placed near the beginning of a Python file.

For example:

```python
import json
import math
from pathlib import Path

from application.config import settings
```

Keeping imports near the top makes dependencies easy to identify.

A common organization is:

1. Standard library imports
2. Third-party package imports
3. Local application imports

For example:

```python
import json
from pathlib import Path

import numpy as np

from application.preprocessing import normalize_data
```

This structure improves readability in larger projects.

---

## Standard Library Imports

Python provides many modules without requiring separate installation.

For example:

```python
import json
from pathlib import Path
import statistics
```

These modules belong to Python's standard library.

Example:

```python
import statistics

scores = [72, 81, 90, 87, 76]

average = statistics.mean(scores)

print(average)
```

No third-party package installation is required for this example.

---

## Third-Party Imports

Third-party packages are distributed separately from Python itself.

For example, a project may use NumPy:

```python
import numpy as np
```

or pandas:

```python
import pandas as pd
```

These packages normally need to be installed in the relevant Python environment before they can be imported.

For example:

```bash
python -m pip install numpy
```

After installation:

```python
import numpy as np

values = np.array([10, 20, 30])

print(values.mean())
```

The exact installation process depends on the project's environment and dependency management approach.

---

## Local Imports

A project can import its own modules.

Suppose:

```text
student_app/
├── main.py
├── students.py
└── validation.py
```

`validation.py`:

```python
def is_valid_age(age: int) -> bool:
    return 0 <= age <= 120
```

`main.py`:

```python
import validation

age = 21

if validation.is_valid_age(age):
    print("Valid age")
```

Here, `validation` is a local module belonging to the application.

---

## Importing a Module Does Not Import Every Name Directly

With:

```python
import math
```

the importing namespace receives the name `math`.

It does not make every name inside `math` directly available.

For example:

```python
import math

print(math.sqrt(25))
```

works.

But this:

```python
import math

print(sqrt(25))
```

does not work because `sqrt` was not bound directly in the importing namespace.

If direct access to `sqrt` is desired, a different import form can be used:

```python
from math import sqrt

print(sqrt(25))
```

---

## Import Aliases

A module can be given a local alias during import:

```python
import statistics as stats
```

The module can then be accessed through `stats`:

```python
scores = [80, 85, 90]

print(stats.mean(scores))
```

Aliases are useful when:

* A module has a long name.
* A conventional alias is widely recognized.
* A name would otherwise conflict with another local name.

Common examples include:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

Aliases should be meaningful and used consistently.

---

## Importing Modules with Names That Conflict

Suppose a module contains:

```python
import statistics

statistics.mean([10, 20, 30])
```

Using the module namespace makes the source of `mean()` clear.

Compare that with:

```python
from statistics import mean

mean([10, 20, 30])
```

The second form is shorter but removes the module name from the call.

In larger codebases, explicit module-qualified names can improve readability when the origin of a function is important.

---

## Common Import Errors

Incorrect imports can result in errors.

### `ModuleNotFoundError`

For example:

```python
import nonexistent_module
```

may produce:

```text
ModuleNotFoundError: No module named 'nonexistent_module'
```

Possible causes include:

* The module does not exist.
* The module is not installed.
* The module is outside Python's import search path.
* The module name is misspelled.
* The wrong Python environment is being used.

---

### `ImportError`

An `ImportError` can occur when Python finds a module but cannot import the requested name.

For example:

```python
from math import nonexistent_function
```

can result in an import error because that name is not provided by `math`.

The distinction between `ModuleNotFoundError` and `ImportError` is useful when diagnosing import problems.

---

## Naming Conflicts

A local file can unintentionally shadow another module.

For example, creating:

```text
json.py
```

in a project that expects to use the standard library's `json` module can cause confusing import behavior.

Likewise, a file named:

```text
random.py
```

can interfere with code that intends to import Python's `random` module.

Avoid naming project modules after standard library modules or important third-party packages.

---

## Importing from the Wrong Environment

Third-party packages are installed into Python environments.

For example, a package may be installed in one virtual environment but the program may be executed with another Python interpreter.

This can lead to:

```text
ModuleNotFoundError
```

even though the package was previously installed.

For this reason, projects should use a clearly defined Python environment and dependency-management workflow.

---

## Circular Imports

A **circular import** occurs when modules depend on each other directly or indirectly.

For example:

```text
module_a.py
    imports module_b

module_b.py
    imports module_a
```

Circular dependencies can cause partially initialized modules and confusing import errors.

A simple example is:

```python
# module_a.py
import module_b
```

and:

```python
# module_b.py
import module_a
```

This design should generally be avoided.

A better solution is often to reorganize responsibilities so that shared functionality belongs in a separate module.

For example:

```text
common.py
module_a.py
module_b.py
```

Both modules can then depend on `common.py` rather than depending directly on each other.

---

## Best Practices

### 1. Prefer Explicit Imports

Use:

```python
import math
```

or:

```python
from math import sqrt
```

instead of:

```python
from math import *
```

Explicit imports make dependencies easier to understand.

### 2. Keep Imports Organized

Place imports near the beginning of the module and group them logically.

### 3. Avoid Unnecessary Imports

Only import functionality that the module actually uses.

### 4. Avoid Import Side Effects

Reusable modules should avoid unexpected actions during import.

### 5. Use Meaningful Aliases

Prefer established aliases such as:

```python
import numpy as np
```

rather than arbitrary aliases that reduce readability.

### 6. Avoid Circular Dependencies

Organize modules around clear responsibilities and dependency relationships.

### 7. Do Not Solve Poor Organization with Path Manipulation

Manually modifying `sys.path` can sometimes be useful for specialized situations, but it should not normally be the primary solution to a poorly structured project.

Proper package and project organization is usually preferable.

---

## Key Takeaways

* The `import` statement provides access to modules.
* `import module_name` binds the module name in the current namespace.
* Module functionality is normally accessed through the module namespace.
* Python can import standard-library, third-party, and project-local modules.
* Imported modules are normally cached in `sys.modules`.
* Importing a module can execute its top-level statements during initialization.
* `import module` and `from module import name` create different namespace bindings.
* Aliases can provide shorter or conventional local names.
* `ModuleNotFoundError` and `ImportError` commonly indicate different import problems.
* Poor naming can cause module shadowing.
* Circular imports should generally be avoided through better module organization.
* Clear, explicit imports improve maintainability and readability.
