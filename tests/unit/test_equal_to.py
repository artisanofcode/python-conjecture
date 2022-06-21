"""
Tests for :meth:`conjecture.equal_to`.
"""

import typing

import hypothesis
import hypothesis.strategies as st

import conjecture


@hypothesis.given(
    value=st.none()
    | st.booleans()
    | st.floats(allow_nan=False)
    | st.integers()
    | st.text()
)
def test_should_match_itself(value: typing.Union[str, int, float, bool, None]) -> None:
    """
    equal_to() should match itself.
    """
    assert conjecture.equal_to(value).resolve(value)


@hypothesis.given(
    value=st.none() | st.booleans() | st.floats() | st.integers() | st.text(),
    other=st.none() | st.booleans() | st.floats() | st.integers() | st.text(),
)
def test_should_not_match_other_values(
    value: typing.Union[str, int, float, bool, None],
    other: typing.Union[str, int, float, bool, None],
) -> None:
    """
    equal_to() should not match other values.
    """
    hypothesis.assume(value != other)

    assert not conjecture.equal_to(value).resolve(other)
