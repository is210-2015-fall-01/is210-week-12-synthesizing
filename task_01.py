# usr/bin/env python
# -*- coding: utf-8 -*-
"""task1"""


class BaseError(Exception):
    """Class BaseError."""
    pass


class StringError(BaseError, TypeError):
    """Class StringError."""
    pass


class NumberError(BaseError, TypeError):
    """Class NumberError."""
    pass


class NonZeroError(NumberError):
    """Class NonZeroError."""
    pass
