#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """A function testing exceptions.

    Args:
        Has three arguments; args1, args2, args3.

    Attributes:
        caught(boolean): Either true or false.

    Returns:
        A boolean or an error

    Example:
        >>> exception_test(['apple'], 0,'p')
        False
        >>> exception_test(43, 1, 1)
        True     
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except (TypeError, KeyError, IndexError):
        caught = True
    return caught
    
