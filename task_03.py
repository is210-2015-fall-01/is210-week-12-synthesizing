#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """Testing an exception.
    Args:
        arg1:(bool) False if any other error is found
        besdies LookupError or TypeError.
        arg2:(bool) False if any other error is found
        besdies LookupError or TypeError.
        arg3:(bool) False if any other error is found
        besdies LookupError or TypeError.
    Returns:
        Returns any uncaught exception besides LookupError or TypeError.
    Examples:
        >>> exception_test(['apple'], 0, 'p')
        False
        >>> exception_test(43, 1, 1)
        True
        >>> exception_test(['apple'], 0, x)
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        NameError: name 'x' is not defined
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except (LookupError, TypeError):
        caught = True

    return caught
