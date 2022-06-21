"""
Tests for :meth:`conjecture.anything`.
"""

import typing

import hypothesis
import hypothesis.strategies as st

import conjecture


@hypothesis.given(
    value=st.none() | st.booleans() | st.floats() | st.integers() | st.text(),
)
def test_should_match_all_types(
    value: typing.Union[str, int, float, bool, None]
) -> None:
    """
    anything() should match all types.
    """
    assert conjecture.anything().resolve(value)
