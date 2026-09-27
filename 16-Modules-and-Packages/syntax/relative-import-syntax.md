# Relative Import Syntax

## Overview

A **relative import** specifies an import path relative to the current package.

Basic syntax:

```python
from .module import name
```

Relative imports are used inside packages to reference modules and subpackages within the same package hierarchy.

---

## Current Package

A single dot represents the current package:

```python
from .utils import format_name
```

Example structure:

```text
application/
├── __init__.py
├── main.py
└── utils.py
```

Inside `main.py`:

```python
from .utils import format_name
```

---

## Import a Module

```python
from . import utils
```

Then:

```python
utils.format_name("Aisha")
```

This imports the `utils` module from the current package.

---

## Import a Specific Name

```python
from .utils import format_name
```

Then:

```python
format_name("Aisha")
```

---

## Import Multiple Names

```python
from .utils import format_name, normalize_text
```

Use them directly:

```python
format_name("Aisha")
normalize_text(" Python ")
```

---

## Parent Package

Two dots represent the parent package:

```python
from ..utils import format_name
```

Example:

```text
application/
├── __init__.py
├── utils/
│   ├── __init__.py
│   └── formatting.py
└── features/
    ├── __init__.py
    └── reports/
        ├── __init__.py
        └── summary.py
```

Inside `summary.py`, the exact number of dots must match the desired package level.

---

## Relative Import from a Subpackage

Suppose:

```text
application/
├── __init__.py
└── services/
    ├── __init__.py
    ├── api.py
    └── formatting.py
```

Inside `api.py`:

```python
from .formatting import format_name
```

The single dot refers to `services`.

---

## Import from a Parent Package

Suppose:

```text
application/
├── __init__.py
├── utils.py
└── services/
    ├── __init__.py
    └── api.py
```

Inside `api.py`:

```python
from ..utils import format_name
```

The two dots move from `services` to its parent package, `application`.

---

## Relative Import with a Subpackage

A relative import can reference a nested module:

```python
from .utils.formatting import format_name
```

Example:

```text
application/
├── __init__.py
└── services/
    ├── __init__.py
    ├── api.py
    └── utils/
        ├── __init__.py
        └── formatting.py
```

Inside `api.py`:

```python
from .utils.formatting import format_name
```

---

## Relative Import Syntax

### Current package

```python
from .module import name
```

### Current package module

```python
from . import module
```

### Parent package

```python
from ..module import name
```

### Parent package module

```python
from .. import module
```

### Nested module

```python
from .subpackage.module import name
```

---

## Relative vs Absolute Import

Absolute:

```python
from application.utils import formatting
```

Relative:

```python
from .utils import formatting
```

Absolute imports describe the package path from the top-level package.

Relative imports describe the location relative to the current package.

---

## Package Context Requirement

Relative imports depend on package context.

For example:

```python
from .utils import formatting
```

may fail if the file is executed directly:

```bash
python application/main.py
```

because Python may not treat the file as part of the expected package hierarchy.

When package context is required, execute the module with:

```bash
python -m application.main
```

---

## Common Mistakes

### 1. Using Relative Imports in a Standalone Script

This may fail:

```python
from .utils import formatting
```

when the file is executed directly as a standalone script.

Relative imports are intended for package contexts.

---

### 2. Incorrect Number of Dots

The number of dots determines how far Python moves upward through the package hierarchy.

For example:

```python
from .utils import helper
```

references the current package.

```python
from ..utils import helper
```

references the parent package's `utils` module.

Use only as many levels as the package structure requires.

---

### 3. Confusing Relative Imports with Filesystem Paths

Do not use filesystem syntax:

```python
from ../utils import helper
```

Python relative imports use dots:

```python
from ..utils import helper
```

---

### 4. Mixing Import Strategies Without Reason

A package should use a consistent import strategy.

Avoid unnecessarily switching between absolute and relative imports throughout the same package.

---

## Quick Reference

### Current package

```python
from .module import name
```

### Current package module

```python
from . import module
```

### Parent package

```python
from ..module import name
```

### Parent package module

```python
from .. import module
```

### Nested module

```python
from .subpackage.module import name
```

### Execute package module

```bash
python -m package.module
```

## Core Principle

Use relative imports to express dependencies within a package hierarchy:

```python
from .utils import helper
```

Remember that relative imports require an appropriate package context and use dots to describe the relationship between packages and modules.
