"""
Tests for :meth:`conjecture.has_key`.
"""

import string

import hypothesis
import hypothesis.strategies as st

import conjecture


@hypothesis.given(
    value=st.text(alphabet=string.ascii_letters, min_size=1),
    other=st.integers(),
)
def test_should_match_when_key_exists(value: str, other: int) -> None:
    """
    has_key() should match when key exists.
    """
    mapping = {value: other}

    assert conjecture.has_key(value).resolve(mapping)


@hypothesis.given(
    value=st.text(alphabet=string.ascii_letters, min_size=1),
    key=st.text(alphabet=string.ascii_letters, min_size=1),
    other=st.integers(),
)
def test_should_not_match_when_key_doesnt_exists(
    value: str,
    key: str,
    other: int,
) -> None:
    """
    has_key() should not match when key doesn't exist.
    """
    hypothesis.assume(value != key)

    mapping = {key: other}

    assert not conjecture.has_key(value).resolve(mapping)


@hypothesis.given(
    value=st.text(alphabet=string.ascii_letters, min_size=1),
    other=st.integers(),
)
def test_should_match_when_key_value_matches(value: str, other: int) -> None:
    """
    has_key() should match when key value matches.
    """
    mapping = {value: other}

    assert conjecture.has_key(value, of=other).resolve(mapping)


@hypothesis.given(
    value=st.text(alphabet=string.ascii_letters, min_size=1),
    wrong=st.integers(),
    other=st.integers(),
)
def test_should_not_match_when_key_value_doesnt_match(
    value: str,
    wrong: int,
    other: int,
) -> None:
    """
    has_key() should not match when key value doesn't match.
    """
    hypothesis.assume(wrong != other)

    mapping = {value: wrong}

    assert not conjecture.has_key(value, of=other).resolve(mapping)


@hypothesis.given(
    value=st.text(alphabet=string.ascii_letters, min_size=1),
    other=st.integers(),
)
def test_should_match_when_key_value_matches_conjecture(value: str, other: int) -> None:
    """
    has_key() should match when key value matches conjecture.
    """
    mapping = {value: other}

    always = conjecture.has(lambda x: True)

    assert conjecture.has_key(value, of=always).resolve(mapping)


@hypothesis.given(
    value=st.text(alphabet=string.ascii_letters, min_size=1),
    other=st.integers(),
)
def test_should_not_match_when_key_value_doesnt_match_conjecture(
    value: str, other: int
) -> None:
    """
    has_key() should not match when key value doesn't match conjecture.
    """
    mapping = {value: other}

    never = conjecture.has(lambda x: False)

    assert not conjecture.has_key(value, of=never).resolve(mapping)
