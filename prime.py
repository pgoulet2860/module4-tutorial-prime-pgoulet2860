"""
prime.py -- Generation of prime factors for a given integer
"""
class PrimeFactors:
    """ An iterable """
    def __init__(self,number):
        """ Initialize the instance """
        self.number = number
        if (isinstance(self.number, int) is False) or (self.number < 1):
            raise ValueError
