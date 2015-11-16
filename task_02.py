#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 12 task_02."""


class CustomError(Exception):
    """CustomError class.
    Args:
        None.
    """

    def __init__(self, message, cause):
        """This funcrion debug custom error.

        Arguments:
            self(mix): a string valuers.
            cause(str): a string.
            message(str): a string.

        Returns:
            Returns values.

        Examples:
            >>> myerr = CustomError('Whoah!', cause='Messed up!')
            >>> print myerr.cause
            Messed up!
        """
        Exception.__init__(self, message)
        self.cause = cause
