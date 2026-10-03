"""Show that repeated imports normally reuse the cached module object."""

import json
import sys

same_object = json is sys.modules["json"]
print(f"json is cached in sys.modules: {same_object}")
