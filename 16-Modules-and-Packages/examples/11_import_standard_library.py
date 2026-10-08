"""Use standard-library modules without installing dependencies."""

import json
from pathlib import Path

record = {"name": "Python", "active": True}
encoded = json.dumps(record, sort_keys=True)

print(encoded)
print(f"Current folder: {Path.cwd().name}")
