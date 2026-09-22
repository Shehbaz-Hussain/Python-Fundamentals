# Third-Party Packages

## Overview

Python's standard library provides many useful modules, but professional software often requires functionality beyond what the standard library provides.

**Third-party packages** are Python packages developed and distributed separately from Python itself.

Examples include:

* NumPy for numerical computing
* pandas for data analysis
* Requests for HTTP requests
* Matplotlib for visualization
* scikit-learn for machine learning
* PyTorch for deep learning
* TensorFlow for machine learning and deep learning

Understanding how third-party packages differ from standard-library modules is essential for building larger Python applications.

---

## What Is a Third-Party Package?

A third-party package is software created outside the Python standard library and distributed separately.

For example:

```python
import requests
```

The `requests` package is not included in Python's standard library.

It normally needs to be installed into the Python environment before it can be imported.

By comparison:

```python
import json
```

uses `json`, which is part of Python's standard library.

---

## Standard Library vs Third-Party Package

The distinction can be summarized as follows:

| Type             | Example        | Normally Installed Separately? |
| ---------------- | -------------- | ------------------------------ |
| Standard library | `json`         | No                             |
| Standard library | `pathlib`      | No                             |
| Standard library | `math`         | No                             |
| Third-party      | `numpy`        | Yes                            |
| Third-party      | `pandas`       | Yes                            |
| Third-party      | `requests`     | Yes                            |
| Third-party      | `scikit-learn` | Yes                            |

The installation requirement depends on the Python distribution and project environment, but third-party dependencies are generally managed separately from the Python standard library.

---

## Installing Third-Party Packages

The Python packaging ecosystem commonly uses **pip** to install packages.

For example:

```bash
python -m pip install requests
```

After installation, the package can be imported:

```python
import requests

response = requests.get("https://example.com")

print(response.status_code)
```

Using:

```bash
python -m pip
```

helps ensure that `pip` is associated with the Python interpreter being used by the command.

---

## Installing a Specific Version

Projects may require a particular package version.

For example:

```bash
python -m pip install requests==2.32.5
```

The exact version should be chosen according to the project's compatibility requirements rather than copied blindly.

Version constraints become increasingly important as projects grow and dependencies interact with one another.

---

## Upgrading a Package

An installed package can be upgraded with:

```bash
python -m pip install --upgrade requests
```

However, upgrading dependencies in a production project should be deliberate.

A newer version can introduce:

* New features
* Bug fixes
* Performance improvements
* Deprecations
* Breaking changes
* Changes in dependency requirements

Professional projects should therefore test dependency upgrades rather than updating everything without verification.

---

## Uninstalling a Package

A package can be removed with:

```bash
python -m pip uninstall requests
```

The command normally asks for confirmation before removing the package.

Only remove a package when it is no longer required by the environment or project.

---

## Virtual Environments

Third-party packages should generally be installed inside a project's virtual environment instead of globally.

A virtual environment creates an isolated Python environment for a project.

Create one with:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Then install the dependency:

```bash
python -m pip install requests
```

On an activated environment, the package is installed for that environment rather than being added to the system Python installation.

---

## Why Virtual Environments Matter

Different projects may require different package versions.

For example:

```text
Project A
└── requests 2.x

Project B
└── requests 3.x
```

Installing everything globally can create conflicts.

Virtual environments allow projects to maintain separate dependency sets.

This becomes especially important in:

* Web development
* Data science
* Machine learning
* Deep learning
* AI engineering
* Automation
* Backend development

---

## Installing Multiple Packages

Multiple dependencies can be installed together:

```bash
python -m pip install numpy pandas
```

However, professional projects should keep dependency management reproducible.

A dependency file can record required packages.

For example:

```text
requests==2.32.5
```

A project can then install the recorded dependencies:

```bash
python -m pip install -r requirements.txt
```

The exact dependency-management approach may vary between projects.

---

## `requirements.txt`

A `requirements.txt` file commonly contains project dependencies.

Example:

```text
requests==2.32.5
numpy==2.3.2
```

A project can install them with:

```bash
python -m pip install -r requirements.txt
```

The file should contain dependencies that the project actually requires.

Avoid adding unrelated packages simply because they happen to exist in the local environment.

---

## Importing an Installed Package

After installation, importing a package usually follows its documented Python import name.

For example, the package installation name and import name can differ.

A common example is:

```bash
python -m pip install scikit-learn
```

but the Python import is:

```python
import sklearn
```

This distinction is important because **distribution/package names and import names are not always identical**.

Always consult the package's documentation for the correct import syntax.

---

## Package Dependencies

Third-party packages can depend on other packages.

For example:

```text
Application
├── Package A
│   └── Dependency C
└── Package B
    └── Dependency D
```

Installing a package can therefore install additional dependencies required by that package.

This dependency graph is one reason professional Python projects need controlled environments and reproducible dependency management.

---

## Dependency Compatibility

Packages may have compatibility requirements involving:

* Python versions
* Operating systems
* CPU architectures
* Other packages
* Specific dependency versions

For example, a package may support:

```text
Python 3.11+
```

while another package may require a different Python version.

Before installing a dependency, check its documentation and compatibility information.

---

## Third-Party Packages in AI Development

Third-party packages are particularly important in AI engineering.

A typical AI project may use packages such as:

```text
NumPy
pandas
scikit-learn
PyTorch
Transformers
```

Each package solves a specialized problem.

For example:

```python
import numpy as np
```

can provide efficient numerical arrays.

```python
import pandas as pd
```

can provide tabular data processing.

```python
from sklearn.model_selection import train_test_split
```

can provide utilities for preparing machine-learning datasets.

The standard library provides the foundation, while specialized third-party packages extend Python's capabilities.

---

## Choosing a Third-Party Package

Do not select a package only because it appears in a tutorial.

Evaluate factors such as:

* Documentation quality
* Maintenance activity
* Compatibility
* License
* Community adoption
* Security considerations
* Dependency requirements
* Project maturity
* Performance
* Long-term suitability

The best package is not necessarily the most popular package.

---

## Avoiding Unnecessary Dependencies

Third-party dependencies introduce additional complexity.

For example, if the standard library provides an adequate solution:

```python
from pathlib import Path
```

there may be no reason to add an external dependency merely to perform basic path operations.

Fewer unnecessary dependencies can make a project easier to:

* Install
* Maintain
* Test
* Deploy
* Upgrade
* Audit

This does not mean avoiding dependencies completely. Specialized projects often require them.

---

## Package Documentation

Before using a third-party package, read its official documentation.

Documentation should be used to determine:

* Installation instructions
* Supported Python versions
* Import names
* API usage
* Configuration
* Exceptions
* Compatibility
* Recommended practices

Do not assume that an API shown in an old tutorial still matches the current package version.

---

## Common Mistakes

### 1. Installing Packages Globally

Installing every project dependency into the system Python environment can cause conflicts.

Prefer project-specific virtual environments.

---

### 2. Using the Wrong Python Environment

A package may appear to be installed but still produce:

```text
ModuleNotFoundError
```

if the program is running with a different Python interpreter.

Check the active interpreter and environment before reinstalling packages repeatedly.

---

### 3. Confusing Installation Names and Import Names

For example:

```bash
python -m pip install scikit-learn
```

does not mean:

```python
import scikit-learn
```

Python import syntax does not allow that package name in this form.

The correct import is:

```python
import sklearn
```

---

### 4. Installing Packages Without Checking Compatibility

A package can fail because of incompatible:

* Python versions
* Operating systems
* Dependency versions
* Binary components

Check compatibility before changing the environment.

---

### 5. Adding Unused Dependencies

Avoid installing packages simply because they might be useful later.

Add dependencies when the project actually requires them.

---

### 6. Blindly Copying Installation Commands

Installation commands from old tutorials may specify outdated versions.

Use current official package documentation and verify compatibility with the project's Python version.

---

## Best Practices

* Use a virtual environment for project dependencies.
* Install packages with `python -m pip`.
* Check official documentation before installation.
* Verify Python and package compatibility.
* Keep project dependencies explicit.
* Avoid unnecessary dependencies.
* Use version constraints when reproducibility requires them.
* Test dependency upgrades.
* Understand the difference between package names and import names.
* Keep development and production dependencies appropriately organized.
* Do not rely on globally installed packages.

---

## Key Takeaways

* Third-party packages extend Python beyond the standard library.
* They are distributed separately from Python.
* `pip` is commonly used to install them.
* Virtual environments isolate project dependencies.
* A package's installation name may differ from its Python import name.
* Third-party packages are essential for many AI, machine-learning, data-science, and software-engineering workflows.
* Dependencies should be selected deliberately and managed reproducibly.
* The standard library should be considered before adding an external dependency.
