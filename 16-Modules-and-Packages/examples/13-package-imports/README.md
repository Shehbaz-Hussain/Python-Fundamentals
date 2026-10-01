# Package Imports

This example demonstrates how Python modules can be imported and accessed through their module namespace.

## Files

```text
13-package-imports/
├── README.md
└── package_imports.py
```

## Example

The program imports Python's built-in `statistics` module:

```text
import statistics
```

Functions provided by the module are then accessed through the module namespace:

```text
statistics.mean(scores)
statistics.median(scores)
```

## Key Concept

A package can contain modules, and modules can provide functions, classes, and other objects.

The Python standard library contains many organized modules. In this example, the `statistics` module provides functions for common statistical calculations.

Using:

```text
import statistics
```

keeps the imported names under the `statistics` namespace.

This makes the source of each function explicit:

```text
statistics.mean(...)
statistics.median(...)
```

This style can improve readability and reduce naming conflicts in larger programs.

## Example Code

```text
import statistics


scores = [72, 85, 90, 68, 95]

average_score = statistics.mean(scores)
middle_score = statistics.median(scores)

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

## Learning Objective

After completing this example, you should understand how to:

* Import a module using `import`
* Access module members through dot notation
* Keep imported names organized under a module namespace
* Use functions provided by the Python standard library
* Understand how modular organization supports maintainable code
