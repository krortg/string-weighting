""" Contains the string generation utilities. """

import abc
import string
import random


class BaseGenerator(metaclass=abc.ABCMeta):
    """ 
    The base class for a random text string generator. A generator is made up of an alphabet
    where the characters used in the generation are and a `generate` function that must be
    overridden for supply the generation logic.
    """
    
    alphabet = None

    @abc.abstractmethod
    def generate(self):
        """
        Generate a random text string using chars in the alphabet
        
        Must be overridden with you generation logic.
        """
        pass

    def save(self, output, lines=10**6):
        """ Create a file with lines text string generated. """

        assert lines > 0, 'The lines parameter must be positive.'
        
        with open(output, 'wt') as fd:
            for _ in range(lines):
                print(self.generate(), file=fd)


class AlphaNumGenerator(BaseGenerator):
    """ A generator that uses an alphanumeric and ensures the placement of non-consecutive white spaces. """

    alphabet = string.ascii_letters + string.digits
    
    def __init__(self, min_size=50, max_size=100, min_spaces=3, max_spaces=5):
        """
        Initialize the generator by specifying the ranges for the string
        size and the range of required whitespace.
        """

        super().__init__()
        assert min_size > 0 and max_size > 0, 'The size range must contains positive numbers.'
        assert min_size <= max_size, 'The max size must be greater or equal than the min size.'

        assert min_spaces > 0 and max_spaces > 0, 'The required whirespaces range must be positives.'
        assert min_size <= max_size, 'The max amount of spaces must be greater or equal than the min amount.'

        # Ensure the invariant for construct valid string according problem 
        assert min_size >= 2 * max_spaces + 1, 'The min size must allow place the max number of spaces.'

        self.min_size = min_size
        self.max_size = max_size
        self.min_spaces = min_spaces
        self.max_spaces = max_spaces

    def generate(self):
        """ Generate an alphanumeric random text string placing required non consecutive whitespaces. """

        size = random.randint(self.min_size, self.max_size)
        sample = random.choices(self.alphabet, k=size)

        # place now the required whitespaces
        spaces = random.randint(self.min_spaces, self.max_spaces)
        idx = -1
        while spaces > 0:
            idx = random.randint(idx + 2, size - 2 * spaces)
            sample[idx] = ' '
            spaces -= 1

        return ''.join(sample)
