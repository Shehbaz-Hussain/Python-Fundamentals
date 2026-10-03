"""Check whether a module can be discovered without importing it."""

from importlib.util import find_spec

for module_name in ("json", "statistics", "module_that_does_not_exist"):
    available = find_spec(module_name) is not None
    print(f"{module_name}: {'available' if available else 'not found'}")
