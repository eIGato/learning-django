#!/usr/bin/env python

from .common import *
try:
    from .local import *
except ImportError:
    pass
