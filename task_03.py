#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """Exception test function.

    This function demonstrates the exception handling via one except
    clause.

    Args:
        arg1 (mixed): A string, character or integer.
        agr2 (int): An integer to serve as index.
        arg3 (int): An integer to serve as index.
    Returns:
        False or True (Boolean): True ot False value for the test.
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except(TypeError, KeyError, IndexError):
        caught = True

    return caught
