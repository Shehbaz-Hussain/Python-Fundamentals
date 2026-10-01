# Absolute Imports

This example demonstrates the syntax and purpose of an absolute import in Python.

## Files

```text
16-absolute-import/
├── README.md
└── absolute_import.py
```

## Key Concept

An **absolute import** specifies the complete path to the module being imported, starting from the top-level package.

For example:

```text
from urllib.parse import quote
```

Here:

* `urllib` is the top-level package.
* `parse` is a module inside `urllib`.
* `quote` is imported from that module.

The import path does not depend on the location of the current module.

## Example

The `quote()` function from `urllib.parse` converts characters that have special meaning in URLs into percent-encoded representations.

```text
from urllib.parse import quote
```

The function can then be used directly:

```text
encoded_text = quote(text)
```

## Example Code

```text
"""
Topic: Absolute Imports

Description:
Demonstrates the structure and syntax of an absolute import
using a module from a standard Python package.
"""


from urllib.parse import quote


text = "Python modules and packages"

encoded_text = quote(text)

print(f"Original text: {text}")
print(f"Encoded text: {encoded_text}")
```

## Expected Output

```text
Original text: Python modules and packages
Encoded text: Python%20modules%20and%20packages
```

## Absolute vs Relative Imports

An absolute import:

```text
from package.module import name
```

uses the complete package path.

A relative import:

```text
from .module import name
```

uses the current package as the reference point.

Absolute imports are often preferred when they make the dependency relationship clear and unambiguous.

## Learning Objective

After completing this example, you should understand:

* What an absolute import is
* How absolute import paths are structured
* How to import a name from a nested module
* The difference between absolute and relative import syntax
* Why clear import paths improve code readability
