# Absolute Import Syntax

## Overview

An **absolute import** specifies the complete import path starting from the top-level package or importable module.

Basic syntax:

```python
from package.module import name
```

Example:

```python
from application.utils import format_name
```

Absolute imports make the location of an imported object explicit.

---

## Import a Module

```python
import application.utils
```

Use the imported module through its namespace:

```python
application.utils.format_name("Aisha")
```

---

## Import from a Package

```python
from application import utils
```

Then:

```python
utils.format_name("Aisha")
```

---

## Import a Specific Name

```python
from application.utils import format_name
```

Then:

```python
format_name("Aisha")
```

---

## Import Multiple Names

```python
from application.utils import format_name, normalize_text
```

Use them directly:

```python
format_name("Aisha")
normalize_text("  Python  ")
```

---

## Absolute Import with an Alias

A module can be given an alias:

```python
import application.utils as utils
```

Use:

```python
utils.format_name("Aisha")
```

A specific name can also be aliased:

```python
from application.utils import format_name as format_user_name
```

---

## Nested Packages

For nested packages:

```text id="j0b2kl"
application/
├── __init__.py
├── core/
│   ├── __init__.py
│   └── processing.py
└── utils/
    ├── __init__.py
    └── formatting.py
```

An absolute import can be:

```python
from application.utils.formatting import format_name
```

Another example:

```python
from application.core.processing import process_data
```

---

## Absolute vs Relative

Absolute import:

```python
from application.utils import formatting
```

Relative import:

```python
from .utils import formatting
```

The absolute form identifies the package from the top-level import path.

The relative form identifies the location relative to the current package.

---

## Import from the Top-Level Package

Suppose:

```text id="6q2bsm"
project/
└── application/
    ├── __init__.py
    └── config.py
```

An absolute import is:

```python
from application import config
```

Then:

```python
print(config.SETTINGS)
```

---

## Executing Package Modules

Absolute imports are commonly used in package-based applications:

```python
from application.utils import format_name
```

Run the application or module with its package context:

```bash
python -m application.main
```

This is particularly useful when the package contains multiple modules and subpackages.

---

## Absolute Import in `__init__.py`

Within a package initializer, imports can use the package's full path:

```python
from application.utils.formatting import format_name
```

However, package-internal imports often use relative imports instead:

```python
from .utils.formatting import format_name
```

The appropriate choice depends on the package's structure and import design.

---

## Common Mistakes

### 1. Incorrect Package Path

If the structure is:

```text
application/
└── utils/
    └── formatting.py
```

the import must match the actual hierarchy:

```python
from application.utils.formatting import format_name
```

---

### 2. Omitting the Top-Level Package

This:

```python
from utils.formatting import format_name
```

may be incorrect if `utils` is actually a subpackage of `application`.

Use:

```python
from application.utils.formatting import format_name
```

when `application` is the intended top-level package.

---

### 3. Running a Package Module Directly

A module containing package imports may fail when executed as a standalone file:

```bash
python application/main.py
```

When package context is required, use:

```bash
python -m application.main
```

---

### 4. Confusing Import and File Paths

Python imports use module names:

```python
from application.utils import formatting
```

They do not normally use filesystem syntax such as:

```python
from application/utils import formatting
```

---

## Quick Reference

### Import module

```python
import package.module
```

### Import module with `from`

```python
from package import module
```

### Import specific name

```python
from package.module import name
```

### Import multiple names

```python
from package.module import name_a, name_b
```

### Module alias

```python
import package.module as module
```

### Name alias

```python
from package.module import name as alias
```

### Nested package

```python
from package.subpackage.module import name
```

### Execute package module

```bash
python -m package.module
```

## Core Principle

Use absolute imports when you want dependencies expressed through the package's complete import path:

```python
from application.utils.formatting import format_name
```

Keep import paths consistent with the package hierarchy and execute package modules with appropriate package context.
