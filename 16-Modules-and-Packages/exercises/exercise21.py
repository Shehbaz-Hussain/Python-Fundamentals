"""Check whether Python can find the json module."""

from importlib.util import find_spec

print(find_spec("json") is not None)
