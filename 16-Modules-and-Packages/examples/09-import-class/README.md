# Import Class

This example demonstrates how to import a class from Python's built-in `datetime` module and use it to create and work with a date object.

## Files

```text
09-import-class/
├── README.md
└── import_class.py
```

## Example

The program imports the `date` class directly from the `datetime` module:

```text
from datetime import date
```

It then calls the class method `today()`:

```text
today = date.today()
```

The returned object represents the current local date.

## Key Concept

A module can contain classes as well as functions.

In this example:

```text
from datetime import date
```

imports the `date` class from the standard-library `datetime` module.

The class can then be referenced directly:

```text
today = date.today()
```

The imported class does not need to be prefixed with `datetime` because it was imported explicitly.

## Accessing Object Attributes

The resulting `date` object provides attributes such as:

```text
today.year
today.month
today.day
```

These values represent the individual components of the date.

## Example Code

```text
from datetime import date


today = date.today()

print(f"Today's date: {today}")
print(f"Year: {today.year}")
print(f"Month: {today.month}")
print(f"Day: {today.day}")
```

## Expected Output

The exact output depends on the date when the program is executed.

For example:

```text
Today's date: 2026-09-15
Year: 2026
Month: 9
Day: 15
```

## Learning Objective

After completing this example, you should understand how to:

* Import a class from a module
* Use `from ... import ...` with a class
* Call a class method
* Work with an object returned by an imported class
* Access attributes of the resulting object
