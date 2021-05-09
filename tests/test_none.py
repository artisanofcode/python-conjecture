"""test conjecture.none."""
from __future__ import annotations

import typing

import hypothesis
import hypothesis.strategies as st
import pytest

import conjecture


@pytest.mark.describe("none")
@pytest.mark.it("should match None")
def test_hould_match_none() -> None:
    assert conjecture.none().resolve(None)


@pytest.mark.describe("none")
@pytest.mark.it("should not match non None")
@hypothesis.given(
    value=st.one_of(st.booleans(), st.floats(), st.integers(), st.text()),
)
def test_should_not_match_non_none(value: typing.Union[bool, float, int, str]) -> None:
    assert not conjecture.none().resolve(value)
