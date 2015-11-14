#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """Doctring
    Args:
        arg1:
        arg2:
        arg3:
    Returns:
        True or False depending on if error caught
    Examples:
        >>>exception_test('Hello', 1, 1)
        True
    caught = False
    """
    caught = 0
    try:
        arg1[arg2].index(arg3)
    except (LookupError, TypeError):
        caught = True

    return caught
