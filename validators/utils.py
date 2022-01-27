from typing import Callable
from inspect import getfullargspec
import itertools
from collections import OrderedDict


class ValidationFailure(Exception):
    def __init__(self, func, args):
        self.func = func
        self.__dict__.update(args)

    def __repr__(self):
        name = self.func.__name__,
        args = {k: v for k, v in self.__dict__.items() if k != 'func'}
        return f"ValidationFailure(func={name}, args={args})"

def func_args_as_dict(func, args, kwargs):
    """
    Return given function's positional and key value arguments as an ordered
    dictionary.
    """
    arg_names = list(
        OrderedDict.fromkeys(
            itertools.chain(
                getfullargspec(func)[0],
                kwargs.keys()
            )
        )
    )
    return OrderedDict(list(zip(arg_names, args)) + list(kwargs.items()))

def validator(func: Callable[..., bool]) -> Callable:
    """
    A decorator that makes given function validator.

    An exception will be raised if `raise_on_failure` and the
    return value of the given function is false, otherwise a boolean
    value is passed.

    Example::

        >>> @validator
        ... def even(value):
        ...     return not (value % 2)

        >>> even(4)
        True

        >>> even(5)
        False
    """
    def wrapper(*args, raise_on_failure: bool=False, **kwargs) -> bool:
        if not isinstance(raise_on_failure, bool):
            raise TypeError("Keyword argument `raise` must be a bool.")
        result = bool(func(*args, **kwargs))
        if not result and raise_on_failure:
            raise ValidationFailure(func, func_args_as_dict(func, args, kwargs))
        return result
    return wrapper
