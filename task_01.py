#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 Docstring"""

class BaseError(Exception):
    """Extends Exception."""
    pass

class StringError(BaseError, TypeError):
    """Subclassed to BaseError and TypeError."""
    pass

class NumberError(BaseError, TypeError):
    """Subclassed to BaseError and TypeError."""
    pass

class NonZeroError(NumberError):
    """Subclassed to NumberError"""
