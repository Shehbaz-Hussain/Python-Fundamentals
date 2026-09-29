# Import Alias

This example demonstrates how to assign an alias to an imported module using the `as` keyword.

## Files

```text
03-import-alias/
├── README.md
└── import_alias.py
```

## Example

The Python file imports the `math` module with the alias `math_tools`:

```text
import math as math_tools


radius = 5

area = math_tools.pi * radius**2

print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
```

## Key Concept

The statement:

```text
import math as math_tools
```

binds the imported module to the name `math_tools` in the current namespace.

The module's members can then be accessed through the alias:

```text
math_tools.pi
```

The alias does not create a different module. It provides another name by which the imported module can be referenced in the current namespace.

## When Aliases Are Useful

Aliases can be useful when:

* A module has a long name
* A conventional alias is commonly used
* A name would otherwise conflict with another name
* The alias improves readability in a particular context

Avoid arbitrary aliases that make code harder to understand.

## Expected Output

```text
Radius: 5
Area: 78.54
```

## Learning Objective

After completing this example, you should understand how to:

* Use `import ... as ...`
* Assign an alias to an imported module
* Access module members through an alias
* Understand that an alias does not create a separate module
