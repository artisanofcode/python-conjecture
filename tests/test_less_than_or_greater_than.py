"""test conjecture.less_than_or_equal_to."""
from __future__ import annotations

import hypothesis
import hypothesis.strategies as st
import pytest

import conjecture


@pytest.mark.describe("less_than_or_equal_to")
@pytest.mark.it("should match smaller value")
@hypothesis.given(
    value=st.shared(base=st.integers(), key="value"),
    other=st.shared(base=st.integers(), key="value").flatmap(
        lambda value: st.integers(max_value=value - 1)
    ),
)
def test_should_match_smaller_value(value: int, other: int) -> None:
    print(value, other)
    assert conjecture.less_than_or_equal_to(value).resolve(other)


@pytest.mark.describe("less_than_or_equal_to")
@pytest.mark.it("should not match bigger value")
@hypothesis.given(
    value=st.shared(base=st.integers(), key="value"),
    other=st.shared(base=st.integers(), key="value").flatmap(
        lambda value: st.integers(min_value=value + 1)
    ),
)
def test_should_not_match_bigger_value(value: int, other: int) -> None:
    assert not conjecture.less_than_or_equal_to(value).resolve(other)


@pytest.mark.describe("less_than_or_equal_to")
@pytest.mark.it("should match equal value")
@hypothesis.given(
    value=st.integers(),
)
def test_should_not_match_equal_value(value: int) -> None:
    assert conjecture.less_than_or_equal_to(value).resolve(value)
