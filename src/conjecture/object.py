"""
object conjectures
"""
import typing

import conjecture.base


def instance_of(
    value: typing.Union[tuple[type, ...], type]
) -> conjecture.base.Conjecture:
    """
    Instance of

    Propose that value is instance of the provided type(s)

    >>> assert value == conjecture.instance_of((str, int))

    :param value: a type or tuple of types to check

    :return: a conjecture object
    """

    return conjecture.base.Conjecture(lambda x: isinstance(x, value))
