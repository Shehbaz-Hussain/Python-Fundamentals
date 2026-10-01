# `__init__.py`

This example introduces the role of the `__init__.py` file in a regular Python package.

## Files

```text
12-init-file/
├── README.md
└── init_file.py
```

## Key Concept

The `__init__.py` file is associated with a regular Python package and can be used to:

* Mark a directory as a regular package
* Initialize package-level state
* Expose selected names at the package level
* Define package metadata
* Provide a controlled public API

For example, a package can be organized as:

```text
text_tools/
├── __init__.py
├── formatting.py
└── validation.py
```

The `__init__.py` file can import selected functionality:

```text
from .formatting import format_text
```

Code using the package can then access the exported name through the package namespace.

## Important Note

Modern Python also supports **namespace packages**, which do not require an `__init__.py` file. Therefore, `__init__.py` is not universally required for every package.

However, it remains important for regular packages and is commonly used when explicit package initialization or package-level API design is needed.

## Example Code

The accompanying Python file demonstrates imported functionality while this README focuses on the package-level role of `__init__.py`.

```text
from math import sqrt


number = 81

result = sqrt(number)

print(f"Number: {number}")
print(f"Square root: {result}")
```

## Expected Output

```text
Number: 81
Square root: 9.0
```

## Learning Objective

After completing this example, you should understand:

* The purpose of `__init__.py`
* How `__init__.py` can expose package-level functionality
* The difference between regular packages and namespace packages
* Why `__init__.py` remains useful in professional Python projects
