#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""wk12 synthesizing task02"""


class CustomError(Exception):
    """A CustomError exception class.
    Attributes:
        Exception(class): an exception class.
            cause(str): a string parameter.
    Args:
        Exception: an exception class.
    """
    def __init__(self, message, cause):
        """CustomError constructor.

        Args:
            message(str): a string parameter.
            cause(str): a string parameter.
        Returns:
            Returns a custom class exception.
        Examples:
        >>> myerr = CustomError('Whoah!', cause='Messed up!')
        >>> print myerr.cause
        Messed up!
        """
        Exception.__init__(self)
        self.message = message
        self.cause = cause
