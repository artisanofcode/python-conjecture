"""test conjecture.prefixed_with."""
from __future__ import annotations

import hypothesis
import hypothesis.strategies as st
import pytest

import conjecture


@pytest.mark.describe("prefixed_with")
@pytest.mark.it("should match prefixed strings")
@hypothesis.given(
    value=st.text(min_size=1),
    other=st.text(),
)
def test_should_match_prefixed_strings(value: str, other: str) -> None:
    assert conjecture.prefixed_with(value).resolve(value + other)


@pytest.mark.describe("prefixed_with")
@pytest.mark.it("should not match other string prefix")
@hypothesis.given(
    value=st.text(min_size=1),
    other=st.text(min_size=1),
)
def test_should_not_match_other_strings(value: str, other: str) -> None:
    hypothesis.assume(not (other + value).startswith(value))

    assert not conjecture.prefixed_with(value).resolve(other + value)


@pytest.mark.describe("prefixed_with")
@pytest.mark.it("should match prefixed bytes")
@hypothesis.given(
    value=st.binary(min_size=1),
    other=st.binary(),
)
def test_should_match_prefixed_bytes(value: bytes, other: bytes) -> None:
    assert conjecture.prefixed_with(value).resolve(value + other)


@pytest.mark.describe("prefixed_with")
@pytest.mark.it("should not match other bytes prefix")
@hypothesis.given(
    value=st.binary(min_size=1),
    other=st.binary(min_size=1),
)
def test_should_not_match_other_bytes(value: bytes, other: bytes) -> None:
    hypothesis.assume(not (other + value).startswith(value))

    assert not conjecture.prefixed_with(value).resolve(other + value)
