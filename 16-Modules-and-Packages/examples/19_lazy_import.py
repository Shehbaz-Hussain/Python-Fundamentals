"""Import a module inside a function when it is needed."""


def make_identifier(value):
    """Return a URL-safe identifier for a string."""
    from urllib.parse import quote

    return quote(value.strip().lower())


if __name__ == "__main__":
    print(make_identifier("Modules & Packages"))
