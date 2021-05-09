"""test conjecture.AnyOfConjecture."""
from __future__ import annotations

import typing
import unittest.mock as mock

import hypothesis
import hypothesis.strategies as st
import pytest

import conjecture


@pytest.mark.describe("all_of")
@pytest.mark.it("resolve() should resolve if all conjectures resolves truely")
@hypothesis.given(
    return_values=st.lists(elements=st.booleans(), min_size=1),
)
def test_resolve_should_resolve_if_all_conjectures_resolves_truely(
    return_values: typing.List[bool],
) -> None:
    proofs = [
        mock.Mock(name=f"proofs[{i}]", return_value=v)
        for i, v in enumerate(return_values)
    ]

    instance = conjecture.all_of(*[conjecture.has(proof) for proof in proofs])

    assert instance.resolve(mock.sentinel.value) == all(return_values)
