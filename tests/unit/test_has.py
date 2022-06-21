"""
Tests for :meth:`conjecture.has`.
"""

import unittest.mock

import hypothesis
import hypothesis.strategies as st

import conjecture


@hypothesis.given(return_value=st.booleans())
def test_should_return_result_of_proof_function(return_value: bool) -> None:
    """
    has() should return result of proof function.
    """
    proof = unittest.mock.Mock(return_value=return_value)

    instance = conjecture.has(proof)

    assert instance.resolve(unittest.mock.sentinel.value) == return_value
    proof.assert_called_once_with(unittest.mock.sentinel.value)
