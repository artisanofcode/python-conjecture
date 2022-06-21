"""
Tests for :meth:`conjecture.Conjecture`.
"""

import unittest.mock

import hypothesis
import hypothesis.strategies as st
import pytest

import conjecture


@hypothesis.given(return_value=st.booleans())
def test_resolve_should_return_result_of_proof_function(return_value: bool) -> None:
    """
    resolve() should should return result of proof function.
    """
    proof = unittest.mock.Mock(return_value=return_value)

    instance = conjecture.Conjecture(proof)

    assert instance.resolve(unittest.mock.sentinel.value) == return_value
    proof.assert_called_once_with(unittest.mock.sentinel.value)


def test_resolve_should_error_without_proof_function() -> None:
    """
    resolve() should error without proof function.
    """
    instance = conjecture.Conjecture()

    with pytest.raises(NotImplementedError):
        instance.resolve(unittest.mock.sentinel.value)


@hypothesis.given(return_value=st.booleans())
def test_eq_should_result_based_on_resolve(return_value: bool) -> None:
    """
    == should result based on resolve().
    """
    proof = unittest.mock.Mock(return_value=return_value)

    instance = conjecture.Conjecture(proof)

    assert (unittest.mock.sentinel.value == instance) == return_value
    proof.assert_called_once_with(unittest.mock.sentinel.value)

    proof.reset_mock()

    assert (instance == unittest.mock.sentinel.value) == return_value
    proof.assert_called_once_with(unittest.mock.sentinel.value)


@hypothesis.given(return_value=st.booleans())
def test_ne_should_result_based_on_resolve(return_value: bool) -> None:
    """
    != should result based on resolve().
    """
    proof = unittest.mock.Mock(return_value=return_value)

    instance = conjecture.Conjecture(proof)

    assert (unittest.mock.sentinel.value != instance) == (not return_value)
    proof.assert_called_once_with(unittest.mock.sentinel.value)

    proof.reset_mock()

    assert (instance != unittest.mock.sentinel.value) == (not return_value)
    proof.assert_called_once_with(unittest.mock.sentinel.value)


@hypothesis.given(return_value=st.booleans())
def test_invert_should_invert_the_resolution(return_value: bool) -> None:
    """
    ~ should invert the resolution.
    """
    proof = unittest.mock.Mock(return_value=return_value)

    instance = ~conjecture.Conjecture(proof)

    assert instance.resolve(unittest.mock.sentinel.value) == (not return_value)
    proof.assert_called_once_with(unittest.mock.sentinel.value)


@hypothesis.given(return_value1=st.booleans(), return_value2=st.booleans())
def test_or_should_create_a_conjecture_that_resolves_if_either_resolves_truly(
    return_value1: bool,
    return_value2: bool,
) -> None:
    """
    | should create a conjecture that resolve if either resolves truly.
    """
    proof1 = unittest.mock.Mock(return_value=return_value1)
    proof2 = unittest.mock.Mock(return_value=return_value2)

    instance = conjecture.Conjecture(proof1) | conjecture.Conjecture(proof2)

    assert instance.resolve(unittest.mock.sentinel.value) == (
        return_value1 or return_value2
    )


@hypothesis.given(return_value1=st.booleans(), return_value2=st.booleans())
def test_and_should_create_a_conjecture_that_resolves_if_both_resolve_truly(
    return_value1: bool,
    return_value2: bool,
) -> None:
    """
    & should create a conjecture that resolve if both resolve truly.
    """
    proof1 = unittest.mock.Mock(return_value=return_value1)
    proof2 = unittest.mock.Mock(return_value=return_value2)

    instance = conjecture.Conjecture(proof1) & conjecture.Conjecture(proof2)

    assert instance.resolve(unittest.mock.sentinel.value) == (
        return_value1 and return_value2
    )


@hypothesis.given(return_value=st.booleans())
def test_or_should_error_on_non_conjecture(return_value: bool) -> None:
    """
    | should error on non conjecture.
    """
    proof = unittest.mock.Mock(return_value=return_value)

    with pytest.raises(ValueError):
        (  # pylint: disable=expression-not-assigned
            conjecture.Conjecture(proof) | unittest.mock.sentinel.value
        )


@hypothesis.given(return_value=st.booleans())
def test_and_error_on_non_conjecture(return_value: bool) -> None:
    """
    & should error on non conjecture.
    """
    proof = unittest.mock.Mock(return_value=return_value)

    with pytest.raises(ValueError):
        (  # pylint: disable=expression-not-assigned
            conjecture.Conjecture(proof) & unittest.mock.sentinel.value
        )
