"""Read an installed package's version without assuming it is installed."""

from importlib import metadata

try:
    print(metadata.version("pip"))
except metadata.PackageNotFoundError:
    print("The package 'pip' is not installed in this environment.")
