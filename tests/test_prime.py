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
