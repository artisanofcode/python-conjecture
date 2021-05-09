"""test conjecture.instance_of."""
from __future__ import annotations

import typing

import hypothesis
import hypothesis.strategies as st
import pytest

import conjecture


@pytest.mark.describe("instance_of")
@pytest.mark.it("should match value type")
@hypothesis.given(
    value=st.one_of(st.none(), st.booleans(), st.floats(), st.integers(), st.text()),
)
def test_should_match_value_type(
    value: typing.Union[None, bool, float, int, str]
) -> None:
    assert conjecture.instance_of(value.__class__).resolve(value)


@pytest.mark.describe("instance_of")
@pytest.mark.it("should not match different type")
@hypothesis.given(
    value=st.one_of(st.none(), st.booleans(), st.floats(), st.integers(), st.text()),
    other=st.sampled_from([type(None), bool, float, int, str]),
)
def test_should_not_match_different_types(
    value: typing.Union[None, bool, float, int, str],
    other: typing.Union[
        typing.Type[None],
        typing.Type[bool],
        typing.Type[float],
        typing.Type[int],
        typing.Type[str],
    ],
) -> None:
    hypothesis.assume(not isinstance(value, other))

    assert not conjecture.instance_of(other).resolve(value)
