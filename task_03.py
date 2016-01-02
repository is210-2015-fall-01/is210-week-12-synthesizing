#!/usr/bin/env python
# -*- coding: utf -8 -*-
"""Task 03 Docstring"""

def exception_test(arg1, arg2, arg3):
    """Function tests exceptions.

    Args:
        arg1 (bool): Boolean Value.
        arg2 (bool): Boolean Value.
        arg3 (bool): Boolean Value.

    Returns:
        Returns a special ExceptionType if any are caught.

    Examples:
        >>> exception_test(['apple'], 0, 'p')
        False
        >>> exception_test(43, 1, 1)
        True
        >>> exception_test(['apple'], 0, x)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'x' is not defined.
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except (LookupError, TypeError):
        caught = True

    return caught
