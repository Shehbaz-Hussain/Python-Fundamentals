"""Serialize a dictionary to JSON and print the result."""

import json

profile = {"name": "Sam", "level": 2}
print(json.dumps(profile, sort_keys=True))
