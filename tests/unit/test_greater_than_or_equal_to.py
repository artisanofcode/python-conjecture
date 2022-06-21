"""
Tests for :meth:`conjecture.greater_than_or_equal_to`.
"""

import hypothesis
import hypothesis.strategies as st

import conjecture


@hypothesis.given(
    value=st.shared(base=st.integers(), key="value"),
    other=st.shared(base=st.integers(), key="value").flatmap(
        lambda x: st.integers(min_value=x + 1)
    ),
)
def test_should_match_bigger_value(value: int, other: int) -> None:
    """
    greater_than_or_equal_to() should match bigger value.
    """
    assert conjecture.greater_than_or_equal_to(value).resolve(other)


@hypothesis.given(
    value=st.shared(base=st.integers(), key="value"),
    other=st.shared(base=st.integers(), key="value").flatmap(
        lambda x: st.integers(max_value=x - 1)
    ),
)
def test_should_not_match_smaller_value(value: int, other: int) -> None:
    """
    greater_than_or_equal_to() should not match smaller value.
    """
    assert not conjecture.greater_than_or_equal_to(value).resolve(other)


@hypothesis.given(
    value=st.integers(),
)
def test_should_not_match_equal_value(value: int) -> None:
    """
    greater_than_or_equal_to() should match equal value.
    """
    assert conjecture.greater_than_or_equal_to(value).resolve(value)
