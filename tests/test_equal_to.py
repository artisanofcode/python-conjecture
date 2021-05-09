"""test conjecture.equal_to."""
from __future__ import annotations

import typing

import hypothesis
import hypothesis.strategies as st
import pytest

import conjecture


@pytest.mark.describe("equal_to")
@pytest.mark.it("should match itself")
@hypothesis.given(
    value=st.one_of(
        st.none(), st.booleans(), st.floats(allow_nan=False), st.integers(), st.text()
    )
)
def test_should_match_itself(value: typing.Union[None, bool, float, int, str]) -> None:
    assert conjecture.equal_to(value).resolve(value)


@pytest.mark.describe("equal_to")
@pytest.mark.it("should not match other values")
@hypothesis.given(
    value=st.one_of(st.none(), st.booleans(), st.floats(), st.integers(), st.text()),
    other=st.one_of(st.none(), st.booleans(), st.floats(), st.integers(), st.text()),
)
def test_should_not_match_other_values(
    value: typing.Union[None, bool, float, int, str],
    other: typing.Union[None, bool, float, int, str],
) -> None:
    hypothesis.assume(value != other)

    assert not conjecture.equal_to(value).resolve(other)
