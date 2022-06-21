"""
Tests for :meth:`conjecture.empty`.
"""

import typing

import hypothesis
import hypothesis.strategies as st

import conjecture


@hypothesis.given(
    value=st.sampled_from([list, set, tuple, frozenset]).map(
        lambda x: x()  # type: ignore
    ),
)
def test_should_match_empty_collections(
    value: typing.Union[list[None], set[None], tuple[None, ...], frozenset[None]]
) -> None:
    """
    empty() should match empty collections.
    """
    assert conjecture.empty().resolve(value)


@hypothesis.given(
    value=st.tuples(
        st.sampled_from([list, set, tuple, frozenset]),
        st.lists(elements=st.integers(), min_size=1),
    ).map(
        lambda x: x[0](x[1])  # type: ignore
    ),
)
def test_should_not_match_other_values(
    value: typing.Union[list[int], set[int], tuple[int, ...], frozenset[int]]
) -> None:
    """
    empty() should not match other values.
    """
    assert not conjecture.empty().resolve(value)
