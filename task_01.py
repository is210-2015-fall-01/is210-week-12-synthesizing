#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creates custom exception class."""


class BaseError(Exception):
    """BaseError"""
    pass


class StringError(BaseError, TypeError):
    """Additional exception subclass. Base and Type"""
    pass


class NumberError(BaseError, TypeError):
    """Additional exception subclass. Base and Type"""
    pass


class NonZeroError(NumberError):
    """Additional exception subclass. Number"""
    pass
