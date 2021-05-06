"""
general conjectures
"""
import conjecture.base


def none() -> conjecture.base.Conjecture:
    """
    None

    Propose that the value is None

    >>> assert value == conjecture.none()

    :return: a conjecture object
    """

    return conjecture.base.Conjecture(lambda x: x is None)


def anything() -> conjecture.base.Conjecture:
    """
    Anything

    Propose that the value meerly exists

    >>> assert value == conjecture.anything()

    :return: a conjecture object
    """

    return conjecture.base.Conjecture(lambda x: True)


def any_of(*conjectures: conjecture.base.Conjecture) -> conjecture.base.Conjecture:
    """
    Any of

    Propose any of the conjectures resolve truely

    >>> assert value == conjecture.any_of(conjecture1, conjecture2)

    :return: a conjecture object
    """
    return conjecture.base.AnyOfConjecture(conjectures)


def all_of(*conjectures: conjecture.base.Conjecture) -> conjecture.base.Conjecture:
    """
    All of

    Propose all of the conjectures resolve truely

    >>> assert value == conjecture.any_of(conjecture1, conjecture2)

    :return: a conjecture object
    """
    return conjecture.base.AllOfConjecture(conjectures)


def has(proof: conjecture.base.Proof) -> conjecture.base.Conjecture:
    """
    Has

    Propose a custom proof function

    >>> assert value == conjecture.has(lambda x: x > 5)

    :return: a conjecture object
    """
    return conjecture.base.Conjecture(proof)
