from typing import Any
from functools import total_ordering


@total_ordering
class _Min(object):
    """
    An object that is less than any other object (except itself).

    Inspired by https://pypi.python.org/pypi/Extremes

    Examples::

        >>> import sys

        >>> Min < -sys.maxint
        True

        >>> Min < None
        True

        >>> Min < ''
        True

    .. versionadded:: 0.2
    """
    def __lt__(self, other: Any) -> bool:
        if other is Min:
            return False
        return True


@total_ordering
class _Max(object):
    """
    An object that is greater than any other object (except itself).

    Inspired by https://pypi.python.org/pypi/Extremes

    Examples::

        >>> import sys

        >>> Max > Min
        True

        >>> Max > sys.maxint
        True

        >>> Max > 99999999999999999
        True

    .. versionadded:: 0.2
    """
    def __gt__(self, other: Any) -> bool:
        if other is Max:
            return False
        return True


Min = _Min()
Max = _Max()
