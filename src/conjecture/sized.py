"""sized conjectures."""

import collections.abc
import typing

import conjecture.base


def empty() -> conjecture.base.Conjecture:
    """
    Empty.

    Propose that a sequence contains no items

    >>> assert value == conjecture.empty()

    :return: a conjecture object
    """
    return conjecture.base.Conjecture(
        lambda x: isinstance(x, collections.abc.Sized) and len(x) == 0
    )


def length_of(
    value: typing.Union[int, conjecture.base.Conjecture]
) -> conjecture.base.Conjecture:
    """
    Length.

    Propose that a sequence contains a the provided number of items

    >>> assert value == conjecture.length(5)
    >>> assert value == conjecture.length(conjecture.less_than(10))

    :return: a conjecture object
    """
    return conjecture.base.Conjecture(
        lambda x: isinstance(x, collections.abc.Sized) and len(x) == value
    )
