#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Some debugging practice."""


class CustomError(Exception):
    """CustomError extends the Exception class."""

    def __init__(self, msg, cause):
        """Constructor docstring."""
        self.msg = msg
        self.cause = cause
