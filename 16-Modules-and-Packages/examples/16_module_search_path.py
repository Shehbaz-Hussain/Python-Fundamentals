"""Inspect Python's module search path."""

import sys

print("Python searches these locations for imports:")
for location in sys.path:
    print(f"- {location or '.'}")
