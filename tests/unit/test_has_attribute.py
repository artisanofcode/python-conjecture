"""
Tests for :meth:`conjecture.has_attribute`.
"""

import dataclasses
import keyword
import string

import hypothesis
import hypothesis.strategies as st

import conjecture


def _not_keyword(value: str) -> bool:
    return not keyword.iskeyword(value)


@hypothesis.given(
    value=st.text(alphabet=string.ascii_letters, min_size=1).filter(_not_keyword),
    other=st.integers(),
)
def test_should_match_when_attribute_exists(value: str, other: int) -> None:
    """
    has_attribute() should match when attribute exists.
    """
    obj = dataclasses.make_dataclass("mock", [(value, int)])(**{value: other})

    assert conjecture.has_attribute(value).resolve(obj)


@hypothesis.given(
    value=st.text(alphabet=string.ascii_letters, min_size=1).filter(_not_keyword),
    key=st.text(alphabet=string.ascii_letters, min_size=1).filter(_not_keyword),
    other=st.integers(),
)
def test_should_not_match_when_attribute_doesnt_exists(
    value: str,
    key: str,
    other: int,
) -> None:
    """
    has_attribute() should not match when attribute doesn't exist.
    """
    hypothesis.assume(value != key)

    obj = dataclasses.make_dataclass("mock", [(key, int)])(**{key: other})

    assert not conjecture.has_attribute(value).resolve(obj)


@hypothesis.given(
    value=st.text(alphabet=string.ascii_letters, min_size=1).filter(_not_keyword),
    other=st.integers(),
)
def test_should_match_when_attribute_value_matches(value: str, other: int) -> None:
    """
    has_attribute() should match when attribute value matches.
    """
    obj = dataclasses.make_dataclass("mock", [(value, int)])(**{value: other})

    assert conjecture.has_attribute(value, of=other).resolve(obj)


@hypothesis.given(
    value=st.text(alphabet=string.ascii_letters, min_size=1).filter(_not_keyword),
    wrong=st.integers(),
    other=st.integers(),
)
def test_should_not_match_when_attribute_value_doesnt_match(
    value: str,
    wrong: int,
    other: int,
) -> None:
    """
    has_attribute() should not match when attribute value doesn't match.
    """
    hypothesis.assume(wrong != other)

    obj = dataclasses.make_dataclass("mock", [(value, int)])(**{value: wrong})

    assert not conjecture.has_attribute(value, of=other).resolve(obj)


@hypothesis.given(
    value=st.text(alphabet=string.ascii_letters, min_size=1).filter(_not_keyword),
    other=st.integers(),
)
def test_should_match_when_attribute_value_matches_conjecture(
    value: str, other: int
) -> None:
    """
    has_attribute() should match when attribute value matches conjecture.
    """
    obj = dataclasses.make_dataclass("mock", [(value, int)])(**{value: other})

    always = conjecture.has(lambda x: True)

    assert conjecture.has_attribute(value, of=always).resolve(obj)


@hypothesis.given(
    value=st.text(alphabet=string.ascii_letters, min_size=1).filter(_not_keyword),
    other=st.integers(),
)
def test_should_not_match_when_attribute_value_doesnt_match_conjecture(
    value: str, other: int
) -> None:
    """
    has_attribute() should not match when attribute value doesn't match conjecture.
    """
    obj = dataclasses.make_dataclass("mock", [(value, int)])(**{value: other})

    never = conjecture.has(lambda x: False)

    assert not conjecture.has_attribute(value, of=never).resolve(obj)
