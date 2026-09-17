# Packages

## Overview

A **package** is a way to organize related Python modules into a hierarchical structure.

While a module commonly represents a single Python source file, a package can organize multiple modules and subpackages under a common namespace.

For example:

```text
project/
└── utilities/
    ├── text.py
    ├── numbers.py
    └── files.py
```

Here, `utilities` can serve as a package containing several related modules.

Packages become especially useful as applications grow beyond a small number of Python files.

---

## Why Packages Matter

A project containing only a few modules may be easy to manage:

```text
project/
├── main.py
├── calculator.py
└── validation.py
```

A larger application can quickly become difficult to organize:

```text
project/
├── main.py
├── users.py
├── authentication.py
├── database.py
├── reports.py
├── file_utils.py
├── text_utils.py
├── validators.py
├── configuration.py
└── ...
```

Packages allow related modules to be grouped:

```text
project/
├── main.py
├── users/
│   ├── models.py
│   ├── authentication.py
│   └── validation.py
├── reports/
│   ├── generator.py
│   └── formatter.py
└── utilities/
    ├── files.py
    └── text.py
```

This creates a clearer project hierarchy.

---

## Package Structure

A common package structure is:

```text
project/
├── main.py
└── utilities/
    ├── __init__.py
    ├── text.py
    └── numbers.py
```

In this example:

* `utilities` is the package.
* `text.py` is a module inside the package.
* `numbers.py` is another module inside the package.
* `__init__.py` identifies and initializes a regular package.

Modern Python also supports **namespace packages**, which do not require an `__init__.py` file. Therefore, `__init__.py` is not mandatory for every package.

---

## A Package with Multiple Modules

Consider:

```text
utilities/
├── __init__.py
├── text.py
└── numbers.py
```

`text.py`:

```python
def normalize_text(text: str) -> str:
    return " ".join(text.strip().split())
```

`numbers.py`:

```python
def is_even(number: int) -> bool:
    return number % 2 == 0
```

Another module can import them using their package-qualified names:

```python
from utilities.text import normalize_text
from utilities.numbers import is_even

print(normalize_text("  Python   modules  "))
print(is_even(10))
```

Output:

```text
Python modules
True
```

The package name provides structure for the imported modules.

---

## Importing a Package Module

A module inside a package can be imported with:

```python
import utilities.text
```

The function can then be accessed through the full namespace:

```python
print(utilities.text.normalize_text("  Python   "))
```

This makes the origin of the function explicit.

---

## Using `from` with a Package

A specific module can be imported with:

```python
from utilities import text
```

Then:

```python
print(text.normalize_text("  Python   "))
```

A specific function can also be imported:

```python
from utilities.text import normalize_text

print(normalize_text("  Python   "))
```

These forms create different local namespace bindings, so the choice should prioritize clarity.

---

## Packages Provide Hierarchical Namespaces

Packages allow names to be organized hierarchically.

For example:

```text
company/
└── analytics/
    ├── reports.py
    └── statistics.py
```

A module can be referenced as:

```python
company.analytics.reports
```

A function inside it could be imported as:

```python
from company.analytics.reports import generate_report
```

The hierarchy helps distinguish modules with similar names in larger systems.

---

## Packages and Subpackages

A package can contain another package.

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

Here:

* `application` is a package.
* `services` is a subpackage.
* `reporting` is another subpackage.
* `generator.py` is a module.

A function from `generator.py` can be imported using an absolute import such as:

```python
from application.services.reporting.generator import generate_report
```

This structure is useful when a project contains several logical layers.

---

## Packages and Separation of Responsibilities

A package should generally group modules that belong to a related area of functionality.

For example:

```text
student_management/
├── __init__.py
├── models.py
├── validation.py
├── storage.py
└── reports.py
```

Possible responsibilities:

* `models.py` — student data structures.
* `validation.py` — input validation.
* `storage.py` — persistence operations.
* `reports.py` — report generation.

The package provides a common organizational boundary for these modules.

---

## Example: Utility Package

Consider:

```text
project/
├── main.py
└── utilities/
    ├── __init__.py
    ├── numbers.py
    └── text.py
```

`numbers.py`:

```python
def calculate_average(values: list[float]) -> float:
    if not values:
        raise ValueError("values cannot be empty")

    return sum(values) / len(values)
```

`text.py`:

```python
def word_count(text: str) -> int:
    normalized = text.strip()

    if not normalized:
        return 0

    return len(normalized.split())
```

`main.py`:

```python
from utilities.numbers import calculate_average
from utilities.text import word_count


def main() -> None:
    average = calculate_average([10.0, 20.0, 30.0])
    words = word_count("Python modules and packages")

    print(f"Average: {average}")
    print(f"Words: {words}")


if __name__ == "__main__":
    main()
```

This is a small but realistic example of package-based organization.

---

## Regular Packages and Namespace Packages

Python supports two important package concepts.

### Regular Package

A traditional package normally contains:

```text
utilities/
├── __init__.py
└── text.py
```

The `__init__.py` file allows the directory to function as a regular Python package and can contain package initialization code.

### Namespace Package

Python also supports namespace packages that can exist without an `__init__.py` file.

For example:

```text
utilities/
└── text.py
```

may participate in a namespace package depending on the project and import environment.

Therefore, it is incorrect to state that every Python package must contain `__init__.py`.

---

## Packages Are Not the Same as Third-Party Packages

The word **package** can describe Python code organized into a package structure, while a **third-party package** is software distributed separately from Python's standard library.

For example, a project may contain its own package:

```text
my_application/
└── utilities/
    ├── __init__.py
    └── files.py
```

It can also depend on an external package such as:

```python
import requests
```

These are different concepts.

A local project package is part of the application's source code, while a third-party package is normally installed into the Python environment.

---

## Packages and Reusability

A well-designed package can make functionality reusable across multiple parts of an application.

For example:

```text
project/
├── application.py
├── reporting/
│   ├── __init__.py
│   ├── csv_report.py
│   └── summary.py
└── validation/
    ├── __init__.py
    └── rules.py
```

Different application components can import only the functionality they need.

This reduces duplication and encourages clear interfaces between components.

---

## Common Mistakes

### 1. Assuming Every Package Requires `__init__.py`

Modern Python supports namespace packages without `__init__.py`.

Therefore, this statement is too broad:

```text
Every package must contain __init__.py.
```

A more accurate statement is:

> `__init__.py` is used for regular packages but is not required for every package structure supported by modern Python.

---

### 2. Mixing Unrelated Modules

Avoid creating a package that contains completely unrelated functionality simply because the files need a common directory.

For example:

```text
random/
├── database.py
├── machine_learning.py
├── image_processing.py
└── payroll.py
```

A better structure would group functionality according to meaningful responsibilities.

---

### 3. Creating Excessively Deep Structures

Packages should improve organization, not make imports unnecessarily difficult.

For example:

```python
from project.application.core.services.utilities.helpers.text.processing.normalization import normalize
```

is a warning sign when such depth is not justified.

Prefer a hierarchy that reflects meaningful architectural boundaries.

---

### 4. Confusing Directory Structure with Import Context

Simply placing files in nested directories does not guarantee that every possible import will work.

Python's import system depends on package structure, module search paths, and execution context.

Project organization should therefore be designed together with the intended import structure.

---

## Best Practices

* Group related modules into packages.
* Give packages clear, descriptive names.
* Keep package responsibilities focused.
* Use subpackages when the project genuinely needs another organizational level.
* Prefer clear absolute imports for many application structures.
* Understand relative imports when working inside packages.
* Do not assume `__init__.py` is required for every modern package.
* Avoid unnecessary package depth.
* Keep public package interfaces intentional.
* Organize packages around meaningful application responsibilities.

---

## Key Takeaways

* A package organizes related Python modules hierarchically.
* Packages help large projects remain structured and maintainable.
* A package can contain modules and subpackages.
* A regular package commonly contains `__init__.py`.
* Modern Python also supports namespace packages without `__init__.py`.
* Package-qualified imports clearly identify where functionality belongs.
* Good package design separates related responsibilities without creating unnecessary complexity.
