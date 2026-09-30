# Main Guard

This example demonstrates the standard Python main guard pattern.

## Files

```text
06-main-guard/
├── README.md
└── main_guard.py
```

## Example

The program defines a `main()` function:

```text
def main():
    """Run the main program."""
    print("Program started.")
```

The main guard calls `main()` only when the file is executed directly:

```text
if __name__ == "__main__":
    main()
```

When `main_guard.py` is executed directly, Python sets:

```text
__name__ == "__main__"
```

The condition is therefore true, and `main()` runs.

## Expected Output

```text
Program started.
```

## Import Behavior

If another Python file imports `main_guard.py`:

```text
import main_guard
```

the following condition is false:

```text
main_guard.__name__ == "__main__"
```

The `main()` function is available through the imported module, but it is not called automatically.

It can be called explicitly:

```text
main_guard.main()
```

## Key Concept

The main guard separates reusable module definitions from code that should run during direct execution.

The standard pattern is:

```text
if __name__ == "__main__":
    main()
```

Not every Python module requires a main guard. It is appropriate when a module also provides behavior intended for direct execution.

## Learning Objective

After completing this example, you should understand:

* The purpose of the main guard
* How `__name__` controls the condition
* The difference between direct execution and importing
* How to structure executable Python modules
