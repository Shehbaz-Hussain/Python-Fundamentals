"""Show relative-import notation used within a package."""

relative_import = "from .helpers import format_name"
parent_import = "from ..shared import settings"

print(relative_import)
print(parent_import)
print("Relative imports are used from within package modules.")
