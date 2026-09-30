# `__name__` Variable

This example demonstrates the special `__name__` variable provided by Python modules.

## Files

```text
05-name-variable/
├── README.md
└── name_variable.py
```

## Example

The Python file contains:

```text
print(f"Module name: {__name__}")
```

When the file is executed directly, Python sets:

```text
__name__ == "__main__"
```

Therefore, running the file produces:

```text
Module name: __main__
```

## Key Concept

Every Python module has a `__name__` variable.

Its value depends on how the module is used.

When a file is executed directly:

```text
__name__ == "__main__"
```

When the file is imported, `__name__` normally contains the module's import name.

For example, if `name_variable.py` is imported as a module:

```text
import name_variable
```

then the imported module's `__name__` is:

```text
name_variable
```

This behavior is the foundation of the common main guard pattern:

```text
if __name__ == "__main__":
    main()
```

## Expected Output

When running `name_variable.py` directly:

```text
Module name: __main__
```

## Learning Objective

After completing this example, you should understand:

* What the `__name__` variable represents
* Why its value is `"__main__"` during direct execution
* How `__name__` differs when a module is imported
* How `__name__` supports the main guard pattern
