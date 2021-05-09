"""test conjecture.suffixed_with."""
from __future__ import annotations

import hypothesis
import hypothesis.strategies as st
import pytest

import conjecture


@pytest.mark.describe("suffixed_with")
@pytest.mark.it("should match suffixed strings")
@hypothesis.given(
    value=st.text(min_size=1),
    other=st.text(),
)
def test_should_match_prefixed_strings(value: str, other: str) -> None:
    assert conjecture.suffixed_with(value).resolve(other + value)


@pytest.mark.describe("suffixed_with")
@pytest.mark.it("should not match other strings suffix")
@hypothesis.given(
    value=st.text(min_size=1),
    other=st.text(min_size=1),
)
def test_should_not_match_other_strings(value: str, other: str) -> None:
    hypothesis.assume(not (value + other).endswith(value))

    assert not conjecture.suffixed_with(value).resolve(value + other)


@pytest.mark.describe("suffixed_with")
@pytest.mark.it("should match suffixed bytes")
@hypothesis.given(
    value=st.binary(min_size=1),
    other=st.binary(),
)
def test_should_match_prefixed_bytes(value: bytes, other: bytes) -> None:
    assert conjecture.suffixed_with(value).resolve(other + value)


@pytest.mark.describe("suffixed_with")
@pytest.mark.it("should not match other bytes suffix")
@hypothesis.given(
    value=st.binary(min_size=1),
    other=st.binary(min_size=1),
)
def test_should_not_match_other_bytes(value: bytes, other: bytes) -> None:
    hypothesis.assume(not (value + other).endswith(value))

    assert not conjecture.suffixed_with(value).resolve(value + other)
