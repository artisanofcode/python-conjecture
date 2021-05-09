"""test conjecture.anything."""
from __future__ import annotations

import typing

import hypothesis
import hypothesis.strategies as st
import pytest

import conjecture


@pytest.mark.describe("anything")
@pytest.mark.it("should match all types")
@hypothesis.given(
    value=st.one_of(st.none(), st.booleans(), st.floats(), st.integers(), st.text()),
)
def test_should_match_all_types(
    value: typing.Union[None, bool, float, int, str]
) -> None:
    assert conjecture.anything().resolve(value)
