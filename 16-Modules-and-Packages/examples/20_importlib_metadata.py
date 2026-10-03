"""Look up installed package metadata using the standard library."""

from importlib import metadata

try:
    version = metadata.version("pip")
except metadata.PackageNotFoundError:
    print("The optional example package 'pip' is not installed.")
else:
    print(f"pip version: {version}")
