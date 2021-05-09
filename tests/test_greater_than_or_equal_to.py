"""test conjecture.greater_than_or_equal_to."""
from __future__ import annotations

import hypothesis
import hypothesis.strategies as st
import pytest

import conjecture


@pytest.mark.describe("greater_than_or_equal_to")
@pytest.mark.it("should match bigger value")
@hypothesis.given(
    value=st.shared(base=st.integers(), key="value"),
    other=st.shared(base=st.integers(), key="value").flatmap(
        lambda x: st.integers(min_value=x + 1)
    ),
)
def test_should_match_bigger_value(value: int, other: int) -> None:
    assert conjecture.greater_than_or_equal_to(value).resolve(other)


@pytest.mark.describe("greater_than_or_equal_to")
@pytest.mark.it("should not match smaller value")
@hypothesis.given(
    value=st.shared(base=st.integers(), key="value"),
    other=st.shared(base=st.integers(), key="value").flatmap(
        lambda x: st.integers(max_value=x - 1)
    ),
)
def test_should_not_match_smaller_value(value: int, other: int) -> None:
    assert not conjecture.greater_than_or_equal_to(value).resolve(other)


@pytest.mark.describe("greater_than_or_equal_to")
@pytest.mark.it("should match equal value")
@hypothesis.given(
    value=st.integers(),
)
def test_should_not_match_equal_value(value: int) -> None:
    assert conjecture.greater_than_or_equal_to(value).resolve(value)
