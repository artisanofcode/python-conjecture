"""
Tests for :meth:`conjecture.suffixed_with`.
"""

import hypothesis
import hypothesis.strategies as st

import conjecture


@hypothesis.given(value=st.text(min_size=1), other=st.text())
def test_should_match_prefixed_strings(value: str, other: str) -> None:
    """
    suffixed_with() should match suffixed strings.
    """
    assert conjecture.suffixed_with(value).resolve(other + value)


@hypothesis.given(value=st.text(min_size=1), other=st.text(min_size=1))
def test_should_not_match_other_strings(value: str, other: str) -> None:
    """
    suffixed_with() should not match other strings suffix.
    """
    hypothesis.assume(not (value + other).endswith(value))

    assert not conjecture.suffixed_with(value).resolve(value + other)


@hypothesis.given(value=st.binary(min_size=1), other=st.binary())
def test_should_match_prefixed_bytes(value: bytes, other: bytes) -> None:
    """
    suffixed_with() should match suffixed bytes.
    """
    assert conjecture.suffixed_with(value).resolve(other + value)


@hypothesis.given(value=st.binary(min_size=1), other=st.binary(min_size=1))
def test_should_not_match_other_bytes(value: bytes, other: bytes) -> None:
    """
    suffixed_with() should not match other bytes suffix.
    """
    hypothesis.assume(not (value + other).endswith(value))

    assert not conjecture.suffixed_with(value).resolve(value + other)
