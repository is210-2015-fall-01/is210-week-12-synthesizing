#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating custom exception classes"""


class BaseError(Exception):
    """A class called BaseError with an argument, Exception"""
    pass
    
class StringError(BaseError, TypeError):
    """A class, StringError, subclassing BaseError"""
    pass

class NumberError(BaseError, TypeError):
    """A class, NumberError, subclassing BaseErrror"""
    pass

class NonZeroError(NumberError):
    """A class, NonZero, subclassing NumberError"""
    pass
