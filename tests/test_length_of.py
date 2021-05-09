"""test conjecture.length_of."""
from __future__ import annotations

import typing

import hypothesis
import hypothesis.strategies as st
import pytest

import conjecture


@pytest.mark.describe("length_of")
@pytest.mark.it("should match collection length")
@hypothesis.given(
    value=st.tuples(
        st.sampled_from([list, set, tuple, frozenset]),
        st.lists(elements=st.integers(), min_size=1),
    ).map(lambda x: x[0](x[1])),
)
def test_should_match_itself(
    value: typing.Union[
        typing.List[int],
        typing.Set[int],
        typing.Tuple[int, ...],
        typing.FrozenSet[int],
    ]
) -> None:
    assert conjecture.length_of(len(value)).resolve(value)


@pytest.mark.describe("length_of")
@pytest.mark.it("should not match other lengths")
@hypothesis.given(
    value=st.tuples(
        st.sampled_from([list, set, tuple, frozenset]),
        st.lists(elements=st.integers(), min_size=1),
    ).map(lambda x: x[0](x[1])),
    other=st.integers(),
)
def test_should_not_match_other_values(
    value: typing.Union[
        typing.List[int],
        typing.Set[int],
        typing.Tuple[int, ...],
        typing.FrozenSet[int],
    ],
    other: int,
) -> None:
    hypothesis.assume(len(value) != other)

    assert not conjecture.length_of(other).resolve(value)
