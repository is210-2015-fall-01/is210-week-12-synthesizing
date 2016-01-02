#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Custom exception class with debugging errors."""


class CustomError(Exception):
    """Subclass. Exception."""

    def __init__(self, msg, cause):
        """Constructor.
        Args:
            Exception: for its constructor
            msg(str)
            cause(str): input
        Returns:
            A custom class exception
        Examples:
            >>> myerr = CustomError('Wow!', cause='Messed up a lot!')
            >>> print myerr.cause
            Messed up a lot!
        """
        msg = Exception.__init__(self, msg)
        self.cause = cause
