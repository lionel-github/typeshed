"""Stub file for the 'time' module."""
# This is an autogenerated file. It serves as a starting point
# for a more percise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

from typing import List, Tuple, Dict, Undefined, GenericType

def asctime(*args, **kwargs) -> str:
    raise ValueError()

def clock() -> float: ...

def ctime(*args, **kwargs) -> str:
    raise ValueError()

def gmtime(*args, **kwargs) -> tuple: ...

def localtime(*args, **kwargs) -> tuple: ...

def mktime(*args, **kwargs) -> float:
    raise OverflowError()

def sleep(a: float) -> None: ...

def strftime(a: str, *args, **kwargs) -> str:
    raise MemoryError()
    raise ValueError()

def strptime(*args, **kwargs) -> object: ...

def time() -> float:
    raise IOError()

def tzset() -> None: ...