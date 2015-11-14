#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Wk12 Synthesizing task01"""


class BaseError(Exception):
    """Error based from Exception."""
    pass


class StringError(BaseError, TypeError):
    """Error is based from BaseError and Type Error."""
    pass


class NumberError(BaseError, TypeError):
    """Error based from BaseError and Type Error."""
    pass


class NonZeroError(NumberError):
    """Error based from NumberError."""
    pass
