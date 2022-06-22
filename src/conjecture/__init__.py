"""
conjecture.

a pythonic assertion framework
"""

from conjecture.base import AllOfConjecture, AnyOfConjecture, Conjecture
from conjecture.general import all_of, any_of, anything, has, none
from conjecture.mapping import has_key
from conjecture.object import equal_to, has_attribute, instance_of
from conjecture.rich import (
    greater_than,
    greater_than_or_equal_to,
    less_than,
    less_than_or_equal_to,
)
from conjecture.sized import empty, length_of
from conjecture.string import prefixed_with, suffixed_with

__all__ = (
    "Conjecture",
    "AnyOfConjecture",
    "AllOfConjecture",
    "all_of",
    "any_of",
    "anything",
    "empty",
    "equal_to",
    "greater_than_or_equal_to",
    "greater_than",
    "has",
    "has_attribute",
    "has_key",
    "instance_of",
    "length_of",
    "less_than_or_equal_to",
    "less_than",
    "none",
    "prefixed_with",
    "suffixed_with",
)
