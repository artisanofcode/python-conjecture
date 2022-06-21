"""
Tests for :meth:`conjecture.less_than_or_equal_to`.
"""

import hypothesis
import hypothesis.strategies as st

import conjecture


@hypothesis.given(
    value=st.shared(base=st.integers(), key="value"),
    other=st.shared(base=st.integers(), key="value").flatmap(
        lambda value: st.integers(max_value=value - 1)
    ),
)
def test_should_match_smaller_value(value: int, other: int) -> None:
    """
    less_than_or_equal_to() should match smaller value.
    """
    assert conjecture.less_than_or_equal_to(value).resolve(other)


@hypothesis.given(
    value=st.shared(base=st.integers(), key="value"),
    other=st.shared(base=st.integers(), key="value").flatmap(
        lambda value: st.integers(min_value=value + 1)
    ),
)
def test_should_not_match_bigger_value(value: int, other: int) -> None:
    """
    less_than_or_equal_to() should not match bigger value.
    """
    assert not conjecture.less_than_or_equal_to(value).resolve(other)


@hypothesis.given(value=st.integers())
def test_should_not_match_equal_value(value: int) -> None:
    """
    less_than_or_equal_to() should match equal value.
    """
    assert conjecture.less_than_or_equal_to(value).resolve(value)
