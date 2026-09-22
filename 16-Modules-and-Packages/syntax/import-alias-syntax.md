# Import Alias Syntax

## Overview

Python allows modules and imported names to be assigned local aliases using the `as` keyword.

Aliases can make long names easier to use and can prevent naming conflicts.

The two primary forms are:

```python
import module_name as alias
```

and:

```python
from module_name import name as alias
```

---

## Module Alias

Basic syntax:

```python
import module_name as alias
```

Example:

```python
import math as mathematics

result = mathematics.sqrt(25)

print(result)
```

Output:

```text
5.0
```

The module is imported under the local name `mathematics`.

---

## Why Use an Alias?

Aliases are useful when:

* A module has a long name.
* A project follows an established naming convention.
* Two imported names would otherwise conflict.
* A commonly accepted ecosystem convention exists.
* A shorter name improves readability without reducing clarity.

Use aliases deliberately rather than shortening every import automatically.

---

## Alias with `from ... import`

A specific name can also be aliased:

```python
from statistics import mean as average
```

The function can then be called as:

```python
values = [10, 20, 30]

result = average(values)

print(result)
```

Output:

```text
20
```

---

## Module Alias vs Name Alias

These two forms have different effects.

### Module Alias

```python
import statistics as stats
```

Usage:

```python
stats.mean([10, 20, 30])
```

### Imported Name Alias

```python
from statistics import mean as average
```

Usage:

```python
average([10, 20, 30])
```

The first aliases the module.

The second aliases the imported name.

---

## Common Library Aliases

Some Python libraries have widely recognized aliases.

For example:

```python
import numpy as np
import pandas as pd
```

Then:

```python
values = np.array([1, 2, 3])
```

and:

```python
data = pd.DataFrame({"score": [80, 90, 95]})
```

These aliases are common conventions in data-science code.

---

## Aliasing `pathlib`

For example:

```python
import pathlib as pl

path = pl.Path("data.txt")

print(path)
```

This is valid Python.

However, shortening a module name is not automatically an improvement. If the standard module name is already short and clear, keeping the original name may be preferable:

```python
import pathlib

path = pathlib.Path("data.txt")
```

---

## Aliasing a Long Module Name

Suppose a package contains:

```text
application/
└── data_processing/
    └── normalization.py
```

An import could be:

```python
import application.data_processing.normalization as normalization
```

Then:

```python
result = normalization.normalize(data)
```

An alias can reduce repetition while retaining a meaningful name.

---

## Preventing Name Conflicts

Aliases are particularly useful when two modules expose the same name.

For example:

```python
from package_a import process as process_data
from package_b import process as process_text
```

Now the two functions can be used independently:

```python
process_data()
process_text()
```

Without aliases, the second import could replace the first local binding.

---

## Preventing Class Name Conflicts

Aliases can also distinguish classes with the same name.

For example:

```python
from package_a import Client as APIClient
from package_b import Client as DatabaseClient
```

Usage:

```python
api_client = APIClient()
database_client = DatabaseClient()
```

The aliases communicate the intended roles.

---

## Aliasing Standard Library Modules

Aliases can be used with standard-library modules:

```python
import datetime as dt
```

Then:

```python
today = dt.date.today()

print(today)
```

This pattern can be appropriate when the alias is widely understood or improves readability.

---

## Aliasing Third-Party Packages

Third-party packages often have established aliases.

For example:

```python
import numpy as np
import pandas as pd
```

These aliases are commonly recognized by Python developers working with data science and AI.

Do not invent unusual aliases when an established convention already exists.

---

## Aliasing Custom Modules

Custom modules can also be aliased:

```python
import file_processing as fp
```

Then:

```python
fp.load_file()
fp.save_file()
```

However, custom-module aliases should remain readable.

An alias such as:

```python
import file_processing as x
```

provides little useful information.

Prefer:

```python
import file_processing as fp
```

when an alias is genuinely helpful.

---

## Alias Names Follow Python Naming Rules

An alias is a Python identifier.

This is valid:

```python
import statistics as stats
```

This is not valid:

```python
import statistics as 123stats
```

Use standard Python naming conventions for aliases.

---

## Aliases Do Not Rename the Original Module

Consider:

```python
import math as mathematics
```

The alias `mathematics` is the name available in the current namespace.

It does not rename the actual Python module on disk or change the package itself.

The alias is a local binding.

---

## Aliases and Namespaces

Consider:

```python
import math as m
```

The current namespace contains the name:

```python
m
```

The module's functions remain accessed through that binding:

```python
m.sqrt(16)
```

The alias therefore changes how the module is referenced locally, not how the module is implemented.

---

## Multiple Aliases

Different modules can have different aliases:

```python
import math as math_module
import statistics as stats
import json as json_module
```

This is valid, but aliases should be used only when they provide a clear benefit.

Excessive aliases can make code harder to read.

---

## Avoid Unnecessary Aliases

This:

```python
import math as m
```

may be less readable than:

```python
import math
```

because `math` is already short and descriptive.

Likewise:

```python
from pathlib import Path as P
```

is generally less clear than:

```python
from pathlib import Path
```

Prefer the original name unless the alias solves a real problem.

---

## Alias Naming Guidelines

Good aliases should generally be:

* Short enough to reduce repetition
* Descriptive enough to remain understandable
* Consistent with project conventions
* Recognizable to other developers
* Appropriate for the imported object

Examples:

```python
import numpy as np
import pandas as pd
import datetime as dt
```

---

## Common Mistakes

### 1. Using the Original Name After Aliasing

This code is incorrect:

```python
import math as mathematics

print(math.sqrt(25))
```

The imported local name is `mathematics`.

Correct:

```python
print(mathematics.sqrt(25))
```

---

### 2. Choosing Meaningless Aliases

Avoid:

```python
import statistics as x
```

Prefer:

```python
import statistics as stats
```

when an alias is useful.

---

### 3. Overusing Aliases

Do not turn every import into an abbreviation.

For example:

```python
import json as j
import math as m
import pathlib as p
```

may make code less readable.

---

### 4. Ignoring Established Conventions

For commonly used packages, established aliases improve consistency.

For example:

```python
import numpy as np
import pandas as pd
```

are widely recognized.

---

## Best Practices

* Use `as` when an alias improves clarity or prevents a conflict.
* Follow established conventions for popular libraries.
* Prefer descriptive aliases for custom modules.
* Avoid unnecessary abbreviations.
* Keep aliases consistent within a project.
* Remember that aliases are local names, not module renames.
* Use aliases to make conflicting names explicit.
* Do not sacrifice readability merely to shorten code.

---

## Quick Reference

### Alias a Module

```python
import module_name as alias
```

Example:

```python
import statistics as stats
```

Usage:

```python
stats.mean([10, 20, 30])
```

### Alias an Imported Name

```python
from module_name import name as alias
```

Example:

```python
from statistics import mean as average
```

Usage:

```python
average([10, 20, 30])
```

### Resolve a Name Conflict

```python
from package_a import Client as APIClient
from package_b import Client as DatabaseClient
```

### Common Convention

```python
import numpy as np
import pandas as pd
```

### Main Principle

Use aliases when they improve readability, consistency, or namespace clarity—not simply because Python allows them.
