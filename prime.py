"""
prime.py -- Generation of prime factors for a given integer
"""
class PrimeFactors:
    """ Prime Factor implemented as an iterable """
    def __init__(self,number):
        """ Initialize the instance """
        self.number = number
        if (isinstance(self.number, int) is False) or (self.number < 1):
            raise ValueError
        self.factor = 2 # initial candidate for a factor

    def __iter__(self):
        """ Returns the instance object which is an iterator. """
        return self

    def __next__(self):
        """ Define the instance object as an iterator."""
        if self.number == 1:
            raise StopIteration
        if self.factor > self.number: # Condition for end of list
            raise StopIteration
        while self.number % self.factor != 0: # if not a multiple of factor
            self.factor += 1 # increment the factor
        self.number = round(self.number/self.factor) # reduce number
        return self.factor # return this factor
