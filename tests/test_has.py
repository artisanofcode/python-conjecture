"""
test conjecture.Conjecture
"""
from __future__ import annotations

import unittest.mock as mock

import hypothesis
import hypothesis.strategies as st
import pytest

import conjecture


@pytest.mark.describe("has")
@pytest.mark.it("should return result of proof function")
@hypothesis.given(
    return_value=st.booleans(),
)
def test_should_return_result_of_proof_function(return_value: bool) -> None:
    proof = mock.Mock(return_value=return_value)

    instance = conjecture.has(proof)

    assert instance.resolve(mock.sentinel.value) == return_value
    proof.assert_called_once_with(mock.sentinel.value)
