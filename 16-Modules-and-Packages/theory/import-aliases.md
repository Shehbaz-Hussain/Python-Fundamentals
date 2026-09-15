# Import Aliases

## Overview

Python allows imported modules and names to be assigned local aliases using the `as` keyword.

An **import alias** is an alternative local name used to refer to an imported module or object.

For example:

```python
import statistics as stats
```

The module is imported normally, but the local name `stats` is used to access it:

```python
print(stats.mean([10, 20, 30]))
```

Aliases can improve readability, shorten long names, and resolve naming conflicts when used appropriately.

---

## Basic Module Alias Syntax

The syntax for assigning an alias to a module is:

```python
import module_name as alias
```

For example:

```python
import statistics as stats
```

The module can then be accessed through `stats`:

```python
scores = [75, 80, 90, 85]

average = stats.mean(scores)

print(average)
```

The alias exists in the current namespace. The original local name `statistics` is not created by this particular import statement.

---

## Why Use Module Aliases?

Aliases are useful for several reasons.

### Shortening Long Names

Suppose a module has a long name:

```python
import temperature_conversion_utilities as temperature_utils
```

Instead of:

```python
temperature_conversion_utilities.celsius_to_fahrenheit(25)
```

the alias allows:

```python
temperature_utils.celsius_to_fahrenheit(25)
```

This can make repeated references easier to read.

### Using Established Conventions

Some libraries have widely recognized aliases.

For example:

```python
import numpy as np
import pandas as pd
```

Then:

```python
import numpy as np

values = np.array([10, 20, 30])
```

and:

```python
import pandas as pd

data = pd.DataFrame({"score": [80, 90, 85]})
```

These aliases are common conventions in the Python data ecosystem.

---

## Importing a Specific Name with an Alias

Aliases can also be used with `from ... import`.

Syntax:

```python
from module_name import name as alias
```

For example:

```python
from statistics import mean as calculate_average
```

The imported function can then be called using the alias:

```python
scores = [80, 90, 85]

average = calculate_average(scores)

print(average)
```

The local name is `calculate_average`, not `mean`.

---

## Module Alias vs Imported-Name Alias

These two forms are different:

```python
import statistics as stats
```

and:

```python
from statistics import mean as calculate_average
```

With the first form:

```python
stats.mean([10, 20, 30])
```

With the second form:

```python
calculate_average([10, 20, 30])
```

The first creates a local name for the module.

The second creates a local name for the imported object.

---

## Aliases and Namespace Bindings

Consider:

```python
import math as mathematics
```

The name `mathematics` is bound in the current namespace.

Therefore:

```python
print(mathematics.sqrt(25))
```

works.

But:

```python
print(math.sqrt(25))
```

does not work merely because the underlying module is the `math` module. The local import binding was given the name `mathematics`.

Likewise:

```python
from math import sqrt as square_root

print(square_root(25))
```

creates the local name `square_root`.

Understanding aliases as **namespace bindings** makes their behavior easier to predict.

---

## Aliases Do Not Rename the Actual Module

Consider:

```python
import statistics as stats
```

The alias `stats` is a local reference to the imported module.

It does not rename the module itself on disk or change its actual module identity.

For example:

```python
import statistics as stats

print(stats.__name__)
```

The result identifies the underlying module:

```text
statistics
```

The local alias is simply the name used by the importing code.

---

## Aliases for Name Conflicts

Aliases are particularly useful when two imported objects have the same name.

Suppose two modules provide a function named `format_data`:

```python
from user_utils import format_data as format_user_data
from report_utils import format_data as format_report_data
```

Now both functions can be used without replacing one local name with another:

```python
user_output = format_user_data(user_data)
report_output = format_report_data(report_data)
```

The aliases communicate each function's purpose.

---

## Aliases Can Improve Clarity

An alias should not merely make a name shorter. It should make the code easier to understand.

For example:

```python
from statistics import mean as calculate_average
```

can make the function's role clearer in a context where `mean` might be ambiguous.

However, arbitrary aliases can have the opposite effect:

```python
import statistics as xyz
```

A reader now has to remember what `xyz` represents.

Prefer meaningful aliases.

---

## Common Library Aliases

Some Python libraries have widely established aliases.

### NumPy

```python
import numpy as np
```

Usage:

```python
values = np.array([1, 2, 3])
```

### pandas

```python
import pandas as pd
```

Usage:

```python
data = pd.DataFrame({"name": ["Ali", "Sara"]})
```

### Matplotlib

A commonly used form is:

```python
import matplotlib.pyplot as plt
```

Usage:

```python
plt.plot([1, 2, 3], [2, 4, 6])
```

These conventions are widely recognized by Python developers.

---

## Aliases in Custom Projects

Aliases are not limited to third-party libraries.

Suppose a project contains:

```text
project/
├── main.py
└── data_processing.py
```

`main.py` can write:

```python
import data_processing as processor
```

Then:

```python
result = processor.clean_data(raw_data)
```

This can be useful when the original module name is long or when the alias better communicates the role the module plays in the current file.

---

## Multiple Aliased Imports

A file can use multiple aliases:

```python
import numpy as np
import pandas as pd
import statistics as stats
```

Each alias is an independent local namespace binding.

For example:

```python
values = np.array([10, 20, 30])
data = pd.DataFrame({"value": values})

average = stats.mean(values)
```

This is common in data-oriented Python applications.

---

## Aliases and Readability

Consider:

```python
import data_preprocessing_pipeline as pipeline
```

This can make repeated usage concise:

```python
pipeline.clean_data(data)
pipeline.normalize_data(data)
pipeline.validate_data(data)
```

Without an alias:

```python
data_preprocessing_pipeline.clean_data(data)
data_preprocessing_pipeline.normalize_data(data)
data_preprocessing_pipeline.validate_data(data)
```

An alias can therefore reduce visual noise when a module is used frequently.

However, shortening every module name is unnecessary. Use aliases where they provide a real readability benefit.

---

## Aliases and Naming Conflicts with Local Variables

An alias can also prevent conflicts with local names.

For example:

```python
import statistics as statistics_module

statistics = "student statistics"

average = statistics_module.mean([80, 90, 85])

print(average)
```

Here, the imported module is given a distinct local name so that the variable `statistics` can be used for another purpose.

In practice, it is usually better to avoid unnecessary name conflicts altogether, but aliases can be useful when a conflict cannot easily be avoided.

---

## Common Mistakes

### 1. Using Meaningless Aliases

Avoid:

```python
import statistics as x
```

when there is no clear reason for the name.

Prefer:

```python
import statistics as stats
```

when a conventional short name is appropriate.

### 2. Inventing Non-Standard Library Aliases

If a library has an established convention, follow it.

For example:

```python
import numpy as np
```

is generally clearer than:

```python
import numpy as numerical_library
```

### 3. Forgetting the Alias

After:

```python
import math as mathematics
```

use:

```python
mathematics.sqrt(25)
```

not:

```python
math.sqrt(25)
```

The name `math` was not introduced by that import statement.

### 4. Overusing Aliases

This can reduce readability:

```python
import math as m
import statistics as s
import pathlib as p
```

Unless the aliases are conventional or genuinely useful, the original module names may be clearer.

### 5. Confusing an Alias with a Module Rename

An alias only affects the local binding created by the import. It does not rename the module itself.

---

## Best Practices

* Use `as` when an alias improves readability or resolves a real naming conflict.
* Follow established conventions for popular libraries.
* Prefer meaningful aliases.
* Avoid arbitrary one-letter aliases unless they are conventional or obvious in context.
* Do not create aliases simply because shorter names are possible.
* Use aliases consistently within a project.
* Remember that an alias changes the local name, not the module's identity.

---

## Key Takeaways

* The `as` keyword creates a local alias during an import.
* Modules can be aliased with:

  ```python
  import module as alias
  ```
* Specific names can be aliased with:

  ```python
  from module import name as alias
  ```
* An alias is a local namespace binding.
* An alias does not rename the underlying module.
* Aliases are useful for long names, established library conventions, and naming conflicts.
* Meaningful aliases improve readability.
* Arbitrary or excessive aliases can make code harder to understand.
