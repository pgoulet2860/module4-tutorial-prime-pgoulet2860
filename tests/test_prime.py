# pylint: disable=missing-docstring
"""
The test module for Prime Factors
"""
import pytest
from prime import PrimeFactors

def test_prime_reject_float_input():
    """
    Assert that when PrimeFactors is called with a data type
    that is a float, a ValueError is raised.
    """
    with pytest.raises(ValueError):
        PrimeFactors(float)

def test_prime_reject_string_input():
    """
    Assert that when PrimeFactors is called with a data type
    that is a string, a ValueError is raised.
    """
    with pytest.raises(ValueError):
        PrimeFactors(str)

def test_prime_call_with_1():
    """
    Assert that when PrimeFactors is called with 1,
    an empty list is returned.
    """
    prime_fact = PrimeFactors(1)
    assert prime_fact.primelist == []

def test_prime_call_with_2():
    """
    Assert that when PrimeFactors is called with 2,
    the list [2] is returned.
    """
    prime_fact = PrimeFactors(2)
    assert prime_fact.primelist == [2]
