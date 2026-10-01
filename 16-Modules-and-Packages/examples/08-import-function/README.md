# Import Function

This example demonstrates how to import specific functions from Python's built-in `statistics` module.

## Files

```text
08-import-function/
├── README.md
└── import_function.py
```

## Example

The program imports two functions directly from `statistics`:

```text
from statistics import mean, median
```

The functions can then be called without using the module name:

```text
average_score = mean(scores)
middle_score = median(scores)
```

## Key Concept

The `from ... import ...` syntax allows specific names to be imported from a module.

In this example:

```text
from statistics import mean, median
```

imports:

* `mean` — calculates the arithmetic mean
* `median` — calculates the middle value of a data set

Both functions are part of Python's standard library, so no external package installation is required.

## Example Code

```text
from statistics import mean, median


scores = [72, 85, 90, 68, 95]

average_score = mean(scores)
middle_score = median(scores)

print(f"Scores: {scores}")
print(f"Mean: {average_score}")
print(f"Median: {middle_score}")
```

## Expected Output

```text
Scores: [72, 85, 90, 68, 95]
Mean: 82
Median: 85
```

## Comparison

Using specific imports:

```text
from statistics import mean

average = mean(scores)
```

Using a regular module import:

```text
import statistics

average = statistics.mean(scores)
```

Both approaches are valid. The first provides direct access to the selected function, while the second keeps the module namespace visible.

## Learning Objective

After completing this example, you should understand how to:

* Import specific functions from a module
* Import multiple names with one `from ... import ...` statement
* Use Python's standard-library modules
* Distinguish direct function access from module-qualified access
