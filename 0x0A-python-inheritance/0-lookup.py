#!/usr/bin/python3
# 0-lookup.py
"""Define an object attribute lookup function."""


def look(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
