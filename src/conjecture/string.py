"""string conjectures."""
from __future__ import annotations

import typing

import conjecture.base


def prefixed_with(value: typing.Union[str, bytes]) -> conjecture.base.Conjecture:
    """
    Prefixed with.

    Propose that a string or byte string starts with provided value

    >>> assert value == conjecture.starts_with("prefix")

    :return: a conjecture object
    """
    if isinstance(value, str):
        prefix_s = value

        return conjecture.base.Conjecture(
            lambda x: isinstance(x, str) and x.startswith(prefix_s)
        )

    prefix_b = value

    return conjecture.base.Conjecture(
        lambda x: isinstance(x, bytes) and x.startswith(prefix_b)
    )


def suffixed_with(value: typing.Union[str, bytes]) -> conjecture.base.Conjecture:
    """
    Suffixed with.

    Propose that a string or byte string ends with provided value

    >>> assert value == conjecture.ends_with("suffix")

    :return: a conjecture object
    """
    if isinstance(value, str):
        suffix_s = value

        return conjecture.base.Conjecture(
            lambda x: isinstance(x, str) and x.endswith(suffix_s)
        )

    suffix_b = value

    return conjecture.base.Conjecture(
        lambda x: isinstance(x, bytes) and x.endswith(suffix_b)
    )
