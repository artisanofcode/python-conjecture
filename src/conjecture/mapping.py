"""mapping conjectures."""

import collections.abc

import conjecture.base

sentinel = object()


def has_key(value: str, of: object = sentinel) -> conjecture.base.Conjecture:
    """
    Has attribute.

    Propose that the value has the given key

    >>> assert value == conjecture.has_key("foo")
    >>> assert value == conjecture.has_key("foo", of=5)
    >>> assert value == conjecture.has_key("foo", of=conjecture.less_than(10))

    :param value: the name of the key
    :param of: an optional value or conjecture to compare the key value against

    :return: a conjecture object
    """
    # pylint: disable=invalid-name
    # of is a perfectly valid name.

    if of is sentinel:
        return conjecture.base.Conjecture(
            lambda x: isinstance(x, collections.abc.Mapping) and value in x
        )

    return conjecture.base.Conjecture(
        lambda x: isinstance(x, collections.abc.Mapping) and x.get(value) == of
    )
