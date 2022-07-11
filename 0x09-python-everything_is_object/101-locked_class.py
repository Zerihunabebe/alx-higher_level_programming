#!/usr/bin/python3
# 101-locked_class.py
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LocedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
