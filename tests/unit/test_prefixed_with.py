"""
Tests for :meth:`conjecture.prefixed_with`.
"""

import hypothesis
import hypothesis.strategies as st

import conjecture


@hypothesis.given(value=st.text(min_size=1), other=st.text())
def test_should_match_prefixed_strings(value: str, other: str) -> None:
    """
    prefixed_with() should match prefixed strings.
    """
    assert conjecture.prefixed_with(value).resolve(value + other)


@hypothesis.given(value=st.text(min_size=1), other=st.text(min_size=1))
def test_should_not_match_other_strings(value: str, other: str) -> None:
    """
    prefixed_with() should not match other string prefix.
    """
    hypothesis.assume(not (other + value).startswith(value))

    assert not conjecture.prefixed_with(value).resolve(other + value)


@hypothesis.given(value=st.binary(min_size=1), other=st.binary())
def test_should_match_prefixed_bytes(value: bytes, other: bytes) -> None:
    """
    prefixed_with() should match prefixed bytes.
    """
    assert conjecture.prefixed_with(value).resolve(value + other)


@hypothesis.given(value=st.binary(min_size=1), other=st.binary(min_size=1))
def test_should_not_match_other_bytes(value: bytes, other: bytes) -> None:
    """
    prefixed_with() should not match other bytes prefix.
    """
    hypothesis.assume(not (other + value).startswith(value))

    assert not conjecture.prefixed_with(value).resolve(other + value)
