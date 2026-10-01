# Nested Packages

This example introduces the concept of nested packages and hierarchical module organization.

## Files

```text id="m7p0qk"
14-nested-package/
├── README.md
└── nested_package.py
```

## Key Concept

A **nested package** is a package structure in which one package exists inside another package.

For example:

```text id="v1j8qa"
application/
├── __init__.py
├── utilities/
│   ├── __init__.py
│   └── formatting.py
└── data/
    ├── __init__.py
    └── processing.py
```

Here, `utilities` and `data` are subpackages of `application`.

Nested packages allow larger applications to organize functionality into logical groups.

## Example

Python's standard library also contains hierarchical module structures. The example uses:

```text id="z2b7kc"
import urllib.parse
```

`urllib` is the top-level package, while `parse` is a module inside it.

The function `quote()` is accessed through the nested namespace:

```text id="q4m3zs"
urllib.parse.quote(...)
```

This demonstrates the same hierarchical naming concept used by nested packages.

## Example Code

```text id="w6t1pf"
import urllib.parse


url = "https://example.com/search?q=python modules"

encoded_url = urllib.parse.quote(url)

print(f"Original URL: {url}")
print(f"Encoded URL: {encoded_url}")
```

## Expected Output

```text id="n8s4yc"
Original URL: https://example.com/search?q=python modules
Encoded URL: https%3A//example.com/search%3Fq%3Dpython%20modules
```

## Learning Objective

After completing this example, you should understand:

* What nested packages are
* How packages can contain subpackages
* How hierarchical module names are structured
* How dotted module paths are accessed
* Why nested organization is useful in larger Python projects
