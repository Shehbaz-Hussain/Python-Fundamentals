# From Import

## Overview

Python provides two common ways to import functionality from a module:

```python
import module_name
```

and:

```python
from module_name import name
```

The `from ... import ...` form allows specific names from a module to be bound directly in the current namespace.

For example:

```python
from math import sqrt

print(sqrt(25))
```

This differs from:

```python
import math

print(math.sqrt(25))
```

Both can use `sqrt()`, but they create different namespace bindings.

---

## Basic Syntax

The basic syntax is:

```python
from module_name import name
```

For example:

```python
from math import sqrt
```

After the import, `sqrt` can be used directly:

```python
result = sqrt(36)

print(result)
```

Output:

```text
6.0
```

The module name `math` does not need to be written when calling `sqrt()`.

---

## Importing Multiple Names

Multiple names can be imported from the same module:

```python
from math import sqrt, ceil, floor
```

They can then be used directly:

```python
print(sqrt(25))
print(ceil(4.2))
print(floor(4.8))
```

This can be useful when a module provides several specific functions that are needed by a file.

For readability, avoid importing a large number of unrelated names from a module unless there is a clear reason to do so.

---

## `import` vs `from ... import`

Consider:

```python
import math

result = math.sqrt(25)
```

The name `math` is bound in the current namespace.

With:

```python
from math import sqrt

result = sqrt(25)
```

the name `sqrt` is bound directly in the current namespace.

Conceptually:

```text
import math
    current namespace → math → sqrt

from math import sqrt
    current namespace → sqrt
```

The module itself still exists as the source of the imported object, but the name available for direct use differs.

---

## Why Use `from ... import`?

The `from ... import` form can make code shorter when only a few names are required.

For example:

```python
from statistics import mean

scores = [75, 80, 91, 88]

average = mean(scores)

print(average)
```

The alternative is:

```python
import statistics

scores = [75, 80, 91, 88]

average = statistics.mean(scores)

print(average)
```

Both are valid.

The appropriate choice depends on readability, naming clarity, and the surrounding code.

---

## Importing Functions

Functions are commonly imported directly.

Suppose a custom module contains:

```python
# calculations.py

def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b
```

Another file can import only `add`:

```python
from calculations import add

print(add(10, 5))
```

`multiply` is not bound directly by that import statement.

If both functions are needed:

```python
from calculations import add, multiply

print(add(10, 5))
print(multiply(4, 3))
```

---

## Importing Classes

Classes can also be imported with `from ... import`.

Suppose:

```python
# student.py

class Student:
    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> str:
        return f"My name is {self.name}."
```

Another file can write:

```python
from student import Student

student = Student("Shehbaz")

print(student.introduce())
```

The `Student` class is directly available in the importing namespace.

---

## Importing Constants

Module-level constants can also be imported.

For example:

```python
# settings.py

DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
```

Another module can import one constant:

```python
from settings import DEFAULT_TIMEOUT

print(DEFAULT_TIMEOUT)
```

Or multiple constants:

```python
from settings import DEFAULT_TIMEOUT, MAX_RETRIES

print(DEFAULT_TIMEOUT)
print(MAX_RETRIES)
```

Direct imports can be useful when the names are specific and unambiguous.

---

## Import Aliases with `as`

A name imported with `from ... import` can also be given an alias.

Syntax:

```python
from module_name import name as alias
```

Example:

```python
from statistics import mean as calculate_average

scores = [80, 85, 90]

print(calculate_average(scores))
```

Here, `calculate_average` is the local name used for the imported `mean` function.

Aliases should improve clarity rather than obscure the original API.

---

## Avoiding Name Conflicts

Direct imports can create naming conflicts.

Suppose two modules both provide a function called `format_data`:

```python
from module_a import format_data
from module_b import format_data
```

The second import binds `format_data` to the object imported from `module_b`, replacing the previous local binding.

This can make code confusing and error-prone.

One solution is to use aliases:

```python
from module_a import format_data as format_user_data
from module_b import format_data as format_report_data
```

Now the two functions have distinct local names.

Another option is to import the modules themselves:

```python
import module_a
import module_b

module_a.format_data()
module_b.format_data()
```

The second approach makes each function's origin explicit.

---

## Importing Names That Do Not Exist

If the requested name does not exist in the module, Python raises an `ImportError`.

For example:

```python
from math import calculate_average
```

will fail because the `math` module does not provide a name called `calculate_average`.

This is different from failing to find the module itself.

For example:

```python
import unknown_module
```

can raise:

```text
ModuleNotFoundError
```

The distinction is useful when diagnosing import problems.

---

## Importing Submodules

Packages can contain multiple modules.

For example:

```text
utilities/
├── __init__.py
├── text.py
└── files.py
```

A specific function can be imported from a submodule:

```python
from utilities.text import normalize_text

result = normalize_text("  Hello World  ")

print(result)
```

Here:

* `utilities` is the package.
* `text` is the module.
* `normalize_text` is the imported name.

Packages and submodule organization are covered in greater detail later.

---

## Wildcard Imports

Python also supports:

```python
from module_name import *
```

For example:

```python
from math import *
```

This makes names from the module available in the current namespace according to Python's wildcard-import rules.

However, wildcard imports are generally discouraged in application code.

They can:

* Make the origin of names unclear.
* Pollute the namespace.
* Create naming conflicts.
* Make static analysis harder.
* Make code more difficult to maintain.
* Hide dependencies.

Prefer explicit imports:

```python
from math import sqrt, ceil, floor
```

or:

```python
import math
```

---

## Choosing Between the Two Forms

Consider:

```python
import statistics

average = statistics.mean(scores)
```

versus:

```python
from statistics import mean

average = mean(scores)
```

The first form makes the origin of `mean()` immediately visible.

The second form is shorter and can be convenient when the imported name is unambiguous.

A practical guideline is:

> Prefer the import style that makes dependencies and name origins easiest to understand.

There is no universal requirement that every import must use one form.

---

## Good Use of `from ... import`

A direct import is often reasonable when:

```python
from pathlib import Path
```

is used throughout the file and `Path` is the primary object needed.

Another common example is:

```python
from datetime import datetime
```

which allows:

```python
current_time = datetime.now()
```

instead of:

```python
import datetime

current_time = datetime.datetime.now()
```

The shorter form can improve readability when the resulting name is clear and does not conflict with other names.

---

## Import Style in Larger Projects

Consider a project containing:

```text
application/
├── main.py
├── validation.py
└── models.py
```

`validation.py`:

```python
def is_valid_age(age: int) -> bool:
    return 0 <= age <= 120
```

`models.py`:

```python
class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
```

`main.py` could use:

```python
from models import User
from validation import is_valid_age

user = User("Shehbaz", 21)

if is_valid_age(user.age):
    print(f"{user.name} is valid.")
```

The imports clearly identify the specific functionality required by `main.py`.

---

## Common Mistakes

### Importing Too Many Names

This can make the top of a file difficult to understand:

```python
from utility import add, subtract, multiply, divide, validate, format_data, save_data, load_data
```

If a module provides many unrelated dependencies, reconsider the module's organization or import only what is actually required.

### Creating Name Collisions

For example:

```python
from module_a import process
from module_b import process
```

The second binding replaces the first local `process` name.

Use aliases or module-qualified imports when necessary.

### Using Wildcard Imports

Avoid:

```python
from module import *
```

in normal application code.

### Assuming Direct Import Changes the Original Module

The statement:

```python
from math import sqrt
```

does not create a new implementation of `sqrt()`.

It binds the imported object to the local name `sqrt`.

---

## Best Practices

* Import only the names that are actually required.
* Prefer explicit imports over wildcard imports.
* Use aliases when they resolve genuine naming conflicts or follow established conventions.
* Keep imports organized near the beginning of the file.
* Choose between `import module` and `from module import name` based on readability.
* Avoid direct imports that create ambiguous or conflicting names.
* Keep module responsibilities focused so imports remain understandable.

---

## Key Takeaways

* `from module import name` imports a specific name from a module.
* The imported name becomes directly available in the current namespace.
* Multiple names can be imported in one statement.
* Functions, classes, constants, and other module-level names can be imported.
* `as` can assign a local alias to an imported name.
* Direct imports can create naming conflicts.
* `from module import *` is generally discouraged.
* `import module` and `from module import name` create different namespace bindings.
* The best import style is the one that keeps dependencies and name origins clear.
