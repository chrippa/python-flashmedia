#!/usr/bin/env python

from .compat import bytes, is_py2

def isstring(val):
    if is_py2:
        return isinstance(val, str) or isinstance(val, unicode)
    else:
        return isinstance(val, str)

def byte(ordinal):
    if isstring(ordinal):
        ordinal = ord(ordinal)

    return bytes((ordinal,))

class flagproperty(object):
    def __init__(self, flags, attr, boolean=False):
        self.flags = flags
        self.attr = attr
        self.boolean = boolean

    def __get__(self, obj, cls):
        flags = getattr(obj, self.flags)
        val = getattr(flags.bit, self.attr)

        if self.boolean:
            val = bool(val)

        return val

    def __set__(self, obj, val):
        flags = getattr(obj, self.flags)
        setattr(flags.bit, self.attr, int(val))


__all__ = ["byte", "isstring", "flagproperty"]

