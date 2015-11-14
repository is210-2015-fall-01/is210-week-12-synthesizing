#!user/bin/env python
# -*- coding: utf-8 -*-
"""Customer Exceptions"""


class BaseError(Exception):
    """Base Error"""
    pass


class StringError(BaseError, TypeError):
    """Subclasses from BaseError and TypeError"""
    pass


class NumberError(BaseError, TypeError):
    """Subclasses from BaseError, TypeError"""
    pass


class NonZeroError(NumberError):
    """Subclasses from NumberError"""
    pass
