"""
Tests for :meth:`conjecture.length_of`.
"""

import typing

import hypothesis
import hypothesis.strategies as st

import conjecture


@hypothesis.given(
    value=st.tuples(
        st.sampled_from([list, set, tuple, frozenset]),
        st.lists(elements=st.integers(), min_size=1),
    ).map(
        lambda x: x[0](x[1])  # type: ignore
    ),
)
def test_should_match_itself(
    value: typing.Union[list[int], set[int], tuple[int, ...], frozenset[int]]
) -> None:
    """
    length_of() should match collection length.
    """
    assert conjecture.length_of(len(value)).resolve(value)


@hypothesis.given(
    value=st.tuples(
        st.sampled_from([list, set, tuple, frozenset]),
        st.lists(elements=st.integers(), min_size=1),
    ).map(
        lambda x: x[0](x[1])  # type: ignore
    ),
    other=st.integers(),
)
def test_should_not_match_other_values(
    value: typing.Union[list[int], set[int], tuple[int, ...], frozenset[int]],
    other: int,
) -> None:
    """
    length_of() should not match other lengths.
    """
    hypothesis.assume(len(value) != other)

    assert not conjecture.length_of(other).resolve(value)
