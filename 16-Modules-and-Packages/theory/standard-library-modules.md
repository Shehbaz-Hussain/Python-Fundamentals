# Standard Library Modules

## Overview

Python includes a large collection of modules and packages in its **standard library**.

The standard library provides ready-to-use functionality for common programming tasks without requiring developers to install separate third-party packages.

Examples include modules for:

* Mathematical operations
* File and path handling
* Date and time operations
* Data serialization
* Statistics
* Operating-system interaction
* Command-line processing
* Regular expressions
* Collections and data structures

Using standard-library modules is an important part of writing practical Python software.

---

## What Is the Standard Library?

The Python standard library is the collection of modules and packages distributed with Python.

For example:

```python
import math
```

The `math` module provides mathematical functions and constants.

Another example:

```python
from pathlib import Path
```

The `pathlib` module provides an object-oriented interface for filesystem paths.

These modules are available as part of Python itself and normally do not need to be installed separately with a package manager.

---

## Why Use Standard Library Modules?

The standard library helps developers avoid implementing common functionality from scratch.

For example, instead of manually calculating a square root:

```python
number = 25
```

you can use:

```python
import math

result = math.sqrt(number)

print(result)
```

Output:

```text id="5pm5zv"
5.0
```

Using established library functionality generally improves reliability, readability, and maintainability.

---

## The `math` Module

The `math` module provides mathematical functions and constants.

Example:

```python
import math

print(math.sqrt(81))
print(math.ceil(4.2))
print(math.floor(4.8))
```

Output:

```text id="tdn6l4"
9.0
5
4
```

Commonly used functionality includes:

```python
math.sqrt()
math.ceil()
math.floor()
math.factorial()
math.gcd()
```

The module also provides constants such as:

```python
math.pi
math.e
```

---

## The `pathlib` Module

The `pathlib` module provides classes for working with filesystem paths.

Example:

```python
from pathlib import Path

path = Path("data.txt")

print(path.exists())
```

A file can be read using:

```python
from pathlib import Path

path = Path("data.txt")

if path.exists():
    content = path.read_text(encoding="utf-8")
    print(content)
```

`pathlib` is often preferable to manually constructing paths with string concatenation because it provides a clearer, platform-aware interface.

---

## The `json` Module

The `json` module provides functionality for working with JSON data.

For example:

```python
import json

data = {
    "name": "Aisha",
    "age": 20,
    "active": True,
}

json_text = json.dumps(data)

print(json_text)
```

Output:

```text id="n1k6fr"
{"name": "Aisha", "age": 20, "active": true}
```

JSON is commonly used for configuration files, APIs, and data exchange.

JSON data can be converted back into Python objects with:

```python
import json

json_text = '{"name": "Aisha", "age": 20}'

data = json.loads(json_text)

print(data["name"])
```

---

## The `statistics` Module

The `statistics` module provides common statistical calculations.

Example:

```python
from statistics import mean, median

values = [10, 20, 30, 40, 50]

print(mean(values))
print(median(values))
```

Output:

```text id="42i6ls"
30
30
```

This module is useful for basic statistical operations without requiring a third-party data-analysis library.

---

## The `datetime` Module

The `datetime` module provides classes for working with dates and times.

Example:

```python
from datetime import datetime

current_time = datetime.now()

print(current_time)
```

A specific date can be created with:

```python
from datetime import date

birthday = date(2005, 7, 15)

print(birthday)
```

Date and time functionality is common in software systems such as:

* Logging systems
* Scheduling applications
* Data processing
* Reporting systems
* APIs
* Databases

---

## The `random` Module

The `random` module provides pseudo-random number generation.

Example:

```python
import random

number = random.randint(1, 10)

print(number)
```

It can also select an item from a sequence:

```python
import random

colors = ["red", "blue", "green"]

choice = random.choice(colors)

print(choice)
```

The `random` module is useful for simulations, simple games, testing, and randomized application behavior.

It is **not** appropriate for security-sensitive randomness. Security-related applications should use the `secrets` module instead.

---

## The `os` Module

The `os` module provides interfaces to operating-system functionality.

For example:

```python
import os

print(os.name)
```

Environment variables can be accessed with:

```python
import os

username = os.getenv("USERNAME")

print(username)
```

Although `os` remains widely used, modern Python code can often use more specialized interfaces such as `pathlib` for filesystem paths.

---

## The `sys` Module

The `sys` module provides access to Python interpreter and runtime information.

For example:

```python
import sys

print(sys.version)
```

The module search path can be inspected with:

```python
import sys

for path in sys.path:
    print(path)
```

The `sys` module is particularly useful when working with:

* Interpreter configuration
* Command-line arguments
* Module search paths
* Runtime information
* Standard input and output

---

## The `collections` Module

The `collections` module provides specialized container types.

For example:

```python
from collections import Counter

words = ["python", "ai", "python", "ml"]

counts = Counter(words)

print(counts)
```

Output:

```text id="7r3l2n"
Counter({'python': 2, 'ai': 1, 'ml': 1})
```

`collections` also provides useful types such as:

```python
deque
defaultdict
namedtuple
Counter
```

These can solve common data-structure problems without implementing specialized containers manually.

---

## The `re` Module

The `re` module provides regular expression functionality.

For example:

```python
import re

text = "Python 3.13"

match = re.search(r"\d+\.\d+", text)

if match:
    print(match.group())
```

Output:

```text id="qfghw7"
3.13
```

Regular expressions are useful for pattern matching and text processing.

They should be used where they improve the solution rather than replacing simpler string operations unnecessarily.

---

## The `argparse` Module

The `argparse` module helps build command-line interfaces.

Example:

```python
import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("name")

    args = parser.parse_args()

    print(f"Hello, {args.name}")


if __name__ == "__main__":
    main()
```

A command such as:

```bash
python greeting.py Aisha
```

can produce:

```text
Hello, Aisha
```

This is useful for building reusable command-line utilities.

---

## The `csv` Module

The `csv` module provides tools for reading and writing CSV files.

Example:

```python
import csv

with open("students.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])
```

The standard library therefore provides basic structured-data processing without requiring a third-party dependency.

---

## Standard Library vs Third-Party Packages

It is important to distinguish standard-library modules from third-party packages.

Standard library:

```python
import json
from pathlib import Path
```

These are provided with Python.

Third-party packages:

```python
import numpy
import pandas
import requests
```

These are developed and distributed separately and normally need to be installed into the relevant Python environment.

A project should not install a third-party package when an adequate standard-library solution already meets its requirements without unnecessary complexity.

---

## Finding Documentation

The official Python documentation provides detailed documentation for standard-library modules.

A developer should consult the documentation when they need:

* Available functions
* Function parameters
* Return values
* Exceptions
* Supported classes
* Version-specific behavior
* Usage examples

Knowing how to read library documentation is an essential software-engineering skill.

---

## Inspecting a Standard Library Module

Python can be used to inspect imported modules.

For example:

```python
import math

print(math.__name__)
print(math.__doc__)
```

You can also inspect available names:

```python
import math

print(dir(math))
```

These techniques can help with exploration, although official documentation should remain the primary reference for understanding an API.

---

## Common Mistakes

### 1. Installing Standard Library Modules Unnecessarily

Modules such as:

```python
json
math
pathlib
statistics
datetime
```

are part of Python's standard library.

They normally do not need to be installed separately.

---

### 2. Confusing a Standard Module with a Third-Party Package

For example:

```python
import pandas
```

is not equivalent to:

```python
import statistics
```

`statistics` is part of the standard library, while `pandas` is a third-party package.

---

### 3. Using a Third-Party Library Without Checking the Standard Library

Before adding a dependency, check whether Python already provides suitable functionality.

For example, `pathlib` provides modern filesystem path handling without requiring an external package.

This does not mean third-party libraries are unnecessary. They are often essential for specialized tasks such as data science and machine learning.

---

### 4. Using the Wrong Module for Security

The `random` module is intended for general pseudo-random behavior.

Do not use it for security-sensitive token generation.

Use:

```python
import secrets

token = secrets.token_hex(16)

print(token)
```

for appropriate security-sensitive random values.

---

## Best Practices

* Learn the commonly used standard-library modules.
* Prefer standard-library functionality when it adequately solves the problem.
* Read official documentation before relying on unfamiliar APIs.
* Avoid unnecessary third-party dependencies.
* Choose specialized standard-library modules instead of manually recreating their functionality.
* Keep imports explicit and readable.
* Check Python version compatibility when using newer standard-library features.
* Use third-party packages when they provide capabilities beyond the standard library.

---

## Key Takeaways

* Python includes a large standard library of reusable modules and packages.
* Standard-library modules normally require no separate installation.
* Important examples include:

  * `math`
  * `pathlib`
  * `json`
  * `statistics`
  * `datetime`
  * `random`
  * `sys`
  * `os`
  * `collections`
  * `re`
  * `argparse`
  * `csv`
* Standard-library knowledge reduces unnecessary dependencies and duplicated code.
* Third-party packages remain important when specialized functionality is required.
* Official Python documentation is the primary reference for standard-library APIs.
