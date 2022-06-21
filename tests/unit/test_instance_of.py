"""
Tests for :meth:`conjecture.instance_of`.
"""

import typing

import hypothesis
import hypothesis.strategies as st

import conjecture


@hypothesis.given(
    value=st.none() | st.booleans() | st.floats() | st.integers() | st.text()
)
def test_should_match_value_type(
    value: typing.Union[str, int, float, bool, None]
) -> None:
    """
    instance_of() should match value type.
    """
    assert conjecture.instance_of(value.__class__).resolve(value)


@hypothesis.given(
    value=st.none() | st.booleans() | st.floats() | st.integers() | st.text(),
    other=st.sampled_from([type(None), bool, float, int, str]),
)
def test_should_not_match_different_types(
    value: typing.Union[str, int, float, bool, None],
    other: typing.Union[type[None], type[bool], type[float], type[int], type[str]],
) -> None:
    """
    instance_of() should not match different type.
    """
    hypothesis.assume(not isinstance(value, other))

    assert not conjecture.instance_of(other).resolve(value)
