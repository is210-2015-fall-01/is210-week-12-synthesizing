#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """Adding more Errors to exception.
    Args:
        args1(mixed): arg can be different values, strings etc.
        args2(mixed): arg can be different values, strings etc.
        args3(mixed): arg can be different values, strings etc.

    Attributes:
        caught(boolean): Which defaults to False.

    Returns:
        A boolean or an error message
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except (TypeError, KeyError, IndexError):
        caught = True

    return caught
