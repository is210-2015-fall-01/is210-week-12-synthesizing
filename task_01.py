#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is task_01 docstring."""


class BaseError(Exception):
    """This is a BaseError class."""
    pass


class StringError(BaseError, TypeError):
    """This is a StrinError class."""
    pass


class NumberError(BaseError, TypeError):
    """This is a NumberError class."""
    pass


class NonZeroError(NumberError):
    """This is a NonZeroError class."""
    pass
