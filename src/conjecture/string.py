"""
string conjectures
"""
import typing

import conjecture.base


def starts_with(value: typing.Union[str, bytes]) -> conjecture.base.Conjecture:
    """
    Starts with

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


def ends_with(value: typing.Union[str, bytes]) -> conjecture.base.Conjecture:
    """
    Ends with

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
