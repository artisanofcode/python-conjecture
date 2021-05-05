from __future__ import annotations

import typing

Predicate = typing.Callable[[object], bool]


class Conjecture:
    def __init__(self, predicate: typing.Optional[Predicate] = None) -> None:
        self._predicate = predicate or self.predicate

    def predicate(self, value: object) -> bool:
        raise NotImplementedError()

    def __eq__(self, other: object) -> bool:
        return self._predicate(other)

    def __ne__(self, other: object) -> bool:
        return not self._predicate(other)

    def __or__(self, other) -> Conjecture:
        return any_of(self, other)

    def __and__(self, other) -> Conjecture:
        return all_of(self, other)

    def __invert__(self) -> Conjecture:
        return Conjecture(lambda value: not self._predicate(value))


class AnyConjecture(Conjecture):
    def __init__(self, conjectures: typing.Iterable[Conjecture]) -> None:
        super().__init__()
        self.conjectures = conjectures

    def predicate(self, value: object) -> None:
        for other in self.conjectures:
            if value == other:
                return True

        return False


class AllConjecture(Conjecture):
    def __init__(self, conjectures: typing.Iterable[Conjecture]) -> None:
        super().__init__()
        self.conjectures = conjectures

    def predicate(self, value: object) -> None:
        for other in self.conjectures:
            if value != other:
                return False

        return True


def has(predicate: Predicate):
    return Conjecture(predicate)


def any_of(*conjectures: Conjecture) -> Conjecture:
    return AnyConjecture(conjectures)


def all_of(*conjectures: Conjecture) -> Conjecture:
    return AllConjecture(conjectures)


def is_between(minimum, maximum) -> Conjecture:
    return Conjecture(lambda value: minimum <= value <= maximum)
