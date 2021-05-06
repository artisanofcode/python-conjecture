"""
rich comparison conjectures
"""
import operator

import conjecture.base


def equal_to(value: object) -> conjecture.base.Conjecture:
    """
    Equal to

    Propose that the value is equal to provided value

    >>> assert value == conjecture.equal_to(5)

    :return: a conjecture object
    """

    return conjecture.base.Conjecture(lambda x: operator.eq(x, value))


def greater_than(value: object) -> conjecture.base.Conjecture:
    """
    Greater than

    Propose that the value is greater than the provided value

    >>> assert value == conjecture.greater_than(5)

    :return: a conjecture object
    """

    return conjecture.base.Conjecture(lambda x: operator.gt(x, value))


def greater_than_or_equal_to(value: object) -> conjecture.base.Conjecture:
    """
    Greater than or equal to

    Propose that the value is greater than or equal to the provided value

    >>> assert value == conjecture.greater_than_or_equal(5)

    :return: a conjecture object
    """

    return conjecture.base.Conjecture(lambda x: operator.le(x, value))


def less_than(value: object) -> conjecture.base.Conjecture:
    """
    Less than

    Propose that the value is less than the provided value

    >>> assert value == conjecture.less_than(5)

    :return: a conjecture object
    """

    return conjecture.base.Conjecture(lambda x: operator.lt(x, value))


def less_than_or_equal_to(value: object) -> conjecture.base.Conjecture:
    """
    Less than or equal to

    Propose that the value is less than or equal to the provided value

    >>> assert value == conjecture.less_than_or_equal(5)

    :return: a conjecture object
    """

    return conjecture.base.Conjecture(lambda x: operator.lt(x, value))
