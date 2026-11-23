"""Check sys.modules for math after importing it."""

import math
import sys

print("math" in sys.modules)
