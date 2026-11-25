"""Expose greet as the only public name from this module."""

__all__ = ["greet"]


def greet(name):
    """Return a greeting for name."""
    return f"Hello, {name}!"


def internal_format(name):
    """Format an internal diagnostic message."""
    return f"internal: {name}"


if __name__ == "__main__":
    print(", ".join(__all__))
    print(greet("Sam"))
