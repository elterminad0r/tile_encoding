#!/usr/bin/env python2

"""
Clone of src/magic_encode, to provide imports for Processing code. Original
docstring:

Program that performs real magic - see README.md and SOLUTION.md.
By default, it will generate a random board, and then test each possible square
to see if the algorithm works. It doesn't cheat, and will actually fail
critically if it gets a single guess wrong.
"""

from operator import xor
from random import randrange
from itertools import count

# start of core problem logic:

def find_money(bits):
    """
    Return the index currently pointed to by the log2(|bits|) "Hamming" bits.
    """
    return reduce(xor, (ind for ind, bit in enumerate(bits) if bit), 0)

def generate_flip(bits, target):
    """
    Generate which bit to flip in order to change the target to `target`.
    """
    return target ^ find_money(bits)

# end of core problem logic. scripting bureaucracy from here

def ilog2(n):
    """
    Return the integer log2 by bitshifting
    """
    for i in count():
        n >>= 1
        if not n:
            return i
    return 0 # linter complains

def power_of_two(arg):
    """
    Bit twiddling to determine if a string represents an integer power of two.
    """
    n = int(arg)
    if n <= 0 or n & (n - 1):
        raise ValueError("not a power of two")
    return n

def generate_bits(size):
    """
    Generate n random bits
    """
    return [randrange(2) for _ in range(size)]
