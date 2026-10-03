"""Use __all__ to document a module's intended public names."""

__all__ = ["greet"]


def greet(name):
    """Return a greeting for name."""
    return f"Hello, {name}!"


def _format_debug_message(name):
    """Internal helper not included in the public exports."""
    return f"debug: {name}"


if __name__ == "__main__":
    print(", ".join(__all__))
    print(greet("Sam"))
