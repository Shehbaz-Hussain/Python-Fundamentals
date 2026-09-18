# Nested Packages

## Overview

A **nested package** is a package contained inside another package.

Nested packages allow a Python project to organize functionality across multiple levels of hierarchy. They are useful when a project becomes large enough that a single package level is no longer sufficient.

A typical structure might look like:

```text
application/
├── __init__.py
├── users/
│   ├── __init__.py
│   └── models.py
└── services/
    ├── __init__.py
    └── reporting/
        ├── __init__.py
        └── generator.py
```

Here:

* `application` is the top-level package.
* `services` is a subpackage.
* `reporting` is a nested subpackage.
* `generator.py` is a module inside the `reporting` package.

Modern Python also supports namespace packages, so `__init__.py` is not required at every package level in every valid package structure.

---

## Why Use Nested Packages?

Nested packages help organize larger applications according to meaningful responsibilities.

For example, an AI application might eventually contain:

```text
ai_application/
├── data/
├── models/
├── training/
├── inference/
└── utilities/
```

Each area can contain multiple modules.

A more detailed structure could be:

```text
ai_application/
├── data/
│   ├── loaders.py
│   ├── preprocessing/
│   │   ├── text.py
│   │   └── numerical.py
│   └── validation.py
├── models/
│   ├── classification/
│   │   └── model.py
│   └── regression/
│       └── model.py
└── utilities/
    └── logging.py
```

This structure makes relationships between components easier to understand.

---

## Basic Nested Package Structure

Consider:

```text
project/
├── main.py
└── application/
    ├── __init__.py
    └── services/
        ├── __init__.py
        └── reporting/
            ├── __init__.py
            └── generator.py
```

The package hierarchy is:

```text
application
    └── services
        └── reporting
            └── generator
```

The fully qualified module name is:

```text
application.services.reporting.generator
```

---

## Importing from a Nested Package

Suppose `generator.py` contains:

```python
def generate_report(title: str) -> str:
    return f"Report: {title}"
```

A module outside the package can import it using an absolute import:

```python
from application.services.reporting.generator import generate_report


def main() -> None:
    report = generate_report("Monthly Sales")
    print(report)


if __name__ == "__main__":
    main()
```

Output:

```text
Report: Monthly Sales
```

The import path follows the package hierarchy.

---

## Importing the Module Instead of a Function

The entire module can also be imported:

```python
import application.services.reporting.generator
```

The function can then be accessed through the module namespace:

```python
report = application.services.reporting.generator.generate_report(
    "Monthly Sales"
)

print(report)
```

This makes the complete origin of the function explicit.

---

## Using an Import Alias

Long package paths can sometimes be shortened with an alias:

```python
import application.services.reporting.generator as report_generator

report = report_generator.generate_report("Monthly Sales")

print(report)
```

Aliases should be used only when they improve readability.

If the alias makes the code harder to understand, an explicit `from` import may be clearer.

---

## Nested Packages and `__init__.py`

Each level of a regular package hierarchy can contain its own `__init__.py`.

For example:

```text
application/
├── __init__.py
└── services/
    ├── __init__.py
    └── reporting/
        ├── __init__.py
        └── generator.py
```

The files can be empty:

```python
# application/__init__.py
```

```python
# application/services/__init__.py
```

```python
# application/services/reporting/__init__.py
```

This is sufficient when no package-level initialization or re-exporting is needed.

Modern namespace-package structures can omit these files where appropriate.

---

## Package-Level Re-Exports

Nested packages can use `__init__.py` to expose selected functionality.

Suppose:

```text
application/
└── services/
    └── reporting/
        ├── __init__.py
        └── generator.py
```

`generator.py`:

```python
def generate_report(title: str) -> str:
    return f"Report: {title}"
```

`reporting/__init__.py`:

```python
from .generator import generate_report
```

Code can then import:

```python
from application.services.reporting import generate_report

print(generate_report("Monthly Sales"))
```

The package initializer provides a simpler public interface.

---

## Nested Packages and Absolute Imports

An **absolute import** starts from a package's top-level import name.

For example:

```python
from application.services.reporting.generator import generate_report
```

This clearly describes the complete location of the module.

Absolute imports are often useful in larger applications because their origin is explicit.

---

## Nested Packages and Relative Imports

Code inside a nested package can also use relative imports.

Suppose:

```text
application/
└── services/
    └── reporting/
        ├── __init__.py
        ├── generator.py
        └── formatter.py
```

`generator.py` can import from the same package:

```python
from .formatter import format_report
```

The single dot means:

> Import from the current package.

A parent package can be referenced with additional dots.

For example:

```python
from ..logging import log_message
```

The exact number of dots depends on the package level and target module.

Relative imports require the module to be executed with an appropriate package context.

---

## Example with Multiple Nested Modules

Consider:

```text
application/
├── __init__.py
└── services/
    ├── __init__.py
    └── reporting/
        ├── __init__.py
        ├── generator.py
        └── formatter.py
```

`formatter.py`:

```python
def format_report(title: str, content: str) -> str:
    return f"{title}\n{'=' * len(title)}\n{content}"
```

`generator.py`:

```python
from .formatter import format_report


def generate_report(title: str, content: str) -> str:
    return format_report(title, content)
```

A top-level application can use:

```python
from application.services.reporting.generator import generate_report


def main() -> None:
    report = generate_report(
        "Monthly Sales",
        "Revenue increased by 12 percent."
    )

    print(report)


if __name__ == "__main__":
    main()
```

Output:

```text
Monthly Sales
=============
Revenue increased by 12 percent.
```

The reporting package separates report generation from report formatting.

---

## Designing Meaningful Package Hierarchies

A nested package should represent a meaningful relationship.

For example:

```text
application/
└── data/
    └── preprocessing/
```

makes sense because preprocessing is part of the data-processing area.

A hierarchy such as:

```text
application/
└── miscellaneous/
    └── other/
        └── helpers/
```

provides little architectural information.

The goal of nesting is not to create as many directories as possible. It is to communicate structure.

---

## Nested Packages in Larger Applications

A realistic software project might use:

```text
ai_platform/
├── __init__.py
├── data/
│   ├── __init__.py
│   ├── loading/
│   │   ├── __init__.py
│   │   └── csv_loader.py
│   └── preprocessing/
│       ├── __init__.py
│       ├── text.py
│       └── numerical.py
├── models/
│   ├── __init__.py
│   └── classification/
│       ├── __init__.py
│       └── classifier.py
└── utilities/
    ├── __init__.py
    └── logging.py
```

Possible responsibilities include:

* `data.loading` — loading datasets.
* `data.preprocessing` — preparing data.
* `models.classification` — classification models.
* `utilities` — general supporting functionality.

This type of structure can scale better than placing every module directly under one directory.

---

## Avoid Excessive Nesting

Nested packages should be introduced when they provide useful organization.

An unnecessarily deep structure such as:

```text
project/
└── application/
    └── core/
        └── services/
            └── data/
                └── processing/
                    └── text/
                        └── utilities/
                            └── normalization/
                                └── module.py
```

can make imports difficult to read:

```python
from application.core.services.data.processing.text.utilities.normalization.module import normalize
```

If several levels do not represent meaningful boundaries, simplify the hierarchy.

---

## Common Mistakes

### 1. Incorrect Import Path

Given:

```text
application/
└── services/
    └── reporting/
        └── generator.py
```

this is incorrect:

```python
from application.reporting.generator import generate_report
```

because `reporting` is inside `services`.

The correct path is:

```python
from application.services.reporting.generator import generate_report
```

---

### 2. Running a Package Module Directly

Suppose `generator.py` contains:

```python
from .formatter import format_report
```

Running it directly as:

```bash
python generator.py
```

can fail because the module may not have the package context required for the relative import.

Package modules should generally be executed in an appropriate package context, often with:

```bash
python -m application.services.reporting.generator
```

when direct module execution is appropriate.

---

### 3. Overusing Relative Imports

Relative imports can be useful inside packages, but deeply nested relative imports can become difficult to understand.

For example:

```python
from ....utilities.helpers import clean_text
```

is difficult to interpret.

Prefer a package structure and import strategy that keeps dependencies clear.

---

### 4. Treating Every Directory as a Package

A directory containing Python files does not automatically mean every possible import relationship is valid.

Package behavior depends on Python's import system, package structure, namespace-package rules, and execution context.

---

## Best Practices

* Use nested packages only when they communicate meaningful structure.
* Organize packages around clear responsibilities.
* Keep package depth reasonable.
* Use absolute imports when explicit package paths improve clarity.
* Use relative imports for closely related modules within a package when appropriate.
* Avoid unnecessary circular dependencies.
* Keep `__init__.py` files lightweight.
* Avoid overly long import paths.
* Execute package modules with an appropriate package context.

---

## Key Takeaways

* A nested package is a package contained within another package.
* Nested packages provide hierarchical organization for larger applications.
* A module inside a nested package has a fully qualified import path.
* Absolute imports can reference the complete package hierarchy.
* Relative imports can reference modules within the current package hierarchy.
* `__init__.py` can be used at each level of a regular package hierarchy.
* Modern Python also supports namespace packages without `__init__.py`.
* Good nesting reflects meaningful architecture rather than simply adding directories.
