"""Use several useful standard-library modules."""

import statistics
import textwrap

values = [12, 14, 15, 19]
print(f"Mean: {statistics.mean(values)}")
print(textwrap.fill("The standard library ships with Python.", width=24))
