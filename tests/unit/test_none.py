"""
Tests for :meth:`conjecture.none`.
"""

import typing

import hypothesis
import hypothesis.strategies as st

import conjecture


def test_hould_match_none() -> None:
    """
    none() should match None.
    """
    assert conjecture.none().resolve(None)


@hypothesis.given(value=st.booleans() | st.floats() | st.integers() | st.text())
def test_should_not_match_non_none(value: typing.Union[bool, float, int, str]) -> None:
    """
    none() should not match non None.
    """
    assert not conjecture.none().resolve(value)
