# usr/bin/env python
# -*- coding: utf-8 -*-
"""task2"""


class CustomError(Exception):
    """Constructor for CustomError."""
    def __init__(self, message, cause):
        """A constructor for CustomError.

        Args:
            Message(str) - a string
            cause(str)- a string

        Attribute:
            cause(mixed): Any value that is inputed.
        """
        Exception.__init__(self)
        self.cause = cause
        self.message = message
