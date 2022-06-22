"""rich comparison conjectures."""

import abc
import typing

import conjecture.base

CT = typing.TypeVar("CT", bound="Comparable")


class Comparable(typing.Protocol):
    """Rich comparison protocol."""

    @abc.abstractmethod
    def __lt__(self: CT, other: CT) -> bool:
        """Check less than."""

    @abc.abstractmethod
    def __gt__(self: CT, other: CT) -> bool:
        """Check greater than."""

    @abc.abstractmethod
    def __le__(self: CT, other: CT) -> bool:
        """Check less than or equal to."""

    @abc.abstractmethod
    def __ge__(self: CT, other: CT) -> bool:
        """Check greater than or equal to."""


def greater_than(value: Comparable) -> conjecture.base.Conjecture:
    """
    Greater than.

    Propose that the value is greater than the provided value

    >>> assert value == conjecture.greater_than(5)

    :return: a conjecture object
    """
    return conjecture.base.Conjecture(lambda x: typing.cast(Comparable, x) > value)


def greater_than_or_equal_to(value: Comparable) -> conjecture.base.Conjecture:
    """
    Greater than or equal to.

    Propose that the value is greater than or equal to the provided value

    >>> assert value == conjecture.greater_than_or_equal(5)

    :return: a conjecture object
    """
    return conjecture.base.Conjecture(lambda x: typing.cast(Comparable, x) >= value)


def less_than(value: Comparable) -> conjecture.base.Conjecture:
    """
    Less than.

    Propose that the value is less than the provided value

    >>> assert value == conjecture.less_than(5)

    :return: a conjecture object
    """
    return conjecture.base.Conjecture(lambda x: typing.cast(Comparable, x) < value)


def less_than_or_equal_to(value: Comparable) -> conjecture.base.Conjecture:
    """
    Less than or equal to.

    Propose that the value is less than or equal to the provided value

    >>> assert value == conjecture.less_than_or_equal(5)

    :return: a conjecture object
    """
    return conjecture.base.Conjecture(lambda x: typing.cast(Comparable, x) <= value)
