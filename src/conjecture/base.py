"""base conjecture classes."""

import collections.abc
import typing

Proof = collections.abc.Callable[[object], bool]


class Conjecture:
    """
    A conjecture describing another object.

    Conjectures can be used to describe an object to which they are to be compared
    against. They assert equality when the proof function resolves truly.

    >>> assert 5 == conjecture.greater_than(0) & conjecture.less_than(10)

    There are many helpful conjecture factories with their proofs already defined.
    """

    # pylint: disable=eq-without-hash

    def __init__(self, proof: typing.Optional[Proof] = None) -> None:
        """
        Create a conjecture.

        :param proof: a callback that asserts some small fact of the passed object
        """
        self._proof = proof

    def resolve(self, value: object) -> bool:
        """
        Resolve conjecture.

        This is an abstract method can either be overwritten in a subclass or by
        providing a proof method to the constructor.

        :param value: the value the conjecture is evaluated against

        :return: whether the conjecture resolved truly

        :raises NotImplementedError: when no proof specified
        """
        if not self._proof:
            raise NotImplementedError()

        return self._proof(value)

    def __eq__(self, other: object) -> bool:
        """
        Resolve conjecture via equality.

        A conjecture can be resolved via `==` or `!=` comparison operators.

        :param other: the value the conjecture is evaluated against

        :return: whether the conjecture resolved truly
        """
        return self.resolve(other)

    def __invert__(self) -> "Conjecture":
        """
        Invert conjecture.

        Invert the resolution of a conjecture

        :return: the inverse conjecture
        """
        return Conjecture(lambda value: not self.resolve(value))

    def __or__(self, other: object) -> "Conjecture":
        """
        Combine using any of.

        :param other: another conjecture

        :return: a conjecture that either of the combined conjectures will
                 resolve truly

        :raises ValueError: when other is not a conjecture
        """
        if not isinstance(other, Conjecture):
            raise ValueError(f"Conjecture cannot be combined with {other!r}")

        return AnyOfConjecture((self, other))

    def __and__(self, other: object) -> "Conjecture":
        """
        Combine using all of.

        :param other: another conjecture

        :return: a conjecture that both of the combined conjectures will resolve truly

        :raises ValueError: when other is not a conjecture
        """
        if not isinstance(other, Conjecture):
            raise ValueError(f"Conjecture cannot be combined with {other!r}")

        return AllOfConjecture((self, other))


class AnyOfConjecture(Conjecture):
    """
    Any of Conjecture.

    An any of conjecture will resolve truly if any of the passed conjectures
    resolve truly themselves.

    """

    # pylint: disable=too-few-public-methods

    def __init__(self, conjectures: collections.abc.Iterable[Conjecture]) -> None:
        """
        Create a combined conjecture.

        :param conjectures: a collection of conjectures
        """
        super().__init__()
        self.conjectures = conjectures

    def resolve(self, value: object) -> bool:
        """
        Resolve conjecture.

        This conjecture will resolve truly if any of the conjectures it was
        created with resolve true.

        :param value: the value the conjecture is evaluated against

        :return: whether the conjecture resolved truly
        """
        for other in self.conjectures:
            if other.resolve(value):
                return True

        return False


class AllOfConjecture(Conjecture):
    """
    All of Conjecture.

    An all of conjecture will resolve truly only when all of the passed conjectures
    resolve truly themselves.

    :param conjectures: a tuple of conjectures
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, conjectures: collections.abc.Iterable[Conjecture]) -> None:
        """
        Create a combined conjecture.

        :param conjectures: a collection of conjectures
        """
        super().__init__()
        self.conjectures = conjectures

    def resolve(self, value: object) -> bool:
        """
        Resolve conjecture.

        This conjecture will resolve truly only if all of the conjectures it was
        created with resolve true.

        :param value: the value the conjecture is evaluated against

        :return: whether the conjecture resolved truly
        """
        for other in self.conjectures:
            if not other.resolve(value):
                return False

        return True
