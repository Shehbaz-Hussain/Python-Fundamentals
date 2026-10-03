"""Keep reusable module imports free of application side effects."""


def build_message(name):
    """Return a message without printing or prompting during import."""
    return f"Welcome, {name}!"


def main():
    """Demonstrate the module's behavior when run directly."""
    print(build_message("Python learner"))


if __name__ == "__main__":
    main()
