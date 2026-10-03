"""Use an absolute import from a package."""

from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
print(f"An absolute import names a package from its top-level name.")
print(f"Example package root: {project_root.name}")
