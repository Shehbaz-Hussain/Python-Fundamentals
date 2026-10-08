"""Import a class from a custom module."""

from pathlib import Path

project_folder = Path(__file__).resolve().parents[2]
print(f"Project folder: {project_folder.name}")
