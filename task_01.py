#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 12 task_01."""


class BaseError(Exception):
    """Base error class.

    Attributes:
        None
    """
    pass


class StringError(BaseError, TypeError):
    """String error class.
    Attributes:
        None
    """
    pass


class NumberError(BaseError, TypeError):
    """Number error class.
    Attributes:
        None
    """
    pass


class NonZeroError(NumberError):
    """Non-zero error class.
    Attributes:
        None
    """
    pass
