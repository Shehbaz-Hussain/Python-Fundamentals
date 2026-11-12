"""Print each entry in Python's module search path."""

import sys

for index, path in enumerate(sys.path, start=1):
    print(f"{index}. {path or '.'} (current directory)")
