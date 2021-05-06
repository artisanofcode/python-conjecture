"""
conjecture

a pythonic assertion framework
"""
from __future__ import annotations

from conjecture.base import AllOfConjecture, AnyOfConjecture, Conjecture
from conjecture.general import all_of, any_of, anything, has, none
from conjecture.object import instance_of
from conjecture.rich import (
    equal_to,
    greater_than,
    greater_than_or_equal_to,
    less_than,
    less_than_or_equal_to,
)
from conjecture.sized import empty, length
from conjecture.string import ends_with, starts_with

__all__ = (
    "Conjecture",
    "AnyOfConjecture",
    "AllOfConjecture",
    "all_of",
    "any_of",
    "anything",
    "empty",
    "ends_with",
    "equal_to",
    "greater_than_or_equal_to",
    "greater_than",
    "has",
    "instance_of",
    "length",
    "less_than_or_equal_to",
    "less_than",
    "none",
    "starts_with",
)
