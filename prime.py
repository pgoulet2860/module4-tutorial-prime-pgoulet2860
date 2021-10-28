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
        if self.number == 1:
            self.primelist = []
        else:
            self.primelist = []
            residual = self.number
            # residual value of the number after division by
            # prime factors - initially equal to the number itself
            factor = 2  # initial candidate for a factor
            while factor <= residual: # continue looking for factors
                while residual % factor == 0:
                    # if residual exactly divisible by factor
                    self.primelist.append(factor)
                    # add an instance of this factor to the list of prime factors
                    residual = round(residual/factor)
                    # reduce the residual value
                factor += 1 # consider next integer as a factor
