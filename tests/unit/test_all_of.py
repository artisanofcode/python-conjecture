"""
Tests for :meth:`conjecture.all`.
"""

import unittest.mock

import hypothesis
import hypothesis.strategies as st

import conjecture


@hypothesis.given(
    return_values=st.lists(elements=st.booleans(), min_size=1),
)
def test_resolve_should_resolve_if_all_conjectures_resolves_truly(
    return_values: list[bool],
) -> None:
    """
    resolve() should resolve if all conjectures resolves truly.
    """
    proofs = [
        unittest.mock.Mock(name=f"proofs[{i}]", return_value=v)
        for i, v in enumerate(return_values)
    ]

    instance = conjecture.all_of(*[conjecture.has(proof) for proof in proofs])

    assert instance.resolve(unittest.mock.sentinel.value) == all(return_values)
