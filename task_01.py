#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Extending the Exception Error Class."""


class BaseError(Exception):
    """BaseError extends the Exception class."""
    pass


class StringError(BaseError, TypeError):
    """BaseError extends the BaseError & TypeError class."""
    pass


class NumberError(BaseError, TypeError):
    """BaseError extends the BaseError & TypeError class."""
    pass


class NonZeroError(NumberError):
    """BaseError extends the NumberError class."""
    pass
