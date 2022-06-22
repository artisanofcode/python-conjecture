"""object conjectures."""

import typing

import conjecture.base

sentinel = object()


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


def has_attribute(value: str, of: object = sentinel) -> conjecture.base.Conjecture:
    """
    Has attribute.

    Propose that the value has the given attribute

    >>> assert value == conjecture.has_attribute("foo")
    >>> assert value == conjecture.has_attribute("foo", of=5)
    >>> assert value == conjecture.has_attribute("foo", of=conjecture.less_than(10))

    :param value: the name of the attribute
    :param of: an optional value or conjecture to compare the attribute value against

    :return: a conjecture object
    """
    # pylint: disable=invalid-name
    # of is a perfectly valid name.

    if of is sentinel:
        return conjecture.base.Conjecture(lambda x: hasattr(x, value))

    return conjecture.base.Conjecture(lambda x: getattr(x, value, sentinel) == of)
