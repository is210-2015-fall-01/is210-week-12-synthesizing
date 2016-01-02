#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is task_02 docstring."""


class CustomError(Exception):
    """This is a CustomError class."""

    def __init__(self, msg, cause):
        """This is a constructor for the CustomError class.

        This is the constructor of the CustomError class. This class inheritts
        from the Exeption class and does some error handling.

        Args:
            msg (str): An error message.
            cause (str): What triggered the error.

        Returns:
            None
        """
        self.cause = cause
        Exception.__init__(self, msg)
