# Module Best Practices

## Overview

Modules and packages allow Python programs to be divided into smaller, reusable components.

A well-designed module should have a clear responsibility, predictable behavior, readable imports, and minimal unnecessary coupling with other parts of the application.

Good module design becomes increasingly important as projects grow from small scripts into software systems.

---

## 1. Give Each Module a Clear Responsibility

A module should have a focused purpose.

For example:

```text
project/
├── file_utils.py
├── text_utils.py
├── validation.py
└── configuration.py
```

Each module has a recognizable responsibility.

Avoid creating a single module that contains unrelated functionality:

```text
utils.py
```

with hundreds of functions covering files, networking, validation, mathematics, database operations, and application logic.

Large generic utility modules become difficult to understand and maintain.

---

## 2. Keep Modules Cohesive

A module is cohesive when its contents belong together.

For example:

```python
# text_utils.py

def normalize_text(text: str) -> str:
    return text.strip().lower()


def word_count(text: str) -> int:
    return len(text.split())
```

Both functions operate on text and naturally belong together.

By contrast, placing unrelated functionality into the same module makes the module's purpose unclear.

---

## 3. Use Meaningful Module Names

Module names should clearly communicate their purpose.

Good examples:

```text
data_loader.py
file_manager.py
text_processing.py
model_config.py
validation.py
```

Avoid vague names when a more descriptive name is available:

```text
stuff.py
misc.py
things.py
helper.py
```

A module name is part of the project's architecture and should communicate intent.

---

## 4. Keep Imports Explicit

Prefer explicit imports.

For example:

```python
from pathlib import Path
```

This clearly communicates which functionality is being used.

Another readable approach is:

```python
import pathlib

path = pathlib.Path("data.txt")
```

Both styles can be appropriate depending on the project.

---

## 5. Avoid Wildcard Imports

Avoid:

```python
from module import *
```

Wildcard imports make it difficult to determine where names came from.

For example:

```python
from math import *
```

does not clearly show which mathematical functions a module depends on.

Prefer:

```python
from math import sqrt
```

or:

```python
import math

result = math.sqrt(25)
```

Explicit imports improve readability and reduce namespace confusion.

---

## 6. Avoid Unnecessary Global State

Modules can contain constants, functions, classes, and other definitions, but excessive mutable global state can make software difficult to reason about.

Avoid patterns such as:

```python
users = []

def add_user(name: str) -> None:
    users.append(name)
```

when the state could instead be managed explicitly by the application.

Passing data through function parameters often makes dependencies clearer.

---

## 7. Keep Top-Level Code Controlled

Importing a module can execute its top-level statements.

Avoid putting application actions directly at module level:

```python
print("Starting application...")
process_data()
send_report()
```

If the file is intended to be executable, use a main function and main guard:

```python
def main() -> None:
    print("Starting application...")
    process_data()
    send_report()


if __name__ == "__main__":
    main()
```

This allows the module to be imported without automatically running the application's main workflow.

---

## 8. Use the Main Guard for Executable Modules

The standard pattern is:

```python
def main() -> None:
    # Application logic
    ...


if __name__ == "__main__":
    main()
```

For a reusable library module that contains only definitions, a main guard may not be necessary.

The main guard is most useful when the same module can be:

* Imported by other modules
* Executed directly as a program

---

## 9. Keep Imports Near the Top

Imports are normally placed near the beginning of a module:

```python
import json
from pathlib import Path

from project.validation import validate_data
```

This makes dependencies easy to identify.

Avoid placing imports throughout a file without a specific reason.

There are legitimate cases for local imports, but they should be intentional rather than accidental.

---

## 10. Avoid Circular Imports

A circular import occurs when modules depend on each other directly or indirectly.

For example:

```text
module_a
    ↓
module_b
    ↓
module_a
```

A simplified example:

```python
# module_a.py

from module_b import function_b
```

and:

```python
# module_b.py

from module_a import function_a
```

This creates a circular dependency.

Circular imports can lead to partially initialized modules and confusing import errors.

The better solution is usually to reorganize responsibilities rather than trying to hide the circular dependency.

---

## 11. Use a Shared Module for Common Dependencies

If two modules need the same shared functionality, extract that functionality into a separate module when appropriate.

For example:

```text
project/
├── main.py
├── configuration.py
├── validation.py
└── formatting.py
```

Instead of:

```text
validation.py
    ↓
main.py
    ↓
validation.py
```

the modules can depend on a common lower-level component.

This reduces unnecessary coupling.

---

## 12. Prefer Absolute Imports for Clear Project Structure

For larger applications, absolute imports often make dependencies easier to understand.

Example:

```python
from application.validation import validate_user
```

The import communicates where the functionality belongs within the project.

Relative imports are also valid and useful within packages:

```python
from .validation import validate_user
```

The choice should be consistent with the project's package structure and conventions.

---

## 13. Keep Relative Imports Within Package Context

Relative imports such as:

```python
from .utils import format_name
```

depend on package context.

A module containing relative imports may fail when executed directly as a standalone file.

For package-based applications, use the appropriate package execution method, commonly:

```bash
python -m package.module
```

rather than assuming every package module should be executed with:

```bash
python module.py
```

---

## 14. Keep Module APIs Small and Clear

A module should expose the functionality that other parts of the application actually need.

For example:

```python
def calculate_total(items: list[float]) -> float:
    return sum(items)
```

is a clear public function.

Avoid exposing unnecessary implementation details when they do not need to be used elsewhere.

A smaller interface generally makes a module easier to maintain.

---

## 15. Use `__all__` Deliberately

A module can define `__all__` to identify names intended for wildcard-import behavior:

```python
__all__ = ["calculate_total", "format_currency"]
```

However, `__all__` does not make wildcard imports automatically good practice.

It is a tool for controlling exported names, not a reason to prefer:

```python
from module import *
```

over explicit imports.

---

## 16. Keep Module Initialization Lightweight

Importing a module should generally be inexpensive and predictable.

Avoid performing expensive work during import:

```python
# Avoid unnecessary import-time work

large_dataset = load_entire_dataset()
train_model()
connect_to_external_service()
```

Instead, put expensive operations inside functions:

```python
def load_dataset():
    return load_entire_dataset()
```

This makes importing the module safer and more predictable.

---

## 17. Avoid Unnecessary Import-Time Side Effects

Importing a module should not unexpectedly:

* Create files
* Modify databases
* Start network connections
* Launch applications
* Perform expensive computations
* Delete data
* Print large amounts of output

For example, avoid:

```python
connect_to_database()
```

at module level unless the application's architecture explicitly requires it.

Prefer controlled initialization:

```python
def create_connection():
    return connect_to_database()
```

The caller can then decide when the operation should occur.

---

## 18. Separate Configuration from Application Logic

Configuration values should not be scattered throughout unrelated modules.

For example:

```python
# configuration.py

DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
```

Other modules can import the configuration they need:

```python
from configuration import DEFAULT_TIMEOUT
```

For larger applications, configuration management may require more sophisticated approaches, but separating configuration concepts is a useful foundation.

---

## 19. Avoid Hard-Coded Environment-Specific Paths

Avoid:

```python
DATA_PATH = "C:\\Users\\Name\\Desktop\\project\\data"
```

Such paths are tied to one machine.

Prefer:

```python
from pathlib import Path

DATA_PATH = Path("data")
```

or obtain environment-specific paths through deliberate configuration.

This improves portability between development machines, servers, containers, and deployment environments.

---

## 20. Use Type Hints Where They Improve Clarity

Type hints can make module interfaces easier to understand.

Example:

```python
def calculate_average(values: list[float]) -> float:
    return sum(values) / len(values)
```

A caller can immediately understand:

* What the function expects
* What the function returns

Type hints are especially useful in larger projects with many modules.

---

## 21. Write Useful Docstrings

Public modules, functions, and classes can benefit from meaningful documentation.

Example:

```python
"""Utilities for validating application input."""


def is_valid_username(username: str) -> bool:
    """Return True when username satisfies the application's rules."""
    return username.isidentifier()
```

Docstrings should explain purpose and behavior rather than restating obvious syntax.

---

## 22. Avoid Overengineering

Good module design does not mean creating dozens of files for a tiny program.

For example, a simple script may reasonably contain:

```text
hello.py
```

There is no need to create:

```text
application/
├── core/
├── services/
├── utilities/
├── managers/
├── adapters/
└── infrastructure/
```

for a program that only prints one message.

Use modular structure when it provides meaningful organizational or reuse benefits.

---

## 23. Organize Growing Projects into Packages

As an application grows, related modules can be grouped into packages.

For example:

```text
application/
├── __init__.py
├── main.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── data/
│   ├── __init__.py
│   └── loader.py
└── validation/
    ├── __init__.py
    └── rules.py
```

The exact structure depends on the application's requirements.

The objective is to make responsibilities and dependencies understandable.

---

## 24. Keep Dependency Direction Understandable

A healthy project structure generally has understandable dependency relationships.

For example:

```text
main
 ↓
services
 ↓
data
```

A lower-level module should not unnecessarily depend on a higher-level application module.

Unclear dependency direction can lead to:

* Circular imports
* Tight coupling
* Difficult testing
* Difficult maintenance

Design modules so that dependencies follow clear architectural boundaries.

---

## 25. Test Modules Independently

Well-designed modules can often be tested independently.

For example:

```python
def add(first: int, second: int) -> int:
    return first + second
```

can be tested without running an entire application.

This is one advantage of separating reusable logic from application startup code.

Modular design and testing therefore reinforce each other.

---

## 26. Keep Third-Party Dependencies Controlled

A module should not introduce unnecessary external dependencies.

For example, if:

```python
from pathlib import Path
```

is sufficient, adding an external package solely for basic path operations creates unnecessary complexity.

When a third-party dependency is genuinely needed, document and manage it through the project's dependency system.

---

## 27. Avoid Module-Level Mutable Objects as Shared State

Be careful with module-level mutable objects such as:

```python
cache = {}
```

or:

```python
users = []
```

These objects can become hidden shared state across the application.

If shared state is necessary, design and document it deliberately.

Otherwise, prefer explicit ownership and data flow.

---

## 28. Use Stable Interfaces

Once other parts of a project depend on a module, changing its public functions or classes can affect many files.

For example:

```python
def calculate_total(items: list[float]) -> float:
    ...
```

If other modules rely on this function, changing its name or parameters requires corresponding updates.

Stable module interfaces reduce unnecessary changes across a project.

---

## 29. Check Imports Before Adding New Dependencies

When implementing functionality, ask:

1. Does Python's standard library already provide what I need?
2. Can the functionality be implemented simply without an external dependency?
3. If not, is there a well-maintained third-party package appropriate for the project?

This approach keeps dependency decisions deliberate.

---

## 30. Design for the Project's Current Scale

Module design should evolve with the project.

A small application may need only:

```text
project/
├── main.py
└── utils.py
```

A larger application may eventually require:

```text
project/
├── src/
│   └── application/
│       ├── main.py
│       ├── data/
│       ├── services/
│       └── validation/
└── tests/
```

There is no universal directory structure that is correct for every Python project.

The important principles are clear responsibilities, manageable dependencies, readable interfaces, and maintainability.

---

## Common Mistakes

### 1. Creating One Giant Module

A module containing hundreds of unrelated functions becomes difficult to navigate and maintain.

Split functionality according to meaningful responsibilities.

### 2. Creating Too Many Tiny Modules

Excessive fragmentation can be just as problematic.

Do not create a separate module for every small function without a meaningful reason.

### 3. Using Wildcard Imports

Avoid:

```python
from module import *
```

Prefer explicit imports.

### 4. Running Application Logic During Import

Avoid unnecessary side effects at module level.

Use functions and a main guard when appropriate.

### 5. Creating Circular Dependencies

Reconsider module responsibilities when two modules depend directly on each other.

### 6. Hard-Coding Machine-Specific Paths

Use `pathlib` and configuration instead of paths tied to a specific computer.

### 7. Hiding Dependencies

A module should make its important dependencies clear through its imports and interfaces.

### 8. Ignoring Package Context

Relative imports require package context. Use appropriate package execution patterns.

---

## Best Practices Checklist

Before considering a module complete, ask:

* Does the module have a clear responsibility?
* Is its name meaningful?
* Are imports explicit and readable?
* Does it avoid unnecessary global state?
* Does it avoid unnecessary import-time side effects?
* Are public functions and classes clearly defined?
* Are type hints useful for its interfaces?
* Are docstrings provided where appropriate?
* Are dependencies reasonable?
* Could the module be tested independently?
* Are package relationships understandable?
* Does the project avoid unnecessary complexity?

---

## Key Takeaways

* Keep modules focused on clear responsibilities.
* Use meaningful module and package names.
* Prefer explicit imports.
* Avoid wildcard imports.
* Minimize mutable global state.
* Keep module initialization lightweight.
* Use the main guard for modules that are both reusable and directly executable.
* Avoid circular imports by designing clear dependencies.
* Use packages to organize growing applications.
* Prefer standard-library solutions when they are sufficient.
* Manage third-party dependencies deliberately.
* Design modules for readability, testing, reuse, and maintainability.
