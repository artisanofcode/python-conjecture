"""test conjecture.Conjecture."""
from __future__ import annotations

import unittest.mock as mock

import hypothesis
import hypothesis.strategies as st
import pytest

import conjecture


@pytest.mark.describe("Conjecture")
@pytest.mark.it("resolve() should should return result of proof function")
@hypothesis.given(
    return_value=st.booleans(),
)
def test_resolve_should_return_result_of_proof_function(return_value: bool) -> None:
    proof = mock.Mock(return_value=return_value)

    instance = conjecture.Conjecture(proof)

    assert instance.resolve(mock.sentinel.value) == return_value
    proof.assert_called_once_with(mock.sentinel.value)


@pytest.mark.describe("Conjecture")
@pytest.mark.it("resolve() should error without proof function")
def test_resolve_should_error_without_proof_function() -> None:
    instance = conjecture.Conjecture()

    with pytest.raises(NotImplementedError):
        instance.resolve(mock.sentinel.value)


@pytest.mark.describe("Conjecture")
@pytest.mark.it("== should result based on resolve()")
@hypothesis.given(
    return_value=st.booleans(),
)
def test_eq_should_result_based_on_resolve(return_value: bool) -> None:
    proof = mock.Mock(return_value=return_value)

    instance = conjecture.Conjecture(proof)

    assert (mock.sentinel.value == instance) == return_value
    proof.assert_called_once_with(mock.sentinel.value)

    proof.reset_mock()

    assert (instance == mock.sentinel.value) == return_value
    proof.assert_called_once_with(mock.sentinel.value)


@pytest.mark.describe("Conjecture")
@pytest.mark.it("!= should result based on resolve()")
@hypothesis.given(
    return_value=st.booleans(),
)
def test_ne_should_result_based_on_resolve(return_value: bool) -> None:
    proof = mock.Mock(return_value=return_value)

    instance = conjecture.Conjecture(proof)

    assert (mock.sentinel.value != instance) == (not return_value)
    proof.assert_called_once_with(mock.sentinel.value)

    proof.reset_mock()

    assert (instance != mock.sentinel.value) == (not return_value)
    proof.assert_called_once_with(mock.sentinel.value)


@pytest.mark.describe("Conjecture")
@pytest.mark.it("~ should invert the resolution")
@hypothesis.given(
    return_value=st.booleans(),
)
def test_invert_should_invert_the_resolution(return_value: bool) -> None:
    proof = mock.Mock(return_value=return_value)

    instance = ~conjecture.Conjecture(proof)

    assert instance.resolve(mock.sentinel.value) == (not return_value)
    proof.assert_called_once_with(mock.sentinel.value)


@pytest.mark.describe("Conjecture")
@pytest.mark.it("| should create a conjecture that resolve if either resolves truely")
@hypothesis.given(
    return_value1=st.booleans(),
    return_value2=st.booleans(),
)
def test_or_shoould_create_a_conjecture_that_resolves_if_either_resolves_truely(
    return_value1: bool,
    return_value2: bool,
) -> None:
    proof1 = mock.Mock(return_value=return_value1)
    proof2 = mock.Mock(return_value=return_value2)

    instance = conjecture.Conjecture(proof1) | conjecture.Conjecture(proof2)

    assert instance.resolve(mock.sentinel.value) == (return_value1 or return_value2)


@pytest.mark.describe("Conjecture")
@pytest.mark.it("& should create a conjecture that resolve if both resolve truely")
@hypothesis.given(
    return_value1=st.booleans(),
    return_value2=st.booleans(),
)
def test_and_shoould_create_a_conjecture_that_resolves_if_both_resolve_truely(
    return_value1: bool,
    return_value2: bool,
) -> None:
    proof1 = mock.Mock(return_value=return_value1)
    proof2 = mock.Mock(return_value=return_value2)

    instance = conjecture.Conjecture(proof1) & conjecture.Conjecture(proof2)

    assert instance.resolve(mock.sentinel.value) == (return_value1 and return_value2)


@pytest.mark.describe("Conjecture")
@pytest.mark.it("| should create a conjecture that resolve if either resolves truely")
@hypothesis.given(
    return_value1=st.booleans(),
    return_value2=st.booleans(),
)
def test_or_should_create_a_conjecture_that_resolves_if_either_resolves_truely(
    return_value1: bool,
    return_value2: bool,
) -> None:
    proof1 = mock.Mock(return_value=return_value1)
    proof2 = mock.Mock(return_value=return_value2)

    instance = conjecture.Conjecture(proof1) | conjecture.Conjecture(proof2)

    assert instance.resolve(mock.sentinel.value) == (return_value1 or return_value2)


@pytest.mark.describe("Conjecture")
@pytest.mark.it("& should create a conjecture that resolve if both resolve truely")
@hypothesis.given(
    return_value1=st.booleans(),
    return_value2=st.booleans(),
)
def test_and_should_create_a_conjecture_that_resolves_if_both_resolve_truely(
    return_value1: bool,
    return_value2: bool,
) -> None:
    proof1 = mock.Mock(return_value=return_value1)
    proof2 = mock.Mock(return_value=return_value2)

    instance = conjecture.Conjecture(proof1) & conjecture.Conjecture(proof2)

    assert instance.resolve(mock.sentinel.value) == (return_value1 and return_value2)


@pytest.mark.describe("Conjecture")
@pytest.mark.it("| should error on non conjecture")
@hypothesis.given(
    return_value=st.booleans(),
)
def test_or_should_error_on_non_conjecture(
    return_value: bool,
) -> None:
    proof = mock.Mock(return_value=return_value)

    with pytest.raises(ValueError):
        (  # pylint: disable=expression-not-assigned
            conjecture.Conjecture(proof) | mock.sentinel.value
        )


@pytest.mark.describe("Conjecture")
@pytest.mark.it("& should create a conjecture that resolve if both resolve truely")
@hypothesis.given(
    return_value=st.booleans(),
)
def test_and_error_on_non_conjecture(
    return_value: bool,
) -> None:
    proof = mock.Mock(return_value=return_value)

    with pytest.raises(ValueError):
        (  # pylint: disable=expression-not-assigned
            conjecture.Conjecture(proof) & mock.sentinel.value
        )
