"""Explain why package-relative imports need a package context."""

relative_statement = "from .helpers import format_name"
print(f"Example relative import: {relative_statement}")
print("Run package modules with `python -m package.module` from the project root.")
