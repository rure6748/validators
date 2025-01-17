from typing import Pattern
import re

from .utils import validator

slug_regex: Pattern = re.compile(r'^[-a-zA-Z0-9_]+$')


@validator
def slug(value: str) -> bool:
    """
    Validate whether or not given value is valid slug.

    Valid slug can contain only alphanumeric characters, hyphens and
    underscores.

    Examples::

        >>> slug('my.slug')
        ValidationFailure(func=slug, args={'value': 'my.slug'})

        >>> slug('my-slug-2134')
        True

    .. versionadded:: 0.6

    :param value: value to validate
    """
    return bool(slug_regex.match(value))
