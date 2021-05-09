"""test conjecture.empty."""
from __future__ import annotations

import typing

import hypothesis
import hypothesis.strategies as st
import pytest

import conjecture


@pytest.mark.describe("empty")
@pytest.mark.it("should match empty collectioons")
@hypothesis.given(
    value=st.sampled_from([list, set, tuple, frozenset]).map(lambda x: x()),
)
def test_should_match_itself(
    value: typing.Union[
        typing.List[None],
        typing.Set[None],
        typing.Tuple[None, ...],
        typing.FrozenSet[None],
    ]
) -> None:
    assert conjecture.empty().resolve(value)


@pytest.mark.describe("empty")
@pytest.mark.it("should not match other values")
@hypothesis.given(
    value=st.tuples(
        st.sampled_from([list, set, tuple, frozenset]),
        st.lists(elements=st.integers(), min_size=1),
    ).map(lambda x: x[0](x[1])),
)
def test_should_not_match_other_values(
    value: typing.Union[
        typing.List[int],
        typing.Set[int],
        typing.Tuple[int, ...],
        typing.FrozenSet[int],
    ]
) -> None:
    assert not conjecture.empty().resolve(value)
