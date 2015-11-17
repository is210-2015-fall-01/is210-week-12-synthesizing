#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 Docstring"""


class CustomError(Exception):
    """Class Subclassed to Exception."""

    def __init__(self, message, cause):
        """Function takes 3 parameters.

        Args:
            self (str): string.
            cause (str): string.
            message(str): string.

        Returns:
            A string message.

        Examples:
            >>> myerr = CustomError('Whoah!', cause='Messed up!')
            >>> print myerr.cause
            Messed up!
        """

        Exception.__init__(self, message)
        self.cause = cause
