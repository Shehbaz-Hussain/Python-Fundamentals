# Images Directory

## Introduction

The `images` folder stores all visual resources used in **Module 09: Logical Operators**. Images help learners understand logical concepts more quickly by presenting information visually. They can also improve the overall appearance of the GitHub repository and make the documentation more engaging.

---

# Purpose of the Images Folder

The `images` folder is intended to store diagrams, illustrations, screenshots, and other visual assets related to logical operators.

Typical uses include:

- Explaining logical operators visually
- Showing truth tables
- Demonstrating operator precedence
- Illustrating short-circuit evaluation
- Supporting README files and documentation
- Improving the learning experience for beginners

---

# Recommended Diagrams

The following diagrams are recommended for this module.

## 1. Logical Operators Overview

A simple diagram showing the three logical operators:

- `and`
- `or`
- `not`

Suggested filename:

```text
logical-operators-overview.png
```

---

## 2. AND Truth Table

A visual representation of the `and` truth table.

Suggested filename:

```text
and-truth-table.png
```

---

## 3. OR Truth Table

A visual representation of the `or` truth table.

Suggested filename:

```text
or-truth-table.png
```

---

## 4. NOT Truth Table

A visual representation of the `not` truth table.

Suggested filename:

```text
not-truth-table.png
```

---

## 5. Operator Precedence

A diagram showing the evaluation order of logical operators.

Example:

```text
Highest
   │
  not
   │
  and
   │
   or
   │
Lowest
```

Suggested filename:

```text
operator-precedence.png
```

---

## 6. Short-Circuit Evaluation

A flow diagram illustrating how Python may stop evaluating an expression when the result is already known.

Suggested filename:

```text
short-circuit-evaluation.png
```

---

## 7. Logical Expression Example

A diagram showing how comparison operators and logical operators work together.

Example:

```text
age >= 18
      │
      and
      │
age <= 60
```

Suggested filename:

```text
logical-expression-example.png
```

---

# Naming Conventions

Use descriptive, lowercase filenames with hyphens.

## Recommended Examples

```text
logical-operators-overview.png
and-truth-table.png
or-truth-table.png
not-truth-table.png
operator-precedence.png
short-circuit-evaluation.png
logical-expression-example.png
```

## Avoid

```text
Image1.png
Picture.png
New File.png
Test.png
abc.png
```

Meaningful filenames make the repository easier to maintain.

---

# Supported Image Formats

The following image formats are recommended:

| Format | Recommended Use |
|---------|-----------------|
| PNG | Diagrams, screenshots, illustrations |
| SVG | Icons and scalable diagrams |
| JPG / JPEG | Photographs (rarely needed for this module) |
| WebP | Optimized images for web documentation |

For most educational diagrams, **PNG** and **SVG** are the preferred formats.

---

# Recommended Image Dimensions

Use consistent image sizes throughout the repository.

| Purpose | Recommended Size |
|----------|------------------|
| Small icons | 128 × 128 px |
| Diagrams | 800 × 600 px |
| Wide diagrams | 1200 × 675 px |
| README illustrations | 1200 × 800 px |
| GitHub social preview | 1280 × 640 px |

Choose dimensions that keep text clear and readable.

---

# Optimization Guidelines

Before adding images to the repository:

- Export images with good quality.
- Keep file sizes as small as possible without reducing readability.
- Avoid blurry or pixelated images.
- Use consistent fonts and colors across diagrams.
- Remove unnecessary whitespace.
- Use descriptive filenames.
- Organize related images together.

Optimized images improve repository performance and reduce loading time.

---

# Suggested Folder Structure

```text
assets/
└── images/
    ├── README.md
    ├── logical-operators-overview.png
    ├── and-truth-table.png
    ├── or-truth-table.png
    ├── not-truth-table.png
    ├── operator-precedence.png
    ├── short-circuit-evaluation.png
    └── logical-expression-example.png
```

---

# Best Practices

- Keep all images relevant to the module.
- Maintain a consistent visual style.
- Use high-resolution diagrams.
- Prefer vector graphics (`.svg`) when possible.
- Use meaningful filenames.
- Update images if the documentation changes.
- Store all image assets inside the `assets/images` directory.

---

# Summary

The `images` folder contains the visual resources for **Module 09: Logical Operators**. Well-designed diagrams and illustrations make concepts such as truth tables, operator precedence, and short-circuit evaluation easier to understand. Following consistent naming conventions, recommended dimensions, and optimization practices helps maintain a professional, organized, and beginner-friendly GitHub repository.