"""object conjectures."""
from __future__ import annotations

import typing

import conjecture.base


def instance_of(
    value: typing.Union[tuple[type, ...], type]
) -> conjecture.base.Conjecture:
    """
    Instance of.

    Propose that value is instance of the provided type(s)

    >>> assert value == conjecture.instance_of((str, int))

    :param value: a type or tuple of types to check

    :return: a conjecture object
    """
    return conjecture.base.Conjecture(lambda x: isinstance(x, value))


def equal_to(value: object) -> conjecture.base.Conjecture:
    """
    Equal to.

    Propose that the value is equal to provided value

    >>> assert value == conjecture.equal_to(5)

    :return: a conjecture object
    """
    return conjecture.base.Conjecture(lambda x: x == value)
