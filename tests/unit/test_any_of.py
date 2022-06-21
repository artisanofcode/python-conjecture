"""
Tests for :meth:`conjecture.any_of`.
"""

import unittest.mock

import hypothesis
import hypothesis.strategies as st

import conjecture


@hypothesis.given(
    return_values=st.lists(elements=st.booleans(), min_size=1),
)
def test_resolve_should_return_if_any_conjecture_resolves_truly(
    return_values: list[bool],
) -> None:
    """
    any_of() should should return if any conjecture resolves truly.
    """
    proofs = [
        unittest.mock.Mock(name=f"proofs[{i}]", return_value=v)
        for i, v in enumerate(return_values)
    ]

    instance = conjecture.any_of(*[conjecture.has(proof) for proof in proofs])

    assert instance.resolve(unittest.mock.sentinel.value) == any(return_values)
