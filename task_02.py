#!user/bin/env python
# -*- coding: utf-8 -*-
"""Customer Exceptions"""


class CustomError(Exception):
    """Subclasses from Exception.
    Arttributes:
        None
    """

    def __init__(self, _, cause):
        """Constructor.
        Args:
            Exception: calls Exception constructor
            cause (str): input to display
        Returns:
            input message for cause variable
        Examples:
            >>>myerr = CustomError('Whoah!', cause='Messed up!')
            Messed up!
        """
        _ = Exception.__init__(self)
        self.cause = cause
