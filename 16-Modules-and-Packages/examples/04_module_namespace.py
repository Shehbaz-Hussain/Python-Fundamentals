"""Inspect names exposed by an imported module."""

import math

public_names = [name for name in dir(math) if not name.startswith("_")]
print(f"math.pi: {math.pi}")
print(f"Number of public names: {len(public_names)}")
print(f"Contains sqrt: {'sqrt' in public_names}")
